---
type: "concept"
title: "Feedforward Layer"
description: "The per-token MLP in each transformer block that transforms representations after attention"
tags: ["feedforward-layer", "transformers", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03762", "https://en.wikipedia.org/wiki/Feedforward_neural_network"]
---

# Feedforward Layer

## Summary
Each transformer block pairs attention with a position-wise feedforward network (usually two linear layers with a nonlinearity). Attention mixes information across tokens; the feedforward layer transforms each token's representation.

## Details
- Typical shape: expand to 4x hidden width, activate (GELU/SiLU variants), project back.
- Feedforward layers are where much of the model's factual knowledge is stored, per interpretability studies.
- Their size dominates parameter count in most transformers.
- RSIS3 relevance: KV-cache and quantization techniques target attention and feedforward weights differently.
- Each transformer block ends with a per-token feedforward network — typically two linear layers with a nonlinearity between them, applied independently to every position.
- The feedforward layer is where much of the model's learned knowledge is stored; the attention layers route information, the feedforward layers transform it.
- Its width (intermediate dimension) is usually several times the hidden size, which makes it the largest parameter block in the model.
- Since it operates per token, it parallelizes trivially and is often the target of MoE-style sparsification in large models.
- **Worked example / comparison** — Worked example — in a 4096-wide hidden layer with a 11008 intermediate dimension, each token independently passes through the two matrices; no information crosses between positions here.
- For mykb, the feedforward layer article sits inside the transformer-architecture cluster and links out to layer-norm and residual-connections.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/ai-ml/layer-norm|Layer Norm]]
- [[wiki/ai-ml/residual-connections|Residual Connections]]
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]]
- [[wiki/ai-ml/quantisation|Quantisation]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
