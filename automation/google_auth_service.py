#!/usr/bin/env python3
"""
Google OAuth 2.0 Authentication Service for Omni Sovereign Operations
Authorizes rgkdevx1@gmail.com for:
- Google Docs API (https://www.googleapis.com/auth/documents)
- Google Drive API (https://www.googleapis.com/auth/drive)
- Google Sheets API (https://www.googleapis.com/auth/spreadsheets)
- Gmail API (https://www.googleapis.com/auth/gmail.send)

Generates Google OAuth login URLs, handles local callback / auth code exchange,
and stores token.json for autonomous Google API access.
"""

import os
import sys
import json
import urllib.parse
from datetime import datetime, timezone
import http.server
import socketserver
import threading

USER_EMAIL = "rgkdevx1@gmail.com"
AUTOMATION_DIR = "/data/data/com.termux/files/home/omni-automation"
CREDENTIALS_DIR = os.path.join(AUTOMATION_DIR, "credentials")
TOKEN_FILE = os.path.join(CREDENTIALS_DIR, "token.json")
CLIENT_CONFIG_FILE = os.path.join(CREDENTIALS_DIR, "client_secret.json")

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/chat.spaces",
    "https://www.googleapis.com/auth/chat.messages.create",
    "https://www.googleapis.com/auth/chat.messages"
]

