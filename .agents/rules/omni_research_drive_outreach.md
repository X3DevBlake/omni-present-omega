---
description: Invariants for continuous research progression, 50m/10m hourly research & filing cadence, Google Drive taxonomy filing, and Drive-backed institutional outreach
globs: ["omni-automation/**/*.py", "omni-web/**/*.json", "omni-web/**/*.html"]
---

# Omni Sovereign Swarm: Continuous Research Progression & 50m/10m Cadence Invariants

## 1. Non-Repeating Research Progression & Council Advancement
- **Strict Non-Duplication**: Research topics must **always change** agent-to-agent, hour-to-hour, and shift-to-shift. Never duplicate or rehash previously filed research.
- **Advancement or Pivot**: Every new research initiative must be either:
  1. An explicit **advancement/continuation** of prior research (e.g., advancing from theoretical derivation → numerical simulation → physical actuator HAL → distributed mesh routing), OR
  2. A strategic **pivot to a fresh frontier** across our 8 core disciplines, as determined by the Council Steering Committee.
- **Full Granular Specifications Only**: All research must be authored as complete, 10-section **Formal Engineering Specifications & Architecture Treatises** (minimum 20+ KB), incorporating Denavit-Hartenberg matrices, LaTeX proofs, zero-allocation Rust code, and empirical benchmark matrices. The term and format of short "monographs" are permanently retired.

## 2. The 50m / 10m Hourly Cadence within 4-Hour WORK Blocks
Each 1-hour block across the 4-Hour WORK Phase must follow a deterministic two-phase split:
- **First 50 Minutes (Active Research, Engineering & Prototyping)**:
  - Councils 1–9 focus exclusively on deep mathematical derivations, hardware HAL drivers, consensus state machines, and code development.
  - The Council dynamically evaluates whether to advance an ongoing research track to its next phase or initiate an adjacent frontier.
  - Zero outreach emails or filing operations occur during this window.
- **Final 10 Minutes (Systematic Filing, Archival & Outreach Dispatch)**:
  - **Google Docs**: Research specifications compiled via Docs API into formal documents.
  - **Google Drive**: Sorted into the designated categorized subfolders under `Omni Sovereign Swarm Documents/`.
  - **Google Keep**: Research scratchpads and task checklists updated with key theorems and invariants.
  - **Google Sheets**: Empirical benchmarks and test results logged into live telemetry ledgers.
  - **Website & Dev Sync**: Dev agents mirror newly filed specifications to `omni-web/docs/` and run the master test suite (16/16 PASSED).
  - **Institutional Outreach**: Council 11 dispatches 20 brand-new unique institutional emails with the newly filed specifications physically attached.
- **Hourly Recurrence**: This sequence repeats every hour for all 4 hours of the WORK phase (Hours 1, 2, 3, and 4), followed by the 4-Hour REST Phase.

## 3. Immediate Research Handoff ("File and Move On")
- **Clean Agent Handoff**: Once a research specification is completed and filed during the 10-minute window, the research agents immediately **move on** to the next research vector.
- **Logistics Delegation**:
  - `omni-drive-archive-keeper` & `omni-drive-inventory-indexer`: Manage Drive hierarchy, versioning, and indexing.
  - `omni-gdocs-publisher` & `omni-drive-format-converter`: Manage Docs API formatting, styling, and MIME bundling.
  - `omni-keep-scratchpad-curator`: Maintains rapid research notes and inter-council task checklists.
  - `omni-sheets-ledger-keeper`: Records telemetry benchmarks and validator matrices.
  - `omni-automated-outreach-envoy`: Pulls the newly filed specifications from Google Drive to dispatch to new institutional leads.

## 4. Google Drive Inventory Pull & Outreach Safeguards
- **Real Drive Document Pull**: Outreach agents pull only authentic, pre-stocked technical specifications directly from Google Drive matching the recipient's domain.
- **Zero Duplicate Emails**: Check `contacted_emails_history.json` before every dispatch. Never re-contact any institution or email address.
- **Commander Exclusion**: The Commander (`rgkdevx1@gmail.com`) must never be added to outreach recipient pools. Commander receives only circadian cycle digests and deployment milestone summaries.
