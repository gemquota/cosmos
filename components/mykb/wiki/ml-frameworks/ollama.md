---
type: "concept"
title: "Ollama"
description: "A local-first runtime for serving open-weight models with a simple API and CLI"
tags: ["ollama", "local-models", "inference", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Ollama

## Summary
Ollama runs open-weight models locally behind an OpenAI-compatible API, managing downloads, quantization, and GPU/CPU execution. It is the fastest way to stand up private LLM inference.

## Details
- Model library covers Llama, Mistral, DeepSeek, and thousands of community tags.
- Runs GGUF quantizations with CPU/GPU offload; simple to script and embed.
- OpenAI-compatible endpoint eases drop-in migration between hosted and local models.
- RSIS3 relevance: Ollama is the default local backend for RSIS3 experiments, keeping data on-device.

## Related
- [[wiki/ai-ml/llama|Llama]] — A flagship model family in its library
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The engine underneath
- [[wiki/ai-ml/quantisation|Quantisation]] — What makes local runs feasible
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Its compatible API surface
- [[wiki/ai-ml/mistral|Mistral]] — Another popular local family
