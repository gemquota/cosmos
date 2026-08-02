---
type: "concept"
title: "Multi-Head Attention"
description: "Running several attention computations in parallel with different projections, then concatenating the results"
tags: ["multi-head-attention", "attention", "transformers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03762", "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"]
---

# Multi-Head Attention

## Summary
Multi-head attention splits the model dimension into parallel attention heads, each learning different relational patterns (syntax, coreference, position). The heads' outputs are concatenated and projected back, giving the model richer joint representations.

## Details
- Heads specialize: some track syntax, others positions, others factual retrieval — visible in interpretability studies.
- Number of heads scales with model size; pruning heads is a common compression technique.
- Computationally it is one batched operation, not a sequential loop, keeping training efficient.
- RSIS3 relevance: head-level specialization underlies mechanistic-interpretability analysis of RSIS3's models.
- Multi-head attention runs several attention operations in parallel over the same sequence, each with its own learned projections, then concatenates the results.
- Different heads learn different relationship types — position, syntax, coreference, and content — which gives the model more expressive capacity per layer.
- The parallel heads cost the same as one attention pass per head, so width trades against depth in the layer budget.
- Head pruning research shows many heads are redundant at inference, which is why head-count is a tuning lever.
- **Worked example / comparison** — Worked example — one head may track positional offsets while another tracks noun-verb agreement, and the concatenation lets the feedforward layer use both signals.
- For mykb, multi-head attention is documented as the layer between attention-mechanism and the full transformer-architecture article.

## Related
- [[wiki/ai-ml/self-attention|Self-Attention]]
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]]
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]]
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/ml-frameworks/pytorch|PyTorch]]
- [[wiki/ai-ml/quantisation|Quantisation]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/concepts/deep-dives|Deep Dives]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
