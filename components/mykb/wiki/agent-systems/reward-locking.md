---
type: "concept"
title: "Reward Locking"
description: "Freezing a reward function against drift"
tags: ["reward-locking", "stability", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Reward Locking

## Summary
Reward locking fixes a reward function or model so it cannot be altered by later training or self-modification.

## Details
- Reward locking fixes a reward function or model so it cannot be altered by later training or self-modification.
- It prevents reward drift and protects evaluation integrity.
- Locking too early bakes in flaws; too late allows gaming.
- RSIS3 relevance: frozen check rules across a pass are reward locking.

## Related
- [[wiki/agent-systems/goal-locking|Goal Locking]] — the goal form
- [[wiki/agent-systems/value-locking|Value Locking]] — the value form
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the mechanism
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — what locking freezes
- [[wiki/concepts/goal-drift|Goal Drift]] — the full treatment of this theme
