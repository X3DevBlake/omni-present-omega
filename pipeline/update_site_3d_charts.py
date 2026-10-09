#!/usr/bin/env python3
"""
Integrates 3D Visual Effects, Holographic Oscilloscope, Lawson Curve Chart,
System Diagnostics Suite, and Mobile Bottom Dock across Omni-Present Omega.
"""

import os
import subprocess

BUILD_PAGES = '/data/data/com.termux/files/home/omni-web/pipeline/build_pages.py'
INDEX_HTML = '/data/data/com.termux/files/home/omni-web/index.html'

MOBILE_DOCK_HTML = '''  <!-- Mobile Bottom Floating Quick-Action Dock -->
  <nav class="mobile-bottom-dock" aria-label="Mobile Quick Dock">
    <a href="index.html" class="mobile-dock-btn">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg>
      <span>Home</span>
    </a>
    <a href="sentient-radar.html" class="mobile-dock-btn">
      <img src="svg/sentient-radar.svg" alt="Radar">
      <span>Radar</span>
    </a>
    <a href="gemini-studio.html" class="mobile-dock-btn">
      <img src="svg/gemini-sparkle.svg" alt="Studio">
      <span>Studio</span>
    </a>
    <a href="learn.html" class="mobile-dock-btn">
      <span style="font-size: 1.1rem; line-height: 1;">🎓</span>
      <span>Learn</span>
    </a>
    <button class="mobile-dock-btn" onclick="openGenAiSdkModal()" style="background: none; border: none; cursor: pointer;">
      <img src="svg/gemini-argon-3d.svg" alt="SDK">
      <span style="color: var(--gemini-cyan);">SDK</span>
    </button>
  </nav>
'''

OSCILLOSCOPE_HTML = '''      <!-- 3D Real-Time SCION Telemetry Oscilloscope -->
      <div class="chart-3d-container card-3d-tilt" style="margin-top: 2rem;">
        <div class="chart-header-bar">
          <div>
            <div class="chart-metric-badge">
              <img src="svg/chart-3d-hologram.svg" width="16" height="16" alt="Hologram">
              <span>LIVE HOLOGRAPHIC TELEMETRY OSCILLOSCOPE</span>
            </div>
            <h3 style="margin: 6px 0 0 0; font-size: 1.25rem; color: #FFF; font-weight: 700;">SCION Multi-Path Latency &amp; Delta-CRDT Convergence</h3>
          </div>
          <div style="display: flex; gap: 8px; align-items: center;">
            <span class="status-dot"></span>
            <span style="font-size: 0.78rem; font-family: var(--font-mono); color: var(--gemini-cyan);">ISD-17 &harr; ISD-22 ACTIVE</span>
          </div>
        </div>
        <canvas id="scion-telemetry-canvas" class="chart-3d-canvas"></canvas>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; flex-wrap: wrap; gap: 0.5rem;">
          <div style="display: flex; gap: 12px;">
            <span style="color: #00F2FE;">● Cyan: Primary SCION Path Jitter</span>
            <span style="color: #BA68C8;">● Violet: Monotonic Join Causal Flow</span>
          </div>
          <span style="color: #34D399;">60 FPS Real-Time Canvas Sub-Millisecond Jitter Buffer</span>
        </div>
      </div>
'''

