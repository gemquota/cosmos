---
type: "decision"
title: "Auto-Update Mechanisms"
description: "Systems that update themselves in production"
tags: ["auto-update", "self-maintenance", "systems", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Package_manager", "https://en.wikipedia.org/wiki/Rollback_(data_management)"]
---

# Auto-Update Mechanisms

## Summary
Auto-update mechanisms let software fetch, validate, and apply its own updates — package managers, over-the-air updates, and agent self-patches. They are mundane today, yet they are exactly the machinery a recursively self-improving system generalizes, including all its failure modes.

## Details
- **Components** — update source (registry), authenticity checks (signatures), staged application, and rollback.
- **Safety properties** — updates must be authenticated, reproducible, and reversible; broken updates must not brick the system.
- **Agent dimension** — an agent updating its own code merges auto-update with self-modification; governance gates apply.
- **Supply-chain exposure** — update channels are prime attack surface (dependency attacks, compromised registries).
- **RSIS3 relevance** — git-pulled knowledge passes and checkpointed state are auto-update with explicit review steps.

## Related
- [[wiki/concepts/supply-chain-attacks-ai|Supply-Chain Attacks on AI]] — the attack surface
- [[wiki/syntheses/patch-management-ai|Patch Management for AI]] — the operational layer
- [[wiki/syntheses/model-updates-risks|Model Update Risks]] — AI-specific update risk
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — reversibility
- [[wiki/decisions/self-hosting|Self-Hosting]] — who builds the update
- [[wiki/agent-systems/rollback-and-recovery|Rollback and Recovery]] — rollback practice
