---
type: "concept"
title: "Leaky Bucket"
description: "A rate limiter that smooths bursts into a fixed output rate"
tags: ["rate-limiting", "leaky-bucket", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Leaky Bucket

## Summary
The leaky bucket holds requests in a queue and drains them at a fixed rate, so output is perfectly smooth regardless of input bursts. It protects downstream capacity but can add latency and drop excess arrivals.

## Details
- Smoothing is the point: constant output rate, bounded queue depth, overflow drops or rejects.
- Contrast with token bucket, which allows bursts; choose based on whether bursts are safe.
- Queue-based variants add latency and need a cap or they become a memory bomb.
- mykb relevance: leaky-bucket the wiki sync queue so link-checking never bursts the source sites.

## Related
- [[wiki/dev-tools/token-bucket|Token Bucket]]
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
