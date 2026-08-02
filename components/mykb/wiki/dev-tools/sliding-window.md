---
type: "concept"
title: "Sliding Window"
description: "A rate limiter that counts requests over a rolling time window"
tags: ["rate-limiting", "sliding-window", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Sliding Window

## Summary
Sliding-window rate limiting counts requests in the most recent fixed duration (e.g. the last minute) and rejects when the count exceeds the limit. It avoids the boundary bursts of fixed windows at a higher memory cost.

## Details
- Sliding log is exact but stores a timestamp per request; sliding counter approximates with two buckets.
- Good for per-user limits where smooth enforcement matters and the count is per key.
- Distributed implementations need a shared counter (Redis) or approximate per-node windows.
- mykb relevance: sliding-window the per-run token usage to stay inside model budgets.

## Related
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/fixed-window|Fixed Window]]
- [[wiki/dev-tools/token-bucket|Token Bucket]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/adaptive-limits|Adaptive Limits]]
