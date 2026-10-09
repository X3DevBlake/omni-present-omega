#!/data/data/com.termux/files/usr/bin/python3
"""
Omni-Present Omega (OPO) Master Test Suite
Runs end-to-end lint, syntax, integrity, mathematical, multi-page, video, and pipeline verification.
"""

import sys
import os
import re
import glob
import subprocess
import urllib.request
import xml.etree.ElementTree as ET

OMNI_WEB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPO_STATED_DIR = "/data/data/com.termux/files/home/opo-stated"

passed_tests = 0
failed_tests = 0

def record_result(name, success, detail=""):
    global passed_tests, failed_tests
    if success:
        passed_tests += 1
        print(f"  ✓ {name}" + (f" ({detail})" if detail else ""))
    else:
        failed_tests += 1
        print(f"  ✗ {name}: {detail}")

print("=" * 70)
print("🛡️  RUNNING OPO MASTER SYSTEM VERIFICATION SUITE")
print("=" * 70)

# 1. JavaScript Syntax Check
print("\n[1/10] JavaScript Syntax & Parsing Check...")
res = subprocess.run(["node", "--check", "js/app.js"], cwd=OMNI_WEB_DIR, capture_output=True, text=True)
record_result("Node --check js/app.js", res.returncode == 0, res.stderr.strip())

# 2. CRDT Mathematical Semilattice Tests
print("\n[2/10] CRDT Semilattice Math Verification...")
res = subprocess.run(["node", "test/crdt_sim_test.js"], cwd=OMNI_WEB_DIR, capture_output=True, text=True)
record_result("Client-Side CRDT Join-Semilattice (S, ⊔, ≤)", res.returncode == 0, "Monotonicity, Commutativity, Idempotency, Deep-Copy")

# 3. All 13 SVGs XML and Gradient Integrity
print("\n[3/10] SVG Vector Asset & Gradient Reference Validation...")
svg_files = sorted(glob.glob(os.path.join(OMNI_WEB_DIR, "svg", "*.svg")))
all_svgs_ok = True
svg_detail = ""
for s in svg_files:
    filename = os.path.basename(s)
    try:
        ET.parse(s)
        content = open(s).read()
        urls = re.findall(r'url\(#([^)]+)\)', content)
        ids = set(re.findall(r'id=[\"\']([^\"\']+)[\"\']', content))
        for u in urls:
            if u not in ids:
                all_svgs_ok = False
                svg_detail = f"Undefined gradient/filter '#{u}' in {filename}"
                break
    except Exception as e:
        all_svgs_ok = False
        svg_detail = f"XML parse error in {filename}: {e}"
        break
record_result(f"All {len(svg_files)} SVGs (XML Parsing & Gradient IDs)", all_svgs_ok, svg_detail or f"{len(svg_files)} SVGs validated")

# 4. Multi-Page Enterprise Suite (10+ Pages Verification)
print("\n[4/10] Multi-Page Enterprise Suite Validation (At Least 10 Pages)...")
html_files = sorted(glob.glob(os.path.join(OMNI_WEB_DIR, "*.html")))
has_at_least_10 = len(html_files) >= 10
all_pages_valid = True
page_errors = []

for h in html_files:
    basename = os.path.basename(h)
    with open(h, encoding='utf-8') as f:
        c = f.read()
    if "<!DOCTYPE html>" not in c:
        all_pages_valid = False
        page_errors.append(f"{basename} missing DOCTYPE")
    if "liquid-glass.css" not in c:
        all_pages_valid = False
        page_errors.append(f"{basename} missing liquid-glass.css")
    if "app.js" not in c:
        all_pages_valid = False
        page_errors.append(f"{basename} missing app.js")

record_result(f"Multi-Page Count (Found {len(html_files)} Pages, Required >= 10)", has_at_least_10, f"{len(html_files)} HTML pages verified")
record_result("HTML Documents Structure & Shared Engine", all_pages_valid, ", ".join(page_errors) if page_errors else "All valid")

# 5. Video Assets & Video Player Integration
print("\n[5/10] HTML5 Video Assets & Stream Validation...")
video_files = [
    "assets/videos/hero-ambient-mesh.mp4",
    "assets/videos/hero-ambient-mesh.webm",
    "assets/videos/telemetry-stream.mp4",
    "assets/videos/telemetry-stream.webm"
]
all_videos_exist = True
video_details = []
for v in video_files:
    full_path = os.path.join(OMNI_WEB_DIR, v)
    if os.path.exists(full_path) and os.path.getsize(full_path) > 10000:
        video_details.append(f"{os.path.basename(v)} ({os.path.getsize(full_path)//1024} KB)")
    else:
        all_videos_exist = False
        video_details.append(f"MISSING: {v}")
