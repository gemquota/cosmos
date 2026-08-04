---
type: "entity"
title: "ONNX"
description: "Open Neural Network Exchange: an open model format for interoperability across frameworks and runtimes"
tags: ["onnx", "interoperability", "model-format"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# ONNX

## Summary
ONNX is an open format for representing trained models so they can move between frameworks (PyTorch, TensorFlow) and runtimes (CPU, GPU, edge). ONNX Runtime executes the format with optimized kernels.

## Details
- Graph format captures ops, weights, and metadata; exporters exist for major frameworks.
- ONNX Runtime supports quantization, GPU/CPU backends, and mobile targets.
- LLM support lags GGUF/vLLM ecosystems but serves hybrid deployments.
- RSIS3 relevance: ONNX is a candidate for porting fine-tuned RSIS3 models to edge devices.

## Related
- [[wiki/ml-frameworks/pytorch|PyTorch]] — Exports to ONNX
- [[wiki/ml-frameworks/tensorflow|TensorFlow]] — Exports to ONNX
- [[wiki/ai-ml/quantisation|Quantisation]] — ONNX quantization paths
- [[wiki/ml-frameworks/llama-cpp|llama.cpp]] — The competing deployment format
- [[wiki/ml-frameworks/hugging-face|Hugging Face]] — Hub hosts ONNX variants
