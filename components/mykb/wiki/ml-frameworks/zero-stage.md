---
type: "concept"
title: "ZeRO Stages"
description: "DeepSpeed optimization levels that shard optimizer state, gradients, and parameters across GPUs"
tags: ["deepspeed", "memory", "distributed"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ZeRO Stages

## Summary
DeepSpeed optimization levels that shard optimizer state, gradients, and parameters across GPUs

## Details
- ZeRO-1 shards optimizer state; ZeRO-2 adds gradient sharding; ZeRO-3 shards parameters too.
- Each stage trades extra communication for lower per-GPU memory.
- ZeRO-3 enables training models that do not fit on any single GPU.
- Offloading moves shards to CPU/NVMe for even larger fits.

## Related
- [[wiki/ml-frameworks/deepspeed|DeepSpeed]] — library that implements ZeRO
- [[wiki/ml-frameworks/sharding-data-parallel|Sharding and Data Parallelism]] — DP baseline it extends
- [[wiki/ml-frameworks/mixed-precision-training|Mixed-Precision Training]] — reduces memory further
- [[wiki/ml-frameworks/checkpointing-training|Training Checkpointing]] — another memory lever
- [[wiki/ml-frameworks/gradient-accumulation|Gradient Accumulation]] — communication cost trade-off