record_result("HTML5 Video Assets (MP4 & WebM)", all_videos_exist, "; ".join(video_details))

# 6. CSS Validation
print("\n[6/10] CSS Syntax & Design System Variables...")
with open(os.path.join(OMNI_WEB_DIR, "css", "liquid-glass.css"), encoding='utf-8') as f:
    css_content = f.read()

open_braces = css_content.count('{')
close_braces = css_content.count('}')
braces_balanced = (open_braces == close_braces)
declared_vars = set(re.findall(r'--([a-zA-Z0-9_-]+):', css_content))
used_vars = set(re.findall(r'var\(--([a-zA-Z0-9_-]+)\)', css_content))
missing_vars = used_vars - declared_vars
record_result("CSS Balanced Braces", braces_balanced, f"{open_braces} blocks")
record_result("CSS Variable Declarations", len(missing_vars) == 0, f"{len(declared_vars)} declared, {len(used_vars)} used")

# 7. Python Multimodal Edge Pipeline Scripts
print("\n[7/10] Edge Sensor Fusion & Multimodal Pipeline...")
res_ekf = subprocess.run([sys.executable, "pipeline/ekf_tracker.py"], cwd=OMNI_WEB_DIR, capture_output=True, text=True)
record_result("Python EKF Tracker (Pure-Python Edge Embedded)", res_ekf.returncode == 0)

res_pipe = subprocess.run([sys.executable, "pipeline/pipecat_multimodal.py"], cwd=OMNI_WEB_DIR, capture_output=True, text=True)
record_result("Python Pipecat Multimodal WebRTC Pipeline", res_pipe.returncode == 0)

res_cli = subprocess.run([sys.executable, "pipeline/test_client.py", "--help"], cwd=OMNI_WEB_DIR, capture_output=True, text=True)
record_result("Python Test Client CLI Help", res_cli.returncode == 0 and "Usage:" in res_cli.stdout)

# 8. Rust opo-stated Daemon Unit Tests
print("\n[8/10] Rust opo-stated Join-Semilattice Unit Tests...")
res_cargo = subprocess.run(["cargo", "test"], cwd=OPO_STATED_DIR, capture_output=True, text=True)
has_4_passed = "4 passed" in res_cargo.stdout
record_result("Rust cargo test in opo-stated", res_cargo.returncode == 0 and has_4_passed, "4 unittests passed: test_state_vector, test_delta_mutation, test_commutative_merge, test_anti_entropy_diff")

# 9. Local HTTP Web Server Multi-Page Availability
print("\n[9/10] Local HTTP Server Multi-Page Routing (Port 8080)...")
server_all_ok = True
pages_checked = []
for h in html_files:
    bname = os.path.basename(h)
    url = f"http://localhost:8080/{bname}"
    try:
        req = urllib.request.urlopen(url, timeout=3)
        if req.status != 200:
            server_all_ok = False
            pages_checked.append(f"{bname}: {req.status}")
    except Exception as e:
        server_all_ok = False
        pages_checked.append(f"{bname}: {e}")
record_result(f"HTTP 200 OK on all {len(html_files)} pages from http://localhost:8080/", server_all_ok, f"{len(html_files)} endpoints served")

# 10. Local Asset Integrity for Index
print("\n[10/10] Local Asset References & Image Integrity...")
with open(os.path.join(OMNI_WEB_DIR, "index.html"), encoding='utf-8') as f:
    idx_content = f.read()
srcs = re.findall(r'src=[\"\']([^\"\']+)[\"\']', idx_content)
missing_local_srcs = [s for s in srcs if not s.startswith("http") and not os.path.exists(os.path.join(OMNI_WEB_DIR, s))]
record_result("Index Local Image/Script References", len(missing_local_srcs) == 0, f"{len(srcs)} src tags verified")

print("\n" + "=" * 70)
print(f"📊 VERIFICATION SUMMARY: {passed_tests} PASSED, {failed_tests} FAILED")
print("=" * 70)

sys.exit(0 if failed_tests == 0 else 1)
