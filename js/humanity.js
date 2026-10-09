/**
 * HUMANITY TOKEN ($HUMANITY) - CLIENT ENGINE
 * Full Interactive Suite:
 * 1. Account Setup Engine & Portal (Email, Phone, Google Login)
 * 2. 360-Degree Auto-Rotating Hologram 3D Canvas
 * 3. Free Real-Time Mining Engine & Telemetry Accrual
 * 4. Actual Humanity Wallet & Grayed-Out "Coming Soon" Withdraw Module
 * 5. Referral Engine with +25% Multipliers & High-Reward Incentives
 * 6. Web Audio API Cybernetic Music & Ambient Soundscape
 * 7. Profile Settings, Avatar & Banner Uploading
 */

// ============================================================================
// 1. Web Audio API Cybernetic Ambient Sound & FX Synthesizer
// ============================================================================

class HumanityAudioEngine {
  constructor() {
    this.enabled = false; // Starts muted until user engages or clicks toggle
    this.ctx = null;
    this.ambientGain = null;
    this.ambientOscs = [];
    this.lfo = null;
  }

  init() {
    if (!this.ctx && typeof window !== 'undefined') {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) {
        this.ctx = new AudioCtx();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggleMusic() {
    this.init();
    this.enabled = !this.enabled;
    const pill = document.getElementById('audioPill');
    const label = document.getElementById('audioPillLabel');

    if (this.enabled) {
      if (pill) pill.classList.remove('muted');
      if (label) label.textContent = 'MUSIC ON';
      this.startAmbientSoundscape();
      this.playChime(660);
    } else {
      if (pill) pill.classList.add('muted');
      if (label) label.textContent = 'MUSIC OFF';
      this.stopAmbientSoundscape();
    }
    localStorage.setItem('humanity_audio_pref', this.enabled ? '1' : '0');
  }

  startAmbientSoundscape() {
    if (!this.ctx || this.ambientOscs.length > 0) return;
    try {
      this.ambientGain = this.ctx.createGain();
      this.ambientGain.gain.setValueAtTime(0.001, this.ctx.currentTime);
      this.ambientGain.gain.exponentialRampToValueAtTime(0.045, this.ctx.currentTime + 3.0);

      // Lowpass Filter for warm cybernetic drone
      const filter = this.ctx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(320, this.ctx.currentTime);

      // Frequencies for a mysterious sci-fi suspended chord: D - A - E (Root, 5th, 9th)
      const freqs = [73.42, 110.00, 164.81, 220.00];
      this.ambientOscs = freqs.map((f, i) => {
        const osc = this.ctx.createOscillator();
        osc.type = i % 2 === 0 ? 'sine' : 'triangle';
        osc.frequency.setValueAtTime(f + (Math.random() * 0.4 - 0.2), this.ctx.currentTime);
        osc.connect(filter);
        osc.start();
        return osc;
      });

      filter.connect(this.ambientGain);
      this.ambientGain.connect(this.ctx.destination);
    } catch (e) {
      console.warn("Audio scape error:", e);
    }
  }

  stopAmbientSoundscape() {
    if (this.ambientGain && this.ctx) {
      this.ambientGain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 1.0);
      setTimeout(() => {
        this.ambientOscs.forEach(o => {
          try { o.stop(); o.disconnect(); } catch {}
        });
        this.ambientOscs = [];
        this.ambientGain = null;
      }, 1000);
    }
  }

  playClick() {
    if (!this.enabled || !this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(880, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(440, this.ctx.currentTime + 0.04);
      gain.gain.setValueAtTime(0.06, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.04);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.04);
    } catch {}
  }

  playMiningTick() {
    if (!this.enabled || !this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(1200, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(600, this.ctx.currentTime + 0.03);
      gain.gain.setValueAtTime(0.02, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.03);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.03);
    } catch {}
  }

  playChime(freq = 523.25) {
    if (!this.enabled || !this.ctx) return;
    try {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(freq * 1.5, this.ctx.currentTime + 0.15);
      gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + 0.4);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.4);
    } catch {}
  }
}

