---
type: "concept"
title: "Fixed Window"
description: "A rate limiter that resets a counter at fixed boundaries"
tags: ["rate-limiting", "fixed-window", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Fixed Window

## Summary
The fixed-window algorithm counts requests per calendar-aligned period (per minute, per hour) and resets at the boundary. It is trivially cheap to implement — one counter and one expiry per key — but allows bursts of up to 2x the limit at window boundaries.

## Details
- Mechanism: for each key, a counter with a TTL matching the window; each request increments and is rejected if the counter exceeds the limit; at the boundary the counter expires and resets to zero; distribution across nodes needs a shared store or sharding by key.
- Concrete example: an API quota of 100 requests/hour per token uses a counter keyed by token with a 1-hour TTL; a daily article-import quota resets at midnight; a script bursts 100 requests at 23:59 and 100 more at 00:00, achieving 2x the limit in seconds.
- Failure modes: the boundary burst — a flood straddling the reset doubles throughput (acceptable for coarse quotas, not for abuse protection); counter drift across replicas when each node keeps its own count; clock skew if the store timestamps differently; keys that never expire, leaking storage.
- Tradeoffs: fixed windows are the cheapest rate limiter — memory-light, fast, and easy to reason about — at the cost of burst tolerance at boundaries; sliding windows and token buckets smooth the rate at the cost of more state and computation; the choice is quota granularity versus enforcement strictness.
- Operational notes: use fixed windows where bursts are harmless (daily quotas), sliding or token-bucket where peaks matter, and always expire counters.
- RSIS3 relevance: fixed windows suit daily quotas (articles per day) where bursts are harmless — the same coarse, cheap enforcement RSIS3 wants for per-day batch limits.

## Practice
- Combine with a small burst allowance inside the window so legitimate short peaks are not rejected wholesale.
## Related
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/dev-tools/token-bucket|Token Bucket]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/leaky-bucket|Leaky Bucket]]
