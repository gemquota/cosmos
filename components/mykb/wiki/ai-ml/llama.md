---
type: "concept"
title: "Llama"
description: "Meta's family of open-weight LLMs, the de facto standard for local and self-hosted deployments"
tags: ["llama", "meta", "open-weights", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Llama

## Summary
Llama is Meta's open-weight model family (Llama 2, 3, and successors) released under research and commercial licenses. Its weights power most local, fine-tuned, and quantized deployments in the ecosystem.

## Details
- Released with model cards, licenses, and safety evaluation reports.
- Ecosystem: countless fine-tunes, quantizations (GGUF), and serving integrations.
- Strong capability-per-dollar for self-hosting; context sizes grew across versions.
- RSIS3 relevance: Llama-family models are the typical backbone for local RSIS3 runs via Ollama/llama.cpp.

## Related
- [[wiki/ml-frameworks/ollama|Ollama]] — Primary local runtime for Llama weights
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The quantization/serving stack
- [[wiki/ai-ml/quantisation|Quantisation]] — How Llama runs on modest hardware
- [[wiki/ai-ml/rotary-embeddings|Rotary Embeddings]] — Architecture detail of the family
- [[wiki/ai-ml/model-cards|Model Cards]] — Meta's published documentation
