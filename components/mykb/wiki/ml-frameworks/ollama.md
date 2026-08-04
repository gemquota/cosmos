---
type: "entity"
title: "Ollama"
description: "A local-first runtime for serving open-weight models with a simple API and CLI"
tags: ["ollama", "local-models", "inference", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Ollama

## Summary

Ollama runs open models locally with a one-command install: model pulls, OpenAI-compatible API, GGUF quantization, and GPU/CPU inference. It is the fastest path from a model name to a local endpoint — and its convenience hides model-variant and resource decisions.

## Details
- Mechanism: ollama pull llama3.2 downloads a GGUF model (quantization variants like 4-bit/q4) into a local store; ollama serve exposes an OpenAI-compatible API (/v1/chat/completions); models run via llama.cpp-style inference on GPU or CPU with configurable context length; Modelfiles customize prompts/templates.
- Concrete example: a laptop runs a 7B model at 4-bit for offline drafting; a dev environment serves the same model to the wiki's loop through the standard chat endpoint; a Modelfile pins system prompt and context, making the local runtime behave like the hosted one for testing.
- Failure modes: resource assumptions — a 70B model does not run on 8GB laptops (check quantization and VRAM); version drift between local and hosted model behavior (test parity); Ollama's defaults (context length, batch) affecting quality; and production-grade needs (multi-user concurrency, autoscaling) outgrowing the local server.
- Operational tradeoffs: Ollama trades deployment simplicity for control (the same models run on vLLM with better throughput at scale); the pattern is Ollama for dev/edge/local and engine-served endpoints for production, with the OpenAI-compatible layer making the swap invisible.
- RSIS3/mykb relevance: the wiki's dev loop points at Ollama endpoints by default, so experiments run offline and at zero marginal cost before scaling up.
- Context and quality: default context windows can truncate long prompts; set num_ctx explicitly and compare outputs against the hosted model for parity.
- Concurrency: Ollama queues requests per model; for multi-user workloads measure queue latency and consider engine-served endpoints instead.

## Related
- [[wiki/ai-ml/llama|Llama]] — A flagship model family in its library
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The engine underneath
- [[wiki/ai-ml/quantisation|Quantisation]] — What makes local runs feasible
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Its compatible API surface
- [[wiki/ai-ml/mistral|Mistral]] — Another popular local family
