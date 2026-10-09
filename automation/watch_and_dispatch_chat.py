#!/usr/bin/env python3
"""
Watches for Google Chat API activation on project 1036007047880.
As soon as the user enables the API in Google Cloud Console,
dispatches the CEO operational briefing into Google Chat immediately.
"""

import os
import sys
import time
import requests
import json

OMNI_HOME = "/data/data/com.termux/files/home"
AUTOMATION_DIR = os.path.join(OMNI_HOME, "omni-automation")
CREDENTIALS_DIR = os.path.join(AUTOMATION_DIR, "credentials")
TOKEN_FILE = os.path.join(CREDENTIALS_DIR, "token.json")

sys.path.insert(0, AUTOMATION_DIR)
from dispatch_google_chat import dispatch_chat, check_chat_api

print("🚀 [Google Chat Watcher] Waiting for Google Chat API activation on project 1036007047880...")
max_checks = 120  # check for up to 10 minutes

for i in range(max_checks):
    status, text = check_chat_api()
    if status == 200:
        print("\n🎉 [Google Chat Watcher] Google Chat API is now ACTIVE!")
        ok, res = dispatch_chat()
        if ok:
            print(f"✓ Message delivered to Google Chat! (ID: {res})")
            sys.exit(0)
        else:
            print(f"⚠️ Dispatch attempt note: {res}")
            sys.exit(1)
    elif i % 6 == 0:
        print(f"[{i*5}s] Awaiting API activation... (Status: {status})")
    time.sleep(5)

print("\n[Google Chat Watcher] Timed out waiting for API activation. Run 'python3 dispatch_google_chat.py' once enabled.")