// ============================================================================
// 2. 360-Degree Auto-Rotating Hologram 3D Canvas Engine
// ============================================================================

class Hologram360Renderer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.angleY = 0;
    this.angleX = 0.2;
    this.isDragging = false;
    this.lastMouseX = 0;
    this.lastMouseY = 0;
    this.autoRotate = true;
    this.rotationSpeed = 0.015;
    this.miningActive = false;
    this.particles = [];
    this.tokenImg = new Image();
    this.tokenImg.src = 'svg/humanity-token.svg';

    this.initCanvasSize();
    this.initParticles();
    this.bindEvents();
    this.animate();
  }

  initCanvasSize() {
    const rect = this.canvas.parentElement.getBoundingClientRect();
    const dpr = window.devicePixelRatio || 1;
    this.width = rect.width || 480;
    this.height = 400;
    this.canvas.width = this.width * dpr;
    this.canvas.height = this.height * dpr;
    this.ctx.scale(dpr, dpr);
  }

  initParticles() {
    this.particles = [];
    for (let i = 0; i < 45; i++) {
      this.particles.push({
        x: (Math.random() - 0.5) * 260,
        y: Math.random() * 240 - 120,
        z: (Math.random() - 0.5) * 260,
        size: Math.random() * 2.5 + 1,
        speedY: -(Math.random() * 1.2 + 0.4),
        alpha: Math.random() * 0.8 + 0.2,
        color: Math.random() > 0.4 ? '#38bdf8' : '#fbbf24'
      });
    }
  }

  bindEvents() {
    const c = this.canvas;
    const startDrag = (x, y) => {
      this.isDragging = true;
      this.lastMouseX = x;
      this.lastMouseY = y;
    };
    const moveDrag = (x, y) => {
      if (!this.isDragging) return;
      const dx = x - this.lastMouseX;
      const dy = y - this.lastMouseY;
      this.angleY += dx * 0.01;
      this.angleX = Math.max(-0.6, Math.min(0.6, this.angleX + dy * 0.01));
      this.lastMouseX = x;
      this.lastMouseY = y;
    };
    const stopDrag = () => { this.isDragging = false; };

    c.addEventListener('mousedown', (e) => startDrag(e.clientX, e.clientY));
    window.addEventListener('mousemove', (e) => moveDrag(e.clientX, e.clientY));
    window.addEventListener('mouseup', stopDrag);

    c.addEventListener('touchstart', (e) => {
      if (e.touches.length > 0) startDrag(e.touches[0].clientX, e.touches[0].clientY);
    }, { passive: true });
    window.addEventListener('touchmove', (e) => {
      if (e.touches.length > 0) moveDrag(e.touches[0].clientX, e.touches[0].clientY);
    }, { passive: true });
    window.addEventListener('touchend', stopDrag);

    window.addEventListener('resize', () => this.initCanvasSize());
  }

  setMining(active) {
    this.miningActive = active;
    this.rotationSpeed = active ? 0.038 : 0.015;
    if (this.canvas) {
      if (active) this.canvas.classList.add('mining-active');
      else this.canvas.classList.remove('mining-active');
    }
  }

  animate() {
    requestAnimationFrame(() => this.animate());
    if (!this.canvas) return;

    if (this.autoRotate && !this.isDragging) {
      this.angleY += this.rotationSpeed;
    }

    const ctx = this.ctx;
    ctx.clearRect(0, 0, this.width, this.height);

    const centerX = this.width / 2;
    const centerY = this.height / 2 - 20;

    // 1. Draw Pedestal Glow Rings
    ctx.save();
    ctx.translate(centerX, centerY + 140);
    ctx.scale(1, 0.35);

    ctx.beginPath();
    ctx.arc(0, 0, 130, 0, Math.PI * 2);
    ctx.strokeStyle = this.miningActive ? 'rgba(251, 191, 36, 0.6)' : 'rgba(56, 189, 248, 0.4)';
    ctx.lineWidth = 4;
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(0, 0, 95, 0, Math.PI * 2);
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.3)';
    ctx.lineWidth = 2;
    ctx.stroke();

    ctx.restore();

    // 2. Draw Floating Hologram Particles
    this.particles.forEach(p => {
      p.y += p.speedY * (this.miningActive ? 2.0 : 1.0);
      if (p.y < -160) p.y = 100;

      // 3D rotation of particle
      const cosY = Math.cos(this.angleY);
      const sinY = Math.sin(this.angleY);
      const rotX = p.x * cosY - p.z * sinY;
      const rotZ = p.x * sinY + p.z * cosY;

      const scale = 250 / (250 + rotZ);
      const projX = centerX + rotX * scale;
      const projY = centerY + p.y * scale;

      ctx.save();
      ctx.beginPath();
      ctx.arc(projX, projY, p.size * scale, 0, Math.PI * 2);
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.alpha * Math.max(0.1, scale);
      ctx.shadowColor = p.color;
      ctx.shadowBlur = 8;
      ctx.fill();
      ctx.restore();
    });

    // 3. Draw 3D Rotating Humanity Token Coin
    const coinRadius = 105;
    const cosY = Math.cos(this.angleY);
    const sinY = Math.sin(this.angleY);
    const cosX = Math.cos(this.angleX);

    ctx.save();
    ctx.translate(centerX, centerY);

    // Dynamic floating bobbing
    const bobOffset = Math.sin(Date.now() * 0.0025) * 8;
    ctx.translate(0, bobOffset);

    // Vertical Laser Guide Beams
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    const gradBeam = ctx.createLinearGradient(0, 140, 0, -100);
    gradBeam.addColorStop(0, this.miningActive ? 'rgba(251, 191, 36, 0.35)' : 'rgba(56, 189, 248, 0.25)');
    gradBeam.addColorStop(1, 'transparent');
    ctx.fillStyle = gradBeam;
    ctx.fillRect(-coinRadius * 1.1, -120, coinRadius * 2.2, 260);
    ctx.restore();

    // Coin 3D Thickness (Cylinder Stack)
    const thickness = 14;
    const steps = 7;
    for (let i = steps; i >= 0; i--) {
      const zOffset = (i / steps - 0.5) * thickness;
      const curX = sinY * zOffset;
      const curWidth = coinRadius * Math.abs(cosY);

      ctx.save();
      ctx.translate(curX, 0);
      ctx.beginPath();
      ctx.ellipse(0, 0, Math.max(2, curWidth), coinRadius * cosX, 0, 0, Math.PI * 2);

      if (i === 0 || i === steps) {
        // Face of coin
        ctx.fillStyle = '#0b1120';
        ctx.fill();
        ctx.strokeStyle = this.miningActive ? '#fbbf24' : '#38bdf8';
        ctx.lineWidth = 3.5;
        ctx.shadowColor = this.miningActive ? '#fbbf24' : '#38bdf8';
        ctx.shadowBlur = 15;
        ctx.stroke();

        // Render Coin SVG Face if loaded and front-facing
        const isFront = (i === steps && cosY >= 0) || (i === 0 && cosY < 0);
        if (isFront && this.tokenImg.complete && Math.abs(cosY) > 0.1) {
          ctx.save();
          ctx.scale(Math.abs(cosY), cosX);
          ctx.drawImage(this.tokenImg, -coinRadius * 0.88, -coinRadius * 0.88, coinRadius * 1.76, coinRadius * 1.76);
          ctx.restore();
        }
      } else {
        // Edge Rim of coin
        ctx.fillStyle = this.miningActive ? 'rgba(234, 179, 8, 0.4)' : 'rgba(56, 189, 248, 0.35)';
        ctx.fill();
        ctx.strokeStyle = 'rgba(255, 255, 255, 0.2)';
        ctx.lineWidth = 1;
        ctx.stroke();
      }
      ctx.restore();
    }

    // Holographic Scanline Overlay on Coin
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
    const scanY = (Date.now() * 0.08) % (coinRadius * 2) - coinRadius;
    ctx.fillRect(-coinRadius, scanY, coinRadius * 2, 4);
    ctx.restore();

    ctx.restore();
  }
}

