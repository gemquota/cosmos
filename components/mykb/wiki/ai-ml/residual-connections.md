---
type: "concept"
title: "Residual Connections"
description: "Skip connections that add a block's input to its output, enabling deep transformer training"
tags: ["residual-connections", "transformers", "training"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Residual Connections

## Summary
Residual connections pass each block's input forward to be added to the block output, giving gradients a highway through the network. They are why 100+ layer transformers train at all.

## Details
- Every attention and feedforward sublayer is wrapped in a residual path.
- Residual streams are the object of 'residual stream' interpretability: information written and read by successive layers.
- Residual paths interact with layer norm placement (pre-norm vs post-norm).
- RSIS3 relevance: residual-stream research informs interpretability tooling like the logit lens.

## Related
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — The architecture residuals make trainable
- [[wiki/ai-ml/layer-norm|Layer Norm]] — The normalization alongside residuals
- [[wiki/ai-ml/feedforward-layer|Feedforward Layer]] — One of the layers residuals wrap
- [[wiki/ai-ml/logit-lens|Logit Lens]] — Reads intermediate residual states
- [[wiki/ai-ml/interpretability|Interpretability]] — Residual streams are a key object of study
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — Residual paths make deep fine-tuning feasible
