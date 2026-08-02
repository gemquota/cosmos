---
type: "concept"
title: "Adaptive Limits"
description: "Concurrency limits that adjust automatically from observed latency and error signals"
tags: ["rate-limiting", "adaptive", "concurrency", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Adaptive Limits

## Summary
Adaptive limits tune in-flight concurrency from live signals instead of static config: when latency climbs, the limit shrinks; when the system is healthy, it grows. Algorithms like Netflix concurrency-limits use queue-time estimates to converge on the knee of the latency curve.

## Details
- Use the difference between observed latency and the no-load baseline to detect queueing.
- Reduce concurrency proportionally on latency or error spikes; increase it slowly when healthy.
- Needs good instrumentation — latency percentiles and in-flight counts — or it fights itself.
- mykb relevance: adaptive limits let the agent pool use full provider capacity without burning it.

## Related
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]]
- [[wiki/dev-tools/concurrency-limiters|Concurrency Limiters]]
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/tail-latency|Tail Latency]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
