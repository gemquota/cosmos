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
Attention computes a weighted combination of values, with weights derived from the similarity between a query and a set of keys. It lets each output position look directly at any input position, sidestepping the distance problem of recurrent networks and giving an O(1) path length between any pair of positions — the mechanism that made transformers work.

## Details
- **Formula** — attention is softmax(QK^T/sqrt(d))V, with learnable Q, K, V projections; the scaling by sqrt(d) keeps the softmax from saturating as the dimension grows.
- **Permutation invariance** — attention itself is indifferent to order, which is why positional encodings are required to give the model sequence information.
- **Multi-head attention** — several attention computations run in parallel, each capturing different relationships (syntactic, positional, semantic), and their outputs are concatenated and projected.
- **Differentiability** — the softmax weighting is differentiable end-to-end, so attention trains cleanly in deep stacks alongside the rest of the network.
- **Cost** — attention is quadratic in sequence length, which motivates sparse patterns, sliding windows, and linear approximations for long contexts.
- **Worked example** — in retrieval, the query is the user question, keys are candidate chunks, and attention weights rank which chunks the answer should draw from; the same mechanics reappear in cross-attention for generation.
- **Interpretability** — attention patterns are studied as evidence of what the model routes between positions, though pattern analysis is descriptive rather than a complete explanation of behavior.

- **Training dynamics** — attention heads specialize during training, with some heads capturing positional or syntactic regularities and others long-range content; pruning and head analysis rely on this structure.
## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — the model family built on attention
- [[wiki/ai-ml/self-attention|Self-Attention]] — attention within one sequence
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — parallel attention heads
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — interpretability view
- [[wiki/ai-ml/positional-encoding|Positional Encoding]] — ordering information
- [[wiki/prompt-engineering/context-windows|Context Windows]] — length limits attention must fit
- [[wiki/ml-frameworks/flash-attention|Flash Attention]] — efficient attention kernels
