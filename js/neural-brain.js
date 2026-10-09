/**
 * Omni-Present Omega // Neural Brain Connectome Engine
 * 3D Animated AI Neurons in Space with Synaptic Transmission & Action Potentials
 * 60 FPS Canvas with Multi-Axis Spatial Parallax and Interactive Cognitive Focus
 */
(function() {
  'use strict';

  class NeuralBrainConnectome {
    constructor(canvasId) {
      this.canvas = document.getElementById(canvasId);
      if (!this.canvas) return;

      this.ctx = this.canvas.getContext('2d', { alpha: true });
      if (!this.ctx) return;

      this.width = 0;
      this.height = 0;
      this.dpr = Math.min(window.devicePixelRatio || 1, 2);

      // 3D Perspective Parameters
      this.fov = 420;
      this.rotX = 0;
      this.rotY = 0;
      this.rotSpeedX = 0.0003;
      this.rotSpeedY = 0.0007;

      // Interaction
      this.pointer = {
        x: -9999,
        y: -9999,
        active: false,
        radius: 180
      };

      // Configuration
      this.isMobile = window.innerWidth <= 768;
      this.nodeCount = this.isMobile ? 48 : 82;
      this.maxConnectDistance = this.isMobile ? 120 : 155;
      this.dustCount = this.isMobile ? 35 : 65;

      // Entities
      this.neurons = [];
      this.synapses = [];
      this.pulses = [];
      this.dust = [];

      // Animation State
      this.isRunning = false;
      this.lastTime = performance.now();
      this.pulseSpawnTimer = 0;

      // Palette
      this.colors = [
        { r: 0, g: 242, b: 254 },   // Cyan
        { r: 56, g: 189, b: 248 },  // Sky
        { r: 139, g: 92, b: 246 },  // Purple
        { r: 167, g: 139, b: 250 }, // Violet
        { r: 16, g: 185, b: 129 },  // Emerald
        { r: 245, g: 158, b: 11 }   // Amber
      ];

      this.init();
    }

    init() {
      this.resize();
      window.addEventListener('resize', () => this.resize(), { passive: true });

      // Pointer tracking
      window.addEventListener('mousemove', (e) => {
        this.pointer.x = e.clientX;
        this.pointer.y = e.clientY;
        this.pointer.active = true;
      }, { passive: true });

      window.addEventListener('mouseleave', () => {
        this.pointer.active = false;
      }, { passive: true });

      // Touch tracking
      window.addEventListener('touchmove', (e) => {
        if (e.touches && e.touches[0]) {
          this.pointer.x = e.touches[0].clientX;
          this.pointer.y = e.touches[0].clientY;
          this.pointer.active = true;
        }
      }, { passive: true });

      window.addEventListener('touchend', () => {
        this.pointer.active = false;
      }, { passive: true });

      // Cognitive Burst on Click / Tap
      window.addEventListener('click', (e) => {
        this.triggerBurst(e.clientX, e.clientY);
      });

      // Tab visibility pause to preserve battery
      document.addEventListener('visibilitychange', () => {
        if (document.hidden) {
          this.isRunning = false;
        } else {
          this.isRunning = true;
          this.lastTime = performance.now();
          this.loop();
        }
      });

      this.spawnEntities();
      this.isRunning = true;
      this.loop();
    }

    resize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      this.canvas.width = this.width * this.dpr;
      this.canvas.height = this.height * this.dpr;
      this.ctx.scale(this.dpr, this.dpr);
      this.isMobile = this.width <= 768;
    }

    spawnEntities() {
      this.neurons = [];
      const spreadX = this.width * 0.9;
      const spreadY = this.height * 0.9;
      const spreadZ = 500;

      for (let i = 0; i < this.nodeCount; i++) {
        const color = this.colors[Math.floor(Math.random() * this.colors.length)];
        this.neurons.push({
          // 3D Space Coordinates
          x: (Math.random() - 0.5) * spreadX,
          y: (Math.random() - 0.5) * spreadY,
          z: (Math.random() - 0.5) * spreadZ,
          // Autonomous Brownian Drift
          vx: (Math.random() - 0.5) * 0.35,
          vy: (Math.random() - 0.5) * 0.35,
          vz: (Math.random() - 0.5) * 0.35,
          // Projected Coordinates
          projX: 0,
          projY: 0,
          scale: 1,
          depthAlpha: 1,
          // Soma Anatomy
          baseRadius: 1.8 + Math.random() * 2.2,
          color: color,
          excitation: 0, // Membrane voltage pulse
          spines: Math.floor(3 + Math.random() * 4), // Micro-dendrites
          pulseTimer: Math.random() * 100
        });
      }

      // Background Starfield / Neurotransmitter Dust
      this.dust = [];
      for (let i = 0; i < this.dustCount; i++) {
        this.dust.push({
          x: (Math.random() - 0.5) * this.width * 1.5,
          y: (Math.random() - 0.5) * this.height * 1.5,
          z: (Math.random() - 0.5) * 800,
          vz: -0.15 - Math.random() * 0.3,
          radius: 0.6 + Math.random() * 1.2,
          alpha: 0.2 + Math.random() * 0.5
        });
      }
    }

    triggerBurst(screenX, screenY) {
      if (!screenX || !screenY) return;
      // Find closest neuron to burst origin
      let closestNeuron = null;
      let minDistance = 99999;

      for (let i = 0; i < this.neurons.length; i++) {
        const n = this.neurons[i];
        const dist = Math.hypot(n.projX - screenX, n.projY - screenY);
        if (dist < minDistance) {
          minDistance = dist;
          closestNeuron = n;
        }
      }

      if (closestNeuron && minDistance < 300) {
        closestNeuron.excitation = 1.0;
        // Fire action potentials to all connected neighbors
        for (let i = 0; i < this.synapses.length; i++) {
          const s = this.synapses[i];
          if (s.from === closestNeuron) {
            this.spawnPulse(s.from, s.to);
          } else if (s.to === closestNeuron) {
            this.spawnPulse(s.to, s.from);
          }
        }
      }
    }

    spawnPulse(fromNeuron, toNeuron) {
      if (this.pulses.length > 50) return; // Cap for 60fps
      this.pulses.push({
        from: fromNeuron,
        to: toNeuron,
        progress: 0,
        speed: 0.02 + Math.random() * 0.025,
        color: fromNeuron.color
      });
    }

    update(dt) {
      this.rotX += this.rotSpeedX * dt * 60;
      this.rotY += this.rotSpeedY * dt * 60;

      const cosX = Math.cos(this.rotX);
      const sinX = Math.sin(this.rotX);
      const cosY = Math.cos(this.rotY);
      const sinY = Math.sin(this.rotY);

      const halfW = this.width / 2;
      const halfH = this.height / 2;
      const boundsX = halfW * 1.1;
      const boundsY = halfH * 1.1;
      const boundsZ = 280;

      // Update Neurons
      for (let i = 0; i < this.neurons.length; i++) {
        const n = this.neurons[i];

        // Brownian Drift
        n.x += n.vx * dt * 60;
        n.y += n.vy * dt * 60;
        n.z += n.vz * dt * 60;

        // Soft Boundary Torus Cycling
        if (n.x < -boundsX) n.x = boundsX;
        if (n.x > boundsX) n.x = -boundsX;
        if (n.y < -boundsY) n.y = boundsY;
        if (n.y > boundsY) n.y = -boundsY;
        if (n.z < -boundsZ) n.z = boundsZ;
        if (n.z > boundsZ) n.z = -boundsZ;

        // 3D Celestial Orbit Rotation
        // Rotate around Y axis
        const x1 = n.x * cosY + n.z * sinY;
        const z1 = -n.x * sinY + n.z * cosY;
        // Rotate around X axis
        const y2 = n.y * cosX - z1 * sinX;
        const z2 = n.y * sinX + z1 * cosX;

        // Perspective Projection
        const f = this.fov;
        const distanceZ = f + z2;
        if (distanceZ > 20) {
          n.scale = f / distanceZ;
          n.projX = halfW + x1 * n.scale;
          n.projY = halfH + y2 * n.scale;
          n.depthAlpha = Math.max(0.12, Math.min(1.0, (z2 + 300) / 550));
        } else {
          n.scale = 0;
          n.depthAlpha = 0;
        }

        // Pointer Cognitive Magnetism
        if (this.pointer.active && n.scale > 0) {
          const dx = this.pointer.x - n.projX;
          const dy = this.pointer.y - n.projY;
          const dist = Math.hypot(dx, dy);
          if (dist < this.pointer.radius && dist > 1) {
            const force = (1 - dist / this.pointer.radius) * 0.12;
            n.x += (dx / dist) * force * 15;
            n.y += (dy / dist) * force * 15;
            n.excitation = Math.min(1.0, n.excitation + 0.04);
          }
        }

        // Decay excitation
        if (n.excitation > 0.01) {
          n.excitation *= 0.93;
        } else {
          n.excitation = 0;
        }

        // Spontaneous Synaptic Burst Timer
        n.pulseTimer += dt * 60;
        if (n.pulseTimer > 280) {
          n.pulseTimer = 0;
          n.excitation = 0.8;
          // Spawn spontaneous pulse to a random neighbor
          if (this.synapses.length > 0) {
            const mySynapses = this.synapses.filter(s => s.from === n || s.to === n);
            if (mySynapses.length > 0) {
              const syn = mySynapses[Math.floor(Math.random() * mySynapses.length)];
              this.spawnPulse(n, syn.from === n ? syn.to : syn.from);
            }
          }
        }
      }

      // Rebuild Synaptic Connectome Pairs
      this.synapses = [];
      const maxDist = this.maxConnectDistance;

      for (let i = 0; i < this.neurons.length; i++) {
        const na = this.neurons[i];
        if (na.scale <= 0) continue;

        for (let j = i + 1; j < this.neurons.length; j++) {
          const nb = this.neurons[j];
          if (nb.scale <= 0) continue;

          const dx = na.projX - nb.projX;
          const dy = na.projY - nb.projY;
          const dist = Math.hypot(dx, dy);

          if (dist < maxDist) {
            const proximityAlpha = (1 - dist / maxDist);
            const combinedDepth = (na.depthAlpha + nb.depthAlpha) * 0.5;
            this.synapses.push({
              from: na,
              to: nb,
              dist: dist,
              alpha: proximityAlpha * combinedDepth * 0.65
            });
          }
        }
      }

      // Update Action Potential Pulses
      for (let i = this.pulses.length - 1; i >= 0; i--) {
        const p = this.pulses[i];
        p.progress += p.speed * dt * 60;

        if (p.progress >= 1.0) {
          // Reached destination neuron: stimulate and maybe cascade
          p.to.excitation = 1.0;
          if (Math.random() < 0.35) {
            // Cascade to another neighbor
            const nextSynapses = this.synapses.filter(s => (s.from === p.to || s.to === p.to) && (s.from !== p.from && s.to !== p.from));
            if (nextSynapses.length > 0) {
              const next = nextSynapses[Math.floor(Math.random() * nextSynapses.length)];
              this.spawnPulse(p.to, next.from === p.to ? next.to : next.from);
            }
          }
          this.pulses.splice(i, 1);
        }
      }

      // Update Cosmic Dust
      for (let i = 0; i < this.dust.length; i++) {
        const d = this.dust[i];
        d.z += d.vz * dt * 60;
        if (d.z < -400) d.z = 400;

        const f = this.fov;
        const scale = f / (f + d.z);
        d.projX = halfW + d.x * scale;
        d.projY = halfH + d.y * scale;
        d.scale = scale;
      }
    }

    render() {
      const ctx = this.ctx;
      ctx.clearRect(0, 0, this.width, this.height);

      // 1. Draw Deep Space Cosmic Dust Particles
      for (let i = 0; i < this.dust.length; i++) {
        const d = this.dust[i];
        if (d.projX < 0 || d.projX > this.width || d.projY < 0 || d.projY > this.height) continue;
        ctx.beginPath();
        ctx.arc(d.projX, d.projY, Math.max(0.5, d.radius * d.scale), 0, Math.PI * 2);
        ctx.fillStyle = `rgba(148, 163, 184, ${d.alpha * d.scale * 0.4})`;
        ctx.fill();
      }

      // 2. Draw Synaptic Axon Filaments (Connections)
      for (let i = 0; i < this.synapses.length; i++) {
        const s = this.synapses[i];
        const na = s.from;
        const nb = s.to;

        // Dynamic Line Gradient between two neuron soma colors
        const grad = ctx.createLinearGradient(na.projX, na.projY, nb.projX, nb.projY);
        grad.addColorStop(0, `rgba(${na.color.r}, ${na.color.g}, ${na.color.b}, ${s.alpha})`);
        grad.addColorStop(1, `rgba(${nb.color.r}, ${nb.color.g}, ${nb.color.b}, ${s.alpha})`);

        ctx.beginPath();
        ctx.moveTo(na.projX, na.projY);
        ctx.lineTo(nb.projX, nb.projY);
        ctx.strokeStyle = grad;
        ctx.lineWidth = Math.max(0.6, (na.scale + nb.scale) * 0.7);
        ctx.stroke();
      }

      // 3. Draw Traveling Action Potentials (Electrical Spikes)
      for (let i = 0; i < this.pulses.length; i++) {
        const p = this.pulses[i];
        const x1 = p.from.projX;
        const y1 = p.from.projY;
        const x2 = p.to.projX;
        const y2 = p.to.projY;

        const curX = x1 + (x2 - x1) * p.progress;
        const curY = y1 + (y2 - y1) * p.progress;
        const tailX = x1 + (x2 - x1) * Math.max(0, p.progress - 0.14);
        const tailY = y1 + (y2 - y1) * Math.max(0, p.progress - 0.14);

        // Luminous glowing tail
        const pulseGrad = ctx.createLinearGradient(tailX, tailY, curX, curY);
        pulseGrad.addColorStop(0, `rgba(${p.color.r}, ${p.color.g}, ${p.color.b}, 0)`);
        pulseGrad.addColorStop(1, `rgba(255, 255, 255, 0.95)`);

        ctx.beginPath();
        ctx.moveTo(tailX, tailY);
        ctx.lineTo(curX, curY);
        ctx.strokeStyle = pulseGrad;
        ctx.lineWidth = 2.2 * p.from.scale;
        ctx.stroke();

        // High-energy white-hot spike head
        ctx.beginPath();
        ctx.arc(curX, curY, 2.2 * p.from.scale, 0, Math.PI * 2);
        ctx.fillStyle = '#FFFFFF';
        ctx.shadowColor = `rgb(${p.color.r}, ${p.color.g}, ${p.color.b})`;
        ctx.shadowBlur = 10;
        ctx.fill();
        ctx.shadowBlur = 0; // reset
      }

      // 4. Draw Neuron Soma Bodies (Nodes)
      for (let i = 0; i < this.neurons.length; i++) {
        const n = this.neurons[i];
        if (n.scale <= 0) continue;

        const radius = n.baseRadius * n.scale * (1 + n.excitation * 0.9);
        const c = n.color;
        const alpha = n.depthAlpha;

        // Outer Membrane Aura Glow
        const glowRadius = radius * (3.0 + n.excitation * 3.5);
        const auraGrad = ctx.createRadialGradient(n.projX, n.projY, radius * 0.3, n.projX, n.projY, glowRadius);
        auraGrad.addColorStop(0, `rgba(${c.r}, ${c.g}, ${c.b}, ${(0.4 + n.excitation * 0.5) * alpha})`);
        auraGrad.addColorStop(1, `rgba(${c.r}, ${c.g}, ${c.b}, 0)`);

        ctx.beginPath();
        ctx.arc(n.projX, n.projY, glowRadius, 0, Math.PI * 2);
        ctx.fillStyle = auraGrad;
        ctx.fill();

        // Micro-Dendritic Spines
        if (n.scale > 0.8) {
          ctx.beginPath();
          const spineCount = n.spines;
          const spineLen = radius * 1.8;
          for (let s = 0; s < spineCount; s++) {
            const angle = (s / spineCount) * Math.PI * 2 + this.rotY * 2;
            const sx = n.projX + Math.cos(angle) * (radius * 0.8);
            const sy = n.projY + Math.sin(angle) * (radius * 0.8);
            const ex = n.projX + Math.cos(angle) * spineLen;
            const ey = n.projY + Math.sin(angle) * spineLen;
            ctx.moveTo(sx, sy);
            ctx.lineTo(ex, ey);
          }
          ctx.strokeStyle = `rgba(${c.r}, ${c.g}, ${c.b}, ${0.35 * alpha})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }

        // Inner Core Nucleus (Brilliant Point)
        ctx.beginPath();
        ctx.arc(n.projX, n.projY, radius, 0, Math.PI * 2);
        if (n.excitation > 0.3) {
          ctx.fillStyle = '#FFFFFF';
        } else {
          ctx.fillStyle = `rgb(${c.r}, ${c.g}, ${c.b})`;
        }
        ctx.fill();
      }

      // 5. Draw Cognitive Pointer Focus Halo (if pointer active)
      if (this.pointer.active) {
        ctx.beginPath();
        ctx.arc(this.pointer.x, this.pointer.y, 4, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(0, 242, 254, 0.85)';
        ctx.shadowColor = '#00F2FE';
        ctx.shadowBlur = 12;
        ctx.fill();
        ctx.shadowBlur = 0;

        ctx.beginPath();
        ctx.arc(this.pointer.x, this.pointer.y, 28, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(0, 242, 254, 0.15)';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
    }

    loop() {
      if (!this.isRunning) return;

      const now = performance.now();
      const dt = Math.min((now - this.lastTime) / 1000, 0.1);
      this.lastTime = now;

      this.update(dt);
      this.render();

      requestAnimationFrame(() => this.loop());
    }
  }

  // Automatic Initialization once DOM is ready
  function initNeuralBackground() {
    let canvas = document.getElementById('neural-brain-canvas');
    if (!canvas) {
      // Find liquid-bg-canvas or inject into body
      const container = document.querySelector('.liquid-bg-canvas') || document.body;
      canvas = document.createElement('canvas');
      canvas.id = 'neural-brain-canvas';
      canvas.className = 'neural-brain-canvas';
      container.prepend(canvas);
    }
    window.neuralBrain = new NeuralBrainConnectome('neural-brain-canvas');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNeuralBackground);
  } else {
    initNeuralBackground();
  }
})();
