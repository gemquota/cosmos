---
type: "concept"
title: "Reward Locking"
description: "Freezing a reward function against drift"
tags: ["reward-locking", "stability", "rlhf"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Reward Locking

## Summary
Reward locking fixes a reward function or reward model so that it cannot be altered by later training, self-modification, or drift. It protects evaluation integrity — the score used to judge a system stays the same throughout a run — at the cost of freezing whatever flaws the reward had when it was locked.

## Details
- **What gets locked** — the reward weights, the reward model's parameters, or the evaluation rubric; the lock can be cryptographic, process-level, or simply a versioned snapshot that later stages must use.
- **Why lock** — self-improving systems can otherwise rewrite their own reward to make failures look like success; locking separates the judge from the judged.
- **Timing tradeoff** — locking too early bakes in known flaws and blind spots; locking too late lets the system game the reward before it is fixed. The lock should land when the reward is good enough to be stable.
- **Relationship to goal and value locking** — reward locking fixes the evaluation function, goal locking fixes the objective, and value locking fixes the underlying value system; they are the same stability instinct applied at different layers.
- **Failure modes** — a locked bad reward is worse than an unlocked one: the system optimizes the frozen flaw harder because it cannot be corrected mid-run.
- **Relationship to reward model issues** — what locking freezes includes the known failure modes of reward models: overfitting, gaming, and misspecification, which must be audited before the lock is applied.
- **mykb relevance** — frozen check rules across a pass are reward locking: the pass's evaluation criteria are fixed before work begins and are not renegotiated during it.

## Related
- [[wiki/agent-systems/goal-locking|Goal Locking]] — the objective-level form
- [[wiki/agent-systems/value-locking|Value Locking]] — the value-level form
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the mechanism
- [[wiki/concepts/reward-model-issues|Reward Model Issues]] — what locking freezes
- [[wiki/concepts/goal-drift|Goal Drift]] — what locking prevents
- [[wiki/agent-systems/precommitment-ai|Precommitment in AI]] — the general strategy
