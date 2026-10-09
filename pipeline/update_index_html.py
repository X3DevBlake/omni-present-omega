#!/usr/bin/env python3
"""
Updates index.html to add sentient-radar.html to nav dropdowns and footer.
Also updates deepTechDossiers in js/app.js to include Project SENTIENT.
"""
import os
import subprocess

INDEX_HTML = '/data/data/com.termux/files/home/omni-web/index.html'
APP_JS = '/data/data/com.termux/files/home/omni-web/js/app.js'

def update_index():
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Frontier Tech Mega-Dropdown
    if 'sentient-radar.html' not in content:
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

        old_frontier_end = '''            <a href="deeptech-robotics.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/humanoid-robotics.svg" alt="Robotics">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Humanoid Robotics</div>
                <div class="dropdown-item-desc">Quasi-direct drive actuators & VLA</div>
              </div>
            </a>
          </div>
        </div>'''

        new_frontier_end = '''            <a href="deeptech-robotics.html" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/humanoid-robotics.svg" alt="Robotics">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">Humanoid Robotics</div>
                <div class="dropdown-item-desc">Quasi-direct drive actuators & VLA</div>
              </div>
            </a>\n''' + frontier_insertion

        content = content.replace(old_frontier_end, new_frontier_end)

        # 2. Developer Studio dropdown
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

        # 3. Footer
        footer_insertion = '      <a href="sentient-radar.html" class="footer-link">Project SENTIENT Radar</a>\n      <a href="deploy.html" class="footer-link">Firebase</a>'
        content = content.replace('      <a href="deploy.html" class="footer-link">Firebase</a>', footer_insertion)

        with open(INDEX_HTML, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ Updated index.html with Project SENTIENT radar links!")
    else:
        print("index.html already has sentient-radar.html links.")

def update_deeptech_dossiers_in_app():
    with open(APP_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    new_dossier = ''',
  {
    id: "sentient",
    title: "Project SENTIENT & Swarm Intelligence",
    category: "quantum",
    icon: "sentient-radar",
    image: "assets/images/hero-mesh-render.png",
    lead: "NRO Orbital Cross-Tasking & 5-Agent Swarm Deliberation",
    breakthrough: "Autonomous machine-intelligence cross-cueing of orbital SAR, SIGINT, and optical sensor constellations within 4.2 seconds of non-Newtonian track detection, paired with 5-agent deliberation running Google Gemini 4.0 Argon.",
    bottlenecks: "Cross-domain satellite ephemeris synchronization, multi-band radar clutter rejection, and real-time Byzantine-tolerant consensus under active electronic countermeasure jamming.",
    synergy: "Feeds real-time multi-spectral radar tracks and boundary layer magnetohydrodynamic (MHD) telemetry directly into OPO's Delta-CRDT mesh across 12 distributed SCION edge gateways.",
    status: "Active NRO Directive → Edge Swarm Integration"
  }
];'''

    old_dossier_end = '''    synergy: "The Pipecat multimodal edge pipeline and local Extended Kalman Filter (EKF) form the sensory 'Body' of the OPO ecosystem, streaming camera tensors and IMU data to execute closed-loop motor policies.",
    status: "Industrial Factory Pilots Active (2026)"
  }
];'''

    if 'Project SENTIENT & Swarm Intelligence' not in content:
        content = content.replace(old_dossier_end, '''    synergy: "The Pipecat multimodal edge pipeline and local Extended Kalman Filter (EKF) form the sensory 'Body' of the OPO ecosystem, streaming camera tensors and IMU data to execute closed-loop motor policies.",
    status: "Industrial Factory Pilots Active (2026)"
  }''' + new_dossier)
        with open(APP_JS, 'w', encoding='utf-8') as f:
            f.write(content)
        print("✓ Added Project SENTIENT to deepTechDossiers in js/app.js")

        res = subprocess.run(['node', '--check', APP_JS], capture_output=True, text=True)
        if res.returncode == 0:
            print("✓ node --check js/app.js passed!")
        else:
            print("✗ node --check error:", res.stderr)
            raise SystemExit(res.returncode)

if __name__ == '__main__':
    update_index()
    update_deeptech_dossiers_in_app()
