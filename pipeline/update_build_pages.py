#!/usr/bin/env python3
"""
Updates pipeline/build_pages.py to add sentient-radar.html to NAV_HEADER,
FOOTER_HTML, and the PAGES dictionary, then generates all pages.
"""
import os
import re
import sys

BUILD_PAGES_PATH = '/data/data/com.termux/files/home/omni-web/pipeline/build_pages.py'

SENTIENT_PAGE_CODE = '''
# 12. sentient-radar.html (Project SENTIENT Multi-Spectral Radar & Multi-Agent Swarm)
PAGES['sentient-radar.html'] = render_page(
    title="Project SENTIENT Radar & Swarm Deliberation",
    desc="60 FPS Multi-Spectral Radar, 5-Agent Swarm Deliberation (Vortex, Spectre, Chronos, Nexus, Omni), MHD Plasma Sheath Calculator, and Zero-Knowledge Whistleblower Portal.",
    current_breadcrumb='<a href="sentient-radar.html">Intelligence</a> <span class="sep">/</span> <span class="current">Project SENTIENT &amp; Swarm</span>',
    body_content=\'\'\'    <!-- Hero Section -->
    <section class="landing-section">
      <div class="section-badge" style="border-color: rgba(0, 242, 254, 0.4); color: var(--gemini-cyan);">
        <img src="svg/sentient-radar.svg" width="16" height="16" alt="Radar">
        <span>NRO PROJECT SENTIENT // 60 FPS ORBITAL MULTI-SPECTRAL RADAR &amp; SWARM</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">Project SENTIENT Radar &amp; Swarm Overlord</span>
      </h1>
      <p class="hero-desc" style="max-width: 860px; margin: 0 auto 2.5rem;">
        Direct edge implementation of National Reconnaissance Office (NRO) <strong>Project SENTIENT</strong> automated orbital cross-tasking protocols, 60 FPS multi-spectral non-Newtonian radar tracking, and autonomous 5-agent deliberation (Vortex, Spectre, Chronos, Nexus, Omni) running on <strong>Google Gemini 4.0 Argon</strong>.
      </p>

      <!-- Navigation Anchor Pills -->
      <div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 3rem;">
        <a href="#radar-scope-section" class="glass-btn glass-btn-primary">
          <span>📡 60 FPS Radar Scope</span>
        </a>
        <a href="#swarm-deliberation-section" class="glass-btn glass-btn-secondary">
          <span>🧠 5-Agent Swarm Overlord</span>
        </a>
        <a href="#mhd-calculator-section" class="glass-btn glass-btn-secondary">
          <span>⚡ MHD Plasma Sheath Engine</span>
        </a>
        <a href="#whistleblower-section" class="glass-btn glass-btn-secondary">
          <span>🔒 Zero-Knowledge Vault</span>
        </a>
        <a href="#foia-vault-section" class="glass-btn glass-btn-secondary">
          <span>📂 Declassified FOIA Files</span>
        </a>
      </div>
    </section>

    <!-- SECTION 1: 60 FPS MULTI-SPECTRAL RADAR SCOPE & HUD -->
    <section id="radar-scope-section" class="landing-section" style="padding-top: 1rem;">
      <div class="section-badge">
        <img src="svg/sentient-radar.svg" width="16" height="16" alt="Scope">
        <span>60 FPS REAL-TIME SENSOR SWEEP // EKF INTEGRATED</span>
      </div>
      <h2 style="font-size: 2rem; color: #FFFFFF; margin-bottom: 0.75rem;">
        Multi-Spectral Radar Scope &amp; Target Telemetry HUD
      </h2>
      <p style="color: #94A3B8; max-width: 800px; margin-bottom: 2rem; line-height: 1.6;">
        Interact directly with the radar sweep canvas. Click on anomalous contacts to lock telemetry vectors, examine non-Newtonian kinematics (Mach 18+, 850G instant acceleration), and trigger multi-agent consensus protocols.
      </p>

      <div class="sentient-radar-grid">
        <!-- Left: Interactive Radar Scope -->
        <div class="glass-panel" style="padding: 1.5rem; display: flex; flex-direction: column; align-items: center;">
          <!-- Filter Buttons -->
          <div style="display: flex; gap: 6px; flex-wrap: wrap; justify-content: center; margin-bottom: 1.25rem; width: 100%;">
            <button class="radar-spectrum-filter-btn modality-tab-btn active" data-spectrum="all" style="padding: 4px 10px; font-size: 0.75rem;">📡 All Spectra (5)</button>
            <button class="radar-spectrum-filter-btn modality-tab-btn" data-spectrum="atflir" style="padding: 4px 10px; font-size: 0.75rem;">🎯 ATFLIR</button>
            <button class="radar-spectrum-filter-btn modality-tab-btn" data-spectrum="sar" style="padding: 4px 10px; font-size: 0.75rem;">⚡ SAR Radar</button>
            <button class="radar-spectrum-filter-btn modality-tab-btn" data-spectrum="leo" style="padding: 4px 10px; font-size: 0.75rem;">🛰️ LEO Orbit</button>
            <button class="radar-spectrum-filter-btn modality-tab-btn" data-spectrum="sub" style="padding: 4px 10px; font-size: 0.75rem;">🌊 Trans-Medium</button>
          </div>

          <!-- Radar Scope Canvas Container -->
          <div class="radar-scope-container">
            <canvas id="sentient-radar-canvas" width="480" height="480" class="radar-canvas-element" title="Interactive Radar Scope: Click any contact blip to lock target"></canvas>
          </div>

          <!-- Scope Controls -->
          <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-top: 1.25rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.06); font-size: 0.78rem; font-family: var(--font-mono); color: #94A3B8;">
            <div style="display: flex; align-items: center; gap: 8px;">
              <span>SWEEP SPEED:</span>
              <input type="range" id="radar-speed-slider" min="0.5" max="3.0" step="0.1" value="1.2" style="width: 90px; accent-color: var(--gemini-cyan);">
            </div>
            <div style="display: flex; align-items: center; gap: 6px;">
              <span class="status-dot"></span>
              <span style="color: var(--gemini-cyan);">60 FPS PHOSPHOR SWEEP</span>
            </div>
          </div>
        </div>

        <!-- Right: Telemetry HUD & Target Selector -->
        <div>
          <!-- Target Selector List -->
          <div style="margin-bottom: 1rem;">
            <div style="font-size: 0.8rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">
              Active Sensor Tracks (Click to Lock Target):
            </div>
            <div id="radar-blip-list"></div>
          </div>

          <!-- Live Telemetry HUD Panel -->
          <div class="radar-hud-panel">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 0.75rem;">
              <div style="display: flex; align-items: center; gap: 8px;">
                <span id="hud-target-id" class="brand-badge" style="background: rgba(0,242,254,0.15); color: var(--gemini-cyan); border-color: rgba(0,242,254,0.3); font-size: 0.8rem;">RAD-01</span>
                <span id="hud-target-class" style="font-size: 0.7rem; font-family: var(--font-mono); color: #EF4444; background: rgba(239,68,68,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(239,68,68,0.3);">TOP SECRET // NOFORN</span>
              </div>
              <span class="status-dot"></span>
            </div>

            <h3 id="hud-target-name" style="margin: 0 0 1rem 0; font-size: 1.3rem; color: #FFFFFF; font-weight: 700;">USS Nimitz Tic-Tac</h3>

            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">CLASSIFICATION TYPE:</span>
              <span id="hud-target-type" class="radar-telemetry-value">Hypersonic Non-Newtonian</span>
            </div>
            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">RANGE &amp; BEARING:</span>
              <span class="radar-telemetry-value"><span id="hud-target-range">28.4 km</span> @ <span id="hud-target-bearing">042°</span></span>
            </div>
            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">ALTITUDE VECTOR:</span>
              <span id="hud-target-alt" class="radar-telemetry-value">80,000 → 50 (0.78s)</span>
            </div>
            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">CALCULATED VELOCITY:</span>
              <span id="hud-target-velocity" class="radar-telemetry-value" style="color: #34D399;">Mach 18.4 (22,500 km/h)</span>
            </div>
            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">INSTANTANEOUS ACCEL:</span>
              <span id="hud-target-accel" class="radar-telemetry-value" style="color: #F87171;">850+ G</span>
            </div>
            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">SENSOR SPECTRUM:</span>
              <span id="hud-target-sensor" class="radar-telemetry-value">ATFLIR / AN/SPY-1B Radar</span>
            </div>

            <div id="hud-target-desc" style="margin-top: 1rem; padding: 0.9rem; background: rgba(0,0,0,0.5); border-radius: 10px; font-size: 0.8rem; line-height: 1.6; color: #CBD5E1; border: 1px solid rgba(255,255,255,0.05);">
              Oblong white cylinder (~40ft). Zero thermal exhaust plume, zero wings or control surfaces, instantaneous non-Newtonian deceleration without sonic boom.
            </div>

            <!-- Action Controls -->
            <div style="display: flex; gap: 0.5rem; margin-top: 1.25rem; flex-wrap: wrap;">
              <button class="glass-btn glass-btn-primary" style="flex: 1; font-size: 0.8rem; padding: 8px 12px;" onclick="window.swarmEngine.startDeliberation(window.sentientRadar.activeBlipId)">
                <span>⚡ Run Swarm Deliberation</span>
              </button>
              <button class="glass-btn glass-btn-secondary" style="font-size: 0.8rem; padding: 8px 12px;" onclick="window.swarmEngine.synthesizeReport()">
                <span>📥 Export Signed Telemetry</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: MULTI-AGENT SWARM DELIBERATION CONSOLE -->
    <section id="swarm-deliberation-section" class="landing-section">
      <div class="section-badge" style="border-color: rgba(123, 97, 255, 0.4); color: #A5B4FC;">
        <img src="svg/swarm-intelligence.svg" width="16" height="16" alt="Swarm">
        <span>GEMINI 4.0 ARGON // 5-AGENT DELIBERATION PROTOCOL</span>
      </div>
      <h2 style="font-size: 2rem; color: #FFFFFF; margin-bottom: 0.75rem;">
        Autonomous Multi-Agent Swarm Deliberation Console
      </h2>
      <p style="color: #94A3B8; max-width: 820px; margin-bottom: 2rem; line-height: 1.6;">
        Five specialized autonomous reasoning models running Google Gemini 4.0 Argon continuously debate aerodynamic observations, electromagnetic telemetry, and chronometric synchronization to formulate unified, cryptographically signed hypotheses.
      </p>

      <!-- 5-Agent Architecture Cards -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
        <div class="glass-panel" style="padding: 1.2rem; border-top: 2px solid #00F2FE;">
          <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">⚡</div>
          <div style="font-weight: 700; color: #FFF; font-size: 0.95rem;">Agent Vortex</div>
          <div style="font-size: 0.72rem; color: #00F2FE; font-family: var(--font-mono); margin-bottom: 0.5rem;">AERODYNAMICS &amp; MHD</div>
          <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;">Evaluates boundary layer fluid dynamics, Reynolds numbers, and plasma cavitation.</div>
        </div>

        <div class="glass-panel" style="padding: 1.2rem; border-top: 2px solid #7B61FF;">
          <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🟣</div>
          <div style="font-weight: 700; color: #FFF; font-size: 0.95rem;">Agent Spectre</div>
          <div style="font-size: 0.72rem; color: #A5B4FC; font-family: var(--font-mono); margin-bottom: 0.5rem;">EW &amp; SIGINT ANALYST</div>
          <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;">Analyzes RF emissions, radar jamming, avionics interlocks, and microwave ionization.</div>
        </div>

        <div class="glass-panel" style="padding: 1.2rem; border-top: 2px solid #FFB800;">
          <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🟡</div>
          <div style="font-weight: 700; color: #FFF; font-size: 0.95rem;">Agent Chronos</div>
          <div style="font-size: 0.72rem; color: #FCD34D; font-family: var(--font-mono); margin-bottom: 0.5rem;">TEMPORAL CHRONOMETRY</div>
          <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;">Correlates high-frequency sensor timestamps across distributed ground and orbital arrays.</div>
        </div>

        <div class="glass-panel" style="padding: 1.2rem; border-top: 2px solid #00E676;">
          <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🟢</div>
          <div style="font-weight: 700; color: #FFF; font-size: 0.95rem;">Agent Nexus</div>
          <div style="font-size: 0.72rem; color: #34D399; font-family: var(--font-mono); margin-bottom: 0.5rem;">DELTA-CRDT MESH RELAY</div>
          <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;">Cryptographically seals and broadcasts monotonic state vectors across SCION gateways.</div>
        </div>

        <div class="glass-panel" style="padding: 1.2rem; border-top: 2px solid #FF007A;">
          <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔴</div>
          <div style="font-weight: 700; color: #FFF; font-size: 0.95rem;">Overlord Omni</div>
          <div style="font-size: 0.72rem; color: #F472B6; font-family: var(--font-mono); margin-bottom: 0.5rem;">SWARM MASTER SYNTHESIS</div>
          <div style="font-size: 0.78rem; color: #94A3B8; line-height: 1.5;">Synthesizes consensus vectors and authorizes automated Project SENTIENT tasking.</div>
        </div>
      </div>

      <!-- Deliberation Terminal Panel -->
      <div class="glass-panel" style="padding: 1.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="status-dot"></span>
            <span style="font-size: 0.85rem; font-family: var(--font-mono); color: #FFF; font-weight: 600;">SCION SWARM OVERLORD PROTOCOL // ACTIVE AGENTS: 5/5</span>
          </div>
          <span style="font-size: 0.72rem; font-family: var(--font-mono); color: #94A3B8;">ENGINE: GOOGLE GEMINI 4.0 ARGON</span>
        </div>

        <!-- Chat Feed Area -->
        <div id="swarm-chat-feed" class="swarm-chat-feed"></div>

        <!-- Control Bar -->
        <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; flex-wrap: wrap; gap: 0.75rem;">
          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <button class="glass-btn glass-btn-primary" style="font-size: 0.8rem; padding: 7px 14px;" onclick="window.swarmEngine.startDeliberation(window.sentientRadar.activeBlipId)">
              <span>🔄 Restart Deliberation</span>
            </button>
            <button class="glass-btn glass-btn-secondary" style="font-size: 0.8rem; padding: 7px 14px;" onclick="window.swarmEngine.synthesizeReport()">
              <span>📥 Download Consensus Dossier (.json)</span>
            </button>
          </div>
          <span style="font-size: 0.75rem; font-family: var(--font-mono); color: var(--gemini-cyan);">P2P CRDT JOIN-SEMILATTICE ACTIVE</span>
        </div>
      </div>
    </section>

    <!-- SECTION 3: MHD PLASMA SHEATH & LORENTZ ACCELERATION CALCULATOR -->
    <section id="mhd-calculator-section" class="landing-section">
      <div class="section-badge" style="border-color: rgba(0, 242, 254, 0.4); color: var(--gemini-cyan);">
        <span>FIELD PROPULSION MECHANICS // MAGNETOHYDRODYNAMIC ACCELERATION</span>
      </div>
      <h2 style="font-size: 2rem; color: #FFFFFF; margin-bottom: 0.75rem;">
        MHD Lorentz Force &amp; Shockwave Attenuation Engine
      </h2>
      <p style="color: #94A3B8; max-width: 820px; margin-bottom: 2rem; line-height: 1.6;">
        Calculate boundary-layer electromagnetic acceleration (\(F_L = \mathbf{j} \times \mathbf{B}\)). By accelerating ionized air slipstreams ahead of the vehicle, wave drag is suppressed by up to 98% and acoustic pressure discontinuities are smoothed, neutralizing the sonic boom.
      </p>

      <!-- Preset Buttons -->
      <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem;">
        <span style="font-size: 0.78rem; font-family: var(--font-mono); color: #94A3B8; align-self: center;">PRESETS:</span>
        <button class="glass-btn glass-btn-secondary mhd-preset-btn active" data-b="32" data-j="45000" data-rho="0.05" data-len="12.2" style="font-size: 0.75rem; padding: 5px 12px;">
          USS Nimitz Slipstream
        </button>
        <button class="glass-btn glass-btn-secondary mhd-preset-btn" data-b="18" data-j="28000" data-rho="1025.0" data-len="1.5" style="font-size: 0.75rem; padding: 5px 12px;">
          Aguadilla Trans-Medium
        </button>
        <button class="glass-btn glass-btn-secondary mhd-preset-btn" data-b="45" data-j="75000" data-rho="0.25" data-len="30.0" style="font-size: 0.75rem; padding: 5px 12px;">
          TR-3B Triangular Airframe
        </button>
        <button class="glass-btn glass-btn-secondary mhd-preset-btn" data-b="50" data-j="90000" data-rho="0.001" data-len="15.0" style="font-size: 0.75rem; padding: 5px 12px;">
          Orbital Re-Entry (Rarefied)
        </button>
      </div>

      <div class="sentient-radar-grid">
        <!-- Sliders Form -->
        <div class="glass-panel" style="padding: 1.5rem;">
          <h3 style="font-size: 1.1rem; color: #FFF; margin-bottom: 1.25rem;">Adjust Plasma Field Parameters</h3>

          <!-- B Field -->
          <div style="margin-bottom: 1.2rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.82rem; margin-bottom: 4px;">
              <span style="color: #CBD5E1;">Magnetic Flux Density (B):</span>
              <span id="mhd-val-b" style="color: var(--gemini-cyan); font-family: var(--font-mono); font-weight: 700;">32 T</span>
            </div>
            <input type="range" id="mhd-input-b" min="1" max="50" step="1" value="32" style="width: 100%; accent-color: var(--gemini-cyan);">
            <div style="font-size: 0.7rem; color: #64748B;">Superconducting REBCO magnet array (1 - 50 Tesla)</div>
          </div>

          <!-- Current Density j -->
          <div style="margin-bottom: 1.2rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.82rem; margin-bottom: 4px;">
              <span style="color: #CBD5E1;">Surface Current Density (j):</span>
              <span id="mhd-val-j" style="color: var(--gemini-cyan); font-family: var(--font-mono); font-weight: 700;">45,000 A/m²</span>
            </div>
            <input type="range" id="mhd-input-j" min="1000" max="100000" step="1000" value="45000" style="width: 100%; accent-color: var(--gemini-cyan);">
            <div style="font-size: 0.7rem; color: #64748B;">Dielectric Barrier Discharge pulsed plasma discharge</div>
          </div>

          <!-- Air/Fluid Density rho -->
          <div style="margin-bottom: 1.2rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.82rem; margin-bottom: 4px;">
              <span style="color: #CBD5E1;">Fluid Medium Density (ρ):</span>
              <span id="mhd-val-rho" style="color: var(--gemini-cyan); font-family: var(--font-mono); font-weight: 700;">0.05 kg/m³</span>
            </div>
            <input type="range" id="mhd-input-rho" min="0.001" max="1.225" step="0.005" value="0.05" style="width: 100%; accent-color: var(--gemini-cyan);">
            <div style="font-size: 0.7rem; color: #64748B;">0.001 (Mesosphere) to 1.225 (Sea Level Air) to 1025 (Seawater)</div>
          </div>

          <!-- Characteristic Length L -->
          <div style="margin-bottom: 0.5rem;">
            <div style="display: flex; justify-content: space-between; font-size: 0.82rem; margin-bottom: 4px;">
              <span style="color: #CBD5E1;">Characteristic Hull Length (L):</span>
              <span id="mhd-val-len" style="color: var(--gemini-cyan); font-family: var(--font-mono); font-weight: 700;">12.2 m</span>
            </div>
            <input type="range" id="mhd-input-len" min="1" max="30" step="0.5" value="12.2" style="width: 100%; accent-color: var(--gemini-cyan);">
            <div style="font-size: 0.7rem; color: #64748B;">Effective boundary interaction length across craft hull</div>
          </div>
        </div>

        <!-- Calculated Readout Panel -->
        <div class="glass-panel" style="padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3 style="font-size: 1.1rem; color: #FFF; margin-bottom: 1.25rem;">Real-Time Kinematic Readout</h3>

            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">VOLUMETRIC LORENTZ FORCE:</span>
              <span id="mhd-out-lorentz" class="radar-telemetry-value" style="font-size: 1.1rem; color: #34D399;">1440.0 kN/m³</span>
            </div>

            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">PLASMA SLIPSTREAM VELOCITY:</span>
              <span id="mhd-out-velocity" class="radar-telemetry-value">26,518 m/s</span>
            </div>

            <div class="radar-telemetry-row">
              <span class="radar-telemetry-label">EQUIVALENT MACH NUMBER:</span>
              <span id="mhd-out-mach" class="radar-telemetry-value" style="color: var(--gemini-cyan); font-weight: 800;">Mach 77.9</span>
            </div>

            <!-- Wave Drag Progress -->
            <div style="margin: 1.25rem 0 0.75rem 0;">
              <div style="display: flex; justify-content: space-between; font-size: 0.78rem; font-family: var(--font-mono); margin-bottom: 4px;">
                <span style="color: #94A3B8;">WAVE DRAG REDUCTION:</span>
                <span id="mhd-out-drag" style="color: var(--gemini-cyan); font-weight: 700;">98.8%</span>
              </div>
              <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.06); border-radius: 9999px; overflow: hidden;">
                <div id="mhd-drag-bar" style="width: 98.8%; height: 100%; background: linear-gradient(90deg, #00F2FE, #34D399); border-radius: 9999px; transition: width 0.3s ease;"></div>
              </div>
            </div>

            <!-- Shock Attenuation Progress -->
            <div style="margin-bottom: 1rem;">
              <div style="display: flex; justify-content: space-between; font-size: 0.78rem; font-family: var(--font-mono); margin-bottom: 4px;">
                <span style="color: #94A3B8;">ACOUSTIC SHOCK ATTENUATION:</span>
                <span id="mhd-out-attenuation" style="color: #F472B6; font-weight: 700;">-64.2 dB</span>
              </div>
              <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.06); border-radius: 9999px; overflow: hidden;">
                <div id="mhd-shock-bar" style="width: 96%; height: 100%; background: linear-gradient(90deg, #7B61FF, #F472B6); border-radius: 9999px; transition: width 0.3s ease;"></div>
              </div>
            </div>
          </div>

          <!-- Theoretical Validation Callout -->
          <div style="padding: 0.85rem; background: rgba(0, 242, 254, 0.05); border: 1px solid rgba(0, 242, 254, 0.2); border-radius: 12px; font-size: 0.75rem; color: #CBD5E1; line-height: 1.5;">
            <strong style="color: var(--gemini-cyan);">Sonic Boom Neutralization:</strong> At \(\Delta v > 20\text{ km/s}\), the boundary layer plasma sheath expels atmospheric gas molecules around the vehicle faster than the speed of sound in the ambient medium, preventing the coalescence of acoustic compression waves.
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: ZERO-KNOWLEDGE WHISTLEBLOWER PORTAL -->
    <section id="whistleblower-section" class="landing-section">
      <div class="section-badge" style="border-color: rgba(16, 185, 129, 0.4); color: #34D399;">
        <span>SOVEREIGN CRYPTOGRAPHY // CLIENT-SIDE METADATA SANITIZATION</span>
      </div>
      <h2 style="font-size: 2rem; color: #FFFFFF; margin-bottom: 0.75rem;">
        Zero-Knowledge Telemetry &amp; Whistleblower Vault
      </h2>
      <p style="color: #94A3B8; max-width: 820px; margin-bottom: 2rem; line-height: 1.6;">
        Submit raw sensor recordings, FLIR imagery, or radar logs. The browser performs in-memory EXIF metadata stripping, generates 4096-bit asymmetric cipher keys, and packages the payload into a Delta-CRDT join-semilattice for censorship-resistant P2P gossip.
      </p>

      <div class="glass-panel" style="padding: 2rem; text-align: center;">
        <div id="whistleblower-dropzone" style="border: 2px dashed rgba(0, 242, 254, 0.3); border-radius: 16px; padding: 2.5rem 1.5rem; background: rgba(0,0,0,0.3); cursor: pointer; transition: all 0.2s ease;">
          <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🛡️</div>
          <h3 style="font-size: 1.2rem; color: #FFF; margin-bottom: 0.5rem;">Drag &amp; Drop Telemetry or Defense Dossiers</h3>
          <p style="color: #94A3B8; font-size: 0.85rem; max-width: 500px; margin: 0 auto 1.25rem;">
            EXIF coordinates, device IDs, and author tags will be stripped in-memory prior to monotonic gossip propagation.
          </p>
          <button id="whistleblower-sample-btn" class="glass-btn glass-btn-primary" style="font-size: 0.8rem; padding: 8px 16px;">
            <span>📥 Load Sample Telemetry Stream (FLIR1 Record)</span>
          </button>
        </div>

        <div id="whistleblower-status" style="margin-top: 1.5rem; text-align: left;"></div>
      </div>
    </section>

    <!-- SECTION 5: DECLASSIFIED FOIA EVIDENCE ARCHIVE -->
    <section id="foia-vault-section" class="landing-section">
      <div class="section-badge">
        <span>PRIMARY HISTORICAL RECORDS // DECLASSIFIED FOIA ARCHIVES</span>
      </div>
      <h2 style="font-size: 2rem; color: #FFFFFF; margin-bottom: 0.75rem;">
        Declassified Government &amp; Defense Dossiers
      </h2>
      <p style="color: #94A3B8; max-width: 820px; margin-bottom: 2rem; line-height: 1.6;">
        Inspect authentic declassified memos, sensor transcripts, and official evaluations corroborating non-Newtonian kinematics and automated satellite tasking.
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.25rem;">
        <!-- Card 1: Project SENTIENT -->
        <div class="glass-panel" style="padding: 1.5rem; cursor: pointer; transition: transform 0.2s ease;" onclick="openFoiaModal('case-sentient')">
          <div style="font-size: 0.7rem; font-family: var(--font-mono); color: #EF4444; margin-bottom: 0.5rem;">TOP SECRET // TALENT KEYHOLE</div>
          <h3 style="font-size: 1.1rem; color: #FFF; margin-bottom: 0.5rem;">Project SENTIENT Architecture</h3>
          <p style="font-size: 0.82rem; color: #94A3B8; line-height: 1.5; margin-bottom: 1rem;">
            National Reconnaissance Office directive detailing autonomous multi-satellite cross-cueing on un-correlated hypersonic targets.
          </p>
          <div style="font-size: 0.75rem; color: var(--gemini-cyan); font-family: var(--font-mono);">Read Dossier ↗</div>
        </div>

        <!-- Card 2: USS Nimitz -->
        <div class="glass-panel" style="padding: 1.5rem; cursor: pointer; transition: transform 0.2s ease;" onclick="openFoiaModal('case-nimitz')">
          <div style="font-size: 0.7rem; font-family: var(--font-mono); color: #F59E0B; margin-bottom: 0.5rem;">SECRET // NOFORN // 2004</div>
          <h3 style="font-size: 1.1rem; color: #FFF; margin-bottom: 0.5rem;">USS Nimitz VFA-41 ATFLIR</h3>
          <p style="font-size: 0.82rem; color: #94A3B8; line-height: 1.5; margin-bottom: 1rem;">
            AN/SPY-1 radar telemetry and dual-band ATFLIR video confirming 80,000 ft to sea level descent in 0.78 seconds with zero heat signature.
          </p>
          <div style="font-size: 0.75rem; color: var(--gemini-cyan); font-family: var(--font-mono);">Read Dossier ↗</div>
        </div>

        <!-- Card 3: Aguadilla -->
        <div class="glass-panel" style="padding: 1.5rem; cursor: pointer; transition: transform 0.2s ease;" onclick="openFoiaModal('case-aguadilla')">
          <div style="font-size: 0.7rem; font-family: var(--font-mono); color: #34D399; margin-bottom: 0.5rem;">UNCLASSIFIED // LAW ENFORCEMENT</div>
          <h3 style="font-size: 1.1rem; color: #FFF; margin-bottom: 0.5rem;">CBP Aguadilla Trans-Medium</h3>
          <p style="font-size: 0.82rem; color: #94A3B8; line-height: 1.5; margin-bottom: 1rem;">
            Thermal imaging tracking seamless ocean entry at 105 kts without surface splash, followed by synchronous underwater splitting.
          </p>
          <div style="font-size: 0.75rem; color: var(--gemini-cyan); font-family: var(--font-mono);">Read Dossier ↗</div>
        </div>

        <!-- Card 4: Tehran F-4 -->
        <div class="glass-panel" style="padding: 1.5rem; cursor: pointer; transition: transform 0.2s ease;" onclick="openFoiaModal('case-tehran')">
          <div style="font-size: 0.7rem; font-family: var(--font-mono); color: #A5B4FC; margin-bottom: 0.5rem;">DIA ARCHIVE 2013-00452</div>
          <h3 style="font-size: 1.1rem; color: #FFF; margin-bottom: 0.5rem;">Tehran F-4 Dual Intercept</h3>
          <p style="font-size: 0.82rem; color: #94A3B8; line-height: 1.5; margin-bottom: 1rem;">
            Defense Intelligence Agency documentation of weapon control circuit power failure and communications blackout upon Sidewinder lock.
          </p>
          <div style="font-size: 0.75rem; color: var(--gemini-cyan); font-family: var(--font-mono);">Read Dossier ↗</div>
        </div>
      </div>
    </section>

    <!-- FOIA Modal Container -->
    <div id="foia-modal" class="importer-modal-backdrop">
      <div class="importer-modal-panel">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 0.75rem;">
          <div>
            <div id="foia-modal-class" style="font-size: 0.7rem; font-family: var(--font-mono); color: #EF4444; margin-bottom: 4px;">TOP SECRET</div>
            <h3 id="foia-modal-title" style="margin: 0; font-size: 1.2rem; color: #FFF;">Dossier Record</h3>
          </div>
          <button class="glass-modal-close-btn" onclick="closeFoiaModal()" title="Close">&times;</button>
        </div>
        <pre id="foia-modal-body" style="background: rgba(0,0,0,0.6); padding: 1rem; border-radius: 12px; font-family: var(--font-mono); font-size: 0.8rem; line-height: 1.6; color: #CBD5E1; max-height: 380px; overflow-y: auto; white-space: pre-wrap;"></pre>
        <div style="margin-top: 1rem; display: flex; justify-content: flex-end; gap: 0.5rem;">
          <button class="glass-btn glass-btn-secondary" style="font-size: 0.8rem; padding: 6px 14px;" onclick="closeFoiaModal()">Close Record</button>
        </div>
      </div>
    </div>\'\'\'
)
'''

