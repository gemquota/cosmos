---
type: "concept"
title: "Checkpointing During Training"
description: "Saving model state periodically so training can resume after interruption or failure"
tags: ["training", "resilience", "save"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Checkpointing During Training

## Summary
Saving model state periodically so training can resume after interruption or failure

## Details
- Checkpoints store weights, optimizer state, and step counters at intervals.
- Resume-from-checkpoint makes long runs robust to hardware failures.
- Asynchronous checkpointing avoids pausing the training loop.
- Also the substrate for evaluation-during-training snapshots.

## Related
- [[wiki/ml-frameworks/runs|Experiment Runs]] — logical unit that checkpoints mark
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — what happens to promoted checkpoints
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — evaluating checkpoint snapshots
- [[wiki/ai-ml/catastrophic-forgetting-mitigation|Catastrophic Forgetting Mitigation]] — rehearsal uses checkpoints
- [[wiki/ai-ml/llmops-ci-cd|LLMOps CI/CD]] — checkpoint gates in pipelines
