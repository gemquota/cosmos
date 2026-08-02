---
type: "concept"
title: "Load Shedding"
description: "Rejecting excess load with 503 responses"
tags: ["load-shedding", "overload", "503", "reliability", "capacity"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://netflixtechblog.com/performance-under-load-3e6bc9a7b7ac", "https://aws.amazon.com/builders-library/using-load-shedding-to-avoid-overload/"]
---

# Load Shedding

## Summary
Load shedding is the deliberate rejection of work when a service approaches capacity: return 503 (or a fast synthetic response) instead of queueing requests that would degrade everyone. It protects tail latency and memory by failing fast on excess load, often using randomized admission control.

## Details
- When to shed: queue depth, CPU, or in-flight concurrency crosses a threshold — the system is already at risk, and every queued request makes it worse.
- Why 503 fast is better than 200 slow: shed requests fail in milliseconds, keeping latency percentiles for accepted requests healthy.
- Random admission: reject a small random percentage of traffic as load grows (for example 5% at 80% capacity) — spread across instances to avoid hot spots.
- Prioritized shedding: shed low-value traffic first (background jobs, non-interactive clients, retries) while protecting critical paths.
- Retry storms are the enemy: shed responses must discourage retries — Retry-After plus a clear signal, and clients must respect it (or shed again).
- Synthetic responses: if the service is a gateway for cached data, serve stale or synthetic content rather than dropping the request entirely.
- Measure: track shed rate, accepted latency, and queue depth so shedding thresholds are evidence-based, not guesses.

## Related
- [[wiki/api-protocols/http-status-codes|HTTP Status Codes]] — 503 is the canonical overload signal
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]] — in-flight caps trigger shedding
- [[wiki/api-protocols/backpressure|Backpressure]] — shedding is reject-style backpressure
- [[wiki/api-protocols/rate-limit-algorithms|Rate Limit Algorithms]] — admission control vs rate limits
- [[wiki/api-protocols/retry-policies|Retry Policies]] — clients must not retry shed load blindly