class GoogleAuthService:
    def __init__(self, user_email=USER_EMAIL):
        self.user_email = user_email
        os.makedirs(CREDENTIALS_DIR, exist_ok=True)

    def is_authenticated(self):
        """Checks if a valid OAuth2 token exists."""
        if not os.path.exists(TOKEN_FILE):
            return False
        try:
            with open(TOKEN_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return bool(data.get("token") or data.get("access_token") or data.get("refresh_token"))
        except Exception:
            return False

    def get_client_credentials(self):
        """Loads client_id and client_secret if present."""
        if os.path.exists(CLIENT_CONFIG_FILE):
            try:
                with open(CLIENT_CONFIG_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # Check installed or web
                    cfg = data.get("installed") or data.get("web") or data
                    return cfg.get("client_id"), cfg.get("client_secret")
            except Exception:
                pass
        # Check environment variables
        client_id = os.environ.get("GOOGLE_CLIENT_ID", "")
        client_secret = os.environ.get("GOOGLE_CLIENT_SECRET", "")
        return client_id, client_secret

    def set_client_credentials(self, client_id, client_secret):
        """Saves client_id and client_secret to client_secret.json."""
        data = {
            "installed": {
                "client_id": client_id,
                "client_secret": client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "redirect_uris": [
                    "http://localhost:8090/oauth2callback",
                    "urn:ietf:wg:oauth:2.0:oob",
                    "http://localhost"
                ]
            }
        }
        with open(CLIENT_CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"[Google Auth] Saved client configuration to {CLIENT_CONFIG_FILE}")

    def generate_authorization_url(self, client_id=None, redirect_uri="http://localhost:8090/oauth2callback"):
        """Generates Google OAuth 2.0 login URL for user consent."""
        if not client_id:
            client_id, _ = self.get_client_credentials()

        if not client_id:
            # Fallback to standard prompt if client ID is missing
            return None, "Missing Google Cloud OAuth2 Client ID. Please provide your Client ID."

        params = {
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "scope": " ".join(SCOPES),
            "access_type": "offline",
            "prompt": "consent",
            "login_hint": self.user_email,
            "state": "omni_sovereign_swarm_auth"
        }
        auth_url = "https://accounts.google.com/o/oauth2/v2/auth?" + urllib.parse.urlencode(params)
        return auth_url, None

    def exchange_code_for_tokens(self, auth_code, redirect_uri="http://localhost:8090/oauth2callback"):
        """Exchanges authorization code for access and refresh tokens using google-auth-oauthlib or requests."""
        import requests
        client_id, client_secret = self.get_client_credentials()

        if not client_id or not client_secret:
            return False, "Missing client_id or client_secret"

        token_url = "https://oauth2.googleapis.com/token"
        payload = {
            "code": auth_code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code"
        }

        try:
            resp = requests.post(token_url, data=payload, timeout=10)
            if resp.status_code == 200:
                tokens = resp.json()
                tokens["created_at"] = datetime.now(timezone.utc).isoformat()
                tokens["account"] = self.user_email
                with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                    json.dump(tokens, f, indent=2)
                print(f"[Google Auth] Authentication successful! Saved tokens to {TOKEN_FILE}")
                return True, "Successfully authorized Google Docs, Sheets, and Gmail!"
            else:
                return False, f"Token exchange failed: {resp.text}"
        except Exception as e:
            return False, f"Error contacting token endpoint: {e}"

    def refresh_access_token(self):
        """Uses refresh_token to obtain a fresh access_token."""
        import requests
        if not os.path.exists(TOKEN_FILE):
            return None, "No token.json found"
        try:
            with open(TOKEN_FILE, "r", encoding="utf-8") as f:
                tokens = json.load(f)
            refresh_token = tokens.get("refresh_token")
            if not refresh_token:
                return None, "No refresh_token found in token.json"

            client_id, client_secret = self.get_client_credentials()
            token_url = "https://oauth2.googleapis.com/token"
            payload = {
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
                "grant_type": "refresh_token"
            }
            resp = requests.post(token_url, data=payload, timeout=10)
            if resp.status_code == 200:
                new_data = resp.json()
                tokens["access_token"] = new_data["access_token"]
                tokens["expires_in"] = new_data.get("expires_in", 3600)
                tokens["refreshed_at"] = datetime.now(timezone.utc).isoformat()
                with open(TOKEN_FILE, "w", encoding="utf-8") as f:
                    json.dump(tokens, f, indent=2)
                return tokens["access_token"], None
            else:
                return None, f"Failed to refresh token: {resp.text}"
        except Exception as e:
            return None, str(e)

    def get_valid_access_token(self):
        """Returns current access token, or refreshes if expired."""
        if not os.path.exists(TOKEN_FILE):
            return None
        try:
            with open(TOKEN_FILE, "r", encoding="utf-8") as f:
                tokens = json.load(f)

            # Check if token is expired based on timestamp
            last_time_str = tokens.get("refreshed_at") or tokens.get("created_at")
            is_expired = True
            if last_time_str:
                try:
                    last_time = datetime.fromisoformat(last_time_str)
                    age_seconds = (datetime.now(timezone.utc) - last_time).total_seconds()
                    expires_in = tokens.get("expires_in", 3600)
                    if age_seconds < (expires_in - 300):  # 5-minute buffer
                        is_expired = False
                except Exception:
                    is_expired = True

            if not is_expired and tokens.get("access_token"):
                return tokens.get("access_token")

            # Token is expired or missing, auto-refresh
            token, err = self.refresh_access_token()
            if token:
                return token
            return tokens.get("access_token")
        except Exception:
            return None

    def get_auth_status(self):
        """Returns clean status summary for CLI and web UI."""
        client_id, _ = self.get_client_credentials()
        has_client = bool(client_id)
        authenticated = self.is_authenticated()

        return {
            "user_email": self.user_email,
            "has_client_credentials": has_client,
            "is_authenticated": authenticated,
            "scopes": SCOPES,
            "token_file": TOKEN_FILE,
            "client_file": CLIENT_CONFIG_FILE,
            "status": "AUTHENTICATED" if authenticated else ("AWAITING_USER_AUTH" if has_client else "CONFIG_REQUIRED")
        }

if __name__ == "__main__":
    service = GoogleAuthService()
    print("=" * 70)
    print("🔐 GOOGLE OAUTH 2.0 AUTHORIZATION MANAGER")
    print(f"Target User Account: {USER_EMAIL}")
    print("=" * 70)

    status = service.get_auth_status()
    print(json.dumps(status, indent=2))

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "set-client" and len(sys.argv) >= 4:
            service.set_client_credentials(sys.argv[2], sys.argv[3])
            url, err = service.generate_authorization_url()
            if url:
                print(f"\n👉 Visit this Google Auth URL in your browser to log in:\n\n{url}\n")
        elif cmd == "auth-code" and len(sys.argv) >= 3:
            ok, msg = service.exchange_code_for_tokens(sys.argv[2])
            print(f"Result: {msg}")
        elif cmd == "url":
            url, err = service.generate_authorization_url()
            if url:
                print(f"\n👉 Google Authorization URL:\n{url}")
            else:
                print(f"Error: {err}")
