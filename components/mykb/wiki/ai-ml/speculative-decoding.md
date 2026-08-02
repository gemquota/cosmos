---
type: "concept"
title: "Speculative Decoding"
description: "Using a small draft model to guess tokens while a large model verifies, speeding up generation"
tags: ["speculative-decoding", "inference", "latency", "decoding"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://arxiv.org/abs/2211.17192", "https://arxiv.org/abs/2302.01318"]
---

# Speculative Decoding

## Summary
Speculative decoding lets a fast draft model propose several tokens while the large model verifies them in parallel. It matters because decoding is memory-bound, and verification costs less than full sequential generation. Correctness is preserved exactly — the output distribution is unchanged.

## Details
- **Mechanism** — draft k tokens, verify with the target model in one forward pass, accept the longest matching prefix.
- **Speedups** — 2-3x on many workloads with negligible quality impact.
- **Worked example** — a 1B draft model speeds a 70B model; acceptance rate ~0.7 yields a 2.3x decode speedup.
- **Requirements** — a good draft model and KV-cache support in the serving engine.
- **mykb relevance** — faster decode makes interactive RSIS3 loops feel local and instant.
- **Worked example** — a 1B draft model speeds a 70B model; acceptance rate around 0.7 yields a 2.3x decode speedup.
- **Quality guarantee** — the sampling distribution is unchanged, so outputs match the target model exactly.

## Related
- [[wiki/ai-ml/kv-cache-management|KV-Cache Management]] — cache interaction
- [[wiki/ml-frameworks/prefill-and-decode|Prefill and Decode]] — decode phase
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — engine support
- [[wiki/prompt-engineering/sampling-vs-greedy|Sampling vs Greedy Decoding]] — distribution preservation
- [[wiki/meta-learning/knowledge-distillation|Knowledge Distillation]] — draft model source
- [[wiki/ml-frameworks/flash-attention|FlashAttention]] — related concept in this cluster
- [[wiki/ai-ml/self-attention|Self-Attention]] — attention foundation
- [[wiki/ai-ml/scaling-laws|Scaling Laws]] — capability scaling context
