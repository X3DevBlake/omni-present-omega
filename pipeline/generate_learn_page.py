#!/usr/bin/env python3
"""
Generates learn.html for the Omni-Present Omega Learning Hub.
"""
import os
import sys

BASE_DIR = '/data/data/com.termux/files/home/omni-web'
sys.path.insert(0, os.path.join(BASE_DIR, 'pipeline'))
import build_pages

learn_body = '''    <section class="landing-section">
      <div class="section-badge" style="border-color: rgba(0, 242, 254, 0.4); color: var(--gemini-cyan);">
        <img src="svg/gemini-sparkle.svg" width="16" height="16" alt="Learn">
        <span>NOTEBOOKLM INTEGRATED LEARNING PLATFORM</span>
      </div>
      <h1 class="hero-title" style="margin-bottom: 1rem;">
        <span class="hero-gradient-text">Research &amp; Knowledge Academy</span>
      </h1>
      <p class="hero-desc" style="max-width: 840px; margin: 0 auto 2rem;">
        Master the physics, engineering, and mathematics of the Omni-Present Omega ecosystem through multi-sensory study modalities: <strong>3D Liquid Glass Flashcards</strong>, <strong>Dual-Host Audio Overview Podcast</strong>, <strong>Mastery Knowledge Checks</strong>, and <strong>Socratic AI Tutoring</strong>.
      </p>

      <!-- Quick Action Buttons -->
      <div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 2.5rem;">
        <button id="open-notebook-importer-btn" class="glass-btn glass-btn-primary">
          <span>📥 Import Custom NotebookLM Notes</span>
        </button>
        <a href="#audio-overview" class="glass-btn glass-btn-secondary">
          <span>🎙️ Audio Deep Dive</span>
        </a>
        <a href="#mastery-quiz" class="glass-btn glass-btn-secondary">
          <span>📝 Mastery Quiz</span>
        </a>
        <a href="#socratic-tutor" class="glass-btn glass-btn-secondary">
          <span>🧠 Socratic AI Tutor</span>
        </a>
      </div>

      <!-- Quick Modality Filter Pills -->
      <div class="learning-modality-tabs">
        <button class="fc-category-filter-btn modality-tab-btn active" data-category="all">🗂️ All Disciplines (27)</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="sentient">🛰️ Project SENTIENT</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="mhd">⚡ MHD Propulsion</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="swarm">🐝 Swarm Overlord</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="crdt">🌐 Delta-CRDT</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="fusion">⚡ SPARC Fusion</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="quantum">🔬 Quantum</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="battery">🔋 Solid-State</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="genomics">🧬 Prime Editing</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="neural">🧠 Neural BCI</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="robotics">🤖 Robotics</button>
      </div>

      <!-- ====================================================================
           SECTION 1: 3D LIQUID GLASS FLASHCARD DECK
           ==================================================================== -->
      <div class="flashcard-stage">
        <div id="interactive-flashcard" class="flashcard-card" title="Click to flip card">
          <!-- Front Face -->
          <div class="flashcard-front">
            <div class="flashcard-meta-bar">
              <span id="fc-badge" class="flashcard-category-tag">Delta-CRDT</span>
              <span class="flashcard-tap-hint">⟲ TAP / CLICK TO FLIP</span>
            </div>
            <div>
              <h2 id="fc-prompt-title" class="flashcard-prompt-title">Join-Semilattice Monotonicity</h2>
              <p id="fc-prompt-sub" class="flashcard-prompt-sub">Why must state mutations in RedComm satisfy the join-semilattice algebraic property (S, ⊔)?</p>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 1rem;">
              <span id="fc-progress-counter" style="font-size: 0.78rem; font-family: var(--font-mono); color: #64748B;">Card 1 of 24</span>
              <span style="font-size: 0.78rem; color: var(--gemini-cyan); font-weight: 600;">Reveals Theorem &amp; Formulation →</span>
            </div>
          </div>

          <!-- Back Face -->
          <div class="flashcard-back">
            <div class="flashcard-meta-bar">
              <span class="flashcard-category-tag" style="border-color: rgba(52, 211, 153, 0.4); color: #34D399;">SCIENTIFIC SOLUTION</span>
              <span class="flashcard-tap-hint">⟲ FLIP BACK</span>
            </div>
            <div>
              <p id="fc-answer-body" class="flashcard-answer-body">
                A join-semilattice guarantees that for any two states a and b, the join operation a ⊔ b is commutative, associative, and idempotent. This ensures all distributed replicas converge monotonically to identical state without distributed locks or 2PC.
              </p>
              <div id="fc-formula-box" class="flashcard-formula-highlight">
                a ⊔ b = b ⊔ a,  (a ⊔ b) ⊔ c = a ⊔ (b ⊔ c),  a ⊔ a = a
              </div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 1rem;">
              <span style="font-size: 0.75rem; color: #94A3B8; font-family: var(--font-mono);">OPO &amp; RedComm Monotonic Core</span>
              <span style="font-size: 0.78rem; color: #34D399; font-weight: 600;">✓ Concept Mastered</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Flashcard Deck Controls -->
      <div class="flashcard-controls-bar">
        <button id="flashcard-prev-btn" class="glass-btn glass-btn-secondary" style="padding: 8px 16px;">
          <span>← Previous Card</span>
        </button>
        <button id="flashcard-shuffle-btn" class="glass-btn glass-btn-secondary" style="padding: 8px 16px;">
          <span>🔀 Shuffle Deck</span>
        </button>
        <button id="flashcard-next-btn" class="glass-btn glass-btn-primary" style="padding: 8px 16px;">
          <span>Next Card →</span>
        </button>
      </div>

      <!-- ====================================================================
           SECTION 2: DUAL-HOST AUDIO OVERVIEW DEEP DIVE PODCAST
           ==================================================================== -->
      <div id="audio-overview" class="audio-overview-card">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.75rem;">
          <div>
            <span class="brand-badge" style="background: rgba(123, 97, 255, 0.15); color: var(--gemini-purple); border-color: rgba(123, 97, 255, 0.35);">
              NOTEBOOKLM AUDIO OVERVIEW • AI SYNTHESIZED
            </span>
            <h2 style="font-size: 1.5rem; color: #FFFFFF; margin-top: 6px;">Deep Dive: Frontier Physics Meets Sovereign CRDTs</h2>
          </div>
          <button id="podcast-play-btn" class="glass-btn glass-btn-primary" style="padding: 8px 18px;">
            <span id="podcast-play-icon">▶️</span>
            <span id="podcast-play-text">PLAY DEEP DIVE</span>
          </button>
        </div>

        <!-- Co-Hosts Meta Chips -->
        <div class="audio-hosts-bar">
          <div class="host-chip">
            <div class="host-avatar">AV</div>
            <span><strong>Dr. Aris Vance</strong> (Systems Architecture)</span>
          </div>
          <div class="host-chip">
            <div class="host-avatar" style="background: linear-gradient(135deg, #EC4899, #F59E0B);">ER</div>
            <span><strong>Dr. Elena Rostova</strong> (Frontier Physics)</span>
          </div>
          <span id="podcast-time-disp" style="margin-left: auto; font-family: var(--font-mono); font-size: 0.85rem; color: #94A3B8;">00:00 / 04:00</span>
        </div>

        <!-- Animated Waveform Canvas -->
        <div class="waveform-canvas-box">
          <canvas id="audio-waveform-canvas"></canvas>
        </div>

        <!-- Synchronized Transcript -->
        <div class="audio-transcript-container">
          <div class="transcript-line active-speaking" data-time="0" data-next="25">
            <span class="transcript-speaker" style="color: var(--gemini-cyan);">Dr. Vance:</span>
            Welcome to the Omni-Present Omega Deep Dive. Today we are bridging six distinct frontier deep tech disciplines into a single sovereign Delta-CRDT state engine.
          </div>
          <div class="transcript-line" data-time="25" data-next="55">
            <span class="transcript-speaker" style="color: #F472B6;">Dr. Rostova:</span>
            That is right, Aris. Most engineering teams treat physics domains in silos. But when you look at the Lawson Criterion in tokamak fusion or TFLN electro-optics in quantum photonics, they all share an identical bottleneck: sub-millisecond deterministic state synchronization.
          </div>
          <div class="transcript-line" data-time="55" data-next="85">
            <span class="transcript-speaker" style="color: var(--gemini-cyan);">Dr. Vance:</span>
            Exactly. The SPARC tokamak requires microsecond magnetics stabilization. If your telemetry relies on centralized cloud coordination, the plasma disrupts before the packet arrives.
          </div>
          <div class="transcript-line" data-time="85" data-next="115">
            <span class="transcript-speaker" style="color: #F472B6;">Dr. Rostova:</span>
            And that is why RedComm implements a join-semilattice (S, ⊔). Every local node can mutate state offline and guarantee mathematical monotonicity when network partitions heal.
          </div>
          <div class="transcript-line" data-time="115" data-next="150">
            <span class="transcript-speaker" style="color: var(--gemini-cyan);">Dr. Vance:</span>
            Let us look at biology and robotics as well: 1024-channel flexible polyimide micro-threads for intracortical BCIs, and quasi-direct drive actuators operating with 1 kHz whole-body impedance loops.
          </div>
          <div class="transcript-line" data-time="150" data-next="180">
            <span class="transcript-speaker" style="color: #F472B6;">Dr. Rostova:</span>
            It is an extraordinary convergence: from quantum optical chips to solid-state batteries, autonomous edge models now execute with zero single points of failure.
          </div>
          <div class="transcript-line" data-time="180" data-next="210">
            <span class="transcript-speaker" style="color: var(--gemini-cyan);">Dr. Vance:</span>
            And now we are integrating National Reconnaissance Office Project SENTIENT principles into our multi-spectral radar. When edge sensors identify non-Newtonian kinematics exceeding Mach 15, the system autonomously tasks orbital and drone arrays without ground-station delay.
          </div>
          <div class="transcript-line" data-time="210" data-next="240">
            <span class="transcript-speaker" style="color: #F472B6;">Dr. Rostova:</span>
            Coupled with our 5-agent Gemini 4.0 Argon swarm—Vortex, Spectre, Chronos, Nexus, and Omni—we can deliberate over boundary-layer magnetohydrodynamic plasma sheaths in real-time, verifying why these vehicles generate zero acoustic shockwave signature.
          </div>
        </div>
      </div>

      <!-- ====================================================================
           SECTION 3: MASTERY QUIZ & KNOWLEDGE ASSESSMENT
           ==================================================================== -->
      <div id="mastery-quiz" class="quiz-container">
        <div class="quiz-card">
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 0.5rem;">
            <div>
              <span class="brand-badge" style="background: rgba(16, 185, 129, 0.15); color: #34D399; border-color: rgba(16, 185, 129, 0.35);">
                MASTERY ASSESSMENT • INSTANT FEEDBACK
              </span>
              <h2 style="font-size: 1.45rem; color: #FFFFFF; margin-top: 4px;">Knowledge Check &amp; Concept Retention</h2>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <span style="font-size: 0.78rem; font-family: var(--font-mono); color: #94A3B8;">SCORE:</span>
              <span id="quiz-score-val" class="brand-badge" style="background: rgba(0, 242, 254, 0.2); color: var(--gemini-cyan);">0 / 1</span>
            </div>
          </div>

          <div id="quiz-progress-text" style="font-size: 0.8rem; font-family: var(--font-mono); color: var(--gemini-cyan); margin-bottom: 0.5rem;">Question 1 of 6</div>
          <h3 id="quiz-question-title" style="font-size: 1.15rem; color: #F8FAFC; line-height: 1.5; margin-bottom: 1.25rem;">Loading question...</h3>

          <!-- Options Container -->
          <div id="quiz-options-container" class="quiz-options-list"></div>

          <!-- Explanation Box -->
          <div id="quiz-explanation-box" class="quiz-explanation-box">
            <div style="font-size: 0.8rem; font-weight: 700; color: #34D399; margin-bottom: 4px;">🔬 SCIENTIFIC EXPLANATION</div>
            <p id="quiz-explanation-text" style="margin: 0;"></p>
          </div>

          <div style="display: flex; justify-content: flex-end; margin-top: 1.5rem;">
            <button id="quiz-next-btn" class="glass-btn glass-btn-primary" style="display: none;">
              <span>Next Question →</span>
            </button>
          </div>
        </div>
      </div>

      <!-- ====================================================================
           SECTION 4: SOCRATIC 'HELP ME LEARN' AI WORKBENCH
           ==================================================================== -->
      <div id="socratic-tutor" class="glass-panel" style="padding: 2.25rem; max-width: 840px; margin: 0 auto 3rem;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; flex-wrap: wrap; gap: 0.5rem;">
          <div style="display: flex; align-items: center; gap: 10px;">
            <img src="svg/gemini-sparkle.svg" width="24" height="24" alt="Tutor">
            <h2 style="font-size: 1.35rem; color: #FFFFFF; margin: 0;">Socratic AI Tutor (&quot;Help Me Learn&quot;)</h2>
          </div>
          <span class="brand-badge" style="background: rgba(0, 242, 254, 0.15); color: var(--gemini-cyan); border-color: rgba(0, 242, 254, 0.35);">POWERED BY GEMINI 4.0 ARGON</span>
        </div>
        <p style="color: #94A3B8; font-size: 0.92rem; line-height: 1.6; margin-bottom: 1.5rem;">
          Rather than just giving flat answers, the Socratic Tutor harnesses <strong>Gemini 4.0 Argon</strong> deep reasoning to guide you through physical derivations, identifying scientific bottlenecks, and exploring architectural synergies step-by-step.
        </p>

        <div style="margin-bottom: 1rem;">
          <label style="display: block; font-size: 0.75rem; font-family: var(--font-mono); color: #94A3B8; margin-bottom: 6px;">EXPLORATION TOPIC</label>
          <input id="socratic-topic-input" type="text" class="glass-input" style="width: 100%;" value="Why does Lawson criterion scaling P_fusion ∝ B⁴ favor compact high-field tokamaks over giant reactors?">
        </div>

        <button class="glass-btn glass-btn-primary" style="width: 100%;" onclick="runGeminiMockInference()">
          <img src="svg/gemini-sparkle.svg" width="18" height="18" alt="Tutor">
          <span>Start Socratic Dialogue with Gemini 4.0 Argon →</span>
        </button>

        <div id="socratic-output-box" style="display: none; margin-top: 1.5rem; min-height: 220px; background: rgba(5, 8, 16, 0.85); border: 1px solid rgba(0, 242, 254, 0.25); border-radius: 12px; padding: 1.25rem; font-family: var(--font-mono); font-size: 0.85rem; color: #E2E8F0; line-height: 1.7; overflow-y: auto; white-space: pre-wrap;"></div>
      </div>

    </section>

    <!-- NotebookLM Notes Importer Modal -->
    <div id="notebook-importer-modal" class="importer-modal-backdrop">
      <div class="importer-modal-panel">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
          <h3 style="color: #FFFFFF; font-size: 1.25rem; margin: 0; display: flex; align-items: center; gap: 8px;">
            <span>📥 Import NotebookLM Notes</span>
          </h3>
          <button id="close-importer-modal-btn" class="glass-modal-close-btn" style="background: none; border: none; font-size: 1.5rem; color: #94A3B8; cursor: pointer;">&times;</button>
        </div>
        <p style="color: #94A3B8; font-size: 0.85rem; line-height: 1.5; margin-bottom: 1rem;">
          Paste notes, questions, or key takeaways from research dossiers, notebooks, or engineering briefs. The system will automatically synthesize them into interactive 3D flashcards and knowledge checks.
        </p>
        <textarea id="imported-notes-textarea" class="glass-input" rows="7" style="width: 100%; margin-bottom: 1.25rem;" placeholder="Paste questions and answers here, for example:&#10;Q: What is the magnetic field of SPARC? A: 12.2 Tesla on-axis with 20T peak coil field.&#10;Q: Why use delta-CRDT? A: Transmits only mutations, saving 98% bandwidth."></textarea>
        <div style="display: flex; justify-content: flex-end; gap: 0.75rem;">
          <button class="glass-btn glass-btn-secondary" onclick="document.getElementById('notebook-importer-modal').classList.remove('open')">
            <span>Cancel</span>
          </button>
          <button id="submit-import-notes-btn" class="glass-btn glass-btn-primary">
            <span>Synthesize into Flashcards ⚡</span>
          </button>
        </div>
      </div>
    </div>'''

html = build_pages.render_page(
    title="Interactive Learning Hub & Audio Overview",
    desc="NotebookLM-inspired Study Modalities: 3D Liquid Glass Flashcards, Audio Deep Dive Podcast, Mastery Quiz, and Socratic AI Guidance.",
    current_breadcrumb='<a href="learn.html">Academy</a> <span class="sep">/</span> <span class="current">Learning Hub</span>',
    body_content=learn_body
)

out_file = os.path.join(BASE_DIR, 'learn.html')
with open(out_file, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated: {out_file} ({len(html)} bytes)")
