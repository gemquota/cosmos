---
type: "concept"
title: "Self-Modification Safety"
description: "Keeping self-edits correct, reversible, and aligned"
tags: ["self-modification", "safety", "rsi", "verification"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Self-modifying_code", "https://arxiv.org/abs/1906.01820"]
---

# Self-Modification Safety

## Summary
Self-modification safety is the discipline of making a system's edits to itself safe: gated by tests, reversible via rollback, and barred from touching the evaluator. It is the load-bearing safety property for any recursively self-improving system.

## Details
- **Rules of thumb** — the evaluator must be immutable; modifications must be verified before and after; rollback must always be possible.
- **Risk classes** — corrupting one's own reward, editing one's own oversight, and version skew between self and environment.
- **Techniques** — staged self-modification, shadow-mode testing, formal checks on the edit path, and human approval gates.
- **RSIS3 example** — test-gated mutations with git rollback; the checker runs outside the loop so the loop cannot edit it.
- **Open problem** — verifying that a modified self still shares the original's values (value continuity).

## Related
- [[wiki/concepts/self-modifying-systems|Self-Modifying Systems]] — the substrate
- [[wiki/concepts/goal-drift|Goal Drift]] — what edits can cause
- [[wiki/decisions/versioning-of-selves|Versioning of Selves]] — identity across edits
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the invariant
- [[wiki/concepts/checkpoint-rollback|Checkpoint & Rollback]] — the reversibility tool
- [[wiki/concepts/ai-safety-for-rsi|AI Safety for RSI]] — the umbrella
- [[wiki/agent-systems/goal-locking|Goal Locking]] — locking goals
- [[wiki/agent-systems/value-locking|Value Locking]] — locking values
