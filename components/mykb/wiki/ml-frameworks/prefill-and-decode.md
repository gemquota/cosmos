---
type: "concept"
title: "Prefill and Decode"
description: "LLM inference splits each request into a parallel prefill phase and a token-by-token decode phase"
tags: ["decode", "inference", "llm"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Prefill and Decode

## Summary

LLM generation splits into prefill (process the prompt, in parallel) and decode (emit tokens one at a time, sequentially) — two phases with opposite performance profiles. Understanding the split explains latency, throughput, and the economics of long prompts.

## Details
- Mechanism: prefill computes the KV cache for the entire prompt in parallel — compute-bound, fast per token, and its cost scales with prompt length; decode generates tokens autoregressively, memory-bandwidth-bound (reading the KV cache), and its latency scales with the total sequence length; serving engines optimize them separately (chunked prefill, speculative decoding for decode).
- Concrete example: a 2,000-token RAG prompt costs most of its time in prefill even though it produces a 200-token answer; a chat stream feels slow because each decode step reads the growing KV cache; engines interleave prefill and decode batches to keep GPUs busy.
- Failure modes: long prompts with short outputs dominated by prefill cost (cache the prefix, use prompt caching); long outputs dominating decode latency (speculative decoding, early-exit where safe); confusing TTFT (prefill) with inter-token latency (decode) in measurements; and KV cache memory growing with sequence length causing OOM at high concurrency.
- Operational tradeoffs: the two phases justify different optimizations — prefill benefits from compute and prompt caching; decode benefits from bandwidth, batching, and speculation; the discipline is measuring both (TTFT and tokens/sec) separately and sizing infrastructure for the phase that dominates your workload.
- RSIS3/mykb relevance: the wiki's serving telemetry separates prefill and decode metrics, so the loop tunes engines and prompt layouts with phase-level data.
- Measurement: record time-to-first-token and tokens-per-second separately in telemetry; optimizing the wrong phase (or a blended average) is the classic latency-misdiagnosis.
- Cache interplay: prompt caching targets prefill cost; speculative decoding targets decode latency — combine them for long-prompt, long-output workloads.

## Related
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — how requests interleave across phases
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — cache written in prefill and read in decode
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — engines that schedule both phases
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency levers for each phase
- [[wiki/ai-ml/speculative-decoding|Speculative Decoding]] — draft-then-verify trick that shortens decode
