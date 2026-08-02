---
type: "concept"
title: "Compiler Optimizations for LLMs"
description: "Compile-time transformations that optimize model graphs for target hardware"
tags: ["llm-compilers", "compilers", "optimization", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Compiler Optimizations for LLMs

## Summary
Compile-time transformations that optimize model graphs for target hardware

## Details
- Graph lowering, operator fusion, and layout transforms happen at compile time.
- Compilers trade build time for runtime performance.
- Frameworks like TVM and TensorRT exemplify the approach.
- Combines with kernels for end-to-end gains.

## Related
- [[wiki/ml-frameworks/tvm-and-llvm|TVM and LLVM]] — compiler stack
- [[wiki/ml-frameworks/kernels-and-inference-optimization|Kernels and Inference Optimization]] — runtime layer
- [[wiki/ml-frameworks/tensorrt-llm|TensorRT-LLM]] — production compiler
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — compiled outputs
- [[wiki/ai-ml/model-quantization|Model Quantization]] — compile-time quantization