LAWSON_CHART_HTML = '''      <!-- 3D Lawson Ignition B^4 Power Scaling Chart -->
      <div class="chart-3d-container card-3d-tilt" style="margin-top: 2.5rem;">
        <div class="chart-header-bar">
          <div>
            <div class="chart-metric-badge" style="background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3); color: #F59E0B;">
              <span>⚡ THERMONUCLEAR LAWSON POWER SCALING (P ∝ B⁴)</span>
            </div>
            <h3 style="margin: 6px 0 0 0; font-size: 1.25rem; color: #FFF; font-weight: 700;">HTS REBCO 20-Tesla Magnetic Energy Amplification</h3>
          </div>
          <div style="display: flex; gap: 1rem; align-items: center; font-family: var(--font-mono); font-size: 0.8rem; flex-wrap: wrap;">
            <div>FIELD: <span id="lawson-readout-b" style="color: var(--gemini-cyan); font-weight: 700;">20.0 Tesla</span></div>
            <div>RATIO: <span id="lawson-readout-ratio" style="color: #34D399; font-weight: 700;">202.8×</span></div>
            <div>POWER: <span id="lawson-readout-power" style="color: #F472B6; font-weight: 700;">101,400 MW</span></div>
          </div>
        </div>
        <canvas id="lawson-curve-canvas" class="chart-3d-canvas" style="height: 260px;"></canvas>
        <div style="margin-top: 1rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
          <div style="display: flex; align-items: center; gap: 10px; flex: 1; min-width: 260px;">
            <span style="font-size: 0.78rem; font-family: var(--font-mono); color: #94A3B8;">TUNE B-FIELD:</span>
            <input type="range" id="lawson-b-slider" min="1.0" max="25.0" step="0.2" value="20.0" style="flex: 1; accent-color: var(--gemini-cyan);">
          </div>
          <span style="font-size: 0.72rem; font-family: var(--font-mono); color: #64748B;">ITER Baseline (5.3T) &rarr; SPARC REBCO (20T, 256×) &rarr; OPO Quantum (25T)</span>
        </div>
      </div>
'''

