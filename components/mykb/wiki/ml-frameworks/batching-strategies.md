---
type: "concept"
title: "Batching Strategies"
description: "Scheduling policies that group requests to maximize serving efficiency"
tags: ["batching", "serving", "throughput", "scheduling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Batching Strategies

## Summary
Scheduling policies that group requests to maximize serving efficiency

## Details
- Static batching groups same-length requests; dynamic batching handles mixed workloads.
- Batching raises throughput but can add queue latency.
- Continuous batching interleaves at token granularity.
- Choice depends on latency and load profiles.

## Related
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — token-level variant
- [[wiki/agent-systems/queueing-agents|Queueing Agents]] — request queues
- [[wiki/testing/latency-budgets-throughput-calibration|Latency Budgets and Throughput Calibration]] — trade-off setting
- [[wiki/ml-frameworks/prefill-decode-disaggregation|Prefill-Decode Disaggregation]] — phase-aware batching
- [[wiki/api-protocols/load-shedding|Load Shedding]] — overload policy
