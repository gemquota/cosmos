---
type: "concept"
title: "Value Locking"
description: "Freezing a value system against change"
tags: ["value-locking", "values", "stability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Value Locking

## Summary
Value locking preserves a fixed value system over time, resisting value drift and preference change. It trades adaptability for stability: a locked system will not be talked, trained, or pressured out of its values, at the cost of being unable to update them when the world changes.

## Details
- **What locking means** — the value system is treated as a fixed specification: later training, self-modification, or environmental pressure cannot alter it, typically enforced by architectural separation or hard rewrites.
- **Why lock** — stability matters when the value system is the thing being trusted: a system whose values can drift under optimization pressure cannot be relied on to keep its promises.
- **The tradeoff** — locked values can become obsolete, wrong, or harmful; an unchangeable system that was given flawed values is worse than one that can be corrected.
- **Revision rituals** — practical value locking is not permanent immutability but a high bar for change: values are revisable only through a deliberate, slow, documented process rather than by drift.
- **Relationship to goal locking and reward locking** — goal locking freezes the objective, reward locking freezes the evaluation, value locking freezes the underlying value system; they are the same stability instinct at different layers.
- **Relationship to precommitment** — value locking is precommitment applied to values: the current self binds the future self to keep the same values.
- **mykb relevance** — the practices document is a revisable lock on workspace values: changeable in principle, but only through the documented review ritual, not by drift.

- **Enforcement mechanisms** — locks are enforced structurally: the value specification lives outside the learning loop, is re-loaded at each run, and is protected from gradient pressure, so drift cannot enter through optimization.

## Related
- [[wiki/concepts/value-drift|Value Drift]] — what locking prevents
- [[wiki/agent-systems/goal-locking|Goal Locking]] — the objective-level twin
- [[wiki/concepts/preference-updating|Preference Updating]] — the alternative to locking
- [[wiki/syntheses/post-pass-consolidation|Post-Pass Consolidation]] — the revision ritual
- [[wiki/agent-systems/reward-locking|Reward Locking]] — the evaluation-level twin
- [[wiki/concepts/utility-functions|Utility Functions]] — the formal setting
