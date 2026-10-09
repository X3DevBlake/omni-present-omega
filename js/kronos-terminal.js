/**
 * Omni-Present Omega (OPO) × OmniKronos Autonomous Swarm Mission Terminal
 * Interactive agentic dispatch engine simulating real-time multi-agent triage,
 * SCION path optimization, and automated Project SENTIENT satellite retasking.
 */

class AutonomousSwarmTerminal {
  constructor() {
    this.terminalEl = null;
    this.isRunning = false;
    this.streamTimer = null;
    this.lineIndex = 0;
    this.currentMode = 'idle';

    this.subagents = [
      { name: 'Kronos-Triage-01', color: '#00F2FE', role: 'Realtime AST & Telemetry Ingestion' },
      { name: 'Sentinel-Alpha', color: '#A5B4FC', role: 'Multi-Spectral RF & Hypersonic Kinematics' },
      { name: 'SCION-Pathfinder', color: '#34D399', role: 'Path-Aware Egress & Jitter Minimization' },
      { name: 'Invariant-Mitigator', color: '#FCD34D', role: 'Monotonic Join-Semilattice CRDT Seal' },
      { name: 'Omni-Overlord', color: '#F472B6', role: 'Executive Consensus & Cross-Tasking' }
    ];

    this.scenarios = {
      dispatch: [
        { agent: 'Kronos-Triage-01', msg: 'Ingesting 60 FPS multi-spectral non-Newtonian radar track (Blip ID: TRK-9904)...' },
        { agent: 'Sentinel-Alpha', msg: 'Velocity vector: Mach 22.4 at FL800. Angle of attack discontinuity = 88.4° with 0.0g lateral strain.' },
        { agent: 'SCION-Pathfinder', msg: 'Initiating cryptographically isolated multi-path route across AS-42 (Zurich) & AS-101 (Tokyo).' },
        { agent: 'Invariant-Mitigator', msg: 'Generating join-semilattice causal delta: (dot: node-alpha:8920, state_hash: 0x8a9f...33c1).' },
        { agent: 'Omni-Overlord', msg: 'Swarm consensus achieved (5/5). Cross-cueing NRO Project SENTIENT orbital satellites KH-11 & USA-245.' },
        { agent: 'Kronos-Triage-01', msg: 'Telemetric mission confirmed. Monotonic state vector merged to global mesh ledger.' }
      ],
      triage: [
        { agent: 'Sentinel-Alpha', msg: 'Threat triage initiated: RF spoofing check and EW electromagnetic signature scan active.' },
        { agent: 'SCION-Pathfinder', msg: 'Detected anomalous BGP hop field on peering gateway. Severing corrupted AS link (Cost: 0.12ms).' },
        { agent: 'Invariant-Mitigator', msg: 'Executing anti-entropy conflict resolution: monotonic join S ⊔ S\' preserves causal dot invariants.' },
        { agent: 'Kronos-Triage-01', msg: 'Patch verified against AST invariants: 0 vulnerabilities, 0 state regressions.' },
        { agent: 'Omni-Overlord', msg: 'Defense triage completed: Mesh cluster hardened. Autonomous failover routes active.' }
      ],
      scan: [
        { agent: 'Kronos-Triage-01', msg: 'Triggering spatial anomaly scan across all 7,420+ global live transponders...' },
        { agent: 'Sentinel-Alpha', msg: 'Correlating ADS-B flight FL-380 transponders with maritime AIS carrier groups in Pacific Basin.' },
        { agent: 'SCION-Pathfinder', msg: 'Edge sensor round-trip latency measured at 0.38 ms over SCION crypto-hops.' },
        { agent: 'Invariant-Mitigator', msg: 'State vector timestamp synchronized to within 1.2 nanoseconds via atomic GPS clocks.' },
        { agent: 'Omni-Overlord', msg: 'Planetary scan complete: 0 unhandled state collisions detected. Spatial lattice nominal.' }
      ],
      patch: [
        { agent: 'Kronos-Triage-01', msg: 'Synthesizing sovereign firmware patch for Rust opo-stated micro-daemon...' },
        { agent: 'Invariant-Mitigator', msg: 'Compiling causal lattice delta compression routine with zero heap allocations.' },
        { agent: 'Sentinel-Alpha', msg: 'Applying SHA-3 / ED25519 signature: 0x7b2f0a1c...99de' },
        { agent: 'SCION-Pathfinder', msg: 'Broadcasting patch across 4 continental cluster hubs via gossip protocol (UDP 9001).' },
        { agent: 'Omni-Overlord', msg: 'Patch deployed successfully: All nodes reporting 100% causal synchronization.' }
      ]
    };

    this.init();
  }

