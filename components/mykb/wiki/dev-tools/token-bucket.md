---
type: "concept"
title: "Token Bucket"
description: "A rate limiter that allows bursts up to a bucket capacity while enforcing a steady average rate"
tags: ["rate-limiting", "token-bucket", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Token Bucket

## Summary
The token bucket algorithm refills tokens at a steady rate and allows a request when a token is available. The bucket size caps burst size, so it permits spikes while still bounding long-run rate.

## Details
- Parameters: refill rate r and capacity b — average rate is r, maximum burst is b.
- Memoryless and cheap to implement with a single counter and timestamp; no per-request history.
- Used per-key with isolated buckets; AWS and gRPC rate limits often model this.
- mykb relevance: a token bucket per tool class keeps agent bursts inside provider limits.

## Related
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/leaky-bucket|Leaky Bucket]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/adaptive-limits|Adaptive Limits]]