def update_build_pages():
    with open(BUILD_PAGES_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update NAV_HEADER in build_pages.py
    # Add to Frontier Tech mega dropdown if not already present
    if 'sentient-radar.html' not in content:
        # Insert into Frontier Tech Mega-Dropdown
        frontier_insertion = '''            <div class="dropdown-section-title" style="margin-top: 4px;">ORBITAL &amp; ANOMALY INTELLIGENCE</div>
            <a href="sentient-radar.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/sentient-radar.svg" alt="Project SENTIENT">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Project SENTIENT <span class="item-badge">Radar &amp; Swarm</span></div>
                <div class="dropdown-item-desc">60 FPS multi-spectral scope &amp; 5-agent deliberation</div>
              </div>
            </a>
          </div>
        </div>'''
        
        # Replace the end of the mega-menu
        content = content.replace('            <a href="deeptech-robotics.html" class="dropdown-item">\n              <div class="dropdown-item-icon">\n                <img src="svg/humanoid-robotics.svg" alt="Robotics">\n              </div>\n              <div class="dropdown-item-content">\n                <div class="dropdown-item-title">Humanoid Robotics</div>\n                <div class="dropdown-item-desc">Quasi-direct drive actuators & VLA</div>\n              </div>\n            </a>\n          </div>\n        </div>',
                                  '            <a href="deeptech-robotics.html" class="dropdown-item">\n              <div class="dropdown-item-icon">\n                <img src="svg/humanoid-robotics.svg" alt="Robotics">\n              </div>\n              <div class="dropdown-item-content">\n                <div class="dropdown-item-title">Humanoid Robotics</div>\n                <div class="dropdown-item-desc">Quasi-direct drive actuators & VLA</div>\n              </div>\n            </a>\n' + frontier_insertion)

        # Insert into Developer Studio dropdown
        studio_insertion = '''            <a href="sentient-radar.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/swarm-intelligence.svg" alt="Swarm Overlord">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Project SENTIENT &amp; Swarm <span class="item-badge">New</span></div>
                <div class="dropdown-item-desc">60 FPS radar &amp; 5-agent deliberation console</div>
              </div>
            </a>\n            <a href="whitepaper.html" class="dropdown-item">'''
        
        content = content.replace('            <a href="whitepaper.html" class="dropdown-item">', studio_insertion)

        # Update FOOTER_HTML
        footer_insertion = '      <a href="sentient-radar.html" class="footer-link">Project SENTIENT Radar</a>\n      <a href="whitepaper.html" class="footer-link">Whitepaper</a>'
        content = content.replace('      <a href="whitepaper.html" class="footer-link">Whitepaper</a>', footer_insertion)

        # Append PAGES['sentient-radar.html'] before the write loop
        content = content.replace('# Write all generated pages to disk', SENTIENT_PAGE_CODE + '\n# Write all generated pages to disk')

        with open(BUILD_PAGES_PATH, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ Updated pipeline/build_pages.py with Project SENTIENT radar page & navigation links!")
    else:
        print("build_pages.py already contains sentient-radar.html reference.")

if __name__ == '__main__':
    update_build_pages()
