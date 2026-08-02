---
type: "concept"
title: "Rate Limiter Design"
description: "Designing token and request rate limits for LLM APIs and gateways"
tags: ["rate-limiter", "rate-limits", "design", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Rate Limiter Design

## Summary
Designing token and request rate limits for LLM APIs and gateways

## Details
- Fixed window, sliding window, and token bucket algorithms differ in burstiness.
- Limits apply per key, user, or route.
- Limit responses should guide clients via headers.
- Complements budget-and-quota-control.

## Related
- [[wiki/ml-frameworks/rate-limit-engineering|Rate Limit Engineering]] — engineering umbrella
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]] — parallelism cap
- [[wiki/agent-systems/budget-and-quota-control|Budget and Quota Control]] — cost quotas
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — client behavior
- [[wiki/api-protocols/load-shedding|Load Shedding]] — server-side drops
