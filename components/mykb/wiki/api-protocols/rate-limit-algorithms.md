---
type: "concept"
title: "Rate Limit Algorithms"
description: "Token bucket, leaky bucket, and window algorithms"
tags: ["rate-limiting", "algorithms", "token-bucket", "api-security", "traffic"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://stripe.com/blog/rate-limiters", "https://www.nginx.com/blog/rate-limiting-nginx/"]
---

# Rate Limit Algorithms

## Summary
Rate limiting algorithms decide when to allow or reject requests: token bucket, leaky bucket, fixed window, sliding window, and GCRA. The choice balances burst tolerance, memory cost, and fairness — token buckets allow bursts up to capacity, windows are simple but spiky, and sliding windows smooth the edges.

## Details
- Token bucket: a bucket holds tokens refilled at a steady rate; each request takes one; bursts up to capacity pass — the standard for APIs (Stripe, GitHub).
- Leaky bucket: requests drip out at a fixed rate; input is buffered then rejected when the buffer overflows — smooths output but queues latency.
- Fixed window: count requests per wall-clock minute and reset; simple and cheap, but allows 2x bursts at boundaries.
- Sliding window: count over a rolling interval (per-request or per-cell approximation) — smooth without reset spikes; needs more state.
- GCRA (generic cell rate algorithm): token bucket with monotonic timestamps, giving precise per-key rates and burst control.
- Distributed state: counters live in Redis (INCR + EXPIRE, sorted sets, or Lua) so all instances share one limit; local algorithms drift under sharding.
- Choosing: per-key token buckets for user fairness, global limits for protection, and client-side hints (Retry-After, headers) for good UX.

## Related
- [[wiki/api-protocols/rate-limit-headers|Rate Limit Headers]] — exposing limits and retry timing to clients
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]] — in-flight limits complement rate limits
- [[wiki/api-protocols/load-shedding|Load Shedding]] — what happens past the limit (503/429)
- [[wiki/api-protocols/redis-streams|Redis Streams]] — shared counter storage for distributed limits
- [[wiki/api-protocols/retry-policies|Retry Policies]] — clients must respect 429 responses
