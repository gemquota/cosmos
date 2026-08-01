---
type: "concept"
title: "Multi-Head Attention"
description: "Running several attention computations in parallel with different projections, then concatenating the results"
tags: ["multi-head-attention", "attention", "transformers"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Multi-Head Attention

## Summary
Multi-head attention splits the model dimension into parallel attention heads, each learning different relational patterns (syntax, coreference, position). The heads' outputs are concatenated and projected back, giving the model richer joint representations.

## Details
- Heads specialize: some track syntax, others positions, others factual retrieval — visible in interpretability studies.
- Number of heads scales with model size; pruning heads is a common compression technique.
- Computationally it is one batched operation, not a sequential loop, keeping training efficient.
- RSIS3 relevance: head-level specialization underlies mechanistic-interpretability analysis of RSIS3's models.

## Related
- [[wiki/ai-ml/self-attention|Self-Attention]] — The operation each head performs
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]] — The underlying mechanism
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — Studying what heads compute
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — Where heads live in the stack
- [[wiki/ml-frameworks/pytorch|PyTorch]] — Reference implementation framework
- [[wiki/ai-ml/quantisation|Quantisation]] — Head pruning as a compression technique
