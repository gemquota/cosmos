---
type: "entity"
title: "TVM and LLVM"
description: "Compiler infrastructure used to generate and optimize machine code for ML workloads"
tags: ["tvm-llvm", "compilers", "ml", "optimization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# TVM and LLVM

## Summary
Compiler infrastructure used to generate and optimize machine code for ML workloads

## Details
- TVM lowers ML graphs to hardware-targeted code with auto-tuning.
- LLVM provides the backend code generation and optimization passes.
- Enables portable performance across CPU, GPU, and accelerators.
- Underpins several inference engines.

## Related
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — compiler family
- [[wiki/ml-frameworks/onnx-runtime|ONNX Runtime]] — consumer of compiled graphs
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — target platforms
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — integration
- [[wiki/ml-frameworks/kernels-and-inference-optimization|Kernels and Inference Optimization]] — generated kernels
