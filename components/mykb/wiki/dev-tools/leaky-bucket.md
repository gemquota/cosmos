---
type: "concept"
title: "Leaky Bucket"
description: "A rate limiter that smooths bursts into a fixed output rate"
tags: ["rate-limiting", "leaky-bucket", "algorithm", "traffic"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Leaky Bucket

## Summary
The leaky bucket holds requests in a queue and drains them at a fixed rate, so output is perfectly smooth regardless of input bursts. It protects downstream capacity but can add latency — and a queue without a cap becomes a memory bomb.

## Details
- Mechanism: arrivals join a FIFO queue (the bucket); a drainer releases tokens at a constant rate; if the queue is full, new arrivals are dropped or rejected; output rate is fixed by construction, and burstiness is absorbed by queueing rather than passed through.
- Concrete example: a worker that syncs the wiki to remote sites drains at 10 requests/second — a burst of 1,000 queued links drains smoothly without hammering the source sites; a network adapter shaping outbound traffic to a fixed rate; an API gateway smoothing a spike into a steady downstream load.
- Failure modes: unbounded queue growth when the input rate exceeds the drain rate for long enough — the queue consumes memory and latency grows without limit (always cap depth); drops without backpressure signals, so senders retry and re-fill the queue; drain rate misconfigured below real capacity, adding avoidable latency; the smoothing latency being unacceptable for interactive requests.
- Tradeoffs: the leaky bucket prioritizes a smooth output rate over latency — bursts pay with queueing delay; the token bucket, by contrast, allows bounded bursts for fast output; the choice is whether downstream capacity is rigid (leaky) or can absorb peaks (token).
- Operational notes: monitor queue depth and drain rate, set explicit caps and drop policies, and size the drain rate from real downstream capacity.
- RSIS3 relevance: leaky-bucket the wiki sync queue so link-checking never bursts the source sites — the smoothing that keeps RSIS3's outbound load predictable.

- Apply it where downstream capacity is genuinely fixed, and prefer token buckets where bursts are acceptable.
## Related
- [[wiki/dev-tools/token-bucket|Token Bucket]]
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/sliding-window|Sliding Window]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/dev-tools/backpressure-handling|Backpressure Handling]]
