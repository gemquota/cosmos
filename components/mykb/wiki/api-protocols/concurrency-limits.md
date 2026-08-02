---
type: "concept"
title: "Concurrency Limits"
description: "In-flight limits and adaptive control"
tags: ["concurrency", "limits", "backpressure", "reliability", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://netflixtechblog.com/performance-under-load-3e6bc9a7b7ac", "https://github.com/Netflix/concurrency-limits"]
---

# Concurrency Limits

## Summary
Concurrency limits bound how many requests are in flight at once, protecting a service from overload before queues balloon. Unlike rate limits (requests per time window), concurrency limits cap simultaneous work — and adaptive algorithms (Netflix's concurrency-limits) tune the cap automatically from latency signals.

## Details
- Why in-flight matters: a queue of waiting requests consumes memory and inflates latency; limiting concurrency pushes rejection upstream (fast fail) instead.
- Metrics: in-flight count = started - completed; a limit is the max outstanding at any instant; requests beyond it are queued briefly or rejected.
- Simple policies: fixed cap per instance (workers * small factor), or per downstream dependency (per-dependency limits isolate slow services).
- Adaptive limits: measure latency at the limit — when it rises (or timeouts increase), shrink the cap; when it falls, grow it — Netflix's Vegas-style algorithm.
- Deployment math: limit per instance must account for instance count: N instances each allowing L inflight tolerate N*L before shedding.
- Interaction: concurrency limits pair with retries — a retry storm multiplies in-flight work, so retries must count against the same budget.
- Where applied: connection pools, HTTP client limits, thread pools, and server admission control all implement concurrency limiting.

## Related
- [[wiki/api-protocols/backpressure|Backpressure]] — in-flight limits are load-side backpressure
- [[wiki/api-protocols/load-shedding|Load Shedding]] — rejecting work past the cap
- [[wiki/api-protocols/retry-policies|Retry Policies]] — retries consume the same in-flight budget
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — rate vs concurrency trade-offs
- [[wiki/api-protocols/bulkhead-pattern|Bulkhead Pattern]] — per-dependency concurrency isolation