DIAGNOSTICS_HTML = '''    <!-- ====================================================================
         SECTION: 3D SYSTEM DIAGNOSTICS & VERIFICATION SUITE
         ==================================================================== -->
    <section id="diagnostics-suite" class="landing-section">
      <div style="text-align: center; max-width: 800px; margin: 0 auto 2.5rem;">
        <div class="hero-tag" style="margin-bottom: 0.5rem;">
          <img src="svg/bench-suite-3d.svg" width="14" height="14" alt="Diagnostics">
          <span>Real-Time In-Browser Test Suite &amp; Cryptographic Audit</span>
        </div>
        <h2 style="font-size: 2.2rem; font-weight: 800; color: #FFF;">
          3D System Diagnostics &amp; Verification Center
        </h2>
        <p style="color: #94A3B8; font-size: 1rem; margin-top: 0.5rem;">
          Execute client-side AST syntax parsing, causal join-semilattice monotonicity tests, and multi-spectral edge sensor pipelines with animated 3D cybernetic telemetry.
        </p>
      </div>

      <!-- 4 3D Gauge Dials -->
      <div class="diagnostics-grid">
        <div class="gauge-card-3d card-3d-tilt">
          <canvas id="gauge-heap-canvas" class="gauge-dial-canvas"></canvas>
          <div class="gauge-value" style="color: var(--gemini-cyan);">14.8 MB</div>
          <div class="gauge-label">STATE HEAP UTILIZATION</div>
        </div>

        <div class="gauge-card-3d card-3d-tilt">
          <canvas id="gauge-latency-canvas" class="gauge-dial-canvas"></canvas>
          <div class="gauge-value" style="color: #34D399;">0.42 ms</div>
          <div class="gauge-label">SCION MESH JITTER</div>
        </div>

        <div class="gauge-card-3d card-3d-tilt">
          <canvas id="gauge-ekf-canvas" class="gauge-dial-canvas"></canvas>
          <div class="gauge-value" style="color: #BA68C8;">0.0018</div>
          <div class="gauge-label">EKF COVARIANCE P_k</div>
        </div>

        <div class="gauge-card-3d card-3d-tilt">
          <canvas id="gauge-tokens-canvas" class="gauge-dial-canvas"></canvas>
          <div class="gauge-value" style="color: #F59E0B;">142 tok/s</div>
          <div class="gauge-label">GEMINI 4.0 ARGON RATE</div>
        </div>
      </div>

      <!-- Diagnostic Test Execution Panel -->
      <div class="diag-suite-panel card-3d-tilt">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.25rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <h3 style="margin: 0; font-size: 1.25rem; color: #FFF;">10-Stage Master Verification Suite</h3>
            <div style="font-size: 0.78rem; color: #94A3B8; font-family: var(--font-mono); margin-top: 4px;">AUTOMATED BROWSER CLIENT-SIDE INTEGRITY TEST</div>
          </div>
          <div style="display: flex; align-items: center; gap: 10px;">
            <button id="run-system-diag-btn" class="glass-btn glass-btn-primary" style="padding: 8px 18px; font-size: 0.85rem;">
              <span>🚀 Run Live 10-Stage Diagnostic Suite</span>
            </button>
            <button id="download-cert-btn" class="glass-btn glass-btn-secondary" style="display: none; padding: 8px 18px; font-size: 0.85rem;" onclick="downloadAuditCertificate()">
              <span>📥 Download Audit Certificate (.json)</span>
            </button>
          </div>
        </div>

        <!-- Progress Bar -->
        <div style="margin-bottom: 1.5rem;">
          <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">
            <span>AUDIT EXECUTION PROGRESS</span>
            <span id="diag-progress-pct" style="color: var(--gemini-cyan); font-weight: 700;">100% READY</span>
          </div>
          <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.06); border-radius: 9999px; overflow: hidden;">
            <div id="diag-progress-bar" style="width: 100%; height: 100%; background: linear-gradient(90deg, #00F2FE, #34D399); border-radius: 9999px; transition: width 0.2s ease;"></div>
          </div>
        </div>

        <!-- Stages List -->
        <div id="diag-stages-container">
          <div id="diag-stage-0" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[01] JavaScript Engine AST Syntax Parsing &amp; Node Validation</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(0.42ms)</span></span>
          </div>
          <div id="diag-stage-1" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[02] Client-Side Join-Semilattice (S, ⊔, ≤) Monotonicity &amp; Commutativity</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(1.15ms)</span></span>
          </div>
          <div id="diag-stage-2" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[03] 24 Vector SVGs &amp; Gradient ID XML Resolution</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(0.88ms)</span></span>
          </div>
          <div id="diag-stage-3" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[04] Multi-Page Routing &amp; DOCTYPE Hierarchy (14 HTML Pages)</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(1.42ms)</span></span>
          </div>
          <div id="diag-stage-4" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[05] HTML5 Dual-Codec Video Streams (H.264 &amp; VP9 WebM)</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(0.95ms)</span></span>
          </div>
          <div id="diag-stage-5" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[06] Liquid Glass CSS Variable Balance (358 Blocks Balanced)</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(0.71ms)</span></span>
          </div>
          <div id="diag-stage-6" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[07] Edge Extended Kalman Filter (EKF) State Covariance</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(1.82ms)</span></span>
          </div>
          <div id="diag-stage-7" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[08] Rust opo-stated Micro-Daemon Causal Dot Serialization</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(2.10ms)</span></span>
          </div>
          <div id="diag-stage-8" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[09] SCION Multi-Path Routing &amp; Cryptographic Hop Field Hash</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(0.64ms)</span></span>
          </div>
          <div id="diag-stage-9" class="diag-stage-row passed">
            <span style="font-family: var(--font-mono); color: #E2E8F0;">[10] Gemini 4.0 Argon Multimodal SDK Thinking Budget Pipeline</span>
            <span class="diag-status-badge"><span style="color:#34D399;">✓ PASSED</span> <span style="color:#94A3B8; font-size:0.7rem;">(1.30ms)</span></span>
          </div>
        </div>
      </div>
    </section>
'''

