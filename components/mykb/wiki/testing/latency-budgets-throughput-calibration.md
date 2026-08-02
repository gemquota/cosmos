---
type: "concept"
title: "Latency Budgets and Throughput Calibration"
description: "Setting per-request latency targets and calibrating serving throughput against them"
tags: ["latency-budgets", "latency", "throughput", "serving"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Latency Budgets and Throughput Calibration

## Summary
Setting per-request latency targets and calibrating serving throughput against them

## Details
- Budgets allocate time across generation, retrieval, and tools.
- Calibration measures tokens/sec and requests/sec under load.
- Reveals where caching and parallelism pay off.
- Feeds llm-latency-optimization decisions.

## Related
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — improvement levers
- [[wiki/testing/cost-per-token-tradeoffs|Cost per Token Tradeoffs]] — cost analog
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — load constraints
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses with SSE]] — perceived latency
- [[wiki/api-protocols/load-shedding|Load Shedding]] — degradation policy