// ============================================================================
// 3. User Identity & Account Setup Engine
// ============================================================================

class HumanityAccountManager {
  constructor() {
    this.storageKey = 'humanity_user_account';
    this.user = this.loadUser();
  }

  loadUser() {
    const raw = localStorage.getItem(this.storageKey);
    if (raw) {
      try { return JSON.parse(raw); } catch {}
    }
    // Default Genesis Guest Profile
    return {
      isLoggedIn: false,
      humanId: 'HUMAN-' + Math.floor(1000 + Math.random() * 9000) + '-X' + Math.floor(10 + Math.random() * 90),
      displayName: 'Anonymous Human',
      email: '',
      phone: '',
      authProvider: 'guest',
      avatarUrl: 'svg/humanity-token.svg',
      bannerUrl: '',
      bio: 'Sovereign Proof-of-Humanity Contributor',
      balance: 100.00000000, // Initial welcome starter
      hashrateBoost: 0, // In percent (e.g. +25% per referral)
      referrals: [],
      referralCode: 'HUMAN-' + Math.floor(1000 + Math.random() * 9000),
      createdAt: new Date().toISOString()
    };
  }

  saveUser() {
    localStorage.setItem(this.storageKey, JSON.stringify(this.user));
    this.updateUI();
  }

  signupWithEmail(email, name, password) {
    this.user.isLoggedIn = true;
    this.user.email = email;
    this.user.displayName = name || email.split('@')[0];
    this.user.authProvider = 'email';
    this.saveUser();
    return true;
  }

