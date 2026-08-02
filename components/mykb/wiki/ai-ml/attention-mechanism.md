---
type: "concept"
title: "Attention Mechanism"
description: "A learned weighting of inputs that lets a model focus on the most relevant parts of its input when producing each output"
tags: ["attention", "transformers", "deep-learning"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Attention_(machine_learning)", "https://arxiv.org/abs/1706.03762"]
---

# Attention Mechanism

## Summary
Attention computes a weighted combination of values, where weights come from the similarity between a query and keys. It lets models route information dynamically — the mechanism that made transformers work.

## Details
- Formula: softmax(QK^T/sqrt(d)) V, with learnable Q, K, V projections.
- Attention is permutation-invariant, which is why positional encodings are required.
- Multi-head attention runs several attention computations in parallel, each capturing different relationships.
- RSIS3 relevance: attention patterns are the object of interpretability work like attention-pattern analysis.
- Attention computes a weighted combination of values, with weights derived from the similarity between a query and a set of keys.
- It lets each output position directly look at any input position, sidestepping the distance problem of recurrent networks and giving O(1) path length between any pair of positions.
- The softmax weighting makes attention differentiable end-to-end, which is why it trains cleanly in deep stacks.
- Attention's cost is quadratic in sequence length, which motivates sparsity, sliding windows, and linear approximations for long contexts.
- **Worked example / comparison** — Worked example — in retrieval, the query is the user question, keys are candidate chunks, and attention weights rank which chunks the answer should draw from.
- For mykb, attention is documented alongside the agent-systems cluster because RSIS3's planner uses attention-like ranking when choosing which memories to load.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/ai-ml/self-attention|Self-Attention]]
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]]
- [[wiki/ai-ml/attention-patterns|Attention Patterns]]
- [[wiki/ai-ml/positional-encoding|Positional Encoding]]
- [[wiki/prompt-engineering/context-windows|Context Windows]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/explainers|Explainers]]
