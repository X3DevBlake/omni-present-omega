#!/data/data/com.termux/files/usr/bin/python3
"""
OPO Sovereign Delta-CRDT Test Client
Communicates with running `opo-stated` local control TCP socket.
"""

import socket
import json
import sys

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8001

def send_command(cmd_dict, host=DEFAULT_HOST, port=DEFAULT_PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        payload = json.dumps(cmd_dict).encode("utf-8")
        sock.sendall(payload)
        resp = sock.recv(65535).decode("utf-8")
        return json.loads(resp)
    finally:
        sock.close()

def main():
    if len(sys.argv) < 2 or sys.argv[1].lower() in ("-h", "--help", "help"):
        print("Usage:")
        print("  python3 test_client.py put <key> <json_value> [port]")
        print("  python3 test_client.py get <key> [port]")
        print("  python3 test_client.py dump [port]")
        print("\nExamples:")
        print("  python3 test_client.py put spatial_focus '{\"target\": \"viewport_1\", \"zoom\": 1.45}' 8001")
        print("  python3 test_client.py get spatial_focus 8002")
        print("  python3 test_client.py dump 8001")
        return

    action = sys.argv[1].lower()

    if action == "put":
        if len(sys.argv) < 4:
            print("Error: 'put' requires <key> and <value>")
            return
        key = sys.argv[2]
        raw_val = sys.argv[3]
        try:
            val = json.loads(raw_val)
        except Exception:
            val = raw_val
        port = int(sys.argv[4]) if len(sys.argv) > 4 else DEFAULT_PORT
        cmd = {"Put": {"key": key, "value": val}}
        res = send_command(cmd, port=port)
        print(f"Put response from port {port}:", json.dumps(res, indent=2))

    elif action == "get":
        if len(sys.argv) < 3:
            print("Error: 'get' requires <key>")
            return
        key = sys.argv[2]
        port = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_PORT
        cmd = {"Get": {"key": key}}
        res = send_command(cmd, port=port)
        print(f"Get response from port {port}:", json.dumps(res, indent=2))

    elif action == "dump":
        port = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_PORT
        cmd = "Dump"
        res = send_command(cmd, port=port)
        print(f"Lattice Dump from port {port}:", json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
