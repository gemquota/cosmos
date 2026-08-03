---
type: "concept"
title: "Token Bucket"
description: "A rate limiter that allows bursts up to a bucket capacity while enforcing a steady average rate"
tags: ["rate-limiting", "token-bucket", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Token Bucket

## Summary
The token bucket algorithm refills tokens at a steady rate and allows a request when a token is available. The bucket size caps burst size, so it permits spikes while still bounding long-run rate — the standard model for per-key API rate limits.

## Details
- Mechanism: parameters are refill rate r (tokens per second) and bucket capacity b; the bucket starts full at b; each request consumes one token; refills happen at rate r up to capacity; a request with no token is rejected (or queued); the effective behavior is average rate r with bursts up to b.
- Concrete example: a provider limit of 10 requests/second with a burst of 20 — the bucket holds 20 tokens, refills at 10/s; a script can burst 20 immediately, then settles to 10/s; AWS and many gateway rate limits model exactly this; per-key buckets isolate tenants from each other's bursts.
- Failure modes: bucket capacity set too large, defeating the long-run limit's protection; refill computed lazily with float drift, mis-counting under load; per-key buckets sharing one global store, becoming a bottleneck; burst allowances consumed by retries, starving legitimate traffic; distributed implementations without atomicity double-spending tokens.
- Tradeoffs: the token bucket is memoryless and cheap (one counter and timestamp per key) and allows useful bursts — the leaky bucket, by contrast, smooths output but adds latency; the choice is burst tolerance versus output smoothness; the token bucket suits APIs where short bursts are fine and the average rate is the real limit.
- Operational notes: monitor bucket depth and rejections, size capacity from real burst needs, and keep per-key state expiry bounded.
- RSIS3 relevance: a token bucket per tool class keeps agent bursts inside provider limits — the same steady-rate-with-bursts model RSIS3 needs for model calls.

## Practice
- Expose the effective rate and burst in documentation so callers know what the limiter allows before they hit it.
## Related
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/leaky-bucket|Leaky Bucket]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/adaptive-limits|Adaptive Limits]]
