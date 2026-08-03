---
type: "concept"
title: "ONNX Runtime"
description: "Cross-platform inference engine that runs models in the Open Neural Network Exchange format"
tags: ["inference", "interop", "runtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# ONNX Runtime

## Summary

ONNX Runtime executes ONNX-format models across hardware — CPU, GPU, and specialized accelerators — with graph optimizations and quantization. It is the portability layer for models that must run in production, edge, and web environments without the training framework.

## Details
- Mechanism: the ONNX format is a framework-neutral graph representation; ONNX Runtime compiles/optimizes it (operator fusion, constant folding, memory planning), quantizes (dynamic/static INT8), and executes via execution providers (CPU, CUDA, TensorRT, DirectML, WebGPU); models export from PyTorch/TF via torch.onnx.export / tf2onnx.
- Concrete example: a fine-tuned BERT classifier exports to ONNX, quantizes to INT8, and serves at 3-5x the throughput of the eager PyTorch path; a vision model runs in the browser via onnxruntime-web; a latency-critical service pins the CPU provider with the right thread settings.
- Failure modes: export failures on dynamic shapes or exotic ops (test the export with the real input shapes); quantization accuracy loss (validate with a calibration set); provider-specific behavior differences between dev and prod; and version drift — ONNX opsets and runtime versions must match the export tooling.
- Operational tradeoffs: ONNX trades framework convenience for deployment control and portability; the discipline is golden-output validation after conversion, quantization evaluated per task, and pinning opset/runtime versions in the build.
- RSIS3/mykb relevance: the wiki's deployed classifiers (tagging, dedup) would run via ONNX Runtime with pinned opsets, so model updates ship without changing the serving stack.
- Serving integration: ONNX Runtime slots into custom servers or via ORT's own serving; define the request/response contract explicitly so model swaps do not change API behavior.
- Opset policy: record the opset and runtime version used at export in the model metadata; re-exporting with a newer opset is a change to be validated, not assumed safe.

## Related
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — one member of the engine family
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — where ONNX Runtime shines
- [[wiki/ai-ml/model-versioning-and-registry|Model Versioning and Registry]] — formats a registry must track
- [[wiki/ml-frameworks/compiler-optimizations-llm|Compiler Optimizations for LLMs]] — graph-level optimizations
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — runtime state it manages
