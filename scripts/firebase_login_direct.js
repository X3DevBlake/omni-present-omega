#!/usr/bin/env node
/**
 * Direct Google OAuth 2.0 Authenticator for Firebase CLI
 * Bypasses the auth.firebase.tools proxy and connects directly to Google OAuth 2.0.
 */

const http = require("http");
const url = require("url");
const { execSync } = require("child_process");
const jwt = require("/data/data/com.termux/files/usr/lib/node_modules/firebase-tools/node_modules/jsonwebtoken");
const api = require("/data/data/com.termux/files/usr/lib/node_modules/firebase-tools/lib/api");
const apiv2 = require("/data/data/com.termux/files/usr/lib/node_modules/firebase-tools/lib/apiv2");
const FormData = require("/data/data/com.termux/files/usr/lib/node_modules/firebase-tools/node_modules/form-data");
const { configstore } = require("/data/data/com.termux/files/usr/lib/node_modules/firebase-tools/lib/configstore");
const scopes = require("/data/data/com.termux/files/usr/lib/node_modules/firebase-tools/lib/scopes");

const SCOPES = [
    scopes.EMAIL,
    scopes.OPENID,
    scopes.CLOUD_PROJECTS_READONLY,
    scopes.FIREBASE_PLATFORM,
    scopes.CLOUD_PLATFORM,
];

const PORT = 9005;
const CALLBACK_URL = `http://localhost:${PORT}`;
const STATE_NONCE = "opo_firebase_" + Math.random().toString(36).substring(2, 12);

const authUrl = "https://accounts.google.com/o/oauth2/auth?" + new URLSearchParams({
    client_id: api.clientId(),
    scope: SCOPES.join(" "),
    response_type: "code",
    state: STATE_NONCE,
    redirect_uri: CALLBACK_URL,
    login_hint: "rgkdevx1@gmail.com",
    prompt: "select_account consent",
    access_type: "offline",
}).toString();

console.log("======================================================================");
console.log("🔥 DIRECT FIREBASE GOOGLE OAUTH 2.0 AUTHENTICATION");
console.log("======================================================================");
console.log(`Port: ${PORT}`);
console.log(`Callback URL: ${CALLBACK_URL}`);
console.log(`Target Account: rgkdevx1@gmail.com`);
console.log("\nDirect Google OAuth URL:\n" + authUrl + "\n");

async function exchangeCodeForTokens(code) {
    const params = {
        code: code,
        client_id: api.clientId(),
        client_secret: api.clientSecret(),
        redirect_uri: CALLBACK_URL,
        grant_type: "authorization_code",
    };
    const client = new apiv2.Client({ urlPrefix: api.authOrigin(), auth: false });
    const form = new FormData();
    for (const [k, v] of Object.entries(params)) {
        form.append(k, v);
    }
    const res = await client.request({
        method: "POST",
        path: "/o/oauth2/token",
        body: form,
        headers: form.getHeaders(),
        skipLog: { body: true, queryParams: true, resBody: true },
    });
    return res.body;
}

const server = http.createServer(async (req, res) => {
    try {
        const parsedUrl = url.parse(req.url, true);
        const { code, state, error, error_description } = parsedUrl.query;

        if (error) {
            console.error(`\n❌ OAuth Error: ${error} - ${error_description}`);
            res.writeHead(400, { "Content-Type": "text/html" });
            res.end(`<h1>Authentication Failed</h1><p>${error}: ${error_description}</p>`);
            return;
        }

        if (!code) {
            res.writeHead(200, { "Content-Type": "text/html" });
            res.end("<h1>OPO Firebase Auth Server Active</h1><p>Awaiting OAuth callback...</p>");
            return;
        }

        console.log("\n📥 Received authorization callback from Google!");
        console.log(`Code prefix: ${code.substring(0, 10)}...`);

        const tokens = await exchangeCodeForTokens(code);
        if (!tokens.access_token && !tokens.refresh_token) {
            throw new Error("Failed to receive valid tokens from Google OAuth.");
        }

        const decodedUser = jwt.decode(tokens.id_token, { json: true }) || { email: "rgkdevx1@gmail.com" };

        configstore.set("user", decodedUser);
        configstore.set("tokens", tokens);
        configstore.set("loginScopes", SCOPES);
        configstore.delete("session");
        configstore.delete("tempLoginState");

        console.log(`\n✅ SUCCESS! Authenticated as: ${decodedUser.email || "rgkdevx1@gmail.com"}`);
        console.log("Tokens securely saved to ~/.config/configstore/firebase-tools.json");

        const successHtml = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Firebase CLI Authenticated</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0B0F17; color: #F8FAFC; display: flex; align-items: center; justify-content: center; min-height: 100vh; margin: 0; padding: 20px; box-sizing: border-box; }
        .card { background: rgba(30, 41, 59, 0.7); backdrop-filter: blur(16px); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 20px; padding: 40px; text-align: center; max-width: 480px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); }
        h1 { color: #60A5FA; margin-bottom: 12px; font-size: 24px; }
        p { color: #94A3B8; font-size: 15px; line-height: 1.6; }
        .badge { display: inline-block; background: rgba(34, 197, 94, 0.15); border: 1px solid rgba(34, 197, 94, 0.4); color: #4ADE80; padding: 6px 14px; border-radius: 9999px; font-weight: 600; font-size: 13px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">✓ CLI AUTHENTICATED</div>
        <h1>Authentication Successful!</h1>
        <p>Omni-Present Omega has authenticated with Google Firebase as <strong>${decodedUser.email}</strong>.</p>
        <p>You can close this tab and return to the terminal. Firebase deployment will continue automatically.</p>
    </div>
</body>
</html>`;

        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(successHtml);

        setTimeout(() => {
            server.close();
            process.exit(0);
        }, 1500);

    } catch (err) {
        console.error("\n❌ Error handling OAuth exchange:", err.message);
        res.writeHead(500, { "Content-Type": "text/html" });
        res.end(`<h1>Authentication Error</h1><p>${err.message}</p>`);
    }
});

server.listen(PORT, "0.0.0.0", () => {
    console.log(`Server listening on 0.0.0.0:${PORT}...`);
    try {
        execSync(`termux-open-url "${authUrl}"`, { stdio: "ignore" });
        console.log("Launched Google Sign-in in Android browser via termux-open-url.");
    } catch (e) {
        console.log("Note: Open the URL above in your browser if not opened automatically.");
    }
});
