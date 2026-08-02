---
type: "concept"
title: "Sharded Data Parallelism"
description: "Distributed training strategy that replicates the model while sharding optimizer state across GPUs"
tags: ["distributed", "training", "memory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sharded Data Parallelism

## Summary
Distributed training strategy that replicates the model while sharding optimizer state across GPUs

## Details
- Each GPU holds a full copy of the model but only a fraction of optimizer state.
- Gradients are averaged globally, then each shard owner updates its slice.
- Lets batch sizes scale linearly with GPU count while capping memory growth.
- Foundation for DeepSpeed ZeRO and PyTorch FSDP.

## Related
- [[wiki/ml-frameworks/zero-stage|ZeRO Stages]] — formal stages of sharding
- [[wiki/ml-frameworks/deepspeed|DeepSpeed]] — main implementation
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — reduces sync frequency
- [[wiki/ml-frameworks/mixed-precision-training|Mixed-Precision Training]] — halves memory footprint
- [[wiki/ml-frameworks/data-loaders-and-pipelines|Data Loaders and Pipelines]] — feeds sharded training runs
