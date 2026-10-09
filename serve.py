#!/data/data/com.termux/files/usr/bin/python3
"""
Omni-Present Omega (OPO) Liquid Glass Web Server
Launches a lightweight local HTTP server for the OPO web application.
"""

import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers for modern web development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

def run():
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            pass

    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), Handler) as httpd:
        print(f"\n" + "="*70)
        print(f"✨ OMNI-PRESENT OMEGA (OPO) LIQUID GLASS PORTAL")
        print(f"💫 Powered by Google Gemini SDK & Sovereign Delta-CRDT Mesh")
        print(f"="*70)
        print(f"📍 Local URL:    http://localhost:{port}")
        print(f"📍 Network URL:  http://127.0.0.1:{port}")
        print(f"📂 Serving from: {DIRECTORY}")
        print(f"="*70)
        print(f"Press Ctrl+C to stop the server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")

if __name__ == '__main__':
    run()
