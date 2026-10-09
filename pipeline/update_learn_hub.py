#!/usr/bin/env python3
"""
Adds Project SENTIENT, MHD Propulsion, and Swarm Intelligence flashcards and quiz questions
to js/app.js, updates pipeline/generate_learn_page.py, and regenerates learn.html.
"""
import os
import subprocess

APP_JS = '/data/data/com.termux/files/home/omni-web/js/app.js'
GEN_LEARN = '/data/data/com.termux/files/home/omni-web/pipeline/generate_learn_page.py'

NEW_FLASHCARDS_CODE = ''',
  {
    category: "sentient",
    badge: "Project SENTIENT",
    title: "Autonomous Orbital Cross-Cueing",
    prompt: "How does NRO Project SENTIENT task optical and SAR satellites without ground-station delays?",
    answer: "Project SENTIENT integrates onboard edge-tensor processors that detect un-correlated non-Newtonian track vectors in real-time, autonomously reprioritizing and slewing adjacent orbital imaging sensors within seconds.",
    formula: "Δt_tasking ≤ 4.2 s,   Δv_vector > Mach 15"
  },
  {
    category: "mhd",
    badge: "MHD Propulsion",
    title: "Boundary Layer Lorentz Force",
    prompt: "How does a Magnetohydrodynamic (MHD) plasma sheath eliminate acoustic sonic booms?",
    answer: "By generating pulsed magnetic fields (B) and surface current density (j), the volumetric Lorentz force (FL = j × B) accelerates ambient ionized air around the vehicle hull faster than ambient sound speed, preventing wave coalescence.",
    formula: "F_L = j × B,   Δv = sqrt(2 · F_L · L / ρ)"
  },
  {
    category: "swarm",
    badge: "Swarm Intelligence",
    title: "5-Agent Monotonic Deliberation",
    prompt: "Why does the OPO Swarm Overlord structure agent consensus as a Delta-CRDT join-semilattice?",
    answer: "By mapping each agent's observations (Vortex, Spectre, Chronos, Nexus, Omni) into monotonic state deltas (S, ⊔), divergent perspectives converge deterministically without Byzantine split-brain or centralized deadlock.",
    formula: "S_consensus = S_0 ⊔ ΔS_vortex ⊔ ΔS_spectre ⊔ ..."
  }
];'''

NEW_QUIZ_CODE = ''',
  {
    question: "In Magnetohydrodynamic (MHD) boundary layer control, what physical force accelerates the ionized slipstream around the craft?",
    options: [
      "Van der Waals force",
      "Volumetric Lorentz force (FL = j × B)",
      "Gravitational slingshot",
      "Electrostatic Coulomb repulsion only"
    ],
    correctIndex: 1,
    explanation: "The volumetric Lorentz force FL = j × B applies electromagnetic acceleration directly to the ionized boundary fluid, eliminating wave drag and acoustic sonic booms."
  },
  {
    question: "What is the primary operational innovation of NRO's Project SENTIENT architecture?",
    options: [
      "Launching heavier chemical rockets",
      "Automated satellite cross-cueing on un-correlated tracks without ground intervention",
      "Replacing all satellites with weather balloons",
      "Storing telemetry exclusively on magnetic tape"
    ],
    correctIndex: 1,
    explanation: "Project SENTIENT uses autonomous machine intelligence to cross-cue multi-spectral orbital sensors (SAR, SIGINT, optical) in seconds without waiting for ground transmission."
  }
];'''

def patch_app_js():
    with open(APP_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    # Insert flashcards before `];\n\nconst PRELOADED_QUIZ = [`
    target_fc_end = '''    formula: "τ = J^T · F_task + (I - J^T J#) · τ_posture"
  }
];'''
    if 'category: "sentient"' not in content:
        content = content.replace(target_fc_end, '''    formula: "τ = J^T · F_task + (I - J^T J#) · τ_posture"
  }''' + NEW_FLASHCARDS_CODE)

    # Insert quiz questions before `];\n\nclass LearningHubController {`
    target_quiz_end = '''    explanation: "Brain tissue has a modulus in the kPa range. Flexible 4-6 µm polyimide micro-threads match neural compliance, eliminating chronic micromotion shear and glial scar insulation."
  }
];'''
    if 'In Magnetohydrodynamic (MHD) boundary layer control' not in content:
        content = content.replace(target_quiz_end, '''    explanation: "Brain tissue has a modulus in the kPa range. Flexible 4-6 µm polyimide micro-threads match neural compliance, eliminating chronic micromotion shear and glial scar insulation."
  }''' + NEW_QUIZ_CODE)

    with open(APP_JS, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Patched PRELOADED_FLASHCARDS and PRELOADED_QUIZ in js/app.js")

    res = subprocess.run(['node', '--check', APP_JS], capture_output=True, text=True)
    if res.returncode == 0:
        print("✓ node --check js/app.js passed!")
    else:
        print("✗ node --check error:", res.stderr)
        raise SystemExit(res.returncode)

def patch_generate_learn():
    with open(GEN_LEARN, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update categories in generate_learn_page.py
    old_pills = '''        <button class="fc-category-filter-btn modality-tab-btn active" data-category="all">🗂️ All Disciplines (24)</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="crdt">🌐 Delta-CRDT</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="fusion">⚡ SPARC Fusion</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="quantum">🔬 Quantum</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="battery">🔋 Solid-State</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="genomics">🧬 Prime Editing</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="neural">🧠 Neural BCI</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="robotics">🤖 Robotics</button>'''

    new_pills = '''        <button class="fc-category-filter-btn modality-tab-btn active" data-category="all">🗂️ All Disciplines (27)</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="sentient">🛰️ Project SENTIENT</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="mhd">⚡ MHD Propulsion</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="swarm">🐝 Swarm Overlord</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="crdt">🌐 Delta-CRDT</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="fusion">⚡ SPARC Fusion</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="quantum">🔬 Quantum</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="battery">🔋 Solid-State</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="genomics">🧬 Prime Editing</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="neural">🧠 Neural BCI</button>
        <button class="fc-category-filter-btn modality-tab-btn" data-category="robotics">🤖 Robotics</button>'''

    if old_pills in content:
        content = content.replace(old_pills, new_pills)

    # Update podcast time
    content = content.replace('00:00 / 03:00', '00:00 / 04:00')

    # Add podcast transcript lines
    old_transcript_end = '''          <div class="transcript-line" data-time="150" data-next="180">
            <span class="transcript-speaker" style="color: #F472B6;">Dr. Rostova:</span>
            It is an extraordinary convergence: from quantum optical chips to solid-state batteries, autonomous edge models now execute with zero single points of failure.
          </div>'''

    new_transcript_end = '''          <div class="transcript-line" data-time="150" data-next="180">
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
          </div>'''

    if old_transcript_end in content and 'Project SENTIENT principles' not in content:
        content = content.replace(old_transcript_end, new_transcript_end)

    with open(GEN_LEARN, 'w', encoding='utf-8') as f:
        f.write(content)
    print("✓ Updated pipeline/generate_learn_page.py")

if __name__ == '__main__':
    patch_app_js()
    patch_generate_learn()
    # Regenerate learn.html
    import generate_learn_page
    print("✓ Regenerated learn.html successfully!")
