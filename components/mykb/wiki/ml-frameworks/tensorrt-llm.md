---
type: "concept"
title: "TensorRT-LLM"
description: "NVIDIA toolkit that compiles LLMs into highly optimized TensorRT engines for GPU serving"
tags: ["nvidia", "inference", "gpu"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# TensorRT-LLM

## Summary
NVIDIA toolkit that compiles LLMs into highly optimized TensorRT engines for GPU serving

## Details
- Compiles model graphs with kernel fusion and automatic layer tuning for a specific GPU.
- Supports FP8 and INT4 weight formats plus in-flight batching for high utilization.
- Requires a build step per model and hardware config, which adds deploy complexity.
- Delivers some of the best latency/throughput numbers on NVIDIA data-center GPUs.

## Related
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — engine family it belongs to
- [[wiki/ai-ml/model-quantization|Model Quantization]] — compressed formats it exploits
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — compilation techniques behind it
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — serving strategy it implements
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — why low latency matters
