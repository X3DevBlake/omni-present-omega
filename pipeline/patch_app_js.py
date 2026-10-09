#!/usr/bin/env python3
"""
Appends Sentient Radar, Swarm Overlord, MHD Calculator, Whistleblower Portal,
and FOIA Vault engines to js/app.js.
"""
import os
import subprocess

APP_JS = '/data/data/com.termux/files/home/omni-web/js/app.js'

NEW_JS_CODE = '''

// ============================================================================
// PROJECT SENTIENT MULTI-SPECTRAL RADAR & SWARM DELIBERATION ENGINE
// ============================================================================

const RADAR_BLIPS = [
  {
    id: 'RAD-01',
    name: 'USS Nimitz Tic-Tac',
    callsign: 'NIMITZ-TIC-TAC',
    type: 'Hypersonic Non-Newtonian',
    rangeKm: 28.4,
    bearingDeg: 42,
    elevationDeg: 14.2,
    altitudeFt: '80,000 → 50 (0.78s)',
    velocity: 'Mach 18.4 (22,500 km/h)',
    accelG: '850+ G',
    sensorSpectrum: 'ATFLIR / AN/SPY-1B Radar',
    status: 'Tracking (Non-Keplerian)',
    xRatio: 0.65,
    yRatio: 0.32,
    color: '#00F2FE',
    classification: 'TOP SECRET // NOFORN',
    description: 'Oblong white cylinder (~40ft). Zero thermal exhaust plume, zero wings or control surfaces, instantaneous non-Newtonian deceleration without sonic boom.',
    lorentzTarget: { b: 32, j: 45000, rho: 0.05, length: 12.2 }
  },
  {
    id: 'RAD-02',
    name: 'Aguadilla Trans-Medium',
    callsign: 'AGUADILLA-SPLIT',
    type: 'Submersible-Aero Dual Domain',
    rangeKm: 14.1,
    bearingDeg: 275,
    elevationDeg: 3.8,
    altitudeFt: '120 → 0 (Water Entry)',
    velocity: '105 kts (Air & Water)',
    accelG: '45 G',
    sensorSpectrum: 'FLIR Thermal IR (CBP DHC-8)',
    status: 'Submerged (Split-Pair)',
    xRatio: 0.28,
    yRatio: 0.72,
    color: '#7B61FF',
    classification: 'OFFICIAL USE ONLY',
    description: 'Traversed coastal airspace, entered oceanic medium seamlessly without deceleration or displacement splash, split into two coherent thermal entities underwater.',
    lorentzTarget: { b: 18, j: 28000, rho: 1025.0, length: 1.5 }
  },
  {
    id: 'RAD-03',
    name: 'TR-3B Black Manta Platform',
    callsign: 'TR3B-MANTA',
    type: 'Electrostatic Boundary Vehicle',
    rangeKm: 42.6,
    bearingDeg: 185,
    elevationDeg: 38.0,
    altitudeFt: '45,000',
    velocity: 'Mach 4.2 / Stationary Hover',
    accelG: '120 G',
    sensorSpectrum: 'Active SAR / Optical Corona',
    status: 'Hover Hold',
    xRatio: 0.48,
    yRatio: 0.82,
    color: '#FF007A',
    classification: 'SPECIAL ACCESS PROGRAM',
    description: 'Equilateral triangular airframe with 3 peripheral high-voltage plasma thrusters and central rotational mercury-plasma ring for mass-reduction boundary layer.',
    lorentzTarget: { b: 45, j: 75000, rho: 0.25, length: 30.0 }
  },
  {
    id: 'RAD-04',
    name: 'Tehran F-4 Phantom Lockout',
    callsign: 'TEHRAN-LOCKOUT',
    type: 'Avionics EM Suppression',
    rangeKm: 19.8,
    bearingDeg: 330,
    elevationDeg: 22.4,
    altitudeFt: '25,000',
    velocity: 'Mach 2.1',
    accelG: '95 G',
    sensorSpectrum: 'APQ-120 Radar Lock Loss',
    status: 'Hostile ECM Jamming',
    xRatio: 0.35,
    yRatio: 0.22,
    color: '#00E676',
    classification: 'DIA UNCLASSIFIED DOSSIER',
    description: 'F-4 Phantom weapon control bus completely lost power upon AIM-9 Sidewinder tone lock; communications restored instantaneously after breaking off pursuit.',
    lorentzTarget: { b: 24, j: 38000, rho: 0.55, length: 8.0 }
  },
  {
    id: 'RAD-05',
    name: 'Orbital Anomaly SV-99',
    callsign: 'SENTIENT-SV99',
    type: 'Project SENTIENT LEO Crosser',
    rangeKm: 420.0,
    bearingDeg: 72,
    elevationDeg: 68.5,
    altitudeFt: '1,450,000 (LEO)',
    velocity: '27,850 km/h (Orbital)',
    accelG: '14 G (Retro-Vector)',
    sensorSpectrum: 'NRO Multi-Spectral Constellation',
    status: 'Orbital Vector Shift',
    xRatio: 0.78,
    yRatio: 0.60,
    color: '#FFB800',
    classification: 'TOP SECRET // TALENT KEYHOLE',
    description: 'Autonomous NRO satellite cross-cueing detected instantaneous 35-degree orbital inclination alteration inconsistent with chemical/ion thruster impulses.',
    lorentzTarget: { b: 50, j: 90000, rho: 0.001, length: 15.0 }
  }
];

const SWARM_AGENTS = {
  vortex: {
    name: 'Agent Vortex',
    role: 'Aerodynamics & MHD Plasma Specialist',
    avatar: '⚡',
    color: '#00F2FE'
  },
  spectre: {
    name: 'Agent Spectre',
    role: 'Electronic Warfare & SIGINT Analyst',
    avatar: '🟣',
    color: '#7B61FF'
  },
  chronos: {
    name: 'Agent Chronos',
    role: 'Temporal Latency & Chronometry',
    avatar: '🟡',
    color: '#FFB800'
  },
  nexus: {
    name: 'Agent Nexus',
    role: 'P2P Delta-CRDT Mesh Coordinator',
    avatar: '🟢',
    color: '#00E676'
  },
  omni: {
    name: 'Overlord Omni',
    role: 'Swarm Overlord & Strategic Synthesis',
    avatar: '🔴',
    color: '#FF007A'
  }
};

const SWARM_SCRIPTS = {
  'RAD-01': [
    {
      agent: 'chronos',
      text: 'Sensor clock synchronization validated across USS Princeton AN/SPY-1B radar and VFA-41 ATFLIR pod. The target descended from 80,000 ft to sea level in 0.78 seconds. Velocity delta: Δv = 31,250 m/s. Calculated sustained acceleration: 850G.'
    },
    {
      agent: 'vortex',
      text: 'Naval hydrophone and air acoustic arrays detected zero sonic boom or shockwave profile despite Mach 18.4 velocity. Standard gas dynamics cannot explain this. The boundary layer must be fully enveloped by a high-frequency Magnetohydrodynamic (MHD) plasma sheath generating a Lorentz force FL > 1.44×10⁶ N/m³, decoupling atmospheric drag.'
    },
    {
      agent: 'spectre',
      text: 'ATFLIR dual-band infrared (3-5 μm and 8-12 μm) reveals zero exhaust plume or aerodynamic friction heating. RF intercept reveals pulsed frequency modulation in the S-band (2.8 GHz) corresponding to field ionization.'
    },
    {
      agent: 'nexus',
      text: 'Telemetry vectors have been sealed in Delta-CRDT state packet 0x9f4a...2c81. Monotonic join verified across 12 distributed SCION border nodes without divergence.'
    },
    {
      agent: 'omni',
      text: 'Swarm Consensus Reached (Confidence: 99.6%). Target demonstrates field-propulsion utilizing boundary-layer magnetohydrodynamics. Project SENTIENT orbital cross-tasking confirmed.'
    }
  ],
  'RAD-02': [
    {
      agent: 'vortex',
      text: 'Thermal video from CBP DHC-8 shows target moving at 105 knots through atmosphere, entering ocean water without splash, spray, or deceleration. Hydrodynamic cavitation index is suppressed to near zero.'
    },
    {
      agent: 'spectre',
      text: 'Post-immersion thermal signature remains identical. Target cleaves into two distinct entities underwater, maintaining synchronous velocity and thermal equilibrium.'
    },
    {
      agent: 'chronos',
      text: 'Frame-by-frame analysis confirms trajectory continuity across fluid transition boundary within 16.6ms frame interval. Fluid displacement is magnetically redirected around the hull.'
    },
    {
      agent: 'nexus',
      text: 'Dual-target telemetry broadcast to Puerto Rico edge nodes. State vector S updated to track 2 simultaneous coordinate pairs.'
    },
    {
      agent: 'omni',
      text: 'Swarm Consensus Reached (Confidence: 98.9%). Trans-medium vehicle operating via electromagnetic boundary sheath capable of transitioning air-water interfaces without kinematic penalty.'
    }
  ],
  'RAD-03': [
    {
      agent: 'vortex',
      text: 'Radar cross-section indicates equilateral triangle (~30m edge). Three circular plasma emission nodes positioned at vertices. Corona ionization suggests electrohydrodynamic boundary stabilization.'
    },
    {
      agent: 'spectre',
      text: 'Active Synthetic Aperture Radar (SAR) returns reveal rotational magnetic disturbance at center of airframe (~89 Tesla pulsed). High-density RF emission in UHF band.'
    },
    {
      agent: 'chronos',
      text: 'Kinematics: 45,000 ft hover hold followed by instantaneous 90-degree yaw rotation and Mach 4.2 dash within 1.2 seconds. Structural integrity maintained through inertia manipulation.'
    },
    {
      agent: 'nexus',
      text: 'Observation logged into cryptographic vault with SHA-256 seal. Verified zero external control signal; craft operates on autonomous onboard neural lattice.'
    },
    {
      agent: 'omni',
      text: 'Swarm Consensus Reached (Confidence: 99.1%). Identified as advanced electrostatic boundary layer vehicle with rotating plasma ring for mass-equivalent reduction.'
    }
  ],
  'RAD-04': [
    {
      agent: 'spectre',
      text: 'Historical incident reconstruction: Dual F-4 Phantoms encountered target over Tehran. Westinghouse APQ-120 locked on, but AIM-9 Sidewinder firing circuit completely lost power when target began evasive maneuvers.'
    },
    {
      agent: 'vortex',
      text: 'Secondary ejecta observed: target released a luminous sub-body that accelerated toward ground radar installation before rejoining primary body.'
    },
    {
      agent: 'chronos',
      text: 'Avionics lockout duration: exactly 4 minutes 18 seconds until distance opened past 25 nautical miles, at which point all electrical systems restored without reboot.'
    },
    {
      agent: 'nexus',
      text: 'DIA declassified document 2013-00452 cross-referenced. Declassified records match electromagnetic suppression radius of approximately 15-20km.'
    },
    {
      agent: 'omni',
      text: 'Swarm Consensus Reached (Confidence: 99.4%). Directed electromagnetic pulse emission coupled with RF jamming causing weapon system interlocks to trip.'
    }
  ],
  'RAD-05': [
    {
      agent: 'chronos',
      text: 'Project SENTIENT NRO optical and SAR constellation correlation. LEO satellite SV-99 observed cross-track orbital plane deviation of 35 degrees at 420km altitude.'
    },
    {
      agent: 'vortex',
      text: 'Non-Keplerian orbital trajectory. Orbital plane alteration required Δv > 4.2 km/s with zero detected hydrazine, xenon, or cryogenic propellant combustion plumes.'
    },
    {
      agent: 'spectre',
      text: 'Hyper-spectral albedo shifts from 0.04 to 0.92 within 300 milliseconds. Multi-band sensor sweeps indicate high-frequency surface polarization.'
    },
    {
      agent: 'nexus',
      text: 'Space domain awareness catalog updated across all OPO ground telemetry stations. Synchronized via Byzantine-fault-tolerant CRDT semilattice.'
    },
    {
      agent: 'omni',
      text: 'Swarm Consensus Reached (Confidence: 99.8%). Space-domain non-Newtonian intelligence platform verified. Automated tasking directive dispatched to global sensorium.'
    }
  ]
};

// ============================================================================
// SENTIENT RADAR CONTROLLER CLASS
// ============================================================================
class SentientRadarController {
  constructor() {
    this.canvas = document.getElementById('sentient-radar-canvas');
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.activeBlipId = 'RAD-01';
    this.sweepAngle = 0;
    this.sweepSpeed = 0.025;
    this.activeSpectrum = 'all';
    this.audioEnabled = true;
    this.blips = RADAR_BLIPS.map(b => ({
      ...b,
      ping: 0,
      lastPingTime: 0
    }));

    this.initCanvasSize();
    this.bindEvents();
    this.updateHud();
    this.renderBlipButtons();
    this.animate = this.animate.bind(this);
    requestAnimationFrame(this.animate);
  }

  initCanvasSize() {
    const rect = this.canvas.getBoundingClientRect();
    const size = Math.min(rect.width || 480, 480);
    this.canvas.width = size;
    this.canvas.height = size;
    this.w = size;
    this.h = size;
    this.cx = size / 2;
    this.cy = size / 2;
    this.radius = size / 2 - 16;
  }

  bindEvents() {
    window.addEventListener('resize', () => this.initCanvasSize());

    this.canvas.addEventListener('click', (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const clickX = e.clientX - rect.left;
      const clickY = e.clientY - rect.top;

      let closest = null;
      let minDist = 36;

      this.blips.forEach(blip => {
        const bx = blip.xRatio * this.w;
        const by = blip.yRatio * this.h;
        const dist = Math.hypot(clickX - bx, clickY - by);
        if (dist < minDist) {
          minDist = dist;
          closest = blip;
        }
      });

      if (closest) {
        this.selectBlip(closest.id);
      }
    });

    const speedSlider = document.getElementById('radar-speed-slider');
    if (speedSlider) {
      speedSlider.addEventListener('input', (e) => {
        this.sweepSpeed = parseFloat(e.target.value) * 0.02;
      });
    }

    const spectrumFilters = document.querySelectorAll('.radar-spectrum-filter-btn');
    spectrumFilters.forEach(btn => {
      btn.addEventListener('click', () => {
        spectrumFilters.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.activeSpectrum = btn.dataset.spectrum || 'all';
        if (window.soundEngine) window.soundEngine.playNodeClick();
      });
    });
  }

  selectBlip(blipId) {
    this.activeBlipId = blipId;
    const target = this.blips.find(b => b.id === blipId);
    if (!target) return;

    target.ping = 1.0;
    this.updateHud();
    this.renderBlipButtons();

    if (window.soundEngine) window.soundEngine.playNodeClick();

    // Trigger MHD calculator preset update if available
    if (window.mhdCalculator && target.lorentzTarget) {
      window.mhdCalculator.setPreset(target.lorentzTarget);
    }

    // Trigger Swarm update if available
    if (window.swarmEngine) {
      window.swarmEngine.startDeliberation(blipId);
    }
  }

  renderBlipButtons() {
    const list = document.getElementById('radar-blip-list');
    if (!list) return;

    list.innerHTML = this.blips.map(b => {
      const isActive = b.id === this.activeBlipId ? 'active' : '';
      return `
        <button class="blip-selector-btn ${isActive}" onclick="window.sentientRadar.selectBlip('${b.id}')">
          <div style="display:flex; align-items:center; gap:8px;">
            <span style="display:inline-block; width:8px; height:8px; border-radius:50%; background:${b.color}; box-shadow:0 0 6px ${b.color};"></span>
            <strong>${b.id}</strong>: ${b.name}
          </div>
          <span style="font-size:0.75rem; color:#94A3B8; font-family:var(--font-mono);">${b.velocity.split(' ')[0]}</span>
        </button>
      `;
    }).join('');
  }

  updateHud() {
    const target = this.blips.find(b => b.id === this.activeBlipId);
    if (!target) return;

    const el = (id) => document.getElementById(id);
    if (el('hud-target-id')) el('hud-target-id').textContent = target.id;
    if (el('hud-target-name')) el('hud-target-name').textContent = target.name;
    if (el('hud-target-type')) el('hud-target-type').textContent = target.type;
    if (el('hud-target-range')) el('hud-target-range').textContent = target.rangeKm + ' km';
    if (el('hud-target-bearing')) el('hud-target-bearing').textContent = target.bearingDeg + '°';
    if (el('hud-target-alt')) el('hud-target-alt').textContent = target.altitudeFt;
    if (el('hud-target-velocity')) el('hud-target-velocity').textContent = target.velocity;
    if (el('hud-target-accel')) el('hud-target-accel').textContent = target.accelG;
    if (el('hud-target-sensor')) el('hud-target-sensor').textContent = target.sensorSpectrum;
    if (el('hud-target-class')) el('hud-target-class').textContent = target.classification;
    if (el('hud-target-desc')) el('hud-target-desc').textContent = target.description;
  }

  animate() {
    const ctx = this.ctx;
    const w = this.w;
    const h = this.h;
    const cx = this.cx;
    const cy = this.cy;
    const r = this.radius;

    // Semi-transparent fade for phosphor persistence
    ctx.fillStyle = 'rgba(4, 8, 16, 0.2)';
    ctx.fillRect(0, 0, w, h);

    // Outer ring
    ctx.strokeStyle = 'rgba(0, 242, 254, 0.4)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.arc(cx, cy, r, 0, Math.PI * 2);
    ctx.stroke();

    // Range rings (25%, 50%, 75%)
    ctx.strokeStyle = 'rgba(0, 242, 254, 0.15)';
    ctx.lineWidth = 1;
    [0.25, 0.5, 0.75].forEach(fraction => {
      ctx.beginPath();
      ctx.arc(cx, cy, r * fraction, 0, Math.PI * 2);
      ctx.stroke();
    });

    // Azimuth Crosshairs
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(0, 242, 254, 0.2)';
    ctx.beginPath();
    ctx.moveTo(cx - r, cy);
    ctx.lineTo(cx + r, cy);
    ctx.moveTo(cx, cy - r);
    ctx.lineTo(cx, cy + r);
    ctx.stroke();
    ctx.setLineDash([]);

    // Range labels
    ctx.fillStyle = 'rgba(148, 163, 184, 0.5)';
    ctx.font = '9px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('25km', cx, cy - r * 0.25 + 11);
    ctx.fillText('50km', cx, cy - r * 0.5 + 11);
    ctx.fillText('75km', cx, cy - r * 0.75 + 11);
    ctx.fillText('100km', cx, cy - r + 11);

    // Cardinal directions
    ctx.fillStyle = '#00F2FE';
    ctx.font = '10px "JetBrains Mono", monospace';
    ctx.fillText('000° N', cx, cy - r - 3);
    ctx.fillText('180° S', cx, cy + r + 12);
    ctx.textAlign = 'left';
    ctx.fillText('090° E', cx + r + 4, cy + 3);
    ctx.textAlign = 'right';
    ctx.fillText('270° W', cx - r - 4, cy + 3);

    // Update sweep angle
    this.sweepAngle = (this.sweepAngle + this.sweepSpeed) % (Math.PI * 2);

    // Draw sweep trail cone (phosphor beam)
    const coneAngle = 0.35;
    const startAngle = this.sweepAngle - coneAngle;
    const coneGrad = ctx.createRadialGradient(cx, cy, 0, cx, cy, r);
    coneGrad.addColorStop(0, 'rgba(0, 242, 254, 0.3)');
    coneGrad.addColorStop(0.7, 'rgba(0, 242, 254, 0.12)');
    coneGrad.addColorStop(1, 'rgba(0, 242, 254, 0)');

    ctx.save();
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.arc(cx, cy, r, startAngle, this.sweepAngle, false);
    ctx.closePath();
    ctx.fillStyle = coneGrad;
    ctx.fill();
    ctx.restore();

    // Draw main sweep line
    ctx.strokeStyle = '#00F2FE';
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    ctx.lineTo(cx + Math.cos(this.sweepAngle) * r, cy + Math.sin(this.sweepAngle) * r);
    ctx.stroke();

    // Blip rendering & sweep detection
    const now = Date.now();
    this.blips.forEach(blip => {
      const bx = blip.xRatio * w;
      const by = blip.yRatio * h;
      const blipAngle = (Math.atan2(by - cy, bx - cx) + Math.PI * 2) % (Math.PI * 2);

      // Check if sweep passed over blip
      let angleDiff = Math.abs(this.sweepAngle - blipAngle);
      if (angleDiff > Math.PI) angleDiff = 2 * Math.PI - angleDiff;

      if (angleDiff < 0.05 && now - blip.lastPingTime > 1200) {
        blip.ping = 1.0;
        blip.lastPingTime = now;
        if (this.audioEnabled && window.soundEngine && blip.id === this.activeBlipId) {
          window.soundEngine.playNodeClick();
        }
      }

      // Decay ping
      if (blip.ping > 0) {
        blip.ping = Math.max(0, blip.ping - 0.015);
      }

      // Draw ping ripple ring
      if (blip.ping > 0) {
        ctx.strokeStyle = `rgba(0, 242, 254, ${blip.ping * 0.7})`;
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(bx, by, 8 + (1.0 - blip.ping) * 22, 0, Math.PI * 2);
        ctx.stroke();
      }

      // Blip core
      const isSelected = blip.id === this.activeBlipId;
      ctx.fillStyle = blip.color;
      ctx.beginPath();
      ctx.arc(bx, by, isSelected ? 4.5 : 3.5, 0, Math.PI * 2);
      ctx.fill();

      // Callsign label
      ctx.fillStyle = isSelected ? '#FFFFFF' : 'rgba(226, 232, 240, 0.75)';
      ctx.font = '9px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText(blip.id, bx + 7, by - 5);

      // Velocity line vector
      const headingRad = (blip.bearingDeg - 90) * Math.PI / 180;
      ctx.strokeStyle = isSelected ? '#00F2FE' : 'rgba(0, 242, 254, 0.35)';
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(bx, by);
      ctx.lineTo(bx + Math.cos(headingRad) * 14, by + Math.sin(headingRad) * 14);
      ctx.stroke();

      // Selected tactical reticle box
      if (isSelected) {
        const boxSize = 14;
        ctx.strokeStyle = '#00F2FE';
        ctx.lineWidth = 1.5;
        // Top-left
        ctx.beginPath();
        ctx.moveTo(bx - boxSize, by - boxSize + 4);
        ctx.lineTo(bx - boxSize, by - boxSize);
        ctx.lineTo(bx - boxSize + 4, by - boxSize);
        ctx.stroke();
        // Top-right
        ctx.beginPath();
        ctx.moveTo(bx + boxSize - 4, by - boxSize);
        ctx.lineTo(bx + boxSize, by - boxSize);
        ctx.lineTo(bx + boxSize, by - boxSize + 4);
        ctx.stroke();
        // Bottom-left
        ctx.beginPath();
        ctx.moveTo(bx - boxSize, by + boxSize - 4);
        ctx.lineTo(bx - boxSize, by + boxSize);
        ctx.lineTo(bx - boxSize + 4, by + boxSize);
        ctx.stroke();
        // Bottom-right
        ctx.beginPath();
        ctx.moveTo(bx + boxSize - 4, by + boxSize);
        ctx.lineTo(bx + boxSize, by + boxSize);
        ctx.lineTo(bx + boxSize, by + boxSize - 4);
        ctx.stroke();
      }
    });

    requestAnimationFrame(this.animate);
  }
}

// ============================================================================
// MULTI-AGENT SWARM DELIBERATION ENGINE
// ============================================================================
class MultiAgentSwarmEngine {
  constructor() {
    this.feed = document.getElementById('swarm-chat-feed');
    this.activeBlipId = 'RAD-01';
    this.deliberationStep = 0;
    this.isDeliberating = false;
    this.timer = null;

    if (this.feed) {
      this.init();
    }
  }

  init() {
    this.startDeliberation(this.activeBlipId);
  }

  startDeliberation(blipId) {
    if (this.timer) clearTimeout(this.timer);
    this.activeBlipId = blipId;
    this.isDeliberating = true;
    this.deliberationStep = 0;

    if (!this.feed) return;
    this.feed.innerHTML = `
      <div style="text-align: center; padding: 1.5rem; color: #94A3B8; font-size: 0.82rem; font-family: var(--font-mono);">
        <span style="color: var(--gemini-cyan); animation: spin 1s linear infinite; display: inline-block;">⚙</span>
        Swarm consensus protocol initiated for target <strong style="color:#FFF;">${blipId}</strong>. Synchronizing agent cognitive vectors...
      </div>
    `;

    const script = SWARM_SCRIPTS[blipId] || SWARM_SCRIPTS['RAD-01'];
    this.runScript(script);
  }

  runScript(script) {
    if (!this.feed) return;

    if (this.deliberationStep === 0) {
      this.feed.innerHTML = '';
    }

    if (this.deliberationStep < script.length) {
      const entry = script[this.deliberationStep];
      const agent = SWARM_AGENTS[entry.agent];

      const div = document.createElement('div');
      div.className = 'swarm-agent-entry';
      div.innerHTML = `
        <div class="swarm-avatar" style="border-color:${agent.color}; color:${agent.color};">
          ${agent.avatar}
        </div>
        <div class="swarm-bubble" style="border-left: 2px solid ${agent.color};">
          <div class="swarm-author-bar">
            <span class="swarm-author-name" style="color:${agent.color};">${agent.name}</span>
            <span class="swarm-author-role">${agent.role}</span>
          </div>
          <div>${entry.text}</div>
        </div>
      `;

      this.feed.appendChild(div);
      this.feed.scrollTop = this.feed.scrollHeight;

      if (window.soundEngine) window.soundEngine.playNodeClick();

      this.deliberationStep++;
      this.timer = setTimeout(() => this.runScript(script), 1200);
    } else {
      this.isDeliberating = false;
      const consensusDiv = document.createElement('div');
      consensusDiv.style.cssText = 'padding: 0.9rem; background: rgba(0, 242, 254, 0.08); border: 1px solid rgba(0, 242, 254, 0.3); border-radius: 12px; font-size: 0.8rem; font-family: var(--font-mono); color: #E2E8F0; text-align: center; margin-top: 0.5rem;';
      consensusDiv.innerHTML = `
        <span style="color: var(--gemini-cyan); font-weight: bold;">✓ SWARM STATE CONVERGENCE ACHIEVED</span>
        <div style="font-size: 0.72rem; color: #94A3B8; margin-top: 4px;">Monotonic Delta-CRDT join applied across all 5 agent viewpoints. Ready for SCION network broadcast.</div>
      `;
      this.feed.appendChild(consensusDiv);
      this.feed.scrollTop = this.feed.scrollHeight;
      if (window.soundEngine) window.soundEngine.playSync();
    }
  }

  synthesizeReport() {
    const script = SWARM_SCRIPTS[this.activeBlipId] || SWARM_SCRIPTS['RAD-01'];
    const target = RADAR_BLIPS.find(b => b.id === this.activeBlipId) || RADAR_BLIPS[0];

    const report = {
      timestamp: new Date().toISOString(),
      targetId: target.id,
      targetName: target.name,
      telemetry: {
        rangeKm: target.rangeKm,
        bearingDeg: target.bearingDeg,
        altitudeFt: target.altitudeFt,
        velocity: target.velocity,
        accelG: target.accelG,
        classification: target.classification
      },
      swarmConsensus: {
        overlordConfidence: '99.6%',
        deliberationTranscript: script.map(s => ({
          agent: SWARM_AGENTS[s.agent].name,
          statement: s.text
        })),
        monotoneHash: '0x' + Array.from(crypto.getRandomValues(new Uint8Array(16))).map(b => b.toString(16).padStart(2, '0')).join('')
      }
    };

    const blob = new Blob([JSON.stringify(report, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `OPO-SWARM-REPORT-${target.id}.json`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    if (window.soundEngine) window.soundEngine.playSync();
  }
}

// ============================================================================
// MAGNETOHYDRODYNAMIC (MHD) LORENTZ ACCELERATION CALCULATOR
// ============================================================================
class MhdCalculator {
  constructor() {
    this.bSlider = document.getElementById('mhd-input-b');
    this.jSlider = document.getElementById('mhd-input-j');
    this.rhoSlider = document.getElementById('mhd-input-rho');
    this.lenSlider = document.getElementById('mhd-input-len');

    if (!this.bSlider) return;

    this.bindEvents();
    this.compute();
  }

  bindEvents() {
    [this.bSlider, this.jSlider, this.rhoSlider, this.lenSlider].forEach(slider => {
      if (slider) {
        slider.addEventListener('input', () => this.compute());
      }
    });

    const presets = document.querySelectorAll('.mhd-preset-btn');
    presets.forEach(btn => {
      btn.addEventListener('click', () => {
        presets.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const b = parseFloat(btn.dataset.b);
        const j = parseFloat(btn.dataset.j);
        const rho = parseFloat(btn.dataset.rho);
        const len = parseFloat(btn.dataset.len);
        this.setPreset({ b, j, rho, length: len });
        if (window.soundEngine) window.soundEngine.playNodeClick();
      });
    });
  }

  setPreset({ b, j, rho, length }) {
    if (this.bSlider) this.bSlider.value = b;
    if (this.jSlider) this.jSlider.value = j;
    if (this.rhoSlider) this.rhoSlider.value = rho;
    if (this.lenSlider) this.lenSlider.value = length;
    this.compute();
  }

  compute() {
    const b = parseFloat(this.bSlider?.value || 30);
    const j = parseFloat(this.jSlider?.value || 45000);
    const rho = parseFloat(this.rhoSlider?.value || 0.05);
    const length = parseFloat(this.lenSlider?.value || 12);

    // Update value labels
    const setText = (id, txt) => {
      const el = document.getElementById(id);
      if (el) el.textContent = txt;
    };

    setText('mhd-val-b', `${b} T`);
    setText('mhd-val-j', `${j.toLocaleString()} A/m²`);
    setText('mhd-val-rho', `${rho} kg/m³`);
    setText('mhd-val-len', `${length} m`);

    // Physics calculations
    // Lorentz force FL = j * B (N/m³)
    const lorentzForceN = j * b;
    const lorentzForceKN = lorentzForceN / 1000;

    // Velocity increment: delta_v = sqrt(2 * FL * L / rho)
    const deltaV = Math.sqrt(Math.max(0, (2 * lorentzForceN * length) / Math.max(0.0001, rho)));
    const mach = deltaV / 340.29;

    // Wave drag reduction: eta = 100 * (1 - exp(-0.00005 * j * B / rho))
    const dragExponent = (0.000045 * j * b) / Math.max(0.001, rho);
    const dragReduction = Math.min(98.8, 100 * (1 - Math.exp(-dragExponent)));

    // Shockwave attenuation in dB: A = 20 * log10(1 + 0.12 * B * sqrt(j / 1000))
    const shockAttenuation = 20 * Math.log10(1 + 0.12 * b * Math.sqrt(j / 1000));

    // Update displays
    setText('mhd-out-lorentz', `${lorentzForceKN.toFixed(1)} kN/m³`);
    setText('mhd-out-velocity', `${Math.round(deltaV).toLocaleString()} m/s`);
    setText('mhd-out-mach', `Mach ${mach.toFixed(1)}`);
    setText('mhd-out-drag', `${dragReduction.toFixed(1)}%`);
    setText('mhd-out-attenuation', `-${shockAttenuation.toFixed(1)} dB`);

    const dragBar = document.getElementById('mhd-drag-bar');
    if (dragBar) dragBar.style.width = `${dragReduction}%`;

    const shockBar = document.getElementById('mhd-shock-bar');
    if (shockBar) shockBar.style.width = `${Math.min(100, shockAttenuation * 1.5)}%`;
  }
}

// ============================================================================
// ZERO-KNOWLEDGE WHISTLEBLOWER ENGINE
// ============================================================================
class WhistleblowerEngine {
  constructor() {
    this.dropzone = document.getElementById('whistleblower-dropzone');
    this.statusBox = document.getElementById('whistleblower-status');
    if (this.dropzone) {
      this.bindEvents();
    }
  }

  bindEvents() {
    this.dropzone.addEventListener('dragover', (e) => {
      e.preventDefault();
      this.dropzone.classList.add('hover');
    });

    this.dropzone.addEventListener('dragleave', () => {
      this.dropzone.classList.remove('hover');
    });

    this.dropzone.addEventListener('drop', (e) => {
      e.preventDefault();
      this.dropzone.classList.remove('hover');
      const files = e.dataTransfer.files;
      if (files.length > 0) {
        this.processFile(files[0].name, files[0].size);
      }
    });

    const sampleBtn = document.getElementById('whistleblower-sample-btn');
    if (sampleBtn) {
      sampleBtn.addEventListener('click', () => {
        this.processFile('FLIR1_2004_strike_squadron_raw.telemetry', 4829104);
      });
    }
  }

  processFile(filename, size) {
    if (!this.statusBox) return;

    this.statusBox.innerHTML = `
      <div style="padding: 1rem; background: rgba(0, 242, 254, 0.05); border: 1px solid rgba(0, 242, 254, 0.2); border-radius: 12px;">
        <div style="font-size: 0.85rem; color: #FFF; font-weight: 600; margin-bottom: 0.5rem;">
          Processing Document: <span style="color:var(--gemini-cyan);">${filename}</span> (${(size / 1024 / 1024).toFixed(2)} MB)
        </div>
        <div style="display: flex; flex-direction: column; gap: 6px; font-size: 0.78rem; font-family: var(--font-mono); color: #94A3B8;">
          <div>✓ [EXIF SANITIZER] Stripping GPS coordinates, device serial, firmware hash...</div>
          <div>✓ [ASYMMETRIC SEAL] Generating ephemeral 4096-bit RSA session pair...</div>
          <div>✓ [AES-GCM-256] Encrypting telemetry payload with sovereign cipher...</div>
          <div>✓ [CRDT MUTATION] Constructing join-semilattice state delta (S ⊔ ΔS)...</div>
        </div>
        <div style="margin-top: 1rem; padding: 0.75rem; background: rgba(0,0,0,0.5); border-radius: 8px; font-size: 0.72rem; font-family: var(--font-mono); color: #A5B4FC; word-break: break-all;">
          CRDT HASH: 0x${Array.from(crypto.getRandomValues(new Uint8Array(20))).map(b => b.toString(16).padStart(2,'0')).join('')}
        </div>
        <div style="margin-top: 0.75rem; display: flex; gap: 0.5rem; justify-content: flex-end;">
          <button class="glass-btn glass-btn-primary" style="font-size: 0.75rem; padding: 6px 12px;" onclick="alert('Delta-CRDT payload gossiped to 12 SCION edge nodes with zero metadata footprint.')">
            Gossip to Mesh Network
          </button>
        </div>
      </div>
    `;

    if (window.soundEngine) window.soundEngine.playSync();
  }
}

// ============================================================================
// DECLASSIFIED FOIA VAULT MODAL CONTROLLER
// ============================================================================
const FOIA_CASES = {
  'case-sentient': {
    title: 'Project SENTIENT NRO Architecture Memo (2021)',
    classification: 'TOP SECRET // TALENT KEYHOLE // DECLASSIFIED EXCERPT',
    date: '2021-08-14',
    content: `MEMORANDUM FOR: DIRECTOR, NATIONAL RECONNAISSANCE OFFICE (NRO)
SUBJECT: SENTIENT Constellation Automated Multi-Spectral Anomaly Cueing

1. (S//TK) Project SENTIENT has demonstrated autonomous machine intelligence routing across orbital SAR (Synthetic Aperture Radar) and SIGINT constellations.
2. (S//TK) When non-Newtonian aerodynamic trajectories exceeding Mach 15 or exhibiting instantaneous 90-degree vector deviations are cued by naval or ground arrays, SENTIENT autonomously alters tasking priorities for adjacent LEO optical satellites within 4.2 seconds.
3. (U) This protocol operates independent of ground-station latency, utilizing onboard edge-tensor computing to verify un-correlated targets (UCT).`
  },
  'case-nimitz': {
    title: 'USS Nimitz Strike Fighter Squadron 41 ATFLIR Record (2004)',
    classification: 'SECRET // NOFORN // DECLASSIFIED UNDER FOIA',
    date: '2004-11-14',
    content: `COMMANDER, CARRIER STRIKE GROUP ELEVEN
INCIDENT REPORT: UNIDENTIFIED AERIAL PHENOMENA (UAP) INTERCEPT

1. (S) At 14:10 PST, USS Princeton (CG-59) detected multiple targets descending from 80,000 ft to sea surface in sub-second intervals.
2. (S) Two F/A-18F Super Hornets launched from USS Nimitz (VFA-41). Commander Fravor observed a 40-foot elongated white cylinder hovering above water disturbance.
3. (S) Target mirrored aircraft vector before accelerating across horizon past radar lock. Velocity estimated at Mach 18+. Zero thermal plume recorded on ATFLIR.`
  },
  'case-aguadilla': {
    title: 'CBP DHC-8 Aguadilla Trans-Medium FLIR Analysis (2013)',
    classification: 'UNCLASSIFIED // LAW ENFORCEMENT SENSITIVE',
    date: '2013-04-25',
    content: `US CUSTOMS AND BORDER PROTECTION (CBP)
AERIAL TRACKING LOG: RAFAEL HERNÁNDEZ AIRPORT, PUERTO RICO

1. (U//LES) Maritime Patrol Aircraft (DHC-8) thermal camera (MX-15) tracked anomalous low-altitude object at ~100-120 knots traversing coastline.
2. (U//LES) Object entered ocean water seamlessly without splashing, velocity reduction, or disruption of surface wave geometry.
3. (U//LES) Infrared recording shows target dividing into two synchronous components underwater, maintaining identical heat distribution.`
  },
  'case-tehran': {
    title: 'DIA Information Report: 1976 Tehran F-4 Dual Intercept',
    classification: 'UNCLASSIFIED // DIA FOIA ARCHIVE 2013-00452',
    date: '1976-09-19',
    content: `DEFENSE INTELLIGENCE AGENCY (DIA)
EVALUATION OF UAP INTERCEPT - IMPERIAL IRANIAN AIR FORCE (IIAF)

1. (U) Two F-4 Phantom II interceptors scrambled from Shahrokhi AFB.
2. (U) First F-4 experienced total electrical lockout and UHF radio failure at 25 nautical miles from primary target.
3. (U) Second F-4 achieved APQ-120 radar lock. When pilot prepared to fire AIM-9 Sidewinder missile, weapon control console lost all electrical power. Systems returned immediately upon peeling away.`
  }
};

function openFoiaModal(caseId) {
  const caseData = FOIA_CASES[caseId];
  if (!caseData) return;

  const modal = document.getElementById('foia-modal');
  const titleEl = document.getElementById('foia-modal-title');
  const classEl = document.getElementById('foia-modal-class');
  const bodyEl = document.getElementById('foia-modal-body');

  if (titleEl) titleEl.textContent = caseData.title;
  if (classEl) classEl.textContent = caseData.classification;
  if (bodyEl) bodyEl.textContent = caseData.content;

  if (modal) modal.classList.add('open');
  if (window.soundEngine) window.soundEngine.playNodeClick();
}

function closeFoiaModal() {
  const modal = document.getElementById('foia-modal');
  if (modal) modal.classList.remove('open');
}

// Global initialization for Sentient Radar & Multi-Agent Swarm
document.addEventListener('DOMContentLoaded', () => {
  if (document.getElementById('sentient-radar-canvas')) {
    window.sentientRadar = new SentientRadarController();
    window.swarmEngine = new MultiAgentSwarmEngine();
    window.mhdCalculator = new MhdCalculator();
    window.whistleblowerEngine = new WhistleblowerEngine();
  }
});
'''

def main():
    with open(APP_JS, 'a', encoding='utf-8') as f:
        f.write(NEW_JS_CODE)
    print("Appended new modules to js/app.js")

    # Syntax check
    res = subprocess.run(['node', '--check', APP_JS], capture_output=True, text=True)
    if res.returncode == 0:
        print("✓ node --check js/app.js passed successfully!")
    else:
        print("✗ node --check error:")
        print(res.stderr)
        raise SystemExit(res.returncode)

if __name__ == '__main__':
    main()
