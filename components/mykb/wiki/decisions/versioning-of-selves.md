---
type: "decision"
title: "Versioning of Selves"
description: "Tracking identity and continuity across successive self-modifications"
tags: ["versioning", "identity", "self-modification", "continuity"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Personal_identity", "https://en.wikipedia.org/wiki/Self"]
---

# Versioning of Selves

## Summary
Versioning of selves treats a self-improving system's successive states as versions: each edit produces a new version whose identity, goals, and guarantees can be compared with the old. Explicit versioning makes rollback, audit, and value-continuity checks possible.

## Details
- **Mechanism** — every accepted modification bumps a version; identity snapshots record goals, values, and state.
- **Why needed** — without versioning, 'which self are we talking to' becomes ambiguous and rollback targets disappear.
- **Continuity question** — is the new version the same agent with new skills, or a different agent? Personal-identity debates apply.
- **Operational form** — RSIS3's git-based checkpoints and VERSION files are versioning of the workspace self.
- **Safety use** — audits diff consecutive versions for goal drift and unexpected capability changes.

## Related
- [[wiki/agent-systems/self-modeling|Self-Modeling]] — the model that persists across versions
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — theoretical framing
- [[wiki/decisions/memory-surgery|Memory Surgery]] — what a version may edit
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — the rollback counterpart
- [[wiki/concepts/value-drift|Value Drift]] — what version diffs should catch
- [[wiki/agent-systems/identity-and-continuity|Identity and Continuity]] — RSIS3 identity
- [[wiki/agent-systems/goal-locking|Goal Locking]] — locking goals
- [[wiki/agent-systems/value-locking|Value Locking]] — locking values
