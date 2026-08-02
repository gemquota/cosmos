---
type: "concept"
title: "Grokking"
description: "Delayed generalization where models memorize first, then suddenly generalize"
tags: ["grokking", "generalization", "mechanistic-interpretability", "dl"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2201.02177", "https://en.wikipedia.org/wiki/Grokking_(machine_learning)"]
---

# Grokking

## Summary
Grokking is the phenomenon where a small transformer trained past overfitting suddenly transitions to perfect generalization, sometimes long after training error is zero. Discovered on modular arithmetic tasks in 2022, it is studied as a window into how networks form generalizing circuits.

## Details
- **Signature** — long plateau of memorization, then a sharp phase transition to clean generalization.
- **Mechanistic account** — the network slowly discovers a periodic/algorithmic circuit that replaces memorized lookups.
- **Research value** — grokking is a controlled setting for studying circuit formation, weight decay's role, and the transition from memorization to understanding.
- **Safety relevance** — generalization that arrives late complicates early capability detection.
- **Parallel** — RSIS3's own slow consolidation: knowledge is memorized (captured) before it is structurally linked (grokked).

## Related
- [[wiki/concepts/memorization-vs-generalization|Memorization vs Generalization]] — the transition grokking studies
- [[wiki/concepts/induction-heads|Induction Heads]] — a circuit implicated in grokked models
- [[wiki/concepts/circuit-analysis|Circuit Analysis]] — toolkit for the transition
- [[wiki/concepts/double-descent|Double Descent]] — another non-monotonic curve
- [[wiki/concepts/regularization-practice|Regularization in Practice]] — weight decay's role
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — scaling context in the existing graph
- [[wiki/concepts/calibration|Calibration]] — measurement honesty in the existing graph
