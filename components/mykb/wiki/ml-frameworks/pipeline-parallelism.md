---
type: "concept"
title: "Pipeline Parallelism"
description: "Distributed training that splits model layers across devices and streams micro-batches through them"
tags: ["parallelism", "training", "distributed"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Pipeline Parallelism

## Summary
Distributed training that splits model layers across devices and streams micro-batches through them

## Details
- Layer groups are assigned to different devices, so each device computes a slice of the forward/backward pass.
- Micro-batching keeps all stages busy and hides pipeline bubbles.
- Reduces per-device memory dramatically but adds communication latency.
- Often combined with tensor parallelism for very large models.

## Related
- [[wiki/ml-frameworks/tensor-parallelism|Tensor Parallelism]] — splits within layers, this splits across layers
- [[wiki/ml-frameworks/sharding-data-parallel|Sharding and Data Parallelism]] — data-parallel alternative
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — related micro-batch trick
- [[wiki/ml-frameworks/deepspeed|DeepSpeed]] — supports pipelining via its engine
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — where these techniques apply
