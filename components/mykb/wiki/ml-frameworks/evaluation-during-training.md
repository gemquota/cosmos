---
type: "concept"
title: "Evaluation During Training"
description: "Running held-out evaluations on checkpoints while training is still in progress"
tags: ["evaluation", "training", "monitoring"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Evaluation During Training

## Summary
Running held-out evaluations on checkpoints while training is still in progress

## Details
- Periodic eval on validation sets catches overfitting and divergence early.
- Loss curves plus task metrics together guide early stopping and LR schedules.
- Eval frequency trades wall-clock time against signal density.
- Snapshot evals feed model registries and comparison dashboards.

## Related
- [[wiki/ml-frameworks/runs|Experiment Runs]] — eval results attach to runs
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — checkpoints are eval points
- [[wiki/ai-ml/model-monitoring|Model Monitoring]] — production analog of training evals
- [[wiki/testing/evals-harness|Evals Harness]] — tooling for systematic evaluation
- [[wiki/testing/llm-regression-testing|LLM Regression Testing]] — catches regressions across runs
