---
type: "concept"
title: "LLM Latency Optimization"
description: "Reducing time-to-first-token and time-per-token for LLM serving"
tags: ["latency", "serving", "optimization", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2309.06180", "https://arxiv.org/abs/2211.17192"]
---

# LLM Latency Optimization

## Summary
Latency optimization targets both prefill time (first token) and decode speed (tokens per second). It matters because users and agents experience latency directly, and slow responses break interactive flows. Levers span kernels, caching, batching, and model choice.

## Details
- **Levers** — flash attention, KV-cache management, speculative decoding, batching policy, and smaller or quantized models.
- **Metrics** — TTFT (time to first token), ITL (inter-token latency), and end-to-end p95.
- **Worked example** — a voice agent uses streaming, prefix caching, and a distilled model to hit a 500ms TTFT budget.
- **Trade-off** — latency work usually trades throughput, cost, or quality; measure all three.
- **mykb relevance** — interactive knowledge retrieval demands low TTFT for a snappy RSIS3 loop.
- **Worked example** — a voice agent uses streaming, prefix caching, and a distilled model to hit a 500ms time-to-first-token budget.
- **Measurement** — track TTFT, inter-token latency, and end-to-end p95 under realistic load.
- **Trade-off** — latency work usually trades throughput, cost, or quality, so measure all three before adopting a technique.

## Related
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — memory speed
- [[wiki/testing/latency-budgets-throughput-calibration|Latency Budgets and Throughput Calibration]] — budgets
- [[wiki/ai-ml/model-quantization|Model Quantization]] — smaller models
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — related concept in this cluster
- [[wiki/ml-frameworks/prefill-decode-disaggregation|Prefill-Decode Disaggregation]] — related concept in this cluster
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — related concept in this cluster
- [[wiki/ai-ml/self-attention|Self-Attention]] — attention foundation
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — architecture foundations
