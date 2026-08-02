---
type: "concept"
title: "Inference Engines"
description: "Runtime software that loads trained LLM weights and serves token generation efficiently"
tags: ["serving", "llm", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Inference Engines

## Summary
Runtime software that loads trained LLM weights and serves token generation efficiently

## Details
- Engines handle weight loading, KV-cache allocation, batching, and device scheduling behind a serving API.
- Popular options include vLLM, TensorRT-LLM, llama.cpp, and Hugging Face TGI; each targets different hardware.
- Engine choice drives throughput, latency, and hardware utilization more than most other serving decisions.
- For self-hosted mykb deployments, the engine is the layer between weights and the gateway.

## Related
- [[wiki/ml-frameworks/vllm|vLLM]] — high-throughput engine with PagedAttention
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — CPU and edge-friendly engine
- [[wiki/ml-frameworks/tensorrt-llm|TensorRT-LLM]] — NVIDIA-optimized engine
- [[wiki/ml-frameworks/tgi|Text Generation Inference]] — Hugging Face serving stack
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — sits in front of engines
