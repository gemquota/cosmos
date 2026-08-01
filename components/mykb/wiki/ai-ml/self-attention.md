---
type: "concept"
title: "Self-Attention"
description: "Attention computed over a sequence against itself, letting every token attend to every other token"
tags: ["self-attention", "transformers", "attention"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Self-Attention

## Summary
Self-attention lets each token in a sequence look at all other tokens, computing context-aware representations. It is the distinguishing operation of transformer blocks and the source of their long-range modelling power.

## Details
- Each position produces a query, key, and value; attention weights reflect inter-token relevance.
- Cost scales quadratically with sequence length — the reason context windows are expensive to grow.
- Causal masking restricts self-attention to past tokens in decoder-only LLMs.
- RSIS3 relevance: self-attention cost explains token-budget economics in RSIS3's planning.

## Related
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]] — The general operation self-attention instantiates
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — How self-attention is parallelized
- [[wiki/prompt-engineering/context-windows|Context Windows]] — The capacity self-attention bounds
- [[wiki/ai-ml/attention-patterns|Attention Patterns]] — Observable behaviour of self-attention
