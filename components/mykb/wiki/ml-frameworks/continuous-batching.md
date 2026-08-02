---
type: "concept"
title: "Continuous Batching"
description: "Serving technique that schedules token generation across requests at every step"
tags: ["continuous-batching", "serving", "throughput", "vllm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Continuous Batching

## Summary
Serving technique that schedules token generation across requests at every step

## Details
- Rather than waiting for whole batches, new sequences join as slots free.
- Dramatically improves GPU utilization and throughput.
- Requires dynamic KV-cache memory management.
- Standard in vLLM and similar engines.

## Related
- [[wiki/ml-frameworks/paged-attention|PagedAttention]] — memory enabler
- [[wiki/ml-frameworks/vllm|vLLM]] — flagship implementation
- [[wiki/ml-frameworks/batching-strategies|Batching Strategies]] — family
- [[wiki/ml-frameworks/prefill-decode-disaggregation|Prefill-Decode Disaggregation]] — phase separation
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — adoption
