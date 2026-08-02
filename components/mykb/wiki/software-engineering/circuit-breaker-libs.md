---
type: "concept"
title: "Circuit Breaker Libraries"
description: "Libraries that implement open/closed/half-open failure gating for calls"
tags: ["circuit-breaker", "libraries", "resilience", "tooling"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Circuit Breaker Libraries

## Summary
Circuit breaker libraries (Hystrix lineage, Resilience4j, Polly, Sentinel) wrap calls to dependencies with stateful failure gating: trips open after errors, probes half-open, recovers closed. They save dependencies from overload and callers from wasted retries.

## Details
- Key knobs: failure threshold, cooldown window, half-open probe size, per-dependency instances.
- Libraries add metrics and hooks, but policy correctness is still your design job.
- Pick per stack: Resilience4j (JVM), Polly (.NET), Hystrix (legacy), tenacity (Python).
- mykb relevance: the agent wraps model providers in a breaker library to fail fast on outages.

## Related
- [[wiki/dev-tools/circuit-open-state|Circuit Open State]]
- [[wiki/dev-tools/half-open-state|Half-Open State]]
- [[wiki/software-engineering/resilience-libs|Resilience Libraries]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/software-engineering/reliability-engineering|Reliability Engineering]]
