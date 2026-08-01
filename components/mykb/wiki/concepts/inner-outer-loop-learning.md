---
type: "concept"
title: "Inner/Outer Loop Learning"
description: "Two nested optimization loops — a fast inner learner and a slow outer updater — the shape of RSIS3's stack"
tags: [meta-learning, inner-loop, outer-loop, rsis3, bilevel]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Inner/Outer Loop Learning

## Summary
Inner/outer loop learning is the bilevel structure where a fast inner loop solves a task while a slow outer loop updates the parameters that shape the inner loop. It is the canonical shape of meta-learning ("learning to learn") and, at the system level, the shape of RSIS3: L1–L3 execute work in a session, L4–L6 tune their parameters between sessions, and L7–L9 tune the tuners.

## Details
- **Inner loop**: fast, high-frequency, task-specific (L1 tool calls, L2 improvement attempts, L3 consolidation).
- **Outer loop**: slow, low-frequency, updates the inner loop's hyperparameters (L4–L6) and their thresholds (L7–L9).
- **Separation of timescales**: inner loops run per-task/per-session (seconds–hours); outer loops run per-N-sessions (hours–days); meta-tuners run on oscillation/stagnation events.
- **Signal flow**: the outer loop needs a scalar performance signal from the inner loop's outcomes — RSIS3's success-rate and fitness history.
- Design rule: keep the inner loop pure of outer-loop bookkeeping; telemetry is the only channel between them.

## Related
- [[wiki/concepts/learning-to-learn|Learning to Learn]] — the meta-learning framing
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — the outer loop's mechanism
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — the concrete stack
- [[wiki/concepts/population-based-evolution|Population-Based Evolution]] — a slow outer loop over strategies