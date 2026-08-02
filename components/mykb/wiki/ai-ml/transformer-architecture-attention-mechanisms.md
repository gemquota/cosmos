---
type: "concept"
title: "Transformer Architecture and Attention"
description: "The self-attention architecture underlying modern LLMs"
tags: ["transformer", "attention", "architecture", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/1706.03762", "https://arxiv.org/abs/2205.14135"]
---

# Transformer Architecture and Attention

## Summary
The transformer is the neural architecture behind modern LLMs: layers of self-attention and feedforward networks process tokens in parallel, with attention letting every token condition on all others. Attention is what enables long-range dependencies and in-context learning. Most scaling advances are variations on its compute and memory costs.

## Details
- **Self-attention** — each token attends to all tokens in the sequence via query, key, and value projections; multi-head attention runs several in parallel.
- **Compute profile** — attention is quadratic in sequence length; KV caches, flash attention, and sparsity address that cost.
- **Components** — residual connections, layer norm, and rotary positional embeddings stabilize and locate the representation.
- **Scaling** — the architecture scales predictably with parameters and data (chinchilla law), which motivated decoder-only LLMs.
- **Worked example** — a causal decoder generates a token per step, attending to its own prior outputs stored in the KV cache.
- **mykb relevance** — transformer architecture, self-attention, and attention mechanisms are existing mykb topics central to understanding model behavior.

## Related
- [[wiki/ai-ml/self-attention|Self-Attention]] — the core mechanism
- [[wiki/ai-ml/multi-head-attention|Multi-Head Attention]] — parallel attention heads
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — fast attention kernels
- [[wiki/ai-ml/positional-encoding|Positional Encoding]] — position information
- [[wiki/ai-ml/rotary-embeddings|Rotary Embeddings]] — rotary positions
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — existing transformer concept
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — scaling behavior
- [[wiki/ml-frameworks/paged-attention|PagedAttention]] — related concept in this cluster
