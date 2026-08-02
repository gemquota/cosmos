---
type: "concept"
title: "Rotary Embeddings"
description: "RoPE: a positional encoding that rotates query and key vectors by angle proportional to position, capturing relative distances"
tags: ["rotary-embeddings", "rope", "positional-encoding", "transformers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2104.09864", "https://blog.eleuther.ai/rotary-embeddings/", "https://huggingface.co/docs/transformers/en/model_doc/llama"]
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
- Rotary position embedding (RoPE) multiplies queries and keys by a rotation matrix whose angle depends on the token's position, encoding relative distance directly into the attention scores.
- Because the rotation applies inside the dot product, RoPE makes attention depend on relative position only, which generalizes better across context lengths.
- It also supports long-context extension techniques: scaling or interpolating the rotation frequencies extends the effective context window.
- RoPE is the default in most modern LLMs, including LLaMA and its successors.
- **Worked example / comparison** — Worked example — with RoPE, token i attending to token j uses the angle proportional to (i-j); halving the frequency schedule roughly doubles the context length the model can handle.
- For mykb, rotary embeddings are documented under AI/ML as the current standard positional scheme for transformer models.

## Related
- [[wiki/ai-ml/positional-encoding|Positional Encoding]]
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]]
- [[wiki/ai-ml/llama|Llama]]
- [[wiki/prompt-engineering/context-windows|Context Windows]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/explainers|Explainers]]
