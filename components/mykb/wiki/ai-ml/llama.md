---
type: "concept"
title: "Llama"
description: "Meta's family of open-weight LLMs, the de facto standard for local and self-hosted deployments"
tags: ["llama", "meta", "open-weights", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Llama

## Summary
Llama is Meta's open-weight model family (Llama 2, 3, and successors) released under research and commercial licenses. Its weights power most local, fine-tuned, and quantized deployments in the ecosystem, making it the de facto baseline for self-hosted inference.

## Details
Each Llama release ships with model cards, license terms, and safety evaluation reports, which set a documentation bar that many open models still do not meet. The license is the practical constraint: research-only terms in early versions gave way to permissive commercial terms later, but redistribution conditions still vary, so any deployment must check the license that matches the exact checkpoint in use. That matters for fine-tuning pipelines, because a derived model inherits the base license.

The ecosystem around the weights is the family's real moat. Countless fine-tunes, quantized GGUF variants, and serving integrations exist, which means a team can usually find a pre-tuned checkpoint for their domain instead of training from scratch. The trade-off is trust: community checkpoints are an unvetted supply chain, so provenance checks, eval on held-out tasks, and reproduction notes are essential before adoption.

Capability-per-dollar is strong for self-hosting, and context sizes grew substantially across versions, but the operational envelope still differs from frontier APIs: smaller quantized models degrade on long-context and complex tool-use tasks, and serving hardware cost grows with context length. Batch inference and prompt caching become the levers that keep local cost sane.

Llama-family models are the typical backbone for local RSIS3 runs via Ollama or llama.cpp, where loop privacy and per-token cost matter. For mykb, the practical artifacts are the exact model version, quant level, and eval results behind any experiment, since a 7B Q4 run and a 70B full-precision run are different systems that should never be compared without recording those parameters.

## Related
- [[wiki/ml-frameworks/ollama|Ollama]] — Primary local runtime for Llama weights
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The quantization/serving stack
- [[wiki/ai-ml/quantisation|Quantisation]] — How Llama runs on modest hardware
- [[wiki/ai-ml/rotary-embeddings|Rotary Embeddings]] — Architecture detail of the family
- [[wiki/ai-ml/model-cards|Model Cards]] — Meta's published documentation
