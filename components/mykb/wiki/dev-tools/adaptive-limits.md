---
type: "concept"
title: "Adaptive Limits"
description: "Concurrency limits that adjust automatically from observed latency and error signals"
tags: ["rate-limiting", "adaptive", "concurrency", "resilience"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Adaptive Limits

## Summary
Adaptive limits tune in-flight concurrency from live signals instead of static config: when latency climbs, the limit shrinks; when the system is healthy, it grows. Algorithms like Netflix concurrency-limits use queue-time estimates to converge on the knee of the latency curve — the operating point where throughput is maximized without letting queueing dominate.

## Details
- Mechanism: measure the no-load baseline latency (the min over recent samples); compare each request's observed latency to the baseline — the difference approximates queueing time; adjust the in-flight limit proportionally (e.g. Vegas-style: decrease when queue time exceeds a target, increase slowly when below); the limit converges to the concurrency at which the service is just saturated.
- Concrete example: Netflix concurrency-limits with Vegas or Gradient2 in an API client: on a healthy dependency the limit rises to hundreds of in-flight calls; when latency spikes, it cuts to a few in seconds, then climbs back; integrated with a circuit breaker, repeated failures can force a reset.
- Failure modes: noisy latency (non-stationary traffic) causing limit thrashing — smooth with EWMA or require sustained signal; the baseline being contaminated by queueing, so the limit never recovers; ignoring error rates, so the limiter keeps adding load to a failing dependency; instrumentation gaps — without good latency percentiles and in-flight counts, the algorithm fights itself.
- Tradeoffs: adaptive limits remove the capacity-tuning burden and react to real conditions, but they add algorithm parameters and require signal quality; static limits are predictable and simple but wrong whenever traffic changes; the payoff is full provider capacity without burning it during degradation.
- Operational notes: log the current limit and its movements, pair with timeouts so slots are not held by hung calls, and alert when the limit stays pinned low.
- RSIS3 relevance: adaptive limits let the agent pool use full provider capacity without burning it — exactly the signal-driven behavior RSIS3 wants in its own loops.

## Related
- [[wiki/api-protocols/concurrency-limits|Concurrency Limits]]
- [[wiki/dev-tools/concurrency-limiters|Concurrency Limiters]]
- [[wiki/dev-tools/rate-limiting-algorithms|Rate Limiting Algorithms]]
- [[wiki/dev-tools/tail-latency|Tail Latency]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
