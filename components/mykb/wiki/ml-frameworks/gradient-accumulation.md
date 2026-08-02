---
type: "concept"
title: "Gradient Accumulation"
description: "Training technique that sums gradients over several micro-batches before applying an optimizer step"
tags: ["accumulation", "training", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Gradient Accumulation

## Summary
Training technique that sums gradients over several micro-batches before applying an optimizer step

## Details
- Emulates larger effective batch sizes without fitting the whole batch in memory.
- Each micro-batch runs forward and backward, but weights update only after N steps.
- Increases throughput on memory-constrained GPUs at the cost of update latency.
- Affects batch-normalization statistics and should be tuned carefully.

## Related
- [[wiki/ml-frameworks/mixed-precision-training|Mixed-Precision Training]] — memory savings that stack with it
- [[wiki/ml-frameworks/sharding-data-parallel|Sharding and Data Parallelism]] — distributed variant that also batches
- [[wiki/ml-frameworks/data-loaders-and-pipelines|Data Loaders and Pipelines]] — source of micro-batches
- [[wiki/ai-ml/llm-fine-tuning|LLM Fine-Tuning]] — common training knob
- [[wiki/ml-frameworks/evaluation-during-training|Evaluation During Training]] — checkpoints between accumulation windows
