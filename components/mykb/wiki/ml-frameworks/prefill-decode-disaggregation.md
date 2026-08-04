---
type: "concept"
title: "Prefill/Decode Disaggregation"
description: "Separating the prefill and decode phases onto different serving resources"
tags: ["pd-disaggregation", "serving", "architecture", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Prefill/Decode Disaggregation

## Summary

Prefill/decode disaggregation separates the two phases of autoregressive generation — processing the prompt and producing tokens — onto different serving resources. Since prefill is compute-bound and bursty while decode is memory-bound and steady, splitting them lets each phase use hardware suited to its demands. This architecture matters for reducing tail latency and stabilizing throughput in production LLM serving.

## Details

- **Definition** — disaggregation routes the prefill phase and the decode phase to different workers or clusters instead of interleaving them on one node.
- **Resource mismatch** — prefill consumes large compute bursts and long contexts; decode repeatedly reads the KV cache with small compute per step.
- **Latency benefits** — separating phases prevents long-prompt prefill from delaying interactive decode requests on the same GPU.
- **Throughput benefits** — decode workers can be sized for memory bandwidth, while prefill workers can be sized for compute, improving utilization.
- **Context transfer** — after prefill, the KV cache must be transferred to a decode worker, so efficient communication is a core engineering concern.
- **Relation to continuous batching** — within a worker, continuous batching still applies; disaggregation operates at the cluster level.
- **Worked example** — a serving system runs prefill on GPU nodes with large compute capacity and decode on nodes with large memory, moving KV caches over high-speed networking.
- **Failure modes** — expensive cache transfer can erase gains, and unbalanced routing can create new bottlenecks at boundaries.
- **Practical relevance** — disaggregation is used by major serving providers to meet strict latency budgets for chat and reasoning workloads.
- **Design space** — variants include full disaggregation, partial overlap, and speculative prefill, each trading complexity against performance.

## Related

- [[wiki/ml-frameworks/prefill-and-decode|Prefill and Decode]] — the two phases
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — the within-node scheduler
- [[wiki/ml-frameworks/serverless-inference|Serverless Inference]] — deployment context
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — the goal
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — the implementing systems
- [[wiki/ml-frameworks/paged-attention|Paged Attention]] — cache management across nodes

