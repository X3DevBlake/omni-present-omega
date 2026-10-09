#!/usr/bin/env python3
"""
Omni Swarm Communication, Code Sharing & Document Exchange Bus
Enables 55 autonomous agents to:
1. Talk and communicate with one another (messages, peer reviews, consensus)
2. Share and exchange code snippets, pull proposals, and bugfixes
3. Share and collaborate on documents (Google Docs, monographs, whitepapers)
"""

import os
import sys
import json
import time
from datetime import datetime, timezone

AUTOMATION_DIR = "/data/data/com.termux/files/home/omni-automation"
BUS_DIR = os.path.join(AUTOMATION_DIR, "bus")
SHARED_CODE_DIR = os.path.join(AUTOMATION_DIR, "shared_code")
SHARED_DOCS_DIR = os.path.join(AUTOMATION_DIR, "workspace_output", "docs")
MESSAGES_LOG = os.path.join(BUS_DIR, "messages.jsonl")
CODE_REGISTRY = os.path.join(SHARED_CODE_DIR, "registry.jsonl")

class SwarmCommunicationBus:
    def __init__(self):
        os.makedirs(BUS_DIR, exist_ok=True)
        os.makedirs(SHARED_CODE_DIR, exist_ok=True)
        os.makedirs(SHARED_DOCS_DIR, exist_ok=True)

    def send_message(self, sender_id, recipient_id, subject, body, msg_type="discussion"):
        """Sends an inter-agent message across the swarm bus."""
        msg_id = f"MSG-{int(time.time() * 1000)}"
        message = {
            "msg_id": msg_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "sender": sender_id,
            "recipient": recipient_id,  # Specific agent ID or "ALL" / "COUNCIL"
            "type": msg_type,
            "subject": subject,
            "body": body
        }

        with open(MESSAGES_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(message) + "\n")

        return message

    def get_inbox(self, agent_id, limit=20):
        """Fetches incoming messages for a specific agent or broadcast messages."""
        inbox = []
        if not os.path.exists(MESSAGES_LOG):
            return inbox

        with open(MESSAGES_LOG, "r", encoding="utf-8") as f:
            for line in reversed(f.readlines()):
                try:
                    msg = json.loads(line)
                    if msg.get("recipient") in [agent_id, "ALL", "COUNCIL"] or msg.get("sender") == agent_id:
                        inbox.append(msg)
                    if len(inbox) >= limit:
                        break
                except:
                    continue

        return inbox

    def share_code(self, author_id, filename, code_snippet, description):
        """Shares code between agents, saving file and logging to code registry."""
        file_path = os.path.join(SHARED_CODE_DIR, filename)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code_snippet)

        record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "author": author_id,
            "filename": filename,
            "path": file_path,
            "description": description,
            "bytes": len(code_snippet)
        }

        with open(CODE_REGISTRY, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

        # Broadcast notice on message bus
        self.send_message(
            author_id,
            "ALL",
            f"Code Shared: {filename}",
            f"Agent {author_id} shared {filename}: {description}",
            msg_type="code_share"
        )

        return record

    def share_document(self, author_id, title, html_body, tags=None):
        """Shares a document across the swarm and logs it to Google Docs directory."""
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")
        safe_title = "".join(c if c.isalnum() else "_" for c in title)
        doc_filename = f"Swarm_Doc_{safe_title}_{timestamp}.html"
        doc_path = os.path.join(SHARED_DOCS_DIR, doc_filename)

        full_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>{title}</title></head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: 40px auto; color: #1e293b;">
  <h1>{title}</h1>
  <div style="font-size: 0.85rem; color: #64748b;">Author: {author_id} • Created: {datetime.now(timezone.utc).isoformat()}</div>
  <hr style="border: 0; border-top: 1px solid #e2e8f0; margin: 20px 0;">
  {html_body}
</body>
</html>"""

        with open(doc_path, "w", encoding="utf-8") as f:
            f.write(full_html)

        # Broadcast notice
        self.send_message(
            author_id,
            "ALL",
            f"Document Shared: {title}",
            f"Agent {author_id} published document: {doc_filename}",
            msg_type="doc_share"
        )

        return doc_path

    def get_live_feed(self, limit=10):
        """Returns the latest inter-agent communication feed."""
        if not os.path.exists(MESSAGES_LOG):
            return []
        feed = []
        with open(MESSAGES_LOG, "r", encoding="utf-8") as f:
            for line in reversed(f.readlines()):
                try:
                    feed.append(json.loads(line))
                    if len(feed) >= limit:
                        break
                except:
                    continue
        return feed

if __name__ == "__main__":
    bus = SwarmCommunicationBus()
    msg = bus.send_message("omni-tech-director", "ALL", "Sprint Directives", "Initiating 4-hour active execution cycle.")
    code = bus.share_code("omni-rust-coder", "crdt_delta.rs", "// Zero-allocation causal dot\npub struct CausalDot { id: u64 }", "Rust CRDT lattice dot compression")
    print(f"Message ID: {msg['msg_id']}")
    print(f"Code Shared: {code['filename']}")
    print(f"Total Feed: {len(bus.get_live_feed())}")
