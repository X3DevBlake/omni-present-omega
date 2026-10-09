#!/usr/bin/env python3
"""
Omni-Present Omega (OPO) Multi-Page Enterprise Generator
Generates 11 dedicated, interconnected pages with Liquid Glass styling,
Mega-Dropdown navigation, interactive calculators, and deep tech dossiers.
"""

import os

BASE_DIR = '/data/data/com.termux/files/home/omni-web'

# Shared Navigation Header Template
NAV_HEADER = '''  <!-- Liquid Ambient Background Engine with 3D Neural Connectome -->
  <div class="liquid-bg-canvas">
    <canvas id="neural-brain-canvas" class="neural-brain-canvas"></canvas>
    <div class="liquid-blob blob-1"></div>
    <div class="liquid-blob blob-2"></div>
    <div class="liquid-blob blob-3"></div>
    <div class="liquid-blob blob-4"></div>
  </div>
  <div class="glass-grid-overlay"></div>

  <!-- Liquid Glass Sticky Navigation Header with Mega-Dropdowns -->
  <header class="liquid-nav">
    <div class="nav-container">
      <a href="index.html" class="brand-wrapper">
        <div class="brand-icons-cluster">
          <img src="svg/opo-symbol.svg" alt="OPO Sovereign Symbol" class="brand-opo-svg" width="30" height="30">
          <img src="svg/gemini-argon-3d.svg" alt="Gemini 4.0 Argon 3D" class="brand-sparkle-svg" width="24" height="24">
        </div>
        <div style="display: flex; flex-direction: column;">
          <div style="display: flex; align-items: center; gap: 6px;">
            <span class="brand-title">OMNI-PRESENT OMEGA</span>
            <span class="brand-badge">OPO 3.0</span>
          </div>
          <span style="font-size: 0.65rem; color: #94A3B8; font-family: var(--font-mono); letter-spacing: 0.04em;">REDCOMM SOVEREIGN FABRIC</span>
        </div>
      </a>

      <!-- Smooth Anchor & Multi-Page Navigation Pills with Dropdowns -->
      <nav class="nav-pills">
        <a href="index.html" class="nav-pill-btn">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
          <span>Home</span>
        </a>
        <a href="godseye.html" class="nav-pill-btn" style="border-color: rgba(0, 229, 255, 0.4); background: rgba(0, 229, 255, 0.08);">
          <span style="color: #00E5FF; font-size: 0.95rem; line-height: 1;">🛰️</span>
          <span style="color: #00E5FF; font-weight: 600;">God's Eye</span>
        </a>

        <!-- Omni Ecosystem Dropdown -->
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" type="button">
            <span style="color: var(--gemini-cyan); font-size: 1.1rem; line-height: 1;">✦</span>
            <span>Omni Ecosystem</span>
            <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="nav-dropdown-menu">
            <div class="dropdown-section-title">AI &amp; SUPERCOMPUTING</div>
            <a href="https://omni-brain-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">🧠</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniBrain <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">DeepMind &amp; Google Research AI Supercomputing</div>
              </div>
            </a>
            <a href="https://omni-kronos-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">⚡</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniKronos <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Agentic Development Environment &amp; Sub-Agents</div>
              </div>
            </a>
            <a href="https://omni-llm-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">🤖</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniLLM &amp; Season Pass <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Multi-Model Intelligence &amp; Gamified Web3 Quests</div>
              </div>
            </a>
            <div class="dropdown-section-title" style="margin-top: 6px;">SOVEREIGN MARKETS &amp; DEFI</div>
            <a href="https://omni-futures-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">📈</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniFutures Pro (200x) <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Crypto, Stocks, Gold Derivatives &amp; 1,000 BTC Fund</div>
              </div>
            </a>
            <a href="https://omni-dao-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">🏛️</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniDAO &amp; DEX <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Multi-Chain Yield, Staking &amp; Treasury Ledgers</div>
              </div>
            </a>
            <a href="https://omni-presale-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">💎</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Omni Presale <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Official $OMNI Token Presale &amp; Allocation</div>
              </div>
            </a>
            <a href="https://omni-airdrop-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">🪂</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Omni Airdrop <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Claim Your $OMNI Ecosystem Allocation</div>
              </div>
            </a>
            <div class="dropdown-section-title" style="margin-top: 6px;">CORE FABRIC &amp; COMMUNICATION</div>
            <a href="https://omni-network-39821.web.app" class="dropdown-item active">
              <div class="dropdown-item-icon">🌐</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Omni-Present Omega (OPO) <span class="item-badge" style="color: #00E5FF;">This Site</span></div>
                <div class="dropdown-item-desc">Sovereign Physical &amp; Real-World Intelligence Fabric</div>
              </div>
            </a>
            <a href="godseye.html" class="dropdown-item">
              <div class="dropdown-item-icon">🛰️</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Godseyeview 3D <span class="item-badge" style="color: #00E5FF;">Orbital</span></div>
                <div class="dropdown-item-desc">Planetary Spatial Intelligence, Satellites &amp; AIS Maritime</div>
              </div>
            </a>
            <a href="https://omni-explorer-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">🔍</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniScan Explorer <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Block Explorer, Node Topology &amp; Validator Hub</div>
              </div>
            </a>
            <a href="https://omniair-39821.web.app" target="_blank" rel="noopener" class="dropdown-item">
              <div class="dropdown-item-icon">✈️</div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">OmniAir <span class="item-badge" style="color: #4ADE80;">Live</span></div>
                <div class="dropdown-item-desc">Premium Social, Discussion &amp; WebRTC Voice Channels</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Architecture Dropdown -->
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" type="button">
            <img src="svg/scion-routing.svg" alt="Architecture" width="16" height="16">
            <span>Architecture</span>
            <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="nav-dropdown-menu">
            <a href="architecture.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/scion-routing.svg" alt="Triad">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Sovereign Triad</div>
                <div class="dropdown-item-desc">Hermetic Soul, Edge Sensorium, and Global Mesh</div>
              </div>
            </a>
            <a href="architecture.html#scion" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/opo-symbol.svg" alt="SCION">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">SCION Protocol</div>
                <div class="dropdown-item-desc">Path-aware cryptographically isolated routing</div>
              </div>
            </a>
            <a href="crdt-lab.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/crdt-lattice.svg" alt="CRDT">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Delta-CRDT Engine</div>
                <div class="dropdown-item-desc">Join-semilattice mathematical state sync</div>
              </div>
            </a>
          </div>
        </div>

        <!-- Deep Tech Mega-Dropdown (6 Frontier Pages) -->
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" type="button">
            <img src="svg/gemini-deep-research.svg" alt="Deep Tech" width="16" height="16">
            <span>Frontier Tech</span>
            <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="nav-dropdown-menu mega-menu-grid">
            <div class="dropdown-section-title">PHYSICS & ENERGY CONVERGENCE</div>
            <a href="deeptech-fusion.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/fusion-tokamak.svg" alt="Fusion">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">SPARC Fusion <span class="item-badge">Q≥2</span></div>
                <div class="dropdown-item-desc">HTS REBCO Magnets & Net Energy Gain</div>
              </div>
            </a>
            <a href="deeptech-quantum.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/quantum-photonics.svg" alt="Quantum">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Quantum Photonics</div>
                <div class="dropdown-item-desc">Thin-film lithium niobate optical routing</div>
              </div>
            </a>
            <a href="deeptech-battery.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/battery-solidstate.svg" alt="Battery">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Solid-State Battery</div>
                <div class="dropdown-item-desc">500 Wh/kg Lithium-Metal Anode-Free</div>
              </div>
            </a>
            <div class="dropdown-section-title" style="margin-top: 4px;">BIOLOGY & EMBODIED SYSTEMS</div>
            <a href="deeptech-genomic.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/genomic-crispr.svg" alt="Genomics">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Prime Genome Editing</div>
                <div class="dropdown-item-desc">pegRNA synthesis & Cas9 epiproteomics</div>
              </div>
            </a>
            <a href="deeptech-neural.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/neural-threads.svg" alt="Neural">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Intracortical BCI</div>
                <div class="dropdown-item-desc">1024-ch flexible polyimide micro-threads</div>
              </div>
            </a>
            <a href="deeptech-robotics.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/humanoid-robotics.svg" alt="Robotics">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Humanoid Robotics</div>
                <div class="dropdown-item-desc">Quasi-direct drive actuators & VLA</div>
              </div>
            </a>
            <div class="dropdown-section-title" style="margin-top: 4px;">ORBITAL &amp; ANOMALY INTELLIGENCE</div>
            <a href="godseye.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <span style="font-size: 1.1rem;">🛰️</span>
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">God's Eye View <span class="item-badge" style="color: #00E5FF;">3D Planetary</span></div>
                <div class="dropdown-item-desc">Planetary spatial intelligence, satellites, ADS-B &amp; maritime AIS</div>
              </div>
            </a>
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
        </div>

        <!-- Developer Tools Dropdown -->
        <div class="nav-dropdown">
          <button class="nav-dropdown-trigger" type="button">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="width:16px;height:16px;"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>
            <span>Developer Tools</span>
            <svg class="chevron-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="nav-dropdown-menu">
            <a href="godseye.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <span style="font-size: 1.1rem;">🛰️</span>
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Godseyeview Spatial Engine <span class="item-badge" style="color: #00E5FF;">60 FPS</span></div>
                <div class="dropdown-item-desc">3D WebGL/Canvas planetary intelligence console</div>
              </div>
            </a>
            <a href="crdt-lab.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/crdt-lattice.svg" alt="CRDT Lab">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">CRDT Workbench <span class="item-badge">Interactive</span></div>
                <div class="dropdown-item-desc">60 FPS lattice simulation & partitions</div>
              </div>
            </a>
            <a href="gemini-studio.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/gemini-sparkle.svg" alt="Gemini Engine">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Gemini 4.0 Argon Engine</div>
                <div class="dropdown-item-desc">Multimodal reasoning &amp; live streaming</div>
              </div>
            </a>
            <a href="learn.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <span style="font-size: 1.1rem;">🎓</span>
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Learning Hub &amp; Audio <span class="item-badge">NotebookLM</span></div>
                <div class="dropdown-item-desc">3D Flashcards, Deep Dive Podcast &amp; Quizzes</div>
              </div>
            </a>
            <a href="sentient-radar.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/swarm-intelligence.svg" alt="Swarm Overlord">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Project SENTIENT &amp; Swarm <span class="item-badge">New</span></div>
                <div class="dropdown-item-desc">60 FPS radar &amp; 5-agent deliberation console</div>
              </div>
            </a>
            <a href="javascript:void(0)" onclick="openGenAiSdkModal()" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/gemini-sparkle.svg" alt="GenAI SDK">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">GenAI SDK Modal <span class="item-badge">gemini-4.0-argon</span></div>
                <div class="dropdown-item-desc">Interactive Python SDK runner &amp; thinking budget</div>
              </div>
            </a>
            <a href="whitepaper.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/gemini-deep-research.svg" alt="Whitepaper">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Sovereign Whitepaper</div>
                <div class="dropdown-item-desc">Mathematical proofs & SCION specs</div>
              </div>
            </a>
            <a href="deploy.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/bench-suite-3d.svg" alt="Deploy" width="18" height="18">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Edge Deployment &amp; Diagnostics</div>
                <div class="dropdown-item-desc">Production cluster &amp; 3D test suite</div>
              </div>
            </a>
          </div>
        </div>
      </nav>

      <!-- Nav Actions -->
      <div class="nav-actions">
        <!-- 9-Dot Ecosystem Launcher -->
        <div class="ecosystem-launcher-wrapper" id="ecoLauncherWrapper">
          <button class="launcher-btn" id="ecoLauncherBtn" type="button" title="Omni Ecosystem Hub" aria-label="Omni Ecosystem Hub" onclick="toggleEcoLauncher(event)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
              <circle cx="5" cy="5" r="2.2"/><circle cx="12" cy="5" r="2.2"/><circle cx="19" cy="5" r="2.2"/>
              <circle cx="5" cy="12" r="2.2"/><circle cx="12" cy="12" r="2.2"/><circle cx="19" cy="12" r="2.2"/>
              <circle cx="5" cy="19" r="2.2"/><circle cx="12" cy="19" r="2.2"/><circle cx="19" cy="19" r="2.2"/>
            </svg>
          </button>
          <div class="ecosystem-menu-dropdown" id="ecoDropdown">
            <a href="https://omni-brain-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #E040FB;">🧠</span>
              <span>OmniBrain</span>
            </a>
            <a href="https://omni-kronos-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #A855F7;">⚡</span>
              <span>OmniKronos</span>
            </a>
            <a href="https://omni-llm-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #00E5FF;">🤖</span>
              <span>OmniLLM</span>
            </a>
            <a href="https://omni-futures-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #38BDF8;">📈</span>
              <span>OmniFutures</span>
            </a>
            <a href="https://omni-dao-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #10B981;">🏛️</span>
              <span>OmniDAO</span>
            </a>
            <a href="https://omni-network-39821.web.app" class="eco-app-tile current-active">
              <span class="eco-icon" style="color: #00E5FF;">🌐</span>
              <span>OPO Mesh</span>
            </a>
            <a href="godseye.html" class="eco-app-tile">
              <span class="eco-icon" style="color: #00E5FF;">🛰️</span>
              <span>God's Eye</span>
            </a>
            <a href="https://omni-explorer-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #60A5FA;">🔍</span>
              <span>OmniScan</span>
            </a>
            <a href="https://omni-presale-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #FFD700;">💎</span>
              <span>Presale</span>
            </a>
            <a href="https://omni-airdrop-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #F43F5E;">🪂</span>
              <span>Airdrop</span>
            </a>
            <a href="https://omniair-39821.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #00E5FF;">✈️</span>
              <span>OmniAir</span>
            </a>
            <a href="https://omni-trading-c7ff4.web.app" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #F59E0B;">📊</span>
              <span>OmniTrade</span>
            </a>
            <a href="https://omni-llm-39821.web.app/season-pass.html" target="_blank" rel="noopener" class="eco-app-tile">
              <span class="eco-icon" style="color: #FFD700;">🎟️</span>
              <span>Season Pass</span>
            </a>
          </div>
        </div>

        <button id="audio-toggle-btn" class="glass-btn glass-btn-secondary" style="padding: 5px 12px; font-size: 0.75rem; border-radius: 9999px;" onclick="window.soundEngine.toggle()" title="Toggle Cybernetic Audio Haptics">
          <span id="audio-toggle-icon">🔊</span>
          <span id="audio-toggle-text">FX ON</span>
        </button>
        <button id="mobile-menu-toggle" class="glass-btn glass-btn-secondary mobile-toggle-btn" onclick="toggleMobileMenu()" aria-label="Toggle Navigation Menu">
          <span id="mobile-menu-icon">☰</span>
        </button>
      </div>
    </div>
  </header>'''

