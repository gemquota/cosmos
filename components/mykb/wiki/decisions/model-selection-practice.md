---
type: "concept"
title: "Model Selection in Practice"
description: "How teams choose models for deployment"
tags: ["model-selection", "practice", "deployment"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Model Selection in Practice

## Summary
Model selection weighs validation performance, robustness, cost, and safety properties.

## Details
- Model selection weighs validation performance, robustness, cost, and safety properties.
- Good practice holds out clean test sets and re-checks on deployment-like data.
- Selection metrics become targets; contamination risk follows.
- RSIS3 relevance: the bundle selects which generated content to consolidate, a model-selection act.

## Related
- [[wiki/decisions/eval-splits|Eval Splits]] — the data hygiene
- [[wiki/decisions/checkpoint-selection|Checkpoint Selection]] — the timing side
- [[wiki/concepts/benchmark-contamination|Benchmark Contamination]] — the risk
- [[wiki/decisions/test-set-discipline|Test Set Discipline]] — the discipline
- [[wiki/concepts/automated-machine-learning|Automated Machine Learning (AutoML)]] — the full treatment of this theme
- [[wiki/ai-ml/model-selection-strategies|Model Selection Strategies]] — existing graph context