  init() {
    if (typeof window === 'undefined') return;
    this.terminalEl = document.getElementById('kronos-swarm-stream');
    if (this.terminalEl && this.terminalEl.children.length === 0) {
      this.log('Kronos-Triage-01', 'OmniKronos Swarm Dispatch Engine initialized. Connected to Gemini 4.0 Argon agentic core.', '#00F2FE');
      this.log('Omni-Overlord', 'Standby. Select a mission command to dispatch autonomous subagents.', '#F472B6');
    }
  }

  log(agentName, text, color = '#34D399') {
    if (!this.terminalEl) this.terminalEl = document.getElementById('kronos-swarm-stream');
    if (!this.terminalEl) return;

    const timeStr = new Date().toISOString().split('T')[1].replace('Z', '');
    const line = document.createElement('div');
    line.style.cssText = `
      margin-bottom: 6px;
      line-height: 1.5;
      font-family: var(--font-mono);
      font-size: 0.78rem;
      color: #CBD5E1;
      display: flex;
      gap: 8px;
      animation: fadeIn 0.2s ease;
    `;

    line.innerHTML = `
      <span style="color: #64748B;">[${timeStr}]</span>
      <span style="color: ${color}; font-weight: 600;">[${agentName}]</span>
      <span>${text}</span>
    `;

    this.terminalEl.appendChild(line);
    this.terminalEl.scrollTop = this.terminalEl.scrollHeight;

    if (window.soundEngine) window.soundEngine.playNodeClick();
  }

  dispatchScenario(scenarioKey) {
    if (this.isRunning) {
      clearInterval(this.streamTimer);
    }
    this.isRunning = true;
    this.currentMode = scenarioKey;
    const steps = this.scenarios[scenarioKey] || this.scenarios.dispatch;
    let stepIndex = 0;

    if (window.soundEngine) window.soundEngine.playClick();
    this.log('Omni-Overlord', `>>> INITIATING MISSION DIRECTIVE: ${scenarioKey.toUpperCase()} <<<`, '#F59E0B');

    this.streamTimer = setInterval(() => {
      if (stepIndex < steps.length) {
        const item = steps[stepIndex];
        const agentObj = this.subagents.find(a => a.name === item.agent) || { color: '#00F2FE' };
        this.log(item.agent, item.msg, agentObj.color);
        stepIndex++;
      } else {
        clearInterval(this.streamTimer);
        this.isRunning = false;
        if (window.soundEngine) window.soundEngine.playSync();
        this.log('Omni-Overlord', `✓ Mission Directive [${scenarioKey.toUpperCase()}] Complete. Swarm entering surveillance mode.`, '#34D399');
      }
    }, 750);
  }

  clearTerminal() {
    if (this.terminalEl) {
      this.terminalEl.innerHTML = '';
      this.log('Kronos-Triage-01', 'Terminal logs cleared. Swarm console reset.', '#94A3B8');
    }
    if (window.soundEngine) window.soundEngine.playClick();
  }

  pauseStream() {
    if (this.isRunning) {
      clearInterval(this.streamTimer);
      this.isRunning = false;
      this.log('Omni-Overlord', 'Mission stream paused by user operator.', '#F59E0B');
    }
    if (window.soundEngine) window.soundEngine.playClick();
  }
}

// Global initialization
if (typeof window !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('kronos-swarm-stream')) {
      window.kronosSwarm = new AutonomousSwarmTerminal();
    }
  });
}
