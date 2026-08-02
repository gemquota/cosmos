---
type: "concept"
title: "Autotuning"
description: "Automatic search for optimal configuration parameters"
tags: ["autotuning", "optimization", "systems", "ml"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Autotuning", "https://en.wikipedia.org/wiki/Hyperparameter_optimization"]
---

# Autotuning

## Summary
Autotuning is the automatic search for configuration parameters — compiler flags, kernel block sizes, hyperparameters — that optimize a performance or quality metric. It turns tuning from an expert activity into a closed-loop search, often using Bayesian optimization or random search.

## Details
- **Scope** — compiler optimization flags, database knobs, ML hyperparameters, and scheduling policies.
- **Methods** — grid/random search, Bayesian optimization, bandit algorithms, and learning-based predictors.
- **Why it matters for RSI** — a system that tunes itself removes a human bottleneck from the improvement loop.
- **Risks** — tuning to a proxy metric (Goodhart), overfitting to benchmark inputs, and instability after deployment.
- **RSIS3 parallel** — meta-parameter tuning and tuning-ownership-diagonal are the triad's autotuning layer.

## Related
- [[wiki/concepts/hyperparameter-self-optimization|Hyperparameter Self-Optimization]] — the self-directed form
- [[wiki/concepts/meta-learning-for-agents|Meta-Learning for Agents]] — learning the tuner
- [[wiki/pulses/improvement-metrics|Improvement Metrics]] — what autotuning optimizes
- [[wiki/concepts/eval-contamination|Eval Contamination]] — overfit to the metric
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — RSIS3 tuning layer
- [[wiki/concepts/tuning-ownership-diagonal|Tuning Ownership Diagonal]] — tuning ownership