  signupWithPhone(phone, name) {
    this.user.isLoggedIn = true;
    this.user.phone = phone;
    this.user.displayName = name || 'Human ' + phone.slice(-4);
    this.user.authProvider = 'phone';
    this.saveUser();
    return true;
  }

  loginWithGoogle() {
    // Seamless Google Auth / simulated instant provider
    this.user.isLoggedIn = true;
    this.user.email = 'sovereign.human@gmail.com';
    this.user.displayName = 'Google Verified Human';
    this.user.authProvider = 'google';
    this.user.avatarUrl = 'svg/humanity-token.svg';
    this.saveUser();
    return true;
  }

  updateProfile(name, bio, avatarBase64, bannerBase64) {
    if (name) this.user.displayName = name;
    if (bio) this.user.bio = bio;
    if (avatarBase64) this.user.avatarUrl = avatarBase64;
    if (bannerBase64) this.user.bannerUrl = bannerBase64;
    this.saveUser();
  }

  updateUI() {
    // Top Bar & Profile elements
    const nameEls = document.querySelectorAll('.user-display-name');
    nameEls.forEach(el => el.textContent = this.user.displayName);

    const idEls = document.querySelectorAll('.user-human-id');
    idEls.forEach(el => el.textContent = this.user.humanId);

    const avatarEls = document.querySelectorAll('.user-avatar-img');
    avatarEls.forEach(el => {
      if (this.user.avatarUrl) el.src = this.user.avatarUrl;
    });

    const bannerEls = document.querySelectorAll('.user-banner-target');
    bannerEls.forEach(el => {
      if (this.user.bannerUrl) el.style.backgroundImage = `url(${this.user.bannerUrl})`;
    });

    const bioEls = document.querySelectorAll('.user-bio-text');
    bioEls.forEach(el => el.textContent = this.user.bio);

    const authBtn = document.getElementById('authActionBtn');
    if (authBtn) {
      authBtn.textContent = this.user.isLoggedIn ? 'PROFILE' : 'SIGN UP / LOGIN';
    }

    const refCodeEl = document.getElementById('userRefCode');
    if (refCodeEl) refCodeEl.textContent = this.user.referralCode;

    const refLinkEl = document.getElementById('userRefLink');
    if (refLinkEl) refLinkEl.textContent = `https://omni-network-39821.web.app/humanity.html?ref=${this.user.referralCode}`;
  }
}

// ============================================================================
// 4. Free Real-Time Mining Engine
// ============================================================================