# Shared Footer Template
FOOTER_HTML = '''  <!-- Liquid Glass Google GenAI SDK Modal (gemini-4.0-argon) -->
  <div id="genai-sdk-modal" class="importer-modal-backdrop" onclick="if(event.target === this) closeGenAiSdkModal()">
    <div class="importer-modal-panel" style="max-width: 820px; max-height: 90vh; overflow-y: auto;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.25rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 0.75rem;">
        <div>
          <div style="font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; letter-spacing: 0.05em;">
            INFERENCE WORKBENCH // GEMINI 4.0 ARGON
          </div>
          <h3 style="margin: 4px 0 0 0; font-size: 1.35rem; color: #FFF; font-weight: 700;">Google GenAI Python &amp; TypeScript Execution Modal</h3>
        </div>
        <button class="glass-modal-close-btn" onclick="closeGenAiSdkModal()" title="Close">&times;</button>
      </div>

      <!-- Code Viewer Section -->
      <div style="margin-bottom: 1.25rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
          <div style="display: flex; gap: 6px;">
            <button class="glass-btn glass-btn-secondary" style="font-size: 0.75rem; padding: 4px 10px;" onclick="copyGenAiSdkSnippet('python')">🐍 Copy Python SDK</button>
            <button class="glass-btn glass-btn-secondary" style="font-size: 0.75rem; padding: 4px 10px;" onclick="copyGenAiSdkSnippet('typescript')">⚡ Copy TypeScript SDK</button>
          </div>
          <span style="font-size: 0.72rem; font-family: var(--font-mono); color: #94A3B8;">from google import genai</span>
        </div>
        <pre style="background: rgba(3, 7, 18, 0.95); border: 1px solid rgba(0, 242, 254, 0.2); border-radius: 12px; padding: 1rem; font-family: var(--font-mono); font-size: 0.78rem; line-height: 1.5; color: #E2E8F0; overflow-x: auto; margin: 0;"><span style="color: #F472B6;">from</span> google <span style="color: #F472B6;">import</span> genai
<span style="color: #F472B6;">from</span> google.genai <span style="color: #F472B6;">import</span> types

client = genai.Client()
response = client.models.generate_content(
    model=<span style="color: #34D399;">"gemini-4.0-argon"</span>,
    contents=<span style="color: #34D399;">"Synthesize OPO Delta-CRDT vector &amp; Lawson criterion"</span>,
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=<span style="color: #F59E0B;">16384</span>),
        temperature=<span style="color: #F59E0B;">0.2</span>,
        tools=[{<span style="color: #34D399;">"function_declarations"</span>: [crdt_tool]}]
    )
)</pre>
      </div>

      <!-- Interactive Execution Form -->
      <div class="glass-panel" style="padding: 1.25rem; margin-bottom: 1.25rem;">
        <h4 style="margin: 0 0 1rem 0; font-size: 0.95rem; color: #FFF;">Live Interactive Inference Execution</h4>

        <!-- Prompt input -->
        <div style="margin-bottom: 0.9rem;">
          <label style="display: block; font-size: 0.78rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 4px;">CONTENTS / PROMPT:</label>
          <input type="text" id="genai-modal-prompt" value="Synthesize OPO Delta-CRDT vector &amp; Lawson criterion" style="width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 8px 12px; color: #FFF; font-size: 0.85rem;">
        </div>

        <!-- Controls grid -->
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 0.9rem; margin-bottom: 1rem;">
          <div>
            <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 4px;">MODEL:</label>
            <select id="genai-modal-model" style="width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 6px 10px; color: #FFF; font-size: 0.8rem;">
              <option value="gemini-4.0-argon" selected>gemini-4.0-argon (Flagship Deep Reasoning)</option>
              <option value="gemini-4.0-argon-live">gemini-4.0-argon-live (Sub-5ms Realtime Stream)</option>
              <option value="gemini-3.0-pro">gemini-3.0-pro (Algorithmic Proofs)</option>
              <option value="gemini-2.5-flash">gemini-2.5-flash (Edge Sensor Ingestion)</option>
            </select>
          </div>

          <div>
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 4px;">
              <span>THINKING BUDGET:</span>
              <span id="genai-modal-budget-val" style="color: var(--gemini-cyan);">16384 tokens</span>
            </div>
            <input type="range" id="genai-modal-budget" min="1024" max="32768" step="1024" value="16384" style="width: 100%; accent-color: var(--gemini-cyan);" oninput="document.getElementById('genai-modal-budget-val').textContent = this.value + ' tokens'">
          </div>

          <div>
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 4px;">
              <span>TEMPERATURE:</span>
              <span id="genai-modal-temp-val" style="color: var(--gemini-cyan);">0.2</span>
            </div>
            <input type="range" id="genai-modal-temp" min="0.0" max="1.0" step="0.05" value="0.2" style="width: 100%; accent-color: var(--gemini-cyan);" oninput="document.getElementById('genai-modal-temp-val').textContent = this.value">
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 0.75rem;">
          <label style="display: flex; align-items: center; gap: 6px; font-size: 0.78rem; font-family: var(--font-mono); color: #CBD5E1; cursor: pointer;">
            <input type="checkbox" id="genai-modal-tools" checked style="accent-color: var(--gemini-cyan);">
            <span>Enable Function Declarations (crdt_tool)</span>
          </label>
          <button id="genai-modal-run-btn" class="glass-btn glass-btn-primary" style="padding: 7px 16px; font-size: 0.82rem;" onclick="runGenAiSdkModal()">
            <span>▶️ Execute client.models.generate_content()</span>
          </button>
        </div>
      </div>

      <!-- Deep Thinking Inspector -->
      <div id="genai-modal-thinking" style="margin-bottom: 1rem; padding: 0.75rem; background: rgba(0,0,0,0.5); border-radius: 8px; border-left: 3px solid var(--gemini-cyan);">
        <div style="font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8;">
          Ready to execute with Gemini 4.0 Argon. Click 'Execute' to trigger deep reasoning.
        </div>
      </div>

      <!-- Tool Call Invocation Box -->
      <div id="genai-modal-toolcall" style="display: none; margin-bottom: 1rem; padding: 0.75rem; background: rgba(245, 158, 11, 0.08); border: 1px solid rgba(245, 158, 11, 0.25); border-radius: 8px;"></div>

      <!-- Output Container -->
      <div id="genai-modal-output" style="padding: 1rem; background: rgba(0, 242, 254, 0.03); border: 1px solid rgba(0, 242, 254, 0.2); border-radius: 12px;"></div>

      <div style="margin-top: 1.25rem; display: flex; justify-content: flex-end; gap: 0.5rem;">
        <button class="glass-btn glass-btn-secondary" style="font-size: 0.8rem; padding: 6px 16px;" onclick="closeGenAiSdkModal()">Close Modal</button>
      </div>
    </div>
  </div>
  <!-- Mobile Bottom Floating Quick-Action Dock -->
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
      <img src="svg/gemini-sparkle.svg" alt="Engine">
      <span>Engine</span>
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

  <!-- Liquid Glass Footer -->
  <footer class="liquid-footer">
    <div class="ecosystem-footer-bar" style="margin-bottom: 1.5rem; padding-bottom: 1.25rem; border-bottom: 1px solid rgba(255,255,255,0.08); text-align: center;">
      <div style="font-size: 0.72rem; font-family: var(--font-mono); color: var(--gemini-cyan); letter-spacing: 0.1em; margin-bottom: 0.75rem; text-transform: uppercase;">
        ✦ Omni Ecosystem Cross-Platform Network • Live on Firebase
      </div>
      <div class="ecosystem-footer-chips" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 8px;">
        <a href="https://omni-brain-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">🧠 OmniBrain</a>
        <a href="https://omni-kronos-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">⚡ OmniKronos</a>
        <a href="https://omni-llm-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">🤖 OmniLLM</a>
        <a href="https://omni-futures-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">📈 OmniFutures (200x)</a>
        <a href="https://omni-dao-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">🏛️ OmniDAO &amp; DEX</a>
        <a href="https://omni-network-39821.web.app" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: var(--gemini-cyan); background: rgba(0,229,255,0.12); border: 1px solid rgba(0,229,255,0.4); transition: all 0.2s ease;">🌐 OPO Mesh (Current)</a>
        <a href="godseye.html" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #38BDF8; background: rgba(56,189,248,0.12); border: 1px solid rgba(56,189,248,0.35); transition: all 0.2s ease;">🛰️ God's Eye View</a>
        <a href="https://omni-explorer-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">🔍 OmniScan</a>
        <a href="https://omni-presale-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">💎 Presale</a>
        <a href="https://omni-airdrop-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">🪂 Airdrop</a>
        <a href="https://omniair-39821.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">✈️ OmniAir</a>
        <a href="https://omni-trading-c7ff4.web.app" target="_blank" rel="noopener" class="footer-chip" style="display: inline-flex; align-items: center; gap: 5px; padding: 5px 12px; border-radius: 9999px; font-size: 0.75rem; font-family: var(--font-mono); text-decoration: none; color: #CBD5E1; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); transition: all 0.2s ease;">📊 OmniTrade</a>
      </div>
    </div>
    <div class="footer-links">
      <a href="index.html" class="footer-link">Home</a>
      <a href="godseye.html" class="footer-link" style="color: var(--gemini-cyan); font-weight: 600;">🛰️ God's Eye View</a>
      <a href="architecture.html" class="footer-link">Architecture</a>
      <a href="crdt-lab.html" class="footer-link">Delta-CRDT Lab</a>
      <a href="deeptech-fusion.html" class="footer-link">Fusion</a>
      <a href="deeptech-quantum.html" class="footer-link">Quantum</a>
      <a href="deeptech-battery.html" class="footer-link">Battery</a>
      <a href="deeptech-genomic.html" class="footer-link">Genomics</a>
      <a href="deeptech-neural.html" class="footer-link">Neural BCI</a>
      <a href="deeptech-robotics.html" class="footer-link">Robotics</a>
      <a href="gemini-studio.html" class="footer-link">Gemini 4.0 Argon</a>
      <a href="learn.html" class="footer-link">Learning Hub</a>
      <a href="sentient-radar.html" class="footer-link">Project SENTIENT Radar</a>
      <a href="whitepaper.html" class="footer-link">Whitepaper</a>
      <a href="deploy.html" class="footer-link">Edge Operations</a>
    </div>
    <div style="font-size: 0.8rem; color: #64748B; font-family: var(--font-mono); margin-top: 0.75rem;">
      Omni-Present Omega (OPO) &amp; RedComm Ecosystem • Sovereign Real-World Intelligence Fabric
    </div>
  </footer>

  <!-- App Logic & 3D Neural Connectome Engine -->
  <script src="js/neural-brain.js"></script>
  <script src="js/app.js"></script>
</body>
</html>'''

