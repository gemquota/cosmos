---
type: "concept"
title: "Self-Attention"
description: "Attention computed over a sequence against itself, letting every token attend to every other token"
tags: ["self-attention", "transformers", "attention"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03762", "https://en.wikipedia.org/wiki/Attention_(machine_learning)"]
---

# Self-Attention

## Summary
Self-attention lets each token in a sequence look at all other tokens, computing context-aware representations. It is the distinguishing operation of transformer blocks and the source of their long-range modelling power.

## Details
- Each position produces a query, key, and value; attention weights reflect inter-token relevance.
- Cost scales quadratically with sequence length — the reason context windows are expensive to grow.
- Causal masking restricts self-attention to past tokens in decoder-only LLMs.
- RSIS3 relevance: self-attention cost explains token-budget economics in RSIS3's planning.
- Self-attention runs attention within one sequence: every token attends to every other token of the same sequence, using the same input as query, key, and value.
- It captures intra-sequence relationships — coreference, syntax, long-range dependencies — without recurrence, which is why it replaced RNNs in transformers.
- Masked self-attention (causal masking) prevents positions from attending to the future, which is what makes decoder-only training and generation possible.
- The quadratic cost of full self-attention is the main scaling constraint, motivating sparse and linear approximations.
- **Worked example / comparison** — Worked example — in a sentence, each word's representation becomes a blend of the words it attends to; 'bank' disambiguates by attending to 'river' or 'money' in context.
- For mykb, self-attention is a cornerstone of the AI/ML cluster; its article links forward to the mechanisms that build on it.

## Related
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]]
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]]
- [[wiki/prompt-engineering/context-windows|Context Windows]]
- [[wiki/ai-ml/attention-patterns|Attention Patterns]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
