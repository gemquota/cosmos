---
type: "concept"
title: "Learning to Learn"
description: "Meta-learning: improving the learner itself across tasks, so each task gets faster — the goal of the loop stack"
tags: [meta-learning, rsis3, transfer, adaptation, learning]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Learning to Learn

## Summary
Learning to learn (meta-learning) is the process of improving the learning procedure itself: across many tasks, the system extracts what made adaptation fast and encodes it as better initial conditions, better hyperparameters, or better update rules. It is the goal of a self-improving system — not just solving tasks, but getting better at solving tasks. RSIS3's loop stack is this idea made operational: sessions solve tasks (L1–L3), tuning loops improve how sessions run (L4–L6), and meta-tuners improve the tuners (L7–L9).

## Details
- **Three classic strategies**: learning better initializations, learning better update rules, and learning better hyperparameters — RSIS3's registry tuning is the third.
- **Transfer vs. meta-learning**: transfer reuses knowledge; meta-learning reuses the *procedure*. The strategy population (L5) is a procedure store.
- **Signal requirement**: meta-learning needs a distribution of tasks and a scalar outcome per task — outcome telemetry is that signal.
- **Failure mode**: overfitting to the task distribution (fixing one benchmark) is the meta-level analogue of memorizing a dataset; stagnation detection (L8) counters it.
- Design rule: separate the timescales — never let a task-level decision tune the meta-level directly.

## Related
- [[wiki/concepts/inner-outer-loop-learning|Inner/Outer Loop Learning]] — the structure that realizes it
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — hyperparameter meta-learning in practice
- [[wiki/meta-learning/transfer-learning|Transfer Learning]] — the cousin that reuses knowledge
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — the system built to do this