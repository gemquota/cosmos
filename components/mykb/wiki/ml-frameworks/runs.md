---
type: "concept"
title: "Training Runs"
description: "A single execution of a training or fine-tuning job tracked with config, metrics, and artifacts"
tags: ["experiment", "tracking", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Training Runs

## Summary
A single execution of a training or fine-tuning job tracked with config, metrics, and artifacts

## Details
- A run bundles hyperparameters, code version, dataset snapshot, and logged metrics.
- Run comparison is how teams decide between configs and seeds.
- Good run hygiene makes results reproducible and auditable.
- Tools like W&B, MLflow, and TensorBoard organize runs.

## Related
- [[wiki/ml-frameworks/wandb-and-experiment-tracking|Weights & Biases and Experiment Tracking]] — tooling that stores runs
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — metrics recorded per run
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — outputs promoted from runs
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — run orchestration in pipelines
- [[wiki/prompt-engineering/prompt-versioning|Prompt Versioning]] — parallel concept for prompts
