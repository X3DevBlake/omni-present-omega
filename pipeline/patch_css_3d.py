#!/usr/bin/env python3
"""
Appends 3D card tilt, charts, diagnostics UI, and mobile bottom dock styles
to css/liquid-glass.css, and verifies balanced braces and CSS variables.
"""

import os
import re

CSS_PATH = '/data/data/com.termux/files/home/omni-web/css/liquid-glass.css'

NEW_CSS = '''

/* ==========================================================================
   3D Card Tilt, Holographic Specular Lighting & Depth Refraction
   ========================================================================== */
.card-3d-tilt {
  position: relative;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), 
              box-shadow 0.3s ease, 
              border-color 0.3s ease;
  transform-style: preserve-3d;
}

.card-3d-tilt:hover {
  transform: translateY(-5px) scale(1.01);
  border-color: rgba(0, 242, 254, 0.4);
  box-shadow: 0 20px 40px -10px rgba(0, 242, 254, 0.2), 
              0 0 35px rgba(123, 97, 255, 0.15),
              var(--glass-specular-top);
}

.card-3d-tilt::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.6), transparent);
  opacity: 0.7;
}

/* ==========================================================================
   3D Graphs, Charts & Oscilloscope Panels
   ========================================================================== */
.chart-3d-container {
  position: relative;
  width: 100%;
  background: rgba(4, 7, 16, 0.85);
  border: 1px solid var(--glass-border-light);
  border-radius: 20px;
  padding: 1.5rem;
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), var(--glass-specular-top);
  margin-bottom: 2rem;
  overflow: hidden;
}

.chart-3d-canvas {
  width: 100%;
  height: 280px;
  display: block;
  border-radius: 12px;
  cursor: crosshair;
}

.chart-header-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.25rem;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.chart-metric-badge {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--gemini-cyan);
  background: rgba(0, 242, 254, 0.1);
  padding: 4px 10px;
  border-radius: 8px;
  border: 1px solid rgba(0, 242, 254, 0.25);
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

/* ==========================================================================
   3D System Diagnostics & Verification Suite UI
   ========================================================================== */
.diagnostics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.gauge-card-3d {
  background: rgba(8, 12, 24, 0.85);
  border: 1px solid var(--glass-border-light);
  border-radius: 20px;
  padding: 1.5rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease, border-color 0.3s ease;
}

.gauge-card-3d:hover {
  transform: translateY(-4px);
  border-color: var(--gemini-cyan);
}

.gauge-dial-canvas {
  width: 120px;
  height: 120px;
  margin: 0 auto 0.75rem;
  display: block;
}

.gauge-value {
  font-size: 1.6rem;
  font-weight: 800;
  font-family: var(--font-mono);
  color: #FFFFFF;
}

.gauge-label {
  font-size: 0.75rem;
  color: #94A3B8;
  font-family: var(--font-mono);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 4px;
}

.diag-suite-panel {
  background: rgba(6, 10, 20, 0.9);
  border: 1px solid var(--glass-border-light);
  border-radius: 24px;
  padding: 2rem;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8), var(--glass-specular-top);
  margin-bottom: 2.5rem;
}

.diag-stage-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1rem;
  margin-bottom: 0.5rem;
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  font-size: 0.85rem;
  transition: all 0.2s ease;
}

.diag-stage-row.passed {
  background: rgba(16, 185, 129, 0.06);
  border-color: rgba(16, 185, 129, 0.3);
}

.diag-stage-row.running {
  background: rgba(0, 242, 254, 0.08);
  border-color: var(--gemini-cyan);
  box-shadow: 0 0 15px rgba(0, 242, 254, 0.2);
}

/* ==========================================================================
   Mobile Bottom Quick-Action Dock & Touch Sizing
   ========================================================================== */
.mobile-bottom-dock {
  display: none;
}

@media (max-width: 768px) {
  .mobile-bottom-dock {
    display: flex;
    position: fixed;
    bottom: 12px;
    left: 12px;
    right: 12px;
    background: rgba(10, 14, 26, 0.94);
    backdrop-filter: blur(28px);
    -webkit-backdrop-filter: blur(28px);
    border: 1px solid rgba(0, 242, 254, 0.35);
    border-radius: 9999px;
    padding: 6px 12px;
    justify-content: space-around;
    align-items: center;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.9), 0 0 25px rgba(0, 242, 254, 0.2);
    z-index: 1200;
  }

  .mobile-dock-btn {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3px;
    color: #94A3B8;
    text-decoration: none;
    font-size: 0.65rem;
    font-family: var(--font-mono);
    padding: 6px 10px;
    border-radius: 12px;
    transition: all 0.2s ease;
  }

  .mobile-dock-btn.active,
  .mobile-dock-btn:hover {
    color: var(--gemini-cyan);
  }

  .mobile-dock-btn svg,
  .mobile-dock-btn img {
    width: 20px;
    height: 20px;
  }

  /* Min height for touchable buttons on mobile */
  .glass-btn,
  .blip-selector-btn,
  .modality-tab-btn {
    min-height: 44px;
  }

  /* Ensure comfortable padding above the fixed mobile dock */
  .app-container {
    padding-bottom: 6rem !important;
  }
}
'''

def main():
    with open(CSS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    if '.card-3d-tilt' not in content:
        content = content + NEW_CSS
        with open(CSS_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ Appended 3D styles and mobile dock to css/liquid-glass.css")

    # Validate braces & variables
    open_braces = content.count('{')
    close_braces = content.count('}')
    print(f"Braces balance: {open_braces} open, {close_braces} close -> {'OK' if open_braces == close_braces else 'MISMATCH'}")

    declared_vars = set(re.findall(r'--([a-zA-Z0-9_-]+):', content))
    used_vars = set(re.findall(r'var\(--([a-zA-Z0-9_-]+)\)', content))
    missing = used_vars - declared_vars
    if missing:
        print("ERROR: Missing variables:", missing)
        raise SystemExit(1)
    else:
        print(f"✓ CSS Variables OK: {len(declared_vars)} declared, {len(used_vars)} used, 0 missing!")

if __name__ == '__main__':
    main()