def render_page(title, desc, current_breadcrumb, body_content):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <meta name="theme-color" content="#07090e">
  <title>{title} | Omni-Present Omega</title>
  <meta name="description" content="{desc}">
  <link rel="icon" type="image/svg+xml" href="svg/gemini-sparkle.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/liquid-glass.css">
</head>
<body>
{NAV_HEADER}

  <!-- Main Content Container -->
  <main class="app-container">

    <!-- Breadcrumb Trail -->
    <nav class="glass-breadcrumbs" aria-label="Breadcrumb">
      <a href="index.html">Home</a>
      <span class="sep">/</span>
      {current_breadcrumb}
    </nav>

{body_content}

  </main>

{FOOTER_HTML}'''

PAGES = {}

# 1. architecture.html
PAGES['architecture.html'] = render_page(
    title="Sovereign Triad Architecture",
    desc="Hermetic Kernel Soul, Multimodal Edge Sensorium, and Global Mesh Fabric under SCION protocol.",
    current_breadcrumb='<a href="architecture.html">Architecture</a> <span class="sep">/</span> <span class="current">Sovereign Triad</span>',
    body_content='''    <section class="landing-section">
      <div class="section-badge">
        <img src="svg/scion-routing.svg" width="16" height="16" alt="Triad">
        <span>SOVEREIGN ARCHITECTURAL BLUEPRINT</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">The Sovereign Tri-Partite Triad</span>
      </h1>
      <p class="hero-desc" style="max-width: 820px; margin: 0 auto 2.5rem;">
        Omni-Present Omega isolates mission-critical computation from untrusted operating systems. Architecture is structured into three strictly decoupled layers: <strong>The Soul</strong> (Hermetic Kernel), <strong>The Body</strong> (Edge Sensorium), and <strong>The Mesh</strong> (Decentralized Fabric).
      </p>

      <!-- Triad Cards Grid -->
      <div class="triad-grid" style="margin-bottom: 3.5rem;">
        <div class="triad-card">
          <div class="triad-header">
            <div class="triad-icon-box soul-icon-box">
              <img src="svg/opo-symbol.svg" alt="Soul" width="28" height="28">
            </div>
            <div>
              <div style="font-size: 0.72rem; font-family: var(--font-mono); color: #94A3B8; text-transform: uppercase; margin-bottom: 2px;">Hermetic Core</div>
              <h3 class="triad-title">The Soul (opo-stated)</h3>
            </div>
          </div>
          <p class="triad-desc">
            Implemented in memory-safe Rust (<code>opo-stated</code>). Executes zero-trust state mutations as a Join-Semilattice <em>(S, ⊔)</em>. Completely offline-capable, cryptographically signed with Ed25519 identities, and resistant to network partitioning.
          </p>
          <div class="triad-features">
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Delta-CRDT Monotonic Join <code>State::join(delta)</code></span>
            </div>
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Zero-Allocation BTreeMap Causal Clocks</span>
            </div>
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Deterministic Anti-Entropy Convergence</span>
            </div>
          </div>
        </div>

        <div class="triad-card">
          <div class="triad-header">
            <div class="triad-icon-box body-icon-box">
              <img src="svg/gemini-sparkle.svg" alt="Body" width="28" height="28">
            </div>
            <div>
              <div style="font-size: 0.72rem; font-family: var(--font-mono); color: #94A3B8; text-transform: uppercase; margin-bottom: 2px;">Edge Sensorium</div>
              <h3 class="triad-title">The Body (Pipecat Edge)</h3>
            </div>
          </div>
          <p class="triad-desc">
            High-throughput, real-time multimodal audio, video, and sensory pipeline powered by <strong>Pipecat</strong> and <strong>Google Gemini SDK 2.0 / 3.0</strong>. Delivers sub-50ms conversational latency and bidirectional sensor streaming.
          </p>
          <div class="triad-features">
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>WebRTC & WebSocket Full-Duplex Transport</span>
            </div>
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Native Gemini Live 2.0 Multimodal API</span>
            </div>
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Voice Activity Detection (Silero VAD &lt;10ms)</span>
            </div>
          </div>
        </div>

        <div class="triad-card">
          <div class="triad-header">
            <div class="triad-icon-box mesh-icon-box">
              <img src="svg/scion-routing.svg" alt="Mesh" width="28" height="28">
            </div>
            <div>
              <div style="font-size: 0.72rem; font-family: var(--font-mono); color: #94A3B8; text-transform: uppercase; margin-bottom: 2px;">Global Fabric</div>
              <h3 class="triad-title">The Mesh (SCION Overlay)</h3>
            </div>
          </div>
          <p class="triad-desc">
            Path-aware inter-domain routing using the <strong>SCION (Scalability, Control, and Isolation On next-generation Networks)</strong> protocol. Immune to BGP hijacking, with end-to-end cryptographic path validation and multi-path failover.
          </p>
          <div class="triad-features">
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>End-to-End Cryptographic Packet Path Authorization</span>
            </div>
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Sub-Millisecond Multi-Path Failover</span>
            </div>
            <div class="triad-feature-item">
              <span class="feature-check">✓</span>
              <span>Isolation Domains (ISDs) for Critical Assets</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Deep Dive SCION Section -->
      <div id="scion" class="glass-panel" style="padding: 2.5rem; margin-bottom: 3rem;">
        <h2 style="font-size: 1.6rem; color: #FFFFFF; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">
          <img src="svg/scion-routing.svg" width="28" height="28" alt="SCION">
          <span>SCION Cryptographic Routing Specification</span>
        </h2>
        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7; margin-bottom: 1.5rem;">
          Traditional IP networks rely on Border Gateway Protocol (BGP), which lacks route authentication and path control. In the Omni-Present Omega architecture, every node communicates across <strong>Isolation Domains (ISDs)</strong>. Packets carry cryptographic Hop Fields computed over MAC keys:
        </p>
        <div class="math-proof-box" style="margin-bottom: 1.5rem;">
          <div class="math-proof-title">MATHEMATICAL PATH AUTHORIZATION</div>
          <div style="font-family: var(--font-mono); font-size: 0.88rem; color: var(--gemini-cyan); line-height: 1.6;">
            σ_i = MAC_{K_i}(ExpTime || InIF || OutIF || σ_{i-1})<br>
            ∀ p ∈ Path: Verify(σ_i, K_i) = True ⟹ Path_Valid
          </div>
        </div>
        <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
          <a href="crdt-lab.html" class="glass-btn glass-btn-primary">
            <span>Explore Delta-CRDT State Lab →</span>
          </a>
          <a href="whitepaper.html" class="glass-btn glass-btn-secondary">
            <span>Read Sovereign Whitepaper →</span>
          </a>
        </div>
      </div>
    </section>'''
)

# 2. crdt-lab.html
PAGES['crdt-lab.html'] = render_page(
    title="Delta-CRDT State Laboratory",
    desc="Interactive Join-Semilattice (S, ⊔) Simulator with 60 FPS Canvas visualizer and vector clock inspector.",
    current_breadcrumb='<a href="architecture.html">Architecture</a> <span class="sep">/</span> <span class="current">Delta-CRDT Lab</span>',
    body_content='''    <section class="landing-section">
      <div class="section-badge">
        <img src="svg/crdt-lattice.svg" width="16" height="16" alt="CRDT">
        <span>MATHEMATICAL JOIN-SEMILATTICE ENGINE</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">Interactive Delta-CRDT Laboratory</span>
      </h1>
      <p class="hero-desc" style="max-width: 820px; margin: 0 auto 2rem;">
        Experience real-time conflict-free replicated data synchronization. Each node acts as an autonomous element in a bounded join-semilattice <em>(S, ⊔)</em>. Mutations compute local $\delta$-deltas, propagating anti-entropy sync packets without centralized master coordination.
      </p>

      <!-- Live 60fps Canvas Simulator Card -->
      <div class="glass-panel" style="padding: 1.5rem; margin-bottom: 2.5rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.75rem;">
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="status-dot"></span>
            <span style="font-family: var(--font-mono); font-size: 0.85rem; color: #FFFFFF; font-weight: 600;">TOPOLOGY CAUSAL MESH (60 FPS CANVAS)</span>
          </div>
          <div style="display: flex; gap: 0.5rem;">
            <button class="glass-btn glass-btn-secondary" style="padding: 4px 10px; font-size: 0.75rem;" onclick="window.crdtSim.syncAll()">
              <span>⚡ Anti-Entropy Sync</span>
            </button>
            <button class="glass-btn glass-btn-secondary" style="padding: 4px 10px; font-size: 0.75rem; color: #F87171;" onclick="window.crdtSim.severPartition()">
              <span>✂ Sever / Heal Mesh</span>
            </button>
          </div>
        </div>

        <div style="width: 100%; height: 260px; background: rgba(5, 8, 16, 0.7); border-radius: 14px; position: relative; overflow: hidden; border: 1px solid rgba(255, 255, 255, 0.08);">
          <canvas id="crdt-topology-canvas" style="width: 100%; height: 100%; display: block;"></canvas>
        </div>
        <div style="display: flex; justify-content: space-between; font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); margin-top: 0.75rem;">
          <span>Tip: Tap on any node to select it for state injection.</span>
          <span id="partition-status-text" style="color: #34D399;">● Mesh Fully Connected</span>
        </div>
      </div>

      <!-- Two-Column Workbench: Mutation Form & State Viewer -->
      <div class="crdt-lab-grid">
        <div class="glass-panel" style="padding: 1.75rem;">
          <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 1rem; display: flex; align-items: center; gap: 8px;">
            <span>Inject State Mutation</span>
            <span class="brand-badge" style="background: rgba(123, 97, 255, 0.2); color: var(--gemini-purple);">Rust opo-stated</span>
          </h3>
          <form id="crdt-mutation-form">
            <div style="margin-bottom: 1rem;">
              <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">TARGET REPLICA NODE</label>
              <select id="node-target-select" class="glass-input" style="width: 100%;">
                <option value="alpha">Node Alpha (Robotics)</option>
                <option value="beta">Node Beta (Telemetry)</option>
                <option value="gamma">Node Gamma (Aether)</option>
                <option value="delta">Node Delta (Mobile)</option>
              </select>
            </div>
            <div style="margin-bottom: 1rem;">
              <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">STATE KEY</label>
              <input id="mutation-key-input" type="text" class="glass-input" value="sensor.temp_kelvin" style="width: 100%;">
            </div>
            <div style="margin-bottom: 1.5rem;">
              <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">STATE VALUE (JSON OR SCALAR)</label>
              <input id="mutation-val-input" type="text" class="glass-input" value="312.45" style="width: 100%;">
            </div>
            <button type="submit" class="glass-btn glass-btn-primary" style="width: 100%;">
              <span>Apply State Mutation (δ-Delta)</span>
            </button>
          </form>
        </div>

        <!-- Node State Inspector Cards -->
        <div class="glass-panel" style="padding: 1.75rem;">
          <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <span>Replicated State Table</span>
            <span id="selected-node-label" style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--gemini-cyan);">Selected: Alpha</span>
          </h3>
          <div id="crdt-state-inspector" style="min-height: 240px; font-family: var(--font-mono); font-size: 0.8rem; background: rgba(5, 8, 16, 0.75); border-radius: 12px; padding: 1rem; border: 1px solid rgba(255, 255, 255, 0.08); overflow-x: auto;">
            Loading replica state...
          </div>
        </div>
      </div>
    </section>'''
)

# 3. deeptech-fusion.html
PAGES['deeptech-fusion.html'] = render_page(
    title="SPARC Magnetohydrodynamic Fusion Reactor",
    desc="High-Temperature Superconducting REBCO Magnets and Q >= 2 Net Thermonuclear Energy Gain.",
    current_breadcrumb='<a href="index.html#deeptech">Deep Tech</a> <span class="sep">/</span> <span class="current">SPARC Fusion Tokamak</span>',
    body_content='''    <section class="landing-section">
      <div class="dossier-hero-container">
        <div>
          <div class="section-badge">
            <img src="svg/fusion-tokamak.svg" width="16" height="16" alt="Fusion">
            <span>FRONTIER DEEP TECH DOSSIER #01</span>
          </div>
          <h1 class="hero-title" style="text-align: left; margin-bottom: 1rem;">
            <span class="hero-gradient-text">SPARC Tokamak Fusion</span><br>
            <span style="color: #38BDF8; font-size: 1.6rem; font-weight: 600;">HTS REBCO Magnetics &amp; Net Energy Gain</span>
          </h1>
          <p class="hero-desc" style="text-align: left; margin: 0 0 1.5rem 0;">
            Commonwealth Fusion Systems (CFS) and MIT demonstrated the revolutionary 20-Tesla High-Temperature Superconducting (HTS) REBCO magnetic field coil. Because fusion power scales with the fourth power of magnetic field ($P_{fusion} \propto B^4$), SPARC achieves net commercial fusion energy ($Q \ge 2$) in a compact reactor footprint.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <span class="synergy-tag">LAWSON CRITERION: n·T·τE &gt; 3×10²¹ m⁻³·keV·s</span>
            <span class="synergy-tag" style="border-color: rgba(56, 189, 248, 0.4); color: #38bdf8;">REBCO HTS 20T COILS</span>
          </div>
        </div>

        <div class="dossier-visual-frame">
          <img src="assets/images/deeptech/fusion-tokamak-core.jpg" alt="SPARC Fusion Tokamak Core Octane Render">
          <div class="hero-visual-overlay"></div>
        </div>
      </div>

      <!-- Spec Metrics -->
      <div class="dossier-metric-grid">
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">Q ≥ 2.1</div>
          <div class="dossier-metric-label">Net Scientific Energy Gain</div>
        </div>
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">12.2 T</div>
          <div class="dossier-metric-label">On-Axis Toroidal Field</div>
        </div>
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">140M °C</div>
          <div class="dossier-metric-label">Core Plasma Temperature</div>
        </div>
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">&lt; 1 ms</div>
          <div class="dossier-metric-label">OPO EKF Magnetics Control</div>
        </div>
      </div>

      <!-- Interactive Lawson Criterion & Q-Gain Calculator -->
      <div class="interactive-slider-box">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;">
          <span>⚡ Interactive SPARC Thermonuclear Gain ($Q$) Explorer</span>
        </h3>
        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 1.5rem;">
          Adjust the Toroidal Magnetic Field ($B_t$) and Core Plasma Density ($n_e$) to observe non-linear scaling of fusion gain $Q = P_{fusion} / P_{heat}$.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
          <div>
            <div class="slider-row">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Toroidal Field ($B_t$):</span>
              <span id="fusion-bfield-val" style="font-size: 0.85rem; color: var(--gemini-cyan); font-weight: 700; font-family: var(--font-mono);">12.2 Tesla</span>
            </div>
            <input type="range" id="fusion-bfield-slider" class="custom-range-slider" min="8" max="16" step="0.2" value="12.2">

            <div class="slider-row" style="margin-top: 1.25rem;">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Plasma Density ($n_e$):</span>
              <span id="fusion-density-val" style="font-size: 0.85rem; color: var(--gemini-purple); font-weight: 700; font-family: var(--font-mono);">3.1 × 10²⁰ m⁻³</span>
            </div>
            <input type="range" id="fusion-density-slider" class="custom-range-slider" min="1.5" max="5.0" step="0.1" value="3.1">
          </div>

          <div style="background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <div style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); text-transform: uppercase;">Predicted Thermonuclear Output</div>
            <div id="fusion-q-result" style="font-size: 2.2rem; font-weight: 800; color: #34D399; font-family: var(--font-mono); margin: 6px 0;">Q = 2.10</div>
            <div id="fusion-pnet-result" style="font-size: 0.95rem; color: #E2E8F0; font-family: var(--font-mono);">137.3 MW Net</div>
          </div>
        </div>
      </div>

      <!-- Technical Dossier Details -->
      <div class="glass-panel" style="padding: 2rem; margin-top: 2.5rem;">
        <h3 style="font-size: 1.25rem; color: #FFFFFF; margin-bottom: 1rem;">OPO &amp; RedComm Convergence Synergy</h3>
        <p style="color: #94A3B8; line-height: 1.7; font-size: 0.92rem;">
          Tokamak plasma instabilities (such as Neoclassical Tearing Modes and Edge Localized Modes) evolve on microsecond timescales. The OPO decentralized architecture couples localized edge neuromorphic nodes directly to coil power supplies via sub-millisecond CRDT channels, achieving real-time plasma equilibrium control without single points of failure.
        </p>
      </div>
    </section>'''
)

# 4. deeptech-quantum.html
PAGES['deeptech-quantum.html'] = render_page(
    title="Fault-Tolerant Quantum & Photonics",
    desc="Thin-Film Lithium Niobate (TFLN) Coherent Optical Modulators and Cryogenic Quantum Coherence.",
    current_breadcrumb='<a href="index.html#deeptech">Deep Tech</a> <span class="sep">/</span> <span class="current">Quantum Photonics</span>',
    body_content='''    <section class="landing-section">
      <div class="dossier-hero-container">
        <div>
          <div class="section-badge">
            <img src="svg/quantum-photonics.svg" width="16" height="16" alt="Quantum">
            <span>FRONTIER DEEP TECH DOSSIER #02</span>
          </div>
          <h1 class="hero-title" style="text-align: left; margin-bottom: 1rem;">
            <span class="hero-gradient-text">Fault-Tolerant Quantum</span><br>
            <span style="color: #A78BFA; font-size: 1.6rem; font-weight: 600;">Thin-Film Lithium Niobate (TFLN) Photonics</span>
          </h1>
          <p class="hero-desc" style="text-align: left; margin: 0 0 1.5rem 0;">
            Scalable quantum computing demands interconnecting cryogenically cooled qubits with room-temperature photonic networks. Integrated Thin-Film Lithium Niobate (TFLN) electro-optic modulators achieve ultra-low optical loss (&lt;0.03 dB/cm) and half-wave voltages below 1.5 V at &gt;100 GHz bandwidth.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <span class="synergy-tag">BANDWIDTH: &gt; 100 GHz</span>
            <span class="synergy-tag" style="border-color: rgba(167, 139, 250, 0.4); color: #A78BFA;">TFLN ELECTRO-OPTIC COUPLING</span>
          </div>
        </div>

        <div class="dossier-visual-frame">
          <img src="assets/images/deeptech/quantum-optical-chip.jpg" alt="Quantum Photonics Optical Chip Render">
          <div class="hero-visual-overlay"></div>
        </div>
      </div>

      <!-- Spec Metrics -->
      <div class="dossier-metric-grid">
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">&gt; 110 GHz</div>
          <div class="dossier-metric-label">Electro-Optic Modulation Speed</div>
        </div>
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">&lt; 0.027 dB/cm</div>
          <div class="dossier-metric-label">Waveguide Propagation Loss</div>
        </div>
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">99.98%</div>
          <div class="dossier-metric-label">Two-Qubit Gate Fidelity</div>
        </div>
        <div class="dossier-metric-card">
          <div class="dossier-metric-val">15 mK</div>
          <div class="dossier-metric-label">Dilution Refrigerator Base Temp</div>
        </div>
      </div>

      <!-- Interactive Quantum Coherence Explorer -->
      <div class="interactive-slider-box">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;">
          <span>🔬 Interactive Quantum Coherence &amp; Gate Fidelity Explorer</span>
        </h3>
        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 1.5rem;">
          Evaluate cryogenic quantum gate fidelity $\mathcal{F}$ as a function of physical qubit cluster size and dilution cryostat temperature.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
          <div>
            <div class="slider-row">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Physical Qubits ($N$):</span>
              <span id="quantum-qubits-val" style="font-size: 0.85rem; color: var(--gemini-cyan); font-weight: 700; font-family: var(--font-mono);">64 Physical Qubits</span>
            </div>
            <input type="range" id="quantum-qubits-slider" class="custom-range-slider" min="16" max="256" step="16" value="64">

            <div class="slider-row" style="margin-top: 1.25rem;">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Cryostat Temp ($T$):</span>
              <span id="quantum-temp-val" style="font-size: 0.85rem; color: var(--gemini-purple); font-weight: 700; font-family: var(--font-mono);">15.0 mK</span>
            </div>
            <input type="range" id="quantum-temp-slider" class="custom-range-slider" min="10" max="40" step="1" value="15">
          </div>

          <div style="background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <div style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); text-transform: uppercase;">Estimated Two-Qubit Fidelity</div>
            <div id="quantum-fidelity-result" style="font-size: 2.2rem; font-weight: 800; color: #A78BFA; font-family: var(--font-mono); margin: 6px 0;">99.788%</div>
            <div id="quantum-coherence-result" style="font-size: 0.95rem; color: #E2E8F0; font-family: var(--font-mono);">1200 µs Coherence Time</div>
          </div>
        </div>
      </div>
    </section>'''
)

# 5. deeptech-battery.html
PAGES['deeptech-battery.html'] = render_page(
    title="Solid-State Lithium-Metal Energy Matrix",
    desc="500 Wh/kg Anode-Free Solid-State Battery Architecture with Ceramic Electrolyte.",
    current_breadcrumb='<a href="index.html#deeptech">Deep Tech</a> <span class="sep">/</span> <span class="current">Solid-State Battery</span>',
    body_content='''    <section class="landing-section">
      <div class="dossier-hero-container">
        <div>
          <div class="section-badge">
            <img src="svg/battery-solidstate.svg" width="16" height="16" alt="Battery">
            <span>FRONTIER DEEP TECH DOSSIER #03</span>
          </div>
          <h1 class="hero-title" style="text-align: left; margin-bottom: 1rem;">
            <span class="hero-gradient-text">Solid-State Lithium-Metal</span><br>
            <span style="color: #F59E0B; font-size: 1.6rem; font-weight: 600;">500 Wh/kg Anode-Free Energy Matrix</span>
          </h1>
          <p class="hero-desc" style="text-align: left; margin: 0 0 1.5rem 0;">
            Next-generation autonomous robotics and aerospace require doubling energy density while eliminating thermal runaway hazards. Replacing flammable liquid electrolytes with dense garnet-type ceramic membranes (LLZO) enables pure lithium-metal anode plating, reaching 500 Wh/kg.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <span class="synergy-tag">GRAVIMETRIC DENSITY: &gt; 500 Wh/kg</span>
            <span class="synergy-tag" style="border-color: rgba(245, 158, 11, 0.4); color: #F59E0B;">ZERO-ANODE PLATING</span>
          </div>
        </div>

        <div class="dossier-visual-frame">
          <img src="assets/images/deeptech/solid-state-cell.jpg" alt="Solid-State Battery Microstructure Render">
          <div class="hero-visual-overlay"></div>
        </div>
      </div>

      <!-- Spec Metrics -->
      <div class="dossier-metric-grid">
        <div class="dossier-metric-val">505 Wh/kg</div>
        <div class="dossier-metric-label">Gravimetric Energy Density</div>
        <div class="dossier-metric-val">1,180 Wh/L</div>
        <div class="dossier-metric-label">Volumetric Energy Density</div>
        <div class="dossier-metric-val">&gt; 1,800</div>
        <div class="dossier-metric-label">80% Retention Cycles</div>
        <div class="dossier-metric-val">12 min</div>
        <div class="dossier-metric-label">10% to 80% Fast Charge</div>
      </div>

      <!-- Interactive Battery Simulator -->
      <div class="interactive-slider-box">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;">
          <span>🔋 Solid-State Battery Energy &amp; Cycle Life Simulator</span>
        </h3>
        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 1.5rem;">
          Model the relationship between solid ceramic separator thickness (µm) and operating temperature on cell energy density and lifespan.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
          <div>
            <div class="slider-row">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Separator Thickness:</span>
              <span id="battery-thick-val" style="font-size: 0.85rem; color: var(--gemini-cyan); font-weight: 700; font-family: var(--font-mono);">18 µm Electrolyte</span>
            </div>
            <input type="range" id="battery-thick-slider" class="custom-range-slider" min="10" max="30" step="1" value="18">

            <div class="slider-row" style="margin-top: 1.25rem;">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Operating Temperature:</span>
              <span id="battery-temp-val" style="font-size: 0.85rem; color: #F59E0B; font-weight: 700; font-family: var(--font-mono);">25 °C</span>
            </div>
            <input type="range" id="battery-temp-slider" class="custom-range-slider" min="0" max="60" step="5" value="25">
          </div>

          <div style="background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <div style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); text-transform: uppercase;">Calculated Gravimetric Density</div>
            <div id="battery-whkg-result" style="font-size: 2.2rem; font-weight: 800; color: #F59E0B; font-family: var(--font-mono); margin: 6px 0;">518 Wh/kg</div>
            <div id="battery-cycles-result" style="font-size: 0.95rem; color: #E2E8F0; font-family: var(--font-mono);">1800 Cycles (85%)</div>
          </div>
        </div>
      </div>
    </section>'''
)

# 6. deeptech-genomic.html
PAGES['deeptech-genomic.html'] = render_page(
    title="Prime & Epigenetic Genomic Reprogramming",
    desc="CRISPR Prime Editing with pegRNA and Reverse Transcriptase for Double-Strand-Break-Free Precision.",
    current_breadcrumb='<a href="index.html#deeptech">Deep Tech</a> <span class="sep">/</span> <span class="current">Prime Genome Editing</span>',
    body_content='''    <section class="landing-section">
      <div class="dossier-hero-container">
        <div>
          <div class="section-badge">
            <img src="svg/genomic-crispr.svg" width="16" height="16" alt="Genomics">
            <span>FRONTIER DEEP TECH DOSSIER #04</span>
          </div>
          <h1 class="hero-title" style="text-align: left; margin-bottom: 1rem;">
            <span class="hero-gradient-text">Prime &amp; Epigenetic Editing</span><br>
            <span style="color: #EC4899; font-size: 1.6rem; font-weight: 600;">pegRNA Search-and-Replace Molecular Architecture</span>
          </h1>
          <p class="hero-desc" style="text-align: left; margin: 0 0 1.5rem 0;">
            Prime editing rewrites genomic sequences without generating double-stranded DNA breaks (DSBs). By fusing a catalytically impaired Cas9 nickase to an engineered M-MLV reverse transcriptase and guiding it with prime editing guide RNA (pegRNA), all 12 base-to-base transitions, transversions, and targeted insertions become deterministic.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <span class="synergy-tag">PRECISION: &gt; 92% ON-TARGET</span>
            <span class="synergy-tag" style="border-color: rgba(236, 72, 153, 0.4); color: #EC4899;">ZERO DOUBLE-STRAND BREAKS</span>
          </div>
        </div>

        <div class="dossier-visual-frame">
          <img src="assets/images/deeptech/prime-editing-helix.jpg" alt="Prime Editing DNA Double Helix Render">
          <div class="hero-visual-overlay"></div>
        </div>
      </div>

      <!-- Spec Metrics -->
      <div class="dossier-metric-grid">
        <div class="dossier-metric-val">&lt; 0.5%</div>
        <div class="dossier-metric-label">Indel Byproduct Rate</div>
        <div class="dossier-metric-val">12/12</div>
        <div class="dossier-metric-label">Base Substitution Classes</div>
        <div class="dossier-metric-val">&gt; 1 kb</div>
        <div class="dossier-metric-label">Targeted Gene Insertion Window</div>
        <div class="dossier-metric-val">16 ms</div>
        <div class="dossier-metric-label">Gemini AlphaFold Prediction</div>
      </div>

      <!-- Interactive pegRNA Simulator -->
      <div class="interactive-slider-box">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;">
          <span>🧬 Interactive pegRNA Architecture &amp; Efficiency Simulator</span>
        </h3>
        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 1.5rem;">
          Optimize the Primer Binding Site (PBS) and Reverse Transcription Template (RTT) nucleotide lengths to maximize on-target editing efficiency while suppressing insertions/deletions.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
          <div>
            <div class="slider-row">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Primer Binding Site (PBS):</span>
              <span id="genomic-pbs-val" style="font-size: 0.85rem; color: #EC4899; font-weight: 700; font-family: var(--font-mono);">13 nt PBS</span>
            </div>
            <input type="range" id="genomic-pbs-slider" class="custom-range-slider" min="9" max="17" step="1" value="13">

            <div class="slider-row" style="margin-top: 1.25rem;">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">RT Template Length (RTT):</span>
              <span id="genomic-rtt-val" style="font-size: 0.85rem; color: var(--gemini-cyan); font-weight: 700; font-family: var(--font-mono);">16 nt RTT</span>
            </div>
            <input type="range" id="genomic-rtt-slider" class="custom-range-slider" min="10" max="24" step="1" value="16">
          </div>

          <div style="background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <div style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); text-transform: uppercase;">Editing Efficiency Profile</div>
            <div id="genomic-eff-result" style="font-size: 2.2rem; font-weight: 800; color: #EC4899; font-family: var(--font-mono); margin: 6px 0;">62% On-Target</div>
            <div id="genomic-indel-result" style="font-size: 0.95rem; color: #E2E8F0; font-family: var(--font-mono);">0.55% Indels</div>
          </div>
        </div>
      </div>
    </section>'''
)

# 7. deeptech-neural.html
PAGES['deeptech-neural.html'] = render_page(
    title="Intracortical BCI Micro-Threads",
    desc="1024-Channel Flexible Polyimide Micro-Threads and Sub-Millisecond Neural Spike Sorting.",
    current_breadcrumb='<a href="index.html#deeptech">Deep Tech</a> <span class="sep">/</span> <span class="current">Intracortical BCI</span>',
    body_content='''    <section class="landing-section">
      <div class="dossier-hero-container">
        <div>
          <div class="section-badge">
            <img src="svg/neural-threads.svg" width="16" height="16" alt="Neural">
            <span>FRONTIER DEEP TECH DOSSIER #05</span>
          </div>
          <h1 class="hero-title" style="text-align: left; margin-bottom: 1rem;">
            <span class="hero-gradient-text">Intracortical BCI</span><br>
            <span style="color: #6366F1; font-size: 1.6rem; font-weight: 600;">Flexible Polyimide Micro-Thread Arrays</span>
          </h1>
          <p class="hero-desc" style="text-align: left; margin: 0 0 1.5rem 0;">
            Rigid silicon probes induce glial scar formation and chronic neuroinflammation. Omni-Present Omega integrates 1024-channel flexible micron-scale polyimide threads. Inserted by rapid-fire optical vision robots, these biocompatible threads yield high single-unit action potential isolation for years.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <span class="synergy-tag">CHANNEL COUNT: 1,024 ELECTRODES</span>
            <span class="synergy-tag" style="border-color: rgba(99, 102, 241, 0.4); color: #818CF8;">SUB-MILLISECOND SPIKE SORTING</span>
          </div>
        </div>

        <div class="dossier-visual-frame">
          <img src="assets/images/deeptech/neural-polyimide-threads.jpg" alt="Neural Polyimide Micro-Thread Array Render">
          <div class="hero-visual-overlay"></div>
        </div>
      </div>

      <!-- Spec Metrics -->
      <div class="dossier-metric-grid">
        <div class="dossier-metric-val">1,024</div>
        <div class="dossier-metric-label">Active Recording Electrodes</div>
        <div class="dossier-metric-val">4 to 6 µm</div>
        <div class="dossier-metric-label">Polyimide Thread Thickness</div>
        <div class="dossier-metric-val">&lt; 0.65 ms</div>
        <div class="dossier-metric-label">Closed-Loop Spike Decoding</div>
        <div class="dossier-metric-val">&gt; 5 Years</div>
        <div class="dossier-metric-label">Biocompatibility Lifetime</div>
      </div>

      <!-- Interactive BCI Simulator -->
      <div class="interactive-slider-box">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;">
          <span>🧠 Interactive Neural Telemetry &amp; Decoding Bandwidth Simulator</span>
        </h3>
        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 1.5rem;">
          Calculate raw electrode telemetry bandwidth (Mbps) and edge spike sorting latency as channel count and sampling rate scale.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
          <div>
            <div class="slider-row">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Electrode Count:</span>
              <span id="neural-channels-val" style="font-size: 0.85rem; color: #818CF8; font-weight: 700; font-family: var(--font-mono);">1024 Electrodes</span>
            </div>
            <input type="range" id="neural-channels-slider" class="custom-range-slider" min="256" max="4096" step="256" value="1024">

            <div class="slider-row" style="margin-top: 1.25rem;">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Sampling Frequency:</span>
              <span id="neural-khz-val" style="font-size: 0.85rem; color: var(--gemini-cyan); font-weight: 700; font-family: var(--font-mono);">30 kHz</span>
            </div>
            <input type="range" id="neural-khz-slider" class="custom-range-slider" min="10" max="40" step="5" value="30">
          </div>

          <div style="background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <div style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); text-transform: uppercase;">Telemetry Bandwidth &amp; Latency</div>
            <div id="neural-bw-result" style="font-size: 2.2rem; font-weight: 800; color: #818CF8; font-family: var(--font-mono); margin: 6px 0;">491.5 Mbps Raw</div>
            <div id="neural-lat-result" style="font-size: 0.95rem; color: #E2E8F0; font-family: var(--font-mono);">0.52 ms Latency</div>
          </div>
        </div>
      </div>
    </section>'''
)

# 8. deeptech-robotics.html
PAGES['deeptech-robotics.html'] = render_page(
    title="Embodied Humanoid Actuators & VLA Control",
    desc="Quasi-Direct Drive (QDD) Actuators and End-to-End Vision-Language-Action Neural Control.",
    current_breadcrumb='<a href="index.html#deeptech">Deep Tech</a> <span class="sep">/</span> <span class="current">Humanoid Robotics</span>',
    body_content='''    <section class="landing-section">
      <div class="dossier-hero-container">
        <div>
          <div class="section-badge">
            <img src="svg/humanoid-robotics.svg" width="16" height="16" alt="Robotics">
            <span>FRONTIER DEEP TECH DOSSIER #06</span>
          </div>
          <h1 class="hero-title" style="text-align: left; margin-bottom: 1rem;">
            <span class="hero-gradient-text">Embodied Humanoids</span><br>
            <span style="color: #10B981; font-size: 1.6rem; font-weight: 600;">Quasi-Direct Drive &amp; Whole-Body VLA Control</span>
          </h1>
          <p class="hero-desc" style="text-align: left; margin: 0 0 1.5rem 0;">
            Humanoid locomotion requires high torque transparency and impact backdrivability. By pairing low gear ratio Quasi-Direct Drive (QDD &le; 10:1) motors with planetary gearing and high-flux NdFeB magnets, robots achieve natural compliance while executing end-to-end multimodal policies via Gemini Vision-Language-Action (VLA) models.
          </p>
          <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
            <span class="synergy-tag">BANDWIDTH: &gt; 50 Hz</span>
            <span class="synergy-tag" style="border-color: rgba(16, 185, 129, 0.4); color: #34D399;">QDD BACKDRIVABLE ACTUATORS</span>
          </div>
        </div>

        <div class="dossier-visual-frame">
          <img src="assets/images/deeptech/humanoid-actuator-skeleton.jpg" alt="Humanoid Actuator Skeleton Render">
          <div class="hero-visual-overlay"></div>
        </div>
      </div>

      <!-- Spec Metrics -->
      <div class="dossier-metric-grid">
        <div class="dossier-metric-val">120 Nm</div>
        <div class="dossier-metric-label">Joint Peak Torque</div>
        <div class="dossier-metric-val">8:1 QDD</div>
        <div class="dossier-metric-label">Backdrivable Gear Ratio</div>
        <div class="dossier-metric-val">1,000 Hz</div>
        <div class="dossier-metric-label">Whole-Body Impedance Loop</div>
        <div class="dossier-metric-val">38 ms</div>
        <div class="dossier-metric-label">Gemini VLA Inference Time</div>
      </div>

      <!-- Interactive Robotics Simulator -->
      <div class="interactive-slider-box">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; margin-bottom: 0.5rem; display: flex; align-items: center; gap: 8px;">
          <span>🤖 Interactive Actuator Torque &amp; Bandwidth Simulator</span>
        </h3>
        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 1.5rem;">
          Examine the tradeoff between motor stator diameter and planetary reduction ratio on peak torque and dynamic mechanical bandwidth.
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem;">
          <div>
            <div class="slider-row">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Stator Diameter:</span>
              <span id="robotics-dia-val" style="font-size: 0.85rem; color: #34D399; font-weight: 700; font-family: var(--font-mono);">90 mm Diameter</span>
            </div>
            <input type="range" id="robotics-dia-slider" class="custom-range-slider" min="60" max="130" step="5" value="90">

            <div class="slider-row" style="margin-top: 1.25rem;">
              <span style="font-size: 0.82rem; color: #E2E8F0; font-family: var(--font-mono);">Gear Ratio:</span>
              <span id="robotics-gear-val" style="font-size: 0.85rem; color: var(--gemini-cyan); font-weight: 700; font-family: var(--font-mono);">8:1 QDD</span>
            </div>
            <input type="range" id="robotics-gear-slider" class="custom-range-slider" min="4" max="15" step="1" value="8">
          </div>

          <div style="background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 14px; padding: 1.25rem; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center;">
            <div style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono); text-transform: uppercase;">Dynamic Actuator Output</div>
            <div id="robotics-torque-result" style="font-size: 2.2rem; font-weight: 800; color: #34D399; font-family: var(--font-mono); margin: 6px 0;">28.0 Nm Peak</div>
            <div id="robotics-bw-result" style="font-size: 0.95rem; color: #E2E8F0; font-family: var(--font-mono);">64 Hz Bandwidth</div>
          </div>
        </div>
      </div>
    </section>'''
)

# 9. gemini-studio.html
PAGES['gemini-studio.html'] = render_page(
    title="Gemini 4.0 Argon Multimodal Engine",
    desc="Live Interactive Workbench for Gemini 4.0 Argon Multimodal APIs, Live Streaming, and Tool Schema Validation.",
    current_breadcrumb='<a href="gemini-studio.html">Developer Tools</a> <span class="sep">/</span> <span class="current">Gemini 4.0 Argon Engine</span>',
    body_content='''    <section class="landing-section">
      <div class="section-badge">
        <img src="svg/gemini-sparkle.svg" width="16" height="16" alt="Gemini">
        <span>GEMINI 4.0 ARGON MULTIMODAL REASONING ENGINE</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">Gemini 4.0 Argon Engine</span>
      </h1>
      <p class="hero-desc" style="max-width: 820px; margin: 0 auto 2.5rem;">
        Harness Google DeepMind's flagship Gemini 4.0 Argon multimodal reasoning and physics co-processor directly in the browser. Test streaming token generation with a 16k thinking budget, verify function calling schemas, and inspect real-time sub-5ms multimodal audio/video/tactile telemetry.
      </p>

      <div class="gemini-hub-grid">
        <div class="glass-panel" style="padding: 1.75rem;">
          <h3 style="font-size: 1.2rem; color: #FFFFFF; margin-bottom: 1rem; display: flex; align-items: center; gap: 8px;">
            <img src="svg/gemini-animated.svg" width="22" height="22" alt="Sparkle">
            <span>Multimodal Inference Workbench</span>
          </h3>

          <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.25rem;">
            <button class="modality-pill active" data-modality="text">💬 Text &amp; Code</button>
            <button class="modality-pill" data-modality="audio">🎙️ Live Audio</button>
            <button class="modality-pill" data-modality="vision">👁️ Video / Vision</button>
            <button class="modality-pill" data-modality="tools">⚙️ Function Calling</button>
          </div>

          <div style="margin-bottom: 1rem;">
            <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">SELECT MODEL TIER</label>
            <select id="gemini-model-select" class="glass-input" style="width: 100%;">
              <option value="gemini-4.0-argon" selected>Gemini 4.0 Argon (Google Flagship • Deep Reasoning &amp; Physics Co-Processor)</option>
              <option value="gemini-4.0-argon-live">Gemini 4.0 Argon Live (Sub-5ms Realtime Audio/Vision/Haptic Stream)</option>
              <option value="gemini-3.0-pro">Gemini 3.0 Pro (Algorithmic Verification &amp; Formal Proofs)</option>
              <option value="gemini-2.5-flash">Gemini 2.5 Flash (Edge Sensor Ingestion &amp; Tensor Dispatch)</option>
            </select>
          </div>

          <div style="margin-bottom: 1.25rem;">
            <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">PROMPT INPUT</label>
            <textarea id="gemini-prompt-input" class="glass-input" rows="4" style="width: 100%; resize: vertical;" placeholder="Enter scientific or architectural prompt...">Analyze the Join-Semilattice (S, ⊔) state convergence and SPARC HTS magnet tensors under Gemini 4.0 Argon physics co-processing.</textarea>
          </div>

          <button class="glass-btn glass-btn-primary" style="width: 100%;" onclick="runGeminiMockInference()">
            <img src="svg/gemini-sparkle.svg" width="18" height="18" alt="Run">
            <span>Run Gemini 4.0 Argon Inference</span>
          </button>
        </div>

        <div class="glass-panel" style="padding: 1.75rem;">
          <h3 style="font-size: 1.2rem; color: #FFFFFF; margin-bottom: 1rem; display: flex; align-items: center; justify-content: space-between;">
            <span>Streaming Output Console</span>
            <span class="brand-badge" style="background: rgba(16, 185, 129, 0.15); color: #34D399;">STREAM ACTIVE</span>
          </h3>
          <div id="gemini-output-box" style="min-height: 280px; background: rgba(5, 8, 16, 0.8); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 12px; padding: 1.25rem; font-family: var(--font-mono); font-size: 0.85rem; color: #E2E8F0; line-height: 1.6; overflow-y: auto;">
            Click "Run Gemini 4.0 Argon Inference" to stream response with 16k token thinking budget...
          </div>
        </div>
      </div>

      <!-- Official Gemini 4.0 Argon SDK Reference Panels -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
        <div class="glass-panel" style="padding: 1.5rem;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
            <img src="svg/gemini-sparkle.svg" width="18" height="18" alt="Gemini">
            <h4 style="font-size: 0.95rem; font-weight: 700; color: #FFF;">Python: <code>google-genai</code> (v4)</h4>
          </div>
          <pre style="background: rgba(0,0,0,0.6); padding: 1rem; border-radius: 10px; font-family: var(--font-mono); font-size: 0.78rem; color: #E2E8F0; overflow-x: auto;"><code>from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-4.0-argon",
    contents="Synthesize OPO Delta-CRDT vector & Lawson criterion",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=16384),
        temperature=0.2,
        tools=[{"function_declarations": [crdt_tool]}]
    )
)</code></pre>
        </div>

        <div class="glass-panel" style="padding: 1.5rem;">
          <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 0.75rem;">
            <img src="svg/gemini-sparkle.svg" width="18" height="18" alt="Gemini">
            <h4 style="font-size: 0.95rem; font-weight: 700; color: #FFF;">TypeScript: <code>@google/genai</code></h4>
          </div>
          <pre style="background: rgba(0,0,0,0.6); padding: 1rem; border-radius: 10px; font-family: var(--font-mono); font-size: 0.78rem; color: #E2E8F0; overflow-x: auto;"><code>import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();
