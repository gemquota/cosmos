---
type: "concept"
title: "W&B and Experiment Tracking"
description: "Platforms that log metrics, artifacts, and hyperparameters for training experiments"
tags: ["tracking", "experiments", "mlops"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# W&B and Experiment Tracking

## Summary
Platforms that log metrics, artifacts, and hyperparameters for training experiments

## Details
- Weights and Biases (W&B) and similar tools centralize run metadata and charts.
- Teams compare sweeps, share dashboards, and link code to results.
- Integration is usually a few lines in the training script.
- Tracking discipline is the backbone of reproducible fine-tuning.

## Related
- [[wiki/ml-frameworks/runs|Experiment Runs]] — the unit being tracked
- [[wiki/ml-frameworks/mlflow-model-registry|MLflow Model Registry]] — artifact-focused alternative
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — metrics that get logged
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — tracking integrated into pipelines
- [[wiki/ai-ml/model-monitoring|Model Monitoring]] — production monitoring analog