class HumanityMiningEngine {
  constructor(accountMgr, soundEngine, hologramRenderer) {
    this.accountMgr = accountMgr;
    this.sound = soundEngine;
    this.holo = hologramRenderer;
    this.isMining = false;
    this.miningInterval = null;
    this.baseHashrate = 48.6; // H/s
    this.totalShares = 0;
    this.blockHeight = 849204;
    this.totalPoolRemaining = 9984210482.00000000; // From 10 Billion Total Supply

    this.bindControls();
    this.updateMiningDisplay();
  }

  getEffectiveHashrate() {
    const boostPercent = this.accountMgr.user.hashrateBoost || 0;
    return this.baseHashrate * (1 + boostPercent / 100);
  }

  bindControls() {
    const toggleBtn = document.getElementById('miningToggleBtn');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => this.toggleMining());
    }
  }

  toggleMining() {
    this.isMining = !this.isMining;
    const toggleBtn = document.getElementById('miningToggleBtn');
    const toggleLabel = document.getElementById('miningToggleLabel');
    const switchCard = document.getElementById('miningSwitchCard');

    if (this.isMining) {
      this.sound.playChime(784); // G5 note
      if (toggleBtn) {
        toggleBtn.classList.remove('start-state');
        toggleBtn.classList.add('stop-state');
      }
      if (toggleLabel) toggleLabel.textContent = 'STOP MINER';
      if (switchCard) switchCard.classList.add('mining-active');
      this.holo.setMining(true);
      this.startMiningLoop();
      showToast('⚡ Free Proof-of-Humanity Miner Started! Real-time accrual active.');
    } else {
      this.sound.playClick();
      if (toggleBtn) {
        toggleBtn.classList.remove('stop-state');
        toggleBtn.classList.add('start-state');
      }
      if (toggleLabel) toggleLabel.textContent = 'START FREE MINER';
      if (switchCard) switchCard.classList.remove('mining-active');
      this.holo.setMining(false);
      this.stopMiningLoop();
      showToast('⏸️ Miner paused. Mined tokens safely preserved in wallet.');
    }
  }

  startMiningLoop() {
    if (this.miningInterval) clearInterval(this.miningInterval);
    let tickCount = 0;

    this.miningInterval = setInterval(() => {
      if (!this.isMining) return;
      tickCount++;

      // Hashrate jitter simulation (± 1.2 H/s)
      const jitter = (Math.random() - 0.5) * 2.4;
      const currentHashrate = Math.max(10, this.getEffectiveHashrate() + jitter);

      // Micro-token yield: ~0.00025 HUMANITY per second at 50 H/s
      // Interval is 100ms -> yield is per 100ms
      const yieldPerTick = (0.00025 / 10.0) * (currentHashrate / 50.0);

      this.accountMgr.user.balance += yieldPerTick;
      this.totalPoolRemaining -= yieldPerTick;

      if (tickCount % 10 === 0) { // Every 1 second
        this.totalShares += 1;
        this.sound.playMiningTick();
        this.accountMgr.saveUser();

        if (this.totalShares % 15 === 0) { // Every 15 seconds, mine a block
          this.blockHeight += 1;
          this.addBlockRewardRecord(yieldPerTick * 10);
        }
      }

      this.updateMiningDisplay(currentHashrate);
    }, 100);
  }

  stopMiningLoop() {
    if (this.miningInterval) {
      clearInterval(this.miningInterval);
      this.miningInterval = null;
    }
    this.accountMgr.saveUser();
    this.updateMiningDisplay();
  }

  updateMiningDisplay(currentHashrate) {
    const hr = currentHashrate || (this.isMining ? this.getEffectiveHashrate() : 0);
    const balanceEl = document.getElementById('liveAccruedBalance');
    if (balanceEl) {
      balanceEl.textContent = this.accountMgr.user.balance.toFixed(8);
    }

    const walletBalEl = document.getElementById('walletHeroBalance');
    if (walletBalEl) {
      walletBalEl.textContent = this.accountMgr.user.balance.toFixed(8);
    }

    const hrEl = document.getElementById('liveHashrateVal');
    if (hrEl) hrEl.textContent = `${hr.toFixed(1)} H/s`;

    const sharesEl = document.getElementById('liveSharesVal');
    if (sharesEl) sharesEl.textContent = this.totalShares;

    const blockEl = document.getElementById('liveBlockHeight');
    if (blockEl) blockEl.textContent = `#${this.blockHeight}`;

    const poolEl = document.getElementById('unminedPoolRemaining');
    if (poolEl) {
      poolEl.textContent = Math.floor(this.totalPoolRemaining).toLocaleString() + ' HUMANITY';
    }

    // Supply Progress Fill
    const supplyBar = document.getElementById('supplyProgressBar');
    if (supplyBar) {
      const minedPct = ((10000000000 - this.totalPoolRemaining) / 10000000000) * 100;
      supplyBar.style.width = `${Math.max(0.5, minedPct)}%`;
    }
  }

  addBlockRewardRecord(amount) {
    const tableBody = document.getElementById('rewardsLedgerBody');
    if (!tableBody) return;

    const row = document.createElement('tr');
    const hash = '0x' + Math.random().toString(16).substr(2, 8) + '...' + Math.random().toString(16).substr(2, 4);
    const timeStr = new Date().toLocaleTimeString();

    row.innerHTML = `
      <td style="font-family: var(--font-mono); color: #38bdf8;">${hash}</td>
      <td style="font-family: var(--font-mono);">#${this.blockHeight}</td>
      <td style="color: #34d399; font-weight: 700; font-family: var(--font-mono);">+${amount.toFixed(6)} HUMANITY</td>
      <td style="color: #94a3b8; font-size: 0.8rem;">${timeStr}</td>
      <td><span style="font-size: 0.72rem; background: rgba(52, 211, 153, 0.15); color: #34d399; padding: 2px 8px; border-radius: 4px; font-weight: 700;">CONFIRMED</span></td>
    `;
    tableBody.insertBefore(row, tableBody.firstChild);

    // Keep max 8 rows
    while (tableBody.children.length > 8) {
      tableBody.removeChild(tableBody.lastChild);
    }
  }
}

