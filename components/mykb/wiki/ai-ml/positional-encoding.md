---
type: "concept"
title: "Positional Encoding"
description: "Information added to token embeddings so the permutation-invariant attention mechanism knows token order"
tags: ["positional-encoding", "transformers", "embeddings"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03762", "https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)"]
---

# Positional Encoding

## Summary
Because attention has no inherent notion of order, transformers inject position via encodings added to embeddings. The original paper used sinusoids; modern models use learned or rotary encodings.

## Details
- Sine/cosine encodings were the original choice; they generalize to unseen lengths.
- Learned positional embeddings are simpler and standard in many LLMs.
- Rotary embeddings (RoPE) encode relative positions in a rotation-friendly form and are now widespread.
- RSIS3 relevance: positional scheme affects extrapolation to long contexts, which matters for big-window deployments.
- Positional encoding injects order information into the input embeddings because self-attention is order-agnostic — the mechanism sees a bag of tokens unless position is added explicitly.
- The original transformer used fixed sinusoidal encodings; learned embeddings and relative position biases are the main alternatives.
- Position encodings must generalize to sequence lengths beyond training, which is a known failure mode for learned absolute encodings.
- Choice of encoding interacts with the attention variant: rotary embeddings, for instance, fold relative positions directly into the attention calculation.
- **Worked example / comparison** — Worked example — sinusoidal encoding adds a different sine/cosine vector per position, so position 5 and position 500 get distinguishable signals even if the model never saw the latter in training.
- For mykb, positional encoding is a building block that is best explained as part of the transformer article cluster.

## Related
- [[wiki/ai-ml/rotary-embeddings|Rotary Embeddings]]
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]]
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/prompt-engineering/context-windows|Context Windows]]
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
