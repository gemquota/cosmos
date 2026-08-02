---
type: "concept"
title: "Prefill/Decode Disaggregation"
description: "Separating the prefill and decode phases onto different serving resources"
tags: ["pd-disaggregation", "serving", "architecture", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Prefill/Decode Disaggregation

## Summary
Separating the prefill and decode phases onto different serving resources

## Details
- Prefill (compute-heavy) and decode (memory-bound) want different hardware ratios.
- Disaggregation lets each phase scale independently.
- Adds data transfer and scheduling complexity.
- A frontier technique in inference-serving design.

## Related
- [[wiki/ml-frameworks/prefill-and-decode|Prefill and Decode]] — phase concepts
- [[wiki/ml-frameworks/continuous-batching|Continuous Batching]] — interaction
- [[wiki/ml-frameworks/serverless-inference|Serverless Inference]] — scalable deployment
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency goals
- [[wiki/ml-frameworks/inference-engines|Inference Engines]] — implementation
