---
type: "concept"
title: "Prefill and Decode"
description: "LLM inference splits each request into a parallel prefill phase and a token-by-token decode phase"
tags: ["decode", "inference", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prefill and Decode

## Summary
LLM inference splits each request into a parallel prefill phase and a token-by-token decode phase

## Details
- Prefill processes the full prompt in parallel, computing KV-cache entries for every input token at once.
- Decode then generates one token at a time, each step reading and extending the cache.
- Prefill is compute-bound; decode is memory-bandwidth-bound — which is why they benefit from different optimizations.
- Serving engines tune this split because latency and throughput trade-offs differ sharply between phases.

## Related
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — how requests interleave across phases
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — cache written in prefill and read in decode
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — engines that schedule both phases
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency levers for each phase
- [[wiki/ai-ml/speculative-decoding|Speculative Decoding]] — draft-then-verify trick that shortens decode