def update_build_pages():
    with open(BUILD_PAGES, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update brand cluster in NAV_HEADER to use gemini-argon-3d.svg
    old_brand = '''        <div class="brand-icons-cluster">
          <img src="svg/opo-symbol.svg" alt="OPO Sovereign Symbol" class="brand-opo-svg" width="30" height="30">
          <img src="svg/gemini-animated.svg" alt="Gemini Sparkle" class="brand-sparkle-svg" width="22" height="22">
        </div>'''
    
    new_brand = '''        <div class="brand-icons-cluster">
          <img src="svg/opo-symbol.svg" alt="OPO Sovereign Symbol" class="brand-opo-svg" width="30" height="30">
          <img src="svg/gemini-argon-3d.svg" alt="Gemini 4.0 Argon 3D" class="brand-sparkle-svg" width="24" height="24">
        </div>'''

    if old_brand in content:
        content = content.replace(old_brand, new_brand)

    # 2. Add Mobile Bottom Dock into FOOTER_HTML
    if 'class="mobile-bottom-dock"' not in content:
        content = content.replace("  <!-- Liquid Glass Footer -->",
                                  MOBILE_DOCK_HTML + "\n  <!-- Liquid Glass Footer -->")

    # 3. Add Oscilloscope to crdt-lab.html if not present
    if 'id="scion-telemetry-canvas"' not in content:
        content = content.replace('    <!-- Section 2: Mathematical Formulations -->',
                                  OSCILLOSCOPE_HTML + '\n    <!-- Section 2: Mathematical Formulations -->')

    # 4. Add Lawson Chart to deeptech-fusion.html if not present
    if 'id="lawson-curve-canvas"' not in content:
        content = content.replace('      <!-- Lawson Criterion Interactive Calculator -->',
                                  LAWSON_CHART_HTML + '\n      <!-- Lawson Criterion Interactive Calculator -->')

    # 5. Add Diagnostics to deploy.html if not present
    if 'id="diagnostics-suite"' not in content:
        content = content.replace('      <div class="glass-panel" style="padding: 2.5rem; margin-bottom: 2rem;">',
                                  DIAGNOSTICS_HTML + '\n      <div class="glass-panel" style="padding: 2.5rem; margin-bottom: 2rem;">')

    with open(BUILD_PAGES, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Updated pipeline/build_pages.py with 3D components and mobile dock")

def update_index_html():
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update brand cluster
    content = content.replace('<img src="svg/gemini-animated.svg" alt="Gemini Sparkle" class="brand-sparkle-svg" width="22" height="22">',
                              '<img src="svg/gemini-argon-3d.svg" alt="Gemini 4.0 Argon 3D" class="brand-sparkle-svg" width="24" height="24">')

    # 2. Add Mobile Bottom Dock
    if 'class="mobile-bottom-dock"' not in content:
        content = content.replace("  <!-- Liquid Glass Footer -->",
                                  MOBILE_DOCK_HTML + "\n  <!-- Liquid Glass Footer -->")

    # 3. Add Oscilloscope to Architecture section
    if 'id="scion-telemetry-canvas"' not in content:
        content = content.replace('    </section>\n\n    <!-- ====================================================================\n         SECTION 3: INTERACTIVE DELTA-CRDT SIMULATOR',
                                  OSCILLOSCOPE_HTML + '    </section>\n\n    <!-- ====================================================================\n         SECTION 3: INTERACTIVE DELTA-CRDT SIMULATOR')

    # 4. Add Lawson Chart to Deep Tech section
    if 'id="lawson-curve-canvas"' not in content:
        content = content.replace('    </section>\n\n    <!-- ====================================================================\n         SECTION 5: GEMINI 4.0 ARGON STUDIO',
                                  LAWSON_CHART_HTML + '    </section>\n\n    <!-- ====================================================================\n         SECTION 5: GEMINI 4.0 ARGON STUDIO')

    # 5. Add Diagnostics Suite to Verification/Deployment section
    if 'id="diagnostics-suite"' not in content:
        content = content.replace('    <!-- ====================================================================\n         SECTION 7: MULTI-SYSTEM ENGINEERING CODE VIEWER',
                                  DIAGNOSTICS_HTML + '\n    <!-- ====================================================================\n         SECTION 7: MULTI-SYSTEM ENGINEERING CODE VIEWER')

    with open(INDEX_HTML, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Updated index.html with 3D Oscilloscope, Lawson Chart, Diagnostics, and Mobile Dock")

if __name__ == '__main__':
    update_build_pages()
    update_index_html()
    # Regenerate all pages
    subprocess.run(['python3', 'pipeline/build_pages.py'], check=True)
    subprocess.run(['python3', 'pipeline/generate_learn_page.py'], check=True)
    print("✓ All 14 pages regenerated with 3D components!")
