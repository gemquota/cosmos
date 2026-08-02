---
type: "concept"
title: "Residual Connections"
description: "Skip connections that add a block's input to its output, enabling deep transformer training"
tags: ["residual-connections", "transformers", "training"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1512.03385", "https://en.wikipedia.org/wiki/Residual_neural_network"]
---

# Residual Connections

## Summary
Residual connections pass each block's input forward to be added to the block output, giving gradients a highway through the network. They are why 100+ layer transformers train at all.

## Details
- Every attention and feedforward sublayer is wrapped in a residual path.
- Residual streams are the object of 'residual stream' interpretability: information written and read by successive layers.
- Residual paths interact with layer norm placement (pre-norm vs post-norm).
- RSIS3 relevance: residual-stream research informs interpretability tooling like the logit lens.
- Residual connections add a layer's input to its output, so the layer learns a delta on top of the identity rather than a full transformation.
- They give gradients a direct highway through deep networks, which is what made hundred-plus-layer transformers trainable.
- In transformer blocks, residuals wrap attention and feedforward sublayers, and the block output is the sum of input and sublayer outputs.
- Residuals interact with layer norm: pre-norm transformers apply norm before the sublayer and leave the residual path mostly unscaled.
- **Worked example / comparison** — Worked example — if a sublayer outputs a useful delta, the residual keeps the original representation intact when the delta is zero, so early layers are not forced to encode everything.
- For mykb, residual connections are documented as the mechanism that makes deep transformer stacks stable and trainable.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/ai-ml/layer-norm|Layer Norm]]
- [[wiki/ai-ml/feedforward-layer|Feedforward Layer]]
- [[wiki/ai-ml/logit-lens|Logit Lens]]
- [[wiki/ai-ml/interpretability|Interpretability]]
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
