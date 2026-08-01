---
type: "concept"
title: "Rotary Embeddings"
description: "RoPE: a positional encoding that rotates query and key vectors by angle proportional to position, capturing relative distances"
tags: ["rotary-embeddings", "rope", "positional-encoding", "transformers"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Rotary Embeddings

## Summary
Rotary position embeddings (RoPE) encode relative position by rotating Q/K vectors, so attention between tokens depends on their distance. RoPE is the de facto standard in modern LLMs and enables length extrapolation.

## Details
- Introduced in 'RoFormer: Enhanced Transformer with Rotary Position Embedding' (2021).
- Relative-position behaviour falls out naturally without extra parameters per position pair.
- Supports longer-context fine-tuning by adjusting the rotation base frequency.
- Used in Llama, Mistral, GPT-NeoX-style models, and many others.
- RSIS3 relevance: RoPE variants explain why some models handle 128K+ windows better than others.

## Related
- [[wiki/ai-ml/positional-encoding|Positional Encoding]] — The family RoPE belongs to
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — The architecture RoPE lives in
- [[wiki/ai-ml/llama|Llama]] — Reference model family using RoPE
- [[wiki/prompt-engineering/context-windows|Context Windows]] — Long-window capability links to RoPE