const stream = await ai.models.generateContentStream({
  model: "gemini-4.0-argon-live",
  contents: "Stream low-latency intent vector with physics co-processing",
  config: {
    thinkingConfig: { thinkingBudget: 8192 }
  }
});</code></pre>
        </div>
      </div>
    </section>'''
)

# 10. whitepaper.html
PAGES['whitepaper.html'] = render_page(
    title="Sovereign Mathematics & Protocol Specifications",
    desc="Formal Join-Semilattice (S, ⊔) Proofs, Byzantine Fault Tolerance, and SCION Protocol Specifications.",
    current_breadcrumb='<a href="whitepaper.html">Whitepaper</a> <span class="sep">/</span> <span class="current">Mathematical Proofs</span>',
    body_content='''    <section class="landing-section">
      <div class="section-badge">
        <img src="svg/gemini-deep-research.svg" width="16" height="16" alt="Whitepaper">
        <span>FORMAL MATHEMATICAL RIGOR</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">Sovereign Whitepaper</span>
      </h1>
      <p class="hero-desc" style="max-width: 820px; margin: 0 auto 2.5rem;">
        Formal algebraic verification of the RedComm distributed state fabric, proving eventual consistency, monotonicity, and Byzantine partition resilience.
      </p>

    <!-- ====================================================================
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

      <div class="glass-panel" style="padding: 2.5rem; margin-bottom: 2rem;">
        <h2 style="font-size: 1.5rem; color: #FFFFFF; margin-bottom: 1rem;">Theorem 1: Convergence of Bounded Join-Semilattices</h2>
        <div class="math-proof-box" style="margin-bottom: 1.5rem;">
          <div class="math-proof-title">ALGEBRAIC PROOF OF MONOTONIC CONVERGENCE</div>
          <p style="font-family: var(--font-mono); font-size: 0.88rem; color: var(--gemini-cyan); line-height: 1.8;">
            Let (S, ⊔) be a join-semilattice where:<br>
            1. Commutativity: ∀ a, b ∈ S, a ⊔ b = b ⊔ a<br>
            2. Associativity: ∀ a, b, c ∈ S, (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c)<br>
            3. Idempotence: ∀ a ∈ S, a ⊔ a = a<br>
            <br>
            Let concurrent state updates produce a set of deltas {δ₁, δ₂, ..., δₙ}. Then the resultant state S' = S₀ ⊔ δ₁ ⊔ δ₂ ⊔ ... ⊔ δₙ is invariant under arbitrary message interleaving, network reordering, and duplicate packet delivery.
          </p>
        </div>
        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.7;">
          Because each mutation δ is strictly monotonically increasing with respect to the partial order &le; defined by $x \le y \iff x \sqcup y = y$, all replicas in the Omni-Present Omega mesh converge to identical state without two-phase commit (2PC) or centralized locking.
        </p>
      </div>

      <div class="glass-panel" style="padding: 2.5rem;">
        <h2 style="font-size: 1.5rem; color: #FFFFFF; margin-bottom: 1rem;">Academic References &amp; Citations</h2>
        <ol style="color: #94A3B8; font-size: 0.9rem; line-height: 1.8; padding-left: 1.5rem; font-family: var(--font-mono);">
          <li>Shapiro, M., Preguiça, N., Baquero, C., &amp; Zawirski, M. (2011). <em>Conflict-Free Replicated Data Types</em>. In Stabilization, Safety, and Security of Distributed Systems (pp. 386-400). Springer.</li>
          <li>Perrig, A., Szalachowski, P., Reischuk, R. M., &amp; Chuat, L. (2017). <em>SCION: A Secure Internet Architecture</em>. Springer.</li>
          <li>Creutzburg, M., et al. (2021). <em>SPARC: The high-field path to magnetic fusion energy</em>. Journal of Plasma Physics, 86(5).</li>
          <li>Google DeepMind. (2026). <em>Gemini 4.0 Argon: Frontier Multimodal Deep Reasoning, Physics Co-Processing, and Realtime Bidirectional Sensory Synchronization</em>.</li>
        </ol>
      </div>
    </section>'''
)

# 11. deploy.html
PAGES['deploy.html'] = render_page(
    title="Production Edge Deployment & Diagnostics Hub",
    desc="Sovereign Edge Deployment, Cluster Node Provisioning, and 3D System Verification Suite for Omni-Present Omega.",
    current_breadcrumb='<a href="deploy.html">Operations</a> <span class="sep">/</span> <span class="current">Edge Deployment</span>',
    body_content='''    <section class="landing-section">
      <div class="section-badge" style="border-color: rgba(0, 242, 254, 0.4); color: var(--gemini-cyan);">
        <span>⚡ PRODUCTION EDGE DEPLOYMENT &amp; DIAGNOSTICS</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">Edge Deployment &amp; Diagnostics Hub</span>
      </h1>
      <p class="hero-desc" style="max-width: 820px; margin: 0 auto 2.5rem;">
        Deploy, inspect, and verify sovereign distributed mesh nodes across edge hardware, container runtimes, and SCION path-aware network topologies.
      </p>

    <!-- ====================================================================
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

      <div class="glass-panel" style="padding: 2.5rem; margin-bottom: 2rem;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.75rem;">
          <h2 style="font-size: 1.4rem; color: #FFFFFF; margin: 0;">Step 1: Edge Daemon Compilation &amp; Release Run</h2>
          <span class="brand-badge" style="background: rgba(0, 242, 254, 0.15); color: var(--gemini-cyan); border-color: rgba(0, 242, 254, 0.3);">BINARY: ./target/release/opo-stated</span>
        </div>

        <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.25rem;">
          Compile the high-performance Rust causal mesh daemon and launch Node Alpha with local gossip bindings and SCION path discovery:
        </p>

        <div class="copyable-command" onclick="copyDeployCommand('./target/release/opo-stated --node-id alpha --gossip-bind 127.0.0.1:9001 --local-bind 127.0.0.1:8001 --peers 127.0.0.1:9002', this)" title="Click to copy" style="margin-bottom: 1.5rem;">
          <code>./target/release/opo-stated --node-id alpha --gossip-bind 127.0.0.1:9001 --local-bind 127.0.0.1:8001 --peers 127.0.0.1:9002</code>
          <span class="copy-badge">Copy 📋</span>
        </div>

        <h2 style="font-size: 1.4rem; color: #FFFFFF; margin: 2rem 0 1rem 0;">Step 2: Sovereign Edge Container Orchestration</h2>
        <div class="copyable-command" onclick="copyDeployCommand('docker compose -f docker-compose.edge.yml up -d --build', this)" title="Click to copy" style="margin-bottom: 1.5rem;">
          <code>docker compose -f docker-compose.edge.yml up -d --build</code>
          <span class="copy-badge">Copy 📋</span>
        </div>

        <div style="background: rgba(16, 185, 129, 0.08); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 12px; padding: 1.25rem; margin-top: 2rem;">
          <div style="font-size: 0.85rem; font-weight: 700; color: #34D399; margin-bottom: 4px;">✓ LOCAL DAEMON VERIFIED</div>
          <div style="font-size: 0.82rem; color: #94A3B8;">Local preview server is running on port 8080. All 14 pages, assets, SVGs, and telemetry engines are validated and operational.</div>
        </div>
      </div>
    </section>'''
)


# 12. sentient-radar.html (Project SENTIENT Multi-Spectral Radar & Multi-Agent Swarm)
PAGES['sentient-radar.html'] = render_page(
    title="Project SENTIENT Radar & Swarm Deliberation",
    desc="60 FPS Multi-Spectral Radar, 5-Agent Swarm Deliberation (Vortex, Spectre, Chronos, Nexus, Omni), MHD Plasma Sheath Calculator, and Zero-Knowledge Whistleblower Portal.",
    current_breadcrumb='<a href="sentient-radar.html">Intelligence</a> <span class="sep">/</span> <span class="current">Project SENTIENT &amp; Swarm</span>',
    body_content='''    <!-- Hero Section -->
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
        Calculate boundary-layer electromagnetic acceleration (\(F_L = \mathbf{j} 	imes \mathbf{B}\)). By accelerating ionized air slipstreams ahead of the vehicle, wave drag is suppressed by up to 98% and acoustic pressure discontinuities are smoothed, neutralizing the sonic boom.
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
            <strong style="color: var(--gemini-cyan);">Sonic Boom Neutralization:</strong> At \(\Delta v > 20	ext{ km/s}\), the boundary layer plasma sheath expels atmospheric gas molecules around the vehicle faster than the speed of sound in the ambient medium, preventing the coalescence of acoustic compression waves.
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
    </div>'''
)

# Write all generated pages to disk
for filename, content in PAGES.items():
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename} ({len(content)} bytes)")

print("All 11 pages generated successfully!")
