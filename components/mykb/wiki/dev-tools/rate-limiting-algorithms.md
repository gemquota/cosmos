---
type: "concept"
title: "Rate Limiting Algorithms"
description: "Algorithms that cap request rates: token bucket, leaky bucket, sliding window, fixed window"
tags: ["rate-limiting", "algorithms", "traffic", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Rate Limiting Algorithms

## Summary
Rate limiting algorithms decide when a request is allowed based on accumulated tokens or windowed counts. Each trades memory, burstiness, and fairness differently; choice depends on what you are protecting.

## Details
- Token bucket allows controlled bursts; leaky bucket smooths output; fixed window is simple but bursty at edges.
- Sliding window variants (log or counter) fix boundary spikes with more memory.
- Implement at the edge and per-key (IP, user, tenant) with clear rejection signals (429, Retry-After).
- mykb relevance: rate-limit model API calls per agent run to stay inside provider quotas.

## Related
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/token-bucket|Token Bucket]]
- [[wiki/dev-tools/leaky-bucket|Leaky Bucket]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]]
