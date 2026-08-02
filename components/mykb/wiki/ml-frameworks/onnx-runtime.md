---
type: "concept"
title: "ONNX Runtime"
description: "Cross-platform inference engine that runs models in the Open Neural Network Exchange format"
tags: ["inference", "interop", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ONNX Runtime

## Summary
Cross-platform inference engine that runs models in the Open Neural Network Exchange format

## Details
- Executes ONNX-exported models across CPU, GPU, and mobile backends with a single format.
- Supports graph optimization, quantization, and hardware-specific execution providers.
- Common in hybrid deployments where models must move between frameworks and devices.
- Acts as an interop layer when parts of a pipeline are PyTorch and parts are TensorFlow.

## Related
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — one member of the engine family
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — where ONNX Runtime shines
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — formats a registry must track
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — graph-level optimizations
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — runtime state it manages
