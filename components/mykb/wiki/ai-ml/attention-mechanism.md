---
type: "concept"
title: "Attention Mechanism"
description: "A learned weighting of inputs that lets a model focus on the most relevant parts of its input when producing each output"
tags: ["attention", "transformers", "deep-learning"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Attention Mechanism

## Summary
Attention computes a weighted combination of values, where weights come from the similarity between a query and keys. It lets models route information dynamically — the mechanism that made transformers work.

## Details
- Formula: softmax(QK^T/sqrt(d)) V, with learnable Q, K, V projections.
- Attention is permutation-invariant, which is why positional encodings are required.
- Multi-head attention runs several attention computations in parallel, each capturing different relationships.
- RSIS3 relevance: attention patterns are the object of interpretability work like attention-pattern analysis.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — The architecture attention powers
- [[wiki/ai-ml/self-attention|Self-Attention]] — Attention where query and keys come from the same sequence
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — Parallel attention heads
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — Interpreting what attention learns
- [[wiki/ai-ml/positional-encoding|Positional Encoding]] — Order information for attention
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Why attention cost bounds windows
