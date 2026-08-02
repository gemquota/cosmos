---
type: "concept"
title: "Weight Decay"
description: "Penalizing large weights during training"
tags: ["weight-decay", "regularization", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Weight Decay

## Summary
Weight decay adds a penalty proportional to weight magnitude, biasing toward small weights.

## Details
- Weight decay adds a penalty proportional to weight magnitude, biasing toward small weights.
- In AdamW it is decoupled from learning rate and is standard in LLM training.
- It interacts with grokking and generalization in subtle ways.
- RSIS3 relevance: small, focused links play weight-decay's role in the graph.

## Related
- [[wiki/concepts/regularization-practice|Regularization in Practice]] — the family
- [[wiki/concepts/grokking|Grokking]] — weight decay's role
- [[wiki/concepts/double-descent|Double Descent]] — the curve context
- [[wiki/concepts/overfitting-llm|Overfitting in LLMs]] — what it curbs
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — existing graph context
