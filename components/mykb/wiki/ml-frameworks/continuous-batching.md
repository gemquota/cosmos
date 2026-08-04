---
type: "concept"
title: "Continuous Batching"
description: "Serving technique that schedules token generation across requests at every step"
tags: ["continuous-batching", "serving", "throughput", "vllm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Continuous Batching

## Summary

Continuous batching is a serving technique that schedules token generation across many requests at every decoding step rather than waiting for whole requests to finish. By mixing requests in different phases of generation, it keeps the GPU busy and dramatically raises throughput. The technique matters because it is the main reason modern inference engines serve many concurrent users from a single model.

## Details

- **Definition** — instead of static request batches, continuous batching adds and removes requests at each step as they complete or arrive.
- **Classic batching problem** — naive static batching wastes capacity because slow requests block fast ones and batches drain unevenly.
- **Iteration-level scheduling** — at each decode step the scheduler selects a working set of requests, enabling fine-grained resource control.
- **Throughput gains** — mixing short and long requests, and prefill with decode work, raises utilization and overall tokens-per-second.
- **Interaction with prefill** — prefill phases consume different resources than decode, so schedulers balance them to avoid latency spikes.
- **Memory foundation** — efficient continuous batching depends on memory managers like paged attention that can grow and shrink KV caches per request.
- **Worked example** — a server with one model processes 100 chat users by advancing every active request one token per step, inserting new arrivals and retiring finished ones.
- **Latency tradeoffs** — high batch utilization can increase per-token latency for individual requests, so schedulers add fairness and deadline policies.
- **Failure modes** — poor scheduling causes head-of-line blocking or memory thrashing; over-batching degrades responsiveness.
- **Practical relevance** — continuous batching is implemented in vLLM, TGI, and other engines, making it the default for cost-efficient LLM serving.

## Related

- [[wiki/ml-frameworks/paged-attention|Paged Attention]] — the memory manager enabling it
- [[wiki/ml-frameworks/vllm|vLLM]] — the reference implementation
- [[wiki/ml-frameworks/batching-strategies|Batching Strategies]] — the design space
- [[wiki/ml-frameworks/prefill-decode-disaggregation|Prefill-Decode Disaggregation]] — phase separation
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — the adopting systems
- [[wiki/ml-frameworks/streaming-responses|Streaming Responses]] — user-facing effect

