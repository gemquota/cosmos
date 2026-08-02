---
type: "concept"
title: "Kernels and Inference Optimization"
description: "Low-level GPU kernel techniques that speed up model forward passes"
tags: ["kernels", "kernels", "inference", "gpu"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Kernels and Inference Optimization

## Summary
Low-level GPU kernel techniques that speed up model forward passes

## Details
- Fused kernels merge elementwise ops and reduce memory traffic.
- Tuning targets specific hardware and tensor shapes.
- Includes attention, GEMM, and quantization kernels.
- Implemented by engines and compilers.

## Related
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — automated kernel generation
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — flagship kernel
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — kernel consumers
- [[wiki/ml-frameworks/tvm-and-llvm|TVM and LLVM]] — compiler stack
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — goal
