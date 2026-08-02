---
type: "concept"
title: "Circuit Open State"
description: "The state where a circuit breaker stops calling a failing dependency"
tags: ["circuit-breaker", "resilience", "failures", "states"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Circuit Open State

## Summary
In the open state, a circuit breaker rejects calls to a dependency immediately, without attempting them, for a cooldown window. It protects the dependency from overload and the caller from wasting time on a doomed request.

## Details
- Open happens after failures exceed a threshold; every call during open fails fast with a specific error.
- The open state must be observable — logs, metrics, and a counter for rejected calls.
- Choose cooldown sensibly: too short thrashes, too long delays recovery detection.
- mykb relevance: the agent circuit-breaks a flaky tool provider instead of burning retries on it.

## Related
- [[wiki/software-engineering/circuit-breaker-libs|Circuit Breaker Libraries]]
- [[wiki/dev-tools/half-open-state|Half-Open State]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/dev-tools/timeout-policy|Timeout Policy]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
