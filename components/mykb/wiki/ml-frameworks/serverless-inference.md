---
type: "concept"
title: "Serverless Inference"
description: "On-demand LLM inference where capacity scales automatically and you pay per use"
tags: ["serverless-inference", "serving", "serverless", "scaling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Serverless Inference

## Summary
On-demand LLM inference where capacity scales automatically and you pay per use

## Details
- Providers run models on shared capacity with per-token billing.
- Eliminates idle cost for bursty traffic.
- Cold starts and concurrency limits are trade-offs.
- Complements self-hosted serving for spiky workloads.

## Related
- [[wiki/ml-frameworks/edge-inference|Edge Inference]] — closest-to-user alternative
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — fronting serverless
- [[wiki/llm-agents/inference-caching|Inference Caching]] — reducing calls
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — concurrency control
- [[wiki/agent-systems/model-fallback-chains|Model Fallback Chains]] — provider mix
