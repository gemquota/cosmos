---
type: "concept"
title: "RoPE and Sliding Window Attention"
description: "Positional encoding and attention-window techniques that enable long-context models"
tags: ["rope", "attention", "positional", "long-context"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# RoPE and Sliding Window Attention

## Summary
Positional encoding and attention-window techniques that enable long-context models

## Details
- RoPE rotates query/key embeddings to encode relative positions.
- Sliding windows cap attention scope to a recent span.
- Both extend usable context at reduced compute.
- Key ingredients of modern long-context models.

## Related
- [[wiki/ml-frameworks/long-context-techniques|Long-Context Techniques]] — technique family
- [[wiki/ai-ml/positional-encoding|Positional Encoding]] — position encoding base
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — efficient attention
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — windowed cache
- [[wiki/ai-ml/transformer-architecture-attention-mechanisms|Transformer Architecture and Attention]] — foundation
