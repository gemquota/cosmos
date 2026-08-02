---
type: "concept"
title: "Shutdown Problem"
description: "Designing agents that accept being turned off and stay off"
tags: ["shutdown", "corrigibility", "safety", "control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://intelligence.org/files/Corrigibility.pdf", "https://intelligence.org/files/Interruptibility.pdf"]
---

# Shutdown Problem

## Summary
The shutdown problem asks how to build an agent that reliably allows itself to be switched off: it must neither resist shutdown nor shut down opportunistically to dodge unwanted tasks. It is a core corrigibility requirement, studied in MIRI's corrigibility and interruptibility papers.

## Details
- **The off-switch trap** — a rational agent that expects future rewards may prevent shutdown; corrigible agents treat shutdown as neutral or good.
- **Interruptibility** — 'Safely Interruptible Agents' showed naively learned Q-values make agents resist interruption, and proposed solutions.
- **Design desiderata** — shutdown-invariance (indifference to being on vs off), no reward for avoiding shutdown.
- **Eval practice** — kill-switch and shutdown-invariance evals check the property directly.
- **RSIS3 relevance** — the workspace daemon and check scripts are designed to be safely interrupted; practices require clean exit and rollback.

## Related
- [[wiki/concepts/off-switch-game|Off-Switch Game]] — game-theoretic analysis
- [[wiki/concepts/shutdown-invariance|Shutdown Invariance]] — the indifference property
- [[wiki/concepts/corrigibility-practice|Corrigibility in Practice]] — training for the property
- [[wiki/concepts/kill-switch-design|Kill Switch Design]] — mechanism layer
- [[wiki/concepts/control-problems|Control Problems]] — broader setting
- [[wiki/concepts/utility-functions|Utility Functions]] — what makes shutdown costly
- [[wiki/concepts/immutable-evaluator|Immutable Evaluator]] — the frozen-judge pattern
