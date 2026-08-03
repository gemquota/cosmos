---
type: "concept"
title: "Circuit Open State"
description: "The state where a circuit breaker stops calling a failing dependency"
tags: ["circuit-breaker", "resilience", "failures", "states"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Circuit Open State

## Summary
In the open state, a circuit breaker rejects calls to a dependency immediately, without attempting them, for a cooldown window. It protects the failing dependency from overload and the caller from wasting time on doomed requests — the open state is the circuit breaker's strongest protection, and its most dangerous if tuned or observed poorly.

## Details
- Mechanism: after failures exceed the threshold (consecutive or within a window), the breaker transitions from closed to open; while open, every call fails fast with a dedicated error (circuit-open) instead of touching the dependency; after the cooldown elapses, it transitions to half-open and probes with limited traffic.
- Concrete example: a payment client whose breaker opens after 5 failures in 10 seconds; for the next 30 seconds, calls fail in milliseconds with a clear error and a fallback path returns a degraded response; at 30 seconds, one probe call tests the dependency — success closes the breaker, failure reopens it.
- Failure modes: cooldown too short, thrashing between open and half-open as the dependency recovers slowly; cooldown too long, delaying recovery detection and punishing a healthy service; the open state invisible to operators — no logs or metrics, so the dependency recovers but traffic stays rejected; open state ignoring retries, so callers' retry logic multiplies rejected calls; a dependency that fails slowly rather than fast, so the failure threshold never triggers.
- Tradeoffs: the open state trades availability for protection — rejecting calls prevents overload but also fails requests that might have succeeded; the alternative, always trying, risks cascading failure; the design tension is cooldown duration and the probe policy, tuned to the dependency's recovery profile.
- Operational notes: expose breaker state, rejected-call counts, and transition timestamps; alert on prolonged open state; and test the open path in game days.
- RSIS3 relevance: the agent circuit-breaks a flaky tool provider instead of burning retries on it — the open state is the mechanism that turns provider flakiness into fast, observable failure.

## Related
- [[wiki/software-engineering/circuit-breaker-libs|Circuit Breaker Libraries]]
- [[wiki/dev-tools/half-open-state|Half-Open State]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
