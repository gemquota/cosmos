---
type: "concept"
title: "Inference Engines"
description: "Runtime software that loads trained LLM weights and serves token generation efficiently"
tags: ["serving", "llm", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Inference Engines

## Summary

Inference engines are the runtimes that execute trained models — vLLM, llama.cpp, TensorRT-LLM, ONNX Runtime, TGI — differing in throughput, latency, quantization, and hardware support. Engine choice is the difference between a model and a service.

## Details
- Mechanism: engines compile/optimize the graph (operator fusion, KV-cache management, continuous batching, quantization: INT8/INT4/FP8) and schedule requests; vLLM and TGI optimize LLM serving with paged attention and continuous batching; llama.cpp runs GGUF quantized models on CPU/GPU edge devices; TensorRT-LLM optimizes for NVIDIA GPUs; engines expose OpenAI-compatible APIs.
- Concrete example: a high-traffic chat service runs vLLM with continuous batching, doubling throughput vs naive generation; a laptop demo runs a 7B model via llama.cpp at 4-bit; an embedded device runs ONNX Runtime with dynamic quantization; the same checkpoint serves differently per engine — throughput, latency tails, and VRAM usage vary 2-5x.
- Failure modes: engine-vs-hardware mismatch (features compiled for one GPU arch); quantization accuracy loss (unsupervised calibration can degrade outputs); KV-cache memory miscalculation causing OOM at load; and engine version drift changing behavior between dev and prod.
- Operational tradeoffs: engines trade engineering effort for serving economics; the discipline is benchmarking the actual workload (throughput, p50/p95 latency, cost per token) across engines, pinning versions, and using OpenAI-compatible endpoints so the app layer stays portable.
- RSIS3/mykb relevance: the wiki's local serving uses a pinned engine with recorded benchmark data, so the loop knows the cost-per-token of every experiment.
- Benchmarking protocol: test with the real workload's input/output lengths and concurrency; short-prompt benchmarks mislead for long-context services.
- Multi-GPU: tensor parallelism changes memory and latency characteristics; measure scaling efficiency before committing to a topology.
- Graceful degradation: engines differ in overload behavior (queue vs reject); define the API's 429/503 semantics so clients back off predictably.
- Model format portability: converting weights between formats (GGUF, safetensors, engine checkpoints) must be validated with golden outputs, since conversion silently changes numerics.

## Related
- [[wiki/ml-frameworks/vllm|vLLM]] — high-throughput engine with PagedAttention
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — CPU and edge-friendly engine
- [[wiki/ml-frameworks/tensorrt-llm|TensorRT-LLM]] — NVIDIA-optimized engine
- [[wiki/ml-frameworks/tgi|Text Generation Inference]] — Hugging Face serving stack
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — sits in front of engines
