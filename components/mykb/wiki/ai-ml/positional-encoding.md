---
type: "concept"
title: "Positional Encoding"
description: "Information added to token embeddings so the permutation-invariant attention mechanism knows token order"
tags: ["positional-encoding", "transformers", "embeddings"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Positional Encoding

## Summary
Because attention has no inherent notion of order, transformers inject position via encodings added to embeddings. The original paper used sinusoids; modern models use learned or rotary encodings.

## Details
- Sine/cosine encodings were the original choice; they generalize to unseen lengths.
- Learned positional embeddings are simpler and standard in many LLMs.
- Rotary embeddings (RoPE) encode relative positions in a rotation-friendly form and are now widespread.
- RSIS3 relevance: positional scheme affects extrapolation to long contexts, which matters for big-window deployments.

## Related
- [[wiki/ai-ml/rotary-embeddings|Rotary Embeddings]] — The modern relative-position encoding
- [[wiki/ai-ml/attention-mechanism|Attention Mechanism]] — What positional encoding complements
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — Where encodings sit in the architecture
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Position encoding limits length extrapolation
- [[wiki/ai-ml/subword-tokenization|Subword Tokenization]] — Embeddings are defined per token
