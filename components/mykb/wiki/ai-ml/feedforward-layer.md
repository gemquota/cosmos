---
type: "concept"
title: "Feedforward Layer"
description: "The per-token MLP in each transformer block that transforms representations after attention"
tags: ["feedforward-layer", "transformers", "architecture"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Feedforward Layer

## Summary
Each transformer block pairs attention with a position-wise feedforward network (usually two linear layers with a nonlinearity). Attention mixes information across tokens; the feedforward layer transforms each token's representation.

## Details
- Typical shape: expand to 4x hidden width, activate (GELU/SiLU variants), project back.
- Feedforward layers are where much of the model's factual knowledge is stored, per interpretability studies.
- Their size dominates parameter count in most transformers.
- RSIS3 relevance: KV-cache and quantization techniques target attention and feedforward weights differently.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — The block structure containing the MLP
- [[wiki/ai-ml/layer-norm|Layer Norm]] — Normalization sandwiching the MLP
- [[wiki/ai-ml/residual-connections|Residual Connections]] — The skip path around the MLP
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Interpretability features found in MLP activations
- [[wiki/ai-ml/quantisation|Quantisation]] — Weight precision affects MLP layers most
