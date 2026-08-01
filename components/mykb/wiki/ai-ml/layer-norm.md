---
type: "concept"
title: "Layer Norm"
description: "Normalizing activations across the feature dimension per token, which stabilizes transformer training"
tags: ["layer-norm", "normalization", "transformers"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Layer Norm

## Summary
Layer normalization rescales each token's activations to zero mean and unit variance (with learned gain/bias), keeping magnitudes stable through deep stacks. It is a quiet but essential ingredient of trainable transformers.

## Details
- RMSNorm and LayerNorm variants are used depending on the model family.
- Placement varies: post-norm (original) vs. pre-norm (most modern LLMs) affects training stability.
- Pre-norm transformers train more stably and are standard in Llama/Mistral-style models.
- RSIS3 relevance: norm placement is part of why models differ in how they respond to long prompts.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — The stack layer-norm stabilizes
- [[wiki/ai-ml/residual-connections|Residual Connections]] — The skip paths norms sit beside
- [[wiki/ai-ml/feedforward-layer|Feedforward Layer]] — The layer norms wrap
- [[wiki/ai-ml/llama|Llama]] — Reference family using pre-norm RMSNorm
- [[wiki/ml-frameworks/pytorch|PyTorch]] — Framework where norms are implemented
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — Stable training is the precondition for fine-tuning
