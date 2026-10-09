---
description: Invariants for continuous Google Drive research stocking, in-between document publication, and Google Drive-backed email outreach dispatch
globs: ["omni-automation/**/*.py", "omni-web/**/*.json", "omni-web/**/*.html"]
---

# Omni Sovereign Swarm: Google Drive Research & Outreach Invariants

## 1. Continuous In-Between Research Stocking to Google Drive
- **Proactive In-Between Production**: Research agents (`omni-drive-research-publisher`, `omni-drive-format-converter`, `omni-dossier-synthesizer`) must continuously author full, publication-grade research monographs between outreach batches and during duty cycle ticks.
- **Native Google Docs Upload**: Every newly researched monograph must be created as a native Google Doc via the Docs API and uploaded directly to Google Drive under `Omni Sovereign Swarm Documents/`.
- **Categorized Folder Taxonomy**: Documents must be sorted into their respective specialized subfolders:
  - `01_AI_Supercomputing_and_Foundation_Models/`
  - `02_Cyber_Physical_Robotics_and_Kinematics/`
  - `03_Distributed_Systems_and_CRDT_Lattices/`
  - `04_SCION_Routing_and_Decentralized_Mesh/`
  - `05_Quantum_Photonics_and_Hardware_Engineering/`
  - `06_Synthetic_Biology_and_Epigenomics/`
  - `07_Sovereign_Staking_and_Formal_Audit/`
  - `08_Swarm_Circadian_Protocols_and_Governance/`
- **Shift Stocking Reserve**: Each shift must ensure Google Drive contains an abundant, continuously refreshed backlog of diverse research monographs (minimum 20+ fresh documents per category) so the next shift always has rich, verified material to pull from.

## 2. Next-Shift Google Drive Document Pull & Dynamic Attachment
- **Pull from Real Drive Inventory**: Outreach agents (`omni-drive-inventory-indexer`, `omni-dossier-package-attacher`, `omni-automated-outreach-envoy`) must query the live Google Drive catalog, select actual pre-stocked research documents matching the recipient's institutional domain, and pull the real files for attachment.
- **No Generic or Placeholder Attachments**: Every email dispatch must attach genuine, distinct research documents with formal mathematical proofs, kinematics/algorithmic formulations, and benchmark tables. Never reuse identical files across different institutional domains.
- **RFC 2822 Physical Attachments**: Attach the actual HTML/PDF document bundle directly to the outgoing message so the recipient receives physical files in addition to live Google Drive view links.

## 3. Deep Document Summaries & Bespoke Proposals
- **Exhaustive Email Summaries**: The email body must provide an in-depth, multi-paragraph technical summary of each attached document, detailing:
  - Executive problem formalization and core thesis.
  - Algorithmic and mathematical framework (Euler-Lagrange, closed-form IK, CRDT join-semilattices, etc.).
  - Hardware specifications, safety envelopes, or empirical benchmarks.
  - Direct Google Drive document link for collaborative review.
- **Bespoke Subject Lines & Value Propositions**: Subject lines and opening narratives must be individually customized to the recipient institution (e.g., robotics centers receive manipulator kinematics; networking institutes receive SCION multipath benchmarks).

## 4. Deduplication & Safety Guardrails
- **Zero Duplicate Emails**: Check `contacted_emails_history.json` before every dispatch. Never contact the same institution or email address twice.
- **Commander Exclusion**: The Commander (`rgkdevx1@gmail.com`) must never be added to outreach recipient pools. Commander receives only circadian cycle digests and deployment milestone summaries.
