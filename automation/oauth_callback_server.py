#!/usr/bin/env python3
"""
OAuth 2.0 Local Callback Server for Omni Sovereign Swarm
Listens on port 8090, intercepts the Google authorization code,
exchanges it for token.json, and renders a confirmation page in the browser.
"""

import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

AUTOMATION_DIR = "/data/data/com.termux/files/home/omni-automation"
sys.path.insert(0, AUTOMATION_DIR)
from google_auth_service import GoogleAuthService

PORT = 8090

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[OAuth Server HTTP] {format % args}")

    def do_GET(self):
        print(f"[OAuth Server] Incoming GET: {self.path}")
        parsed = urllib.parse.urlparse(self.path)
        qs = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/oauth2callback" or "code" in qs:
            code = qs.get("code", [""])[0]
            error = qs.get("error", [""])[0]

            if error:
                print(f"[OAuth Server] Received error from Google: {error}")
                self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(f"""<!DOCTYPE html>
<html>
<body style="font-family: sans-serif; background:#07090e; color:#F87171; padding:40px; text-align:center;">
  <h2>❌ Authorization Denied / Error</h2>
  <p>{error}</p>
</body>
</html>""".encode("utf-8"))
                return

            if code:
                print(f"[OAuth Server] Received authorization code. Exchanging tokens...")
                # Exchange code for tokens
                service = GoogleAuthService()
                success, msg = service.exchange_code_for_tokens(code, redirect_uri=f"http://localhost:{PORT}/oauth2callback")

                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()

                if success:
                    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Omni Swarm | Google Auth Complete</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #07090e;
      color: #FFFFFF;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .card {
      background: rgba(18, 24, 40, 0.9);
      border: 1px solid rgba(0, 242, 254, 0.4);
      padding: 40px;
      border-radius: 20px;
      text-align: center;
      max-width: 500px;
      box-shadow: 0 0 50px rgba(0, 242, 254, 0.2);
    }
    h1 { color: #00F2FE; margin-bottom: 12px; font-size: 1.8rem; }
    p { color: #94A3B8; font-size: 1rem; line-height: 1.6; margin-bottom: 24px; }
    .badge {
      display: inline-block;
      background: rgba(16, 185, 129, 0.2);
      border: 1px solid rgba(16, 185, 129, 0.4);
      color: #34D399;
      font-weight: 700;
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 0.85rem;
      margin-bottom: 16px;
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="badge">✓ OAUTH 2.0 CONNECTED</div>
    <h1>Google Docs &amp; Drive Authorized!</h1>
    <p>The 55 sovereign agents are now authenticated for account <strong style="color:#FFF;">rgkdevx1@gmail.com</strong>.</p>
    <p>You can close this tab and return to the chat or your Workspace Hub.</p>
  </div>
</body>
</html>"""
                    self.wfile.write(html.encode("utf-8"))
                    print(f"\n🎉 [OAuth Callback] Successfully exchanged authorization code for token.json!")
                    print(f"Account: {service.user_email} is now connected to Google Docs, Sheets, Drive, and Gmail.\n")
                    
                    # Also sync to web assets
                    try:
                        from google_workspace import GoogleWorkspaceSuite
                        GoogleWorkspaceSuite().sync_to_web_assets()
                    except Exception as e:
                        print(f"[OAuth Server] Note during web sync: {e}")

                    # Exit after short delay
                    def shutdown():
                        import time
                        time.sleep(2)
                        os._exit(0)
                    import threading
                    threading.Thread(target=shutdown).start()
                    return
                else:
                    self.wfile.write(f"<h3>Token exchange failed: {msg}</h3>".encode("utf-8"))
                    print(f"[OAuth Server] Token exchange failed: {msg}")
                    return

        # Default fallback
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Omni OAuth Listener Running on Port 8090.")

def run_server():
    server = HTTPServer(("0.0.0.0", PORT), OAuthCallbackHandler)
    print(f"⚡ [OAuth Server] Listening for Google OAuth callback on http://localhost:{PORT}/oauth2callback...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[OAuth Server] Stopped.")

if __name__ == "__main__":
    run_server()
