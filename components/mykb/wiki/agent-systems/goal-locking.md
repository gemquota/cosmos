---
type: "concept"
title: "Goal Locking"
description: "Freezing an agent's goals against modification"
tags: ["goal-locking", "goals", "stability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Goal Locking

## Summary
Goal locking prevents an agent's goals from being altered by its own actions or by updates to its weights or prompts. It protects against goal drift in self-improving systems, where a system that can rewrite its own objectives may optimize for something its operators never approved.

## Details
- **What is locked** — the high-level objective, its priority ordering, and the constraints around it; implementation details below the locked level remain free to change.
- **Why it matters for self-improvement** — a self-improving system that can edit its own goals is optimizing under a moving target; locking separates "improve how you pursue the goal" from "change the goal."
- **Mechanisms** — goals live outside the modifiable surface (read-only identity files, hashed and checked at startup), and any proposed goal change goes through an external approval path.
- **Governance questions** — locking raises the question of who fixes the goals and who may update them, and under what evidence; a lock with no update path is brittle, one with a trivial update path is theater.
- **Relationship to reward and value locking** — reward locking freezes the reward signal, value locking freezes the value function; goal locking is the same discipline applied to the objective statement itself.
- **RSIS3 relevance** — the identity system's stated purpose is the bundle's goal lock: the operating objective is recorded and change is gated, not free-form.
- **Pathological extreme** — lobotomized optimizers show the failure of over-locking: freezing every aspect of optimization leaves no capacity to improve; the lock must cover goals, not all behavior.

- **Hash-and-verify** — the locked goal file is hashed and verified at startup and before any self-modifying step, so an unauthorized change to the objective is detected rather than silently accepted.
## Related
- [[wiki/agent-systems/reward-locking|Reward Locking]] — the reward form
- [[wiki/concepts/goal-drift|Goal Drift]] — what locking prevents
- [[wiki/agent-systems/value-locking|Value Locking]] — the value form
- [[wiki/agent-systems/lobotomized-optimizers|Lobotomized Optimizers]] — the pathological extreme
- [[wiki/agent-systems/precommitment-ai|Precommitment in AI]] — binding future behavior
- [[wiki/concepts/utility-functions|Utility Functions]] — the objective formalism
