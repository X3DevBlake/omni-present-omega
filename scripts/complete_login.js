#!/usr/bin/env node
/**
 * Direct Token Exchanger for Firebase CLI
 * Usage: node scripts/complete_login.js <authorization_code_or_full_redirect_url>
 */

const url = require("url");
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

let rawInput = process.argv[2];
if (!rawInput) {
    console.error("Usage: node scripts/complete_login.js <code_or_url>");
    process.exit(1);
}

let code = rawInput.trim();
let callbackUrl = "http://localhost:9005";

if (code.startsWith("http")) {
    try {
        const parsed = new URL(code);
        const codeParam = parsed.searchParams.get("code");
        if (codeParam) {
            code = codeParam;
            callbackUrl = `${parsed.protocol}//${parsed.host}${parsed.pathname}`;
        }
    } catch (e) {}
}

async function run() {
    console.log("Exchanging code with Google OAuth 2.0...");
    console.log("Callback URL used:", callbackUrl);
    console.log("Code:", code.substring(0, 15) + "...");

    const params = {
        code: code,
        client_id: api.clientId(),
        client_secret: api.clientSecret(),
        redirect_uri: callbackUrl,
        grant_type: "authorization_code",
    };

    const client = new apiv2.Client({ urlPrefix: api.authOrigin(), auth: false });
    const form = new FormData();
    for (const [k, v] of Object.entries(params)) {
        form.append(k, v);
    }

    try {
        const res = await client.request({
            method: "POST",
            path: "/o/oauth2/token",
            body: form,
            headers: form.getHeaders(),
            skipLog: { body: true, queryParams: true, resBody: true },
        });

        const tokens = res.body;
        if (!tokens.access_token && !tokens.refresh_token) {
            console.error("Error: Token response missing access_token/refresh_token:", tokens);
            process.exit(1);
        }

        const decodedUser = jwt.decode(tokens.id_token, { json: true }) || { email: "rgkdevx1@gmail.com" };

        configstore.set("user", decodedUser);
        configstore.set("tokens", tokens);
        configstore.set("loginScopes", SCOPES);
        configstore.delete("session");
        configstore.delete("tempLoginState");

        console.log("======================================================================");
        console.log("✅ SUCCESS! Logged in as:", decodedUser.email);
        console.log("Credentials stored in configstore.");
        console.log("======================================================================");
    } catch (err) {
        console.error("❌ OAuth Exchange Failed:", err.message);
        if (err.response?.body) {
            console.error("Response:", JSON.stringify(err.response.body, null, 2));
        }
        process.exit(1);
    }
}

run();
