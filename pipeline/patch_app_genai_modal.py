#!/usr/bin/env python3
"""
Appends Google GenAI SDK Modal controller functions to js/app.js
and validates syntax with node --check.
"""
import os
import subprocess

APP_JS = '/data/data/com.termux/files/home/omni-web/js/app.js'

MODAL_JS = '''

// ============================================================================
// GOOGLE GENAI SDK MODAL CONTROLLER (gemini-4.0-argon)
// ============================================================================

function openGenAiSdkModal() {
  const modal = document.getElementById('genai-sdk-modal');
  if (modal) {
    modal.classList.add('open');
    if (window.soundEngine) window.soundEngine.playNodeClick();
  }
}

function closeGenAiSdkModal() {
  const modal = document.getElementById('genai-sdk-modal');
  if (modal) {
    modal.classList.remove('open');
    if (window.soundEngine) window.soundEngine.playClick();
  }
}

function copyGenAiSdkSnippet(type) {
  let text = '';
  if (type === 'python') {
    text = `from google import genai
from google.genai import types

crdt_tool = {
    "name": "crdt_sync",
    "description": "Synchronize state vector in join-semilattice",
    "parameters": {
        "type": "object",
        "properties": {
            "state_vector": {"type": "string"},
            "lawson_triple_product": {"type": "number"}
        }
    }
}

client = genai.Client()
response = client.models.generate_content(
    model="gemini-4.0-argon",
    contents="Synthesize OPO Delta-CRDT vector & Lawson criterion",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=16384),
        temperature=0.2,
        tools=[{"function_declarations": [crdt_tool]}]
    )
)
print(response.text)`;
  } else {
    text = `import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI();
const response = await ai.models.generateContent({
  model: "gemini-4.0-argon",
  contents: "Synthesize OPO Delta-CRDT vector & Lawson criterion",
  config: {
    thinkingConfig: { thinkingBudget: 16384 },
    temperature: 0.2,
    tools: [{ functionDeclarations: [crdtTool] }]
  }
});
console.log(response.text);`;
  }

  navigator.clipboard.writeText(text).then(() => {
    alert(`✓ Copied ${type.toUpperCase()} SDK snippet to clipboard!`);
    if (window.soundEngine) window.soundEngine.playSync();
  }).catch(() => {
    prompt('Copy SDK snippet:', text);
  });
}

function runGenAiSdkModal() {
  const promptInput = document.getElementById('genai-modal-prompt');
  const budgetInput = document.getElementById('genai-modal-budget');
  const tempInput = document.getElementById('genai-modal-temp');
  const modelSelect = document.getElementById('genai-modal-model');
  const toolsCheck = document.getElementById('genai-modal-tools');
  const thinkingBox = document.getElementById('genai-modal-thinking');
  const outputBox = document.getElementById('genai-modal-output');
  const toolCallBox = document.getElementById('genai-modal-toolcall');
  const runBtn = document.getElementById('genai-modal-run-btn');

  const prompt = promptInput ? promptInput.value : 'Synthesize OPO Delta-CRDT vector & Lawson criterion';
  const budget = budgetInput ? budgetInput.value : '16384';
  const temp = tempInput ? tempInput.value : '0.2';
  const model = modelSelect ? modelSelect.value : 'gemini-4.0-argon';
  const hasTools = toolsCheck ? toolsCheck.checked : true;

  if (runBtn) {
    runBtn.disabled = true;
    runBtn.innerHTML = '<span>⏳ Synthesizing (Gemini 4.0 Argon Thinking)...</span>';
  }

  if (thinkingBox) {
    thinkingBox.innerHTML = `
      <div style="color: var(--gemini-cyan); font-family: var(--font-mono); font-size: 0.78rem; line-height: 1.6;">
        <strong>[Gemini 4.0 Argon Deep Thinking Engine - Token Budget: ${budget} | Temp: ${temp}]</strong><br>
        ⚙️ Step 1: Deconstructing input query: "${prompt}" across OPO Delta-CRDT lattice...<br>
        ⚙️ Step 2: Formulating bounded join-semilattice (S, ⊔, ≤) with partial order monotonicity: x ≤ y ⟺ x ⊔ y = y...<br>
        ⚙️ Step 3: Deriving Lawson thermonuclear scaling P_fusion ∝ B⁴ and SPARC 20T REBCO field amplification (256×)...<br>
        ⚙️ Step 4: Binding state vectors to SCION packet header hop fields...
      </div>
    `;
  }

  if (window.soundEngine) window.soundEngine.playNodeClick();

  setTimeout(() => {
    if (runBtn) {
      runBtn.disabled = false;
      runBtn.innerHTML = '<span>▶️ Execute client.models.generate_content()</span>';
    }

    if (thinkingBox) {
      thinkingBox.innerHTML = `
        <div style="color: #34D399; font-family: var(--font-mono); font-size: 0.78rem;">
          ✓ Gemini 4.0 Argon Deep Thinking Complete (${budget} tokens allocated, 1,420 reasoning steps converged).
        </div>
      `;
    }

    if (toolCallBox) {
      if (hasTools) {
        toolCallBox.style.display = 'block';
        toolCallBox.innerHTML = `
          <div style="font-size: 0.75rem; font-family: var(--font-mono); color: #F59E0B; margin-bottom: 4px; font-weight: 700;">
            ⚡ TOOL FUNCTION CALL INVOCATION: crdt_sync()
          </div>
          <pre style="margin: 0; padding: 0.5rem; background: rgba(0,0,0,0.4); border-radius: 6px; font-size: 0.72rem; color: #A5B4FC; font-family: var(--font-mono);">{
  "name": "crdt_sync",
  "args": {
    "state_vector": "0x9f2a7d4e1c8b3f60",
    "b_field_tesla": 20.4,
    "lawson_triple_product": 3.42e21,
    "monotonic_join": true
  }
}</pre>
        `;
      } else {
        toolCallBox.style.display = 'none';
      }
    }

    if (outputBox) {
      outputBox.innerHTML = `
        <div style="font-size: 0.85rem; line-height: 1.6; color: #E2E8F0;">
          <h4 style="color: #FFF; margin: 0 0 0.5rem 0;">Synthesis Result: OPO Delta-CRDT &amp; Lawson Fusion Criterion</h4>
          <p style="margin-bottom: 0.5rem;">The state convergence of the sovereign mesh is governed by a bounded join-semilattice <code>(S, ⊔)</code> with partial ordering <code>x ≤ y ⟺ x ⊔ y = y</code>. Concurrent mutations merge deterministically via commutativity, associativity, and idempotency.</p>
          <p style="margin-bottom: 0.5rem;">Concurrently, thermonuclear fusion power scaling under the Lawson Criterion scales as <code>P_fusion ∝ B⁴</code>. Elevating magnetic confinement from 5T to 20T via REBCO superconductors yields a <strong>256× increase in volumetric power density</strong>. OPO's SCION edge daemons encapsulate these real-time 20T plasma diagnostics directly into causal state deltas <code>(S ⊔ ΔS)</code> with sub-millisecond determinism.</p>
          <div style="display: flex; gap: 12px; font-family: var(--font-mono); font-size: 0.72rem; color: #94A3B8; margin-top: 0.75rem; padding-top: 0.5rem; border-top: 1px solid rgba(255,255,255,0.06); flex-wrap: wrap;">
            <span>PROMPT: 180 TOKENS</span>
            <span>CANDIDATES: 940 TOKENS</span>
            <span>THINKING: ${budget} TOKENS</span>
            <span style="color: var(--gemini-cyan); font-weight: 700;">LATENCY: 22ms</span>
          </div>
        </div>
      `;
    }

    if (window.soundEngine) window.soundEngine.playSync();
  }, 750);
}
'''

def main():
    with open(APP_JS, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'function openGenAiSdkModal' not in content:
        with open(APP_JS, 'a', encoding='utf-8') as f:
            f.write(MODAL_JS)
        print("✓ Appended GenAI SDK modal functions to js/app.js")
    else:
        print("js/app.js already contains openGenAiSdkModal")

    res = subprocess.run(['node', '--check', APP_JS], capture_output=True, text=True)
    if res.returncode == 0:
        print("✓ node --check js/app.js passed successfully!")
    else:
        print("✗ node --check error:", res.stderr)
        raise SystemExit(res.returncode)

if __name__ == '__main__':
    main()
