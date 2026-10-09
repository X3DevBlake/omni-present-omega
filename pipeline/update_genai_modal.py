#!/usr/bin/env python3
"""
Adds the interactive Google GenAI SDK Modal (gemini-4.0-argon) to:
- pipeline/build_pages.py (FOOTER_HTML, NAV_HEADER, gemini-studio.html)
- index.html
- Regenerates all pages and verifies.
"""
import os
import re
import subprocess

BUILD_PAGES = '/data/data/com.termux/files/home/omni-web/pipeline/build_pages.py'
INDEX_HTML = '/data/data/com.termux/files/home/omni-web/index.html'

GENAI_MODAL_HTML = '''  <!-- Liquid Glass Google GenAI SDK Modal (gemini-4.0-argon) -->
  <div id="genai-sdk-modal" class="importer-modal-backdrop" onclick="if(event.target === this) closeGenAiSdkModal()">
    <div class="importer-modal-panel" style="max-width: 820px; max-height: 90vh; overflow-y: auto;">
      <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.25rem; border-bottom: 1px solid rgba(255,255,255,0.08); padding-bottom: 0.75rem;">
        <div>
          <div style="display: flex; align-items: center; gap: 8px;">
            <span class="brand-badge" style="background: rgba(0,242,254,0.15); color: var(--gemini-cyan); border-color: rgba(0,242,254,0.3); font-size: 0.75rem;">GOOGLE GENAI SDK</span>
            <span style="font-size: 0.7rem; font-family: var(--font-mono); color: #34D399; background: rgba(16,185,129,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid rgba(16,185,129,0.3);">MODEL: GEMINI-4.0-ARGON</span>
          </div>
          <h3 style="margin: 6px 0 0 0; font-size: 1.35rem; color: #FFF; font-weight: 700;">Google GenAI Python &amp; TypeScript Execution Modal</h3>
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
  </div>\n'''

def update_build_pages():
    with open(BUILD_PAGES, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add GenAI Modal into FOOTER_HTML
    if 'id="genai-sdk-modal"' not in content:
        content = content.replace("FOOTER_HTML = '''  <!-- Liquid Glass Footer -->",
                                  "FOOTER_HTML = '''" + GENAI_MODAL_HTML + "  <!-- Liquid Glass Footer -->")
        print("✓ Injected genai-sdk-modal into FOOTER_HTML")

    # Add Nav Trigger into Developer Studio Dropdown
    nav_studio_trigger = '''            <a href="javascript:void(0)" onclick="openGenAiSdkModal()" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/gemini-sparkle.svg" alt="GenAI SDK">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">GenAI SDK Modal <span class="item-badge">gemini-4.0-argon</span></div>
                <div class="dropdown-item-desc">Interactive Python SDK runner &amp; thinking budget</div>
              </div>
            </a>\n'''
    if 'onclick="openGenAiSdkModal()"' not in content:
        content = content.replace('            <a href="whitepaper.html" class="dropdown-item">',
                                  nav_studio_trigger + '            <a href="whitepaper.html" class="dropdown-item">')
        print("✓ Injected GenAI SDK Modal trigger into NAV_HEADER")

    # Add Hero Launch Button into gemini-studio.html
    hero_btn = '''      <!-- Launch GenAI SDK Modal Button -->
      <div style="display: flex; justify-content: center; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 2.5rem;">
        <button class="glass-btn glass-btn-primary" onclick="openGenAiSdkModal()" style="padding: 10px 22px; font-size: 0.9rem;">
          <img src="svg/gemini-sparkle.svg" width="18" height="18" alt="Gemini">
          <span>⚡ Launch Google GenAI SDK Modal (gemini-4.0-argon)</span>
        </button>
      </div>\n'''
    if 'Launch Google GenAI SDK Modal' not in content:
        content = content.replace('      <div class="gemini-hub-grid">', hero_btn + '      <div class="gemini-hub-grid">')
        print("✓ Injected Launch Button into gemini-studio.html")

    with open(BUILD_PAGES, 'w', encoding='utf-8') as f:
        f.write(content)

def update_index_html():
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add Nav trigger if missing
    nav_studio_trigger = '''            <a href="javascript:void(0)" onclick="openGenAiSdkModal()" class="dropdown-item">
              <div class="dropdown-item-icon">
                <img src="svg/gemini-sparkle.svg" alt="GenAI SDK">
              </div>
              <div class="dropdown-item-content">
                <div class="dropdown-item-title">GenAI SDK Modal <span class="item-badge">gemini-4.0-argon</span></div>
                <div class="dropdown-item-desc">Interactive Python SDK runner &amp; thinking budget</div>
              </div>
            </a>\n'''
    if 'onclick="openGenAiSdkModal()"' not in content:
        content = content.replace('            <a href="whitepaper.html" class="dropdown-item">',
                                  nav_studio_trigger + '            <a href="whitepaper.html" class="dropdown-item">')

    # Add Launch Button in Section 5
    launch_btn = '''        <div style="text-align: center; margin-top: 1.5rem; margin-bottom: 1.5rem;">
          <button class="glass-btn glass-btn-primary" onclick="openGenAiSdkModal()" style="padding: 10px 22px; font-size: 0.9rem;">
            <img src="svg/gemini-sparkle.svg" width="18" height="18" alt="Gemini">
            <span>⚡ Launch Google GenAI SDK Modal (gemini-4.0-argon)</span>
          </button>
        </div>\n'''
    if 'Launch Google GenAI SDK Modal' not in content:
        content = content.replace('      <!-- Dossier Grid Container -->',
                                  launch_btn + '      <!-- Dossier Grid Container -->')

    # Inject Modal before </body>
    if 'id="genai-sdk-modal"' not in content:
        content = content.replace('  <!-- Liquid Glass Footer -->',
                                  GENAI_MODAL_HTML + '\n  <!-- Liquid Glass Footer -->')
        print("✓ Injected genai-sdk-modal into index.html")

    with open(INDEX_HTML, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    update_build_pages()
    update_index_html()
    # Regenerate all pages
    subprocess.run(['python3', 'pipeline/build_pages.py'], check=True)
    subprocess.run(['python3', 'pipeline/generate_learn_page.py'], check=True)
    print("✓ All pages regenerated with Google GenAI SDK Modal!")