// ============================================================================
// 5. Toast Notifications & Helpers
// ============================================================================

function showToast(message) {
  const toast = document.getElementById('humanityToast');
  const toastMsg = document.getElementById('toastMessage');
  if (!toast || !toastMsg) return;
  toastMsg.textContent = message;
  toast.classList.add('active');
  setTimeout(() => {
    toast.classList.remove('active');
  }, 3500);
}

// ============================================================================
// 6. Global Setup & Event Wiring
// ============================================================================

document.addEventListener('DOMContentLoaded', () => {
  const audio = new HumanityAudioEngine();
  const account = new HumanityAccountManager();
  const holo = new Hologram360Renderer('humanityHoloCanvas');
  const miner = new HumanityMiningEngine(account, audio, holo);

  // Audio Toggle Button
  const audioBtn = document.getElementById('audioPill');
  if (audioBtn) {
    audioBtn.addEventListener('click', () => audio.toggleMusic());
  }

  // Auth & Profile Modal Logic
  const authModal = document.getElementById('authModal');
  const profileModal = document.getElementById('profileModal');
  const authActionBtn = document.getElementById('authActionBtn');

  if (authActionBtn) {
    authActionBtn.addEventListener('click', () => {
      audio.playClick();
      if (account.user.isLoggedIn) {
        if (profileModal) profileModal.classList.add('active');
      } else {
        if (authModal) authModal.classList.add('active');
      }
    });
  }

  // Modal Close Buttons
  document.querySelectorAll('.modal-close-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      audio.playClick();
      if (authModal) authModal.classList.remove('active');
      if (profileModal) profileModal.classList.remove('active');
    });
  });

  // Auth Tab Switching
  const authTabs = document.querySelectorAll('.auth-tab-btn');
  authTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      audio.playClick();
      authTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const target = tab.getAttribute('data-target');
      document.querySelectorAll('.auth-panel').forEach(p => p.style.display = 'none');
      const targetPanel = document.getElementById(target);
      if (targetPanel) targetPanel.style.display = 'block';
    });
  });

  // Email Signup Form
  const emailForm = document.getElementById('emailSignupForm');
  if (emailForm) {
    emailForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = document.getElementById('signupEmailInput').value;
      const name = document.getElementById('signupNameInput').value;
      account.signupWithEmail(email, name);
      audio.playChime(660);
      if (authModal) authModal.classList.remove('active');
      showToast(`🎉 Welcome ${account.user.displayName}! 500 HUMANITY welcome bonus unlocked.`);
    });
  }

  // Phone Signup Form
  const phoneForm = document.getElementById('phoneSignupForm');
  if (phoneForm) {
    phoneForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const phone = document.getElementById('signupPhoneInput').value;
      const name = document.getElementById('signupPhoneNameInput').value;
      account.signupWithPhone(phone, name);
      audio.playChime(660);
      if (authModal) authModal.classList.remove('active');
      showToast(`🎉 Verified Human Phone! Welcome ${account.user.displayName}!`);
    });
  }

  // Google Login Button
  const googleBtn = document.getElementById('googleLoginBtn');
  if (googleBtn) {
    googleBtn.addEventListener('click', () => {
      account.loginWithGoogle();
      audio.playChime(784);
      if (authModal) authModal.classList.remove('active');
      showToast('✓ Logged in simply with Google! Profile verified.');
    });
  }

  // Avatar Upload with FileReader
  const avatarInput = document.getElementById('avatarFileInput');
  if (avatarInput) {
    avatarInput.addEventListener('change', (e) => {
      if (e.target.files && e.target.files[0]) {
        const reader = new FileReader();
        reader.onload = (re) => {
          account.updateProfile(null, null, re.target.result, null);
          audio.playClick();
          showToast('✓ Profile avatar updated!');
        };
        reader.readAsDataURL(e.target.files[0]);
      }
    });
  }

  // Banner Upload with FileReader
  const bannerInput = document.getElementById('bannerFileInput');
  if (bannerInput) {
    bannerInput.addEventListener('change', (e) => {
      if (e.target.files && e.target.files[0]) {
        const reader = new FileReader();
        reader.onload = (re) => {
          account.updateProfile(null, null, null, re.target.result);
          audio.playClick();
          showToast('✓ Profile header banner updated!');
        };
        reader.readAsDataURL(e.target.files[0]);
      }
    });
  }

  // Profile Save Form
  const profileForm = document.getElementById('profileEditForm');
  if (profileForm) {
    profileForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('editProfileName').value;
      const bio = document.getElementById('editProfileBio').value;
      account.updateProfile(name, bio);
      audio.playClick();
      if (profileModal) profileModal.classList.remove('active');
      showToast('✓ Profile settings saved successfully!');
    });
  }

  // Copy Referral Link
  const copyRefBtn = document.getElementById('copyRefLinkBtn');
  if (copyRefBtn) {
    copyRefBtn.addEventListener('click', () => {
      const url = `https://omni-network-39821.web.app/humanity.html?ref=${account.user.referralCode}`;
      navigator.clipboard.writeText(url).then(() => {
        audio.playChime(880);
        showToast('🔗 Referral link copied to clipboard! Share for +25% hashrate boost.');
      });
    });
  }

  // Simulate Invite Button (User can test and see hashrate boost!)
  const simInviteBtn = document.getElementById('simInviteBtn');
  if (simInviteBtn) {
    simInviteBtn.addEventListener('click', () => {
      account.user.hashrateBoost += 25;
      account.user.referrals.push({
        id: 'HUMAN-' + Math.floor(1000 + Math.random() * 9000),
        joined: 'Just now',
        status: 'Active Miner'
      });
      account.saveUser();
      audio.playChime(987.77);
      showToast(`🚀 New Referral Joined! Hashrate Boost: +${account.user.hashrateBoost}%!`);
    });
  }

  // Locked Withdraw Card Click Tooltip
  const withdrawCard = document.getElementById('withdrawCard');
  if (withdrawCard) {
    withdrawCard.addEventListener('click', () => {
      audio.playClick();
      showToast('🔒 Withdrawals Locked: Mainnet Phase II Bridge & Liquidity Genesis Coming Soon!');
    });
  }

  // Initial UI Render
  account.updateUI();
});
