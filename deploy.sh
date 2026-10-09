#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "=========================================================="
echo "🔥 OMNI-PRESENT OMEGA (OPO) FIREBASE DEPLOYMENT ASSISTANT"
echo "Target Account: rgkdevx1@gmail.com"
echo "Target Project: omni-present-omega"
echo "=========================================================="

cd "$(dirname "$0")"

# 1. Run Integrity & Syntax Check
echo "🔍 Running comprehensive system verification suite..."
python3 test/run_tests.py
echo "✓ All pre-flight checks passed."

# 2. Check Firebase Authentication
echo "🔍 Verifying Firebase authentication..."
if firebase projects:list > /dev/null 2>&1; then
    echo "✓ Firebase credentials active."
else
    echo ""
    echo "⚠️  Firebase is not authenticated yet in this terminal environment."
    echo "👉 To sign in with rgkdevx1@gmail.com, run:"
    echo ""
    echo "   firebase login --no-localhost"
    echo ""
    echo "   Copy the verification URL into your browser, grant permissions,"
    echo "   and paste the authorization code back here."
    echo ""
    exit 1
fi

# 3. Deploy Hosting
echo "🚀 Deploying hosting assets to Google Firebase CDN..."
firebase deploy --only hosting

echo ""
echo "✨ Deployment successful!"
echo "🌐 Production URL: https://omni-present-omega.web.app"
echo "🌐 Custom Domain:  https://omni-present-omega.firebaseapp.com"
