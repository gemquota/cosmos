---
type: "concept"
title: "Logit Lens"
description: "A technique for decoding a model's predictions from intermediate layers, revealing how computation unfolds"
tags: ["logit-lens", "interpretability", "transformers"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Logit Lens

## Summary
The logit lens projects each layer's hidden state through the model's unembedding to read 'what the model would predict right now'. It turns layer stacks into readable traces of how predictions develop.

## Details
- Works because residual streams and unembeddings align; mostly valid for decoder-only transformers.
- Reveals early commitment, late correction, and where factual knowledge gets resolved.
- Cheap and model-agnostic; a staple first look in interpretability work.
- RSIS3 relevance: tracing RSIS3's reasoning across layers could localize prompt-induced confusion.

## Related
- [[wiki/ai-ml/interpretability|Interpretability]] — The umbrella field
- [[wiki/ai-ml/mechanistic-interpretability|Mechanistic Interpretability]] — The rigorous cousin
- [[wiki/ai-ml/residual-connections|Residual Connections]] — The residual stream logit lens reads
- [[wiki/ai-ml/probing|Probing]] — Related activation-reading method
- [[wiki/ai-ml/sparse-autoencoders|Sparse Autoencoders]] — Complementary feature extraction
- [[wiki/testing/llm-evaluation|LLM Evaluation]] — Layer traces help diagnose eval failures
