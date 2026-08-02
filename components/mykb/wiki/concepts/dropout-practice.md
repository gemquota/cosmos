---
type: "concept"
title: "Dropout in Practice"
description: "Randomly dropping units during training to reduce overfitting"
tags: ["dropout", "regularization", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dropout in Practice

## Summary
Dropout zeroes random units per training step, forcing the network to learn redundant, robust features.

## Details
- Dropout zeroes random units per training step, forcing the network to learn redundant, robust features.
- It was transformative for feedforward nets; transformer training often uses variants or none.
- Its effectiveness varies with scale and architecture.
- RSIS3 relevance: random-link sampling in graph training plays a dropout-like role.

## Related
- [[wiki/concepts/regularization-practice|Regularization in Practice]] — the family
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — the target
- [[wiki/concepts/reward-ensemble|reward-ensemble]] — note
- [[wiki/concepts/weight-decay|Weight Decay]] — the modern default
- [[wiki/concepts/grokking|Grokking]] — the full treatment of this theme
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — existing graph context
