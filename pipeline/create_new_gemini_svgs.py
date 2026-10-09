#!/usr/bin/env python3
"""
Creates modern 3D Google Gemini SVG vectors:
- svg/gemini-argon-3d.svg
- svg/chart-3d-hologram.svg
- svg/bench-suite-3d.svg
- svg/gemini-multimodal-lens.svg
Validates XML parsing and gradient reference IDs.
"""

import os
import re
import xml.etree.ElementTree as ET

SVG_DIR = '/data/data/com.termux/files/home/omni-web/svg'

SVGS = {
    'gemini-argon-3d.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <defs>
    <linearGradient id="argon-facet-top" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4E82EE" />
    </linearGradient>
    <linearGradient id="argon-facet-left" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4E82EE" />
      <stop offset="100%" stop-color="#7B61FF" />
    </linearGradient>
    <linearGradient id="argon-facet-right" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7B61FF" />
      <stop offset="100%" stop-color="#F472B6" />
    </linearGradient>
    <radialGradient id="argon-core-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.9" />
      <stop offset="50%" stop-color="#7B61FF" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#7B61FF" stop-opacity="0" />
    </radialGradient>
    <filter id="argon-glow-filter" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Ambient Glow -->
  <circle cx="32" cy="32" r="26" fill="url(#argon-core-glow)" opacity="0.6" filter="url(#argon-glow-filter)" />

  <!-- Orbital Ellipse -->
  <ellipse cx="32" cy="32" rx="28" ry="10" stroke="#00F2FE" stroke-width="1.2" stroke-dasharray="3 3" opacity="0.5" transform="rotate(-25 32 32)" />
  <circle cx="10" cy="22" r="2" fill="#00F2FE" />
  <circle cx="54" cy="42" r="2" fill="#F472B6" />

  <!-- 3D Polyhedral Diamond Faces -->
  <!-- Top Point to Center -->
  <polygon points="32,6 32,32 18,22" fill="url(#argon-facet-top)" opacity="0.95" />
  <polygon points="32,6 46,22 32,32" fill="url(#argon-facet-right)" opacity="0.9" />

  <!-- Center to Bottom Point -->
  <polygon points="32,32 18,42 32,58" fill="url(#argon-facet-left)" opacity="0.95" />
  <polygon points="32,32 32,58 46,42" fill="url(#argon-facet-right)" opacity="0.85" />

  <!-- Lateral Wings (4-Point Gemini Star) -->
  <polygon points="6,32 18,22 32,32" fill="url(#argon-facet-left)" opacity="0.9" />
  <polygon points="6,32 32,32 18,42" fill="url(#argon-facet-top)" opacity="0.8" />
  <polygon points="58,32 32,32 46,22" fill="url(#argon-facet-top)" opacity="0.9" />
  <polygon points="58,32 46,42 32,32" fill="url(#argon-facet-right)" opacity="0.85" />

  <!-- Specular Center Highlight -->
  <circle cx="32" cy="32" r="3.5" fill="#FFFFFF" opacity="0.95" />
</svg>''',

    'chart-3d-hologram.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <defs>
    <linearGradient id="bar-grad-1" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4E82EE" />
    </linearGradient>
    <linearGradient id="bar-grad-2" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#7B61FF" />
      <stop offset="100%" stop-color="#4E82EE" />
    </linearGradient>
    <linearGradient id="bar-grad-3" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#F472B6" />
      <stop offset="100%" stop-color="#7B61FF" />
    </linearGradient>
    <linearGradient id="spline-line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#BA68C8" />
      <stop offset="100%" stop-color="#F472B6" />
    </linearGradient>
    <radialGradient id="chart-ambient-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0" />
    </radialGradient>
    <filter id="hologram-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Ambient Glow Base -->
  <ellipse cx="32" cy="46" rx="26" ry="12" fill="url(#chart-ambient-glow)" opacity="0.6" />

  <!-- 3D Isometric Base Plane -->
  <polygon points="32,42 56,52 32,60 8,52" fill="rgba(12, 18, 36, 0.85)" stroke="#00F2FE" stroke-width="1" stroke-opacity="0.4" />
  <line x1="20" y1="47" x2="44" y2="57" stroke="rgba(0, 242, 254, 0.25)" stroke-width="0.8" />
  <line x1="44" y1="47" x2="20" y2="57" stroke="rgba(0, 242, 254, 0.25)" stroke-width="0.8" />

  <!-- 3D Bar 1 (Left - Height 20) -->
  <polygon points="18,48 24,45 24,30 18,33" fill="url(#bar-grad-1)" opacity="0.8" />
  <polygon points="24,45 30,48 30,33 24,30" fill="url(#bar-grad-1)" opacity="0.6" />
  <polygon points="18,33 24,30 30,33 24,36" fill="#00F2FE" opacity="0.95" />

  <!-- 3D Bar 2 (Center - Height 32) -->
  <polygon points="26,44 32,41 32,18 26,21" fill="url(#bar-grad-2)" opacity="0.85" />
  <polygon points="32,41 38,44 38,21 32,18" fill="url(#bar-grad-2)" opacity="0.65" />
  <polygon points="26,21 32,18 38,21 32,24" fill="#7B61FF" opacity="0.95" />

  <!-- 3D Bar 3 (Right - Height 26) -->
  <polygon points="34,48 40,45 40,24 34,27" fill="url(#bar-grad-3)" opacity="0.85" />
  <polygon points="40,45 46,48 46,27 40,24" fill="url(#bar-grad-3)" opacity="0.65" />
  <polygon points="34,27 40,24 46,27 40,30" fill="#F472B6" opacity="0.95" />

  <!-- Glowing Spline Trend Line -->
  <path d="M12 40 Q 24 22, 32 16 T 52 18" stroke="url(#spline-line-grad)" stroke-width="2.5" fill="none" stroke-linecap="round" filter="url(#hologram-glow)" />

  <!-- Data Point Orbs -->
  <circle cx="12" cy="40" r="2.5" fill="#00F2FE" />
  <circle cx="32" cy="16" r="3" fill="#BA68C8" />
  <circle cx="52" cy="18" r="2.5" fill="#F472B6" />
</svg>''',

    'bench-suite-3d.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <defs>
    <linearGradient id="gauge-arc-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="50%" stop-color="#34D399" />
      <stop offset="100%" stop-color="#7B61FF" />
    </linearGradient>
    <radialGradient id="gauge-center-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#34D399" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#00F2FE" stop-opacity="0" />
    </radialGradient>
    <filter id="gauge-glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Ambient Glow -->
  <circle cx="32" cy="32" r="22" fill="url(#gauge-center-glow)" opacity="0.4" />

  <!-- Outer Dial Track -->
  <circle cx="32" cy="32" r="26" stroke="rgba(255, 255, 255, 0.1)" stroke-width="3" stroke-dasharray="4 2" />

  <!-- Main Active Speedometer Arc (270 deg) -->
  <path d="M 13 46 A 24 24 0 1 1 51 46" stroke="url(#gauge-arc-grad)" stroke-width="4" stroke-linecap="round" fill="none" filter="url(#gauge-glow-filter)" />

  <!-- Inner Scale Ring -->
  <circle cx="32" cy="32" r="18" stroke="rgba(0, 242, 254, 0.25)" stroke-width="1.2" />

  <!-- Tick Marks -->
  <line x1="32" y1="9" x2="32" y2="13" stroke="#00F2FE" stroke-width="1.5" />
  <line x1="15" y1="20" x2="18" y2="22" stroke="#00F2FE" stroke-width="1.5" />
  <line x1="49" y1="20" x2="46" y2="22" stroke="#34D399" stroke-width="1.5" />
  <line x1="9" y1="32" x2="13" y2="32" stroke="#00F2FE" stroke-width="1.5" />
  <line x1="55" y1="32" x2="51" y2="32" stroke="#34D399" stroke-width="1.5" />

  <!-- Center Diagnostic Core & Shield -->
  <polygon points="32,20 42,25 42,37 32,44 22,37 22,25" fill="rgba(8, 14, 28, 0.9)" stroke="#34D399" stroke-width="1.8" />

  <!-- Centered Checkmark -->
  <path d="M26 31 L30 35 L38 27" stroke="#34D399" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
</svg>''',

    'gemini-multimodal-lens.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" fill="none">
  <defs>
    <linearGradient id="lens-rim-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#4E82EE" />
      <stop offset="70%" stop-color="#7B61FF" />
      <stop offset="100%" stop-color="#F472B6" />
    </linearGradient>
    <radialGradient id="aperture-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0.8" />
      <stop offset="60%" stop-color="#7B61FF" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#7B61FF" stop-opacity="0" />
    </radialGradient>
    <filter id="lens-glow-filter" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Ambient Light Cone -->
  <circle cx="32" cy="32" r="26" fill="url(#aperture-glow)" opacity="0.6" filter="url(#lens-glow-filter)" />

  <!-- Outer Aperture Ring -->
  <circle cx="32" cy="32" r="27" stroke="url(#lens-rim-grad)" stroke-width="2.2" />

  <!-- Focus Iris Blades -->
  <circle cx="32" cy="32" r="21" stroke="rgba(255, 255, 255, 0.15)" stroke-width="1" stroke-dasharray="6 3" />
  <circle cx="32" cy="32" r="15" stroke="rgba(0, 242, 254, 0.3)" stroke-width="1.2" />

  <!-- Cross-Spectral Crosshairs -->
  <line x1="32" y1="5" x2="32" y2="12" stroke="#00F2FE" stroke-width="1.5" />
  <line x1="32" y1="52" x2="32" y2="59" stroke="#00F2FE" stroke-width="1.5" />
  <line x1="5" y1="32" x2="12" y2="32" stroke="#00F2FE" stroke-width="1.5" />
  <line x1="52" y1="32" x2="59" y2="32" stroke="#00F2FE" stroke-width="1.5" />

  <!-- Central Gemini 4-Point Sparkle Core -->
  <path d="M32 18 C32 25.73 25.73 32 18 32 C25.73 32 32 38.27 32 46 C32 38.27 38.27 32 46 32 C38.27 32 32 25.73 32 18 Z" fill="url(#lens-rim-grad)" />
  <circle cx="32" cy="32" r="2" fill="#FFFFFF" />
</svg>'''
}

def main():
    for name, content in SVGS.items():
        filepath = os.path.join(SVG_DIR, name)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip())
        
        # Verify XML parsing
        ET.parse(filepath)
        # Verify gradient ID references
        urls = re.findall(r'url\(#([^)]+)\)', content)
        ids = set(re.findall(r'id=[\"\']([^\"\']+)[\"\']', content))
        for u in urls:
            if u not in ids:
                raise ValueError(f"Missing ID #{u} in {name}")
        print(f"✓ Created and validated {name}")

if __name__ == '__main__':
    main()
