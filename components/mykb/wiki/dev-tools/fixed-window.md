---
type: "concept"
title: "Fixed Window"
description: "A rate limiter that resets a counter at fixed boundaries"
tags: ["rate-limiting", "fixed-window", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Fixed Window

## Summary
The fixed-window algorithm counts requests per calendar-aligned period (per minute, per hour) and resets at the boundary. It is trivially cheap to implement but allows bursts up to 2x the limit at boundaries.

## Details
- Boundary burst: a flood at the end of one window plus the start of the next doubles throughput.
- The 2x burst is acceptable for coarse quotas; sliding windows exist for stricter enforcement.
- Cheap enough to run per key at the edge — one counter and one expiry per key.
- mykb relevance: fixed windows suit daily quotas (articles per day) where bursts are harmless.

## Related
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/dev-tools/token-bucket|Token Bucket]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/leaky-bucket|Leaky Bucket]]
