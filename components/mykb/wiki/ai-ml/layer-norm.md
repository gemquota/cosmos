---
type: "concept"
title: "Layer Norm"
description: "Normalizing activations across the feature dimension per token, which stabilizes transformer training"
tags: ["layer-norm", "normalization", "transformers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1607.06450", "https://en.wikipedia.org/wiki/Layer_normalization"]
---

# Layer Norm

## Summary
Layer normalization rescales each token's activations to zero mean and unit variance (with learned gain/bias), keeping magnitudes stable through deep stacks. It is a quiet but essential ingredient of trainable transformers.

## Details
- RMSNorm and LayerNorm variants are used depending on the model family.
- Placement varies: post-norm (original) vs. pre-norm (most modern LLMs) affects training stability.
- Pre-norm transformers train more stably and are standard in Llama/Mistral-style models.
- RSIS3 relevance: norm placement is part of why models differ in how they respond to long prompts.
- Layer normalization normalizes activations across the feature dimension for each token independently, subtracting the mean and dividing by the standard deviation, then applies learned scale and shift.
- It stabilizes training by keeping activation statistics consistent across layers and is more parallel-friendly than batch normalization because it does not depend on batch statistics.
- In transformers, layer norm is typically applied before each sublayer (pre-norm) or after (post-norm); pre-norm is the common choice in modern LLMs.
- The normalization removes magnitude information, so scale must be re-introduced through the learned parameters when it matters.
- **Worked example / comparison** — Worked example — a token's 4096-dim vector is rescaled to unit variance; without this, deep stacks drift into vanishing or exploding activation scales.
- For mykb, layer-norm is documented as a core training-stability mechanism within the transformer cluster.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/ai-ml/residual-connections|Residual Connections]]
- [[wiki/ai-ml/feedforward-layer|Feedforward Layer]]
- [[wiki/ai-ml/llama|Llama]]
- [[wiki/ml-frameworks/pytorch|PyTorch]]
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
