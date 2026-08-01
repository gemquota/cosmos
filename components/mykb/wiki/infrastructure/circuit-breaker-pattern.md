---
type: "concept"
title: "Circuit Breaker Pattern"
description: "Failing fast when a dependency degrades, protecting callers from cascading failure"
tags: ["circuit-breaker", "resilience", "patterns", "microservices"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Circuit Breaker Pattern

## Summary
A circuit breaker trips when a dependency's failure rate crosses a threshold, short-circuiting calls instead of letting them pile up. It converts dependency outages into fast, controlled failures.

## Details
- States: closed (normal), open (failing fast), half-open (probing recovery).
- Thresholds, timeouts, and probe intervals are tuned per dependency — the api-protocols article has the full mechanics.
- Pair with retries and backoff carefully: retrying into an open circuit makes everything worse.
- Open question: how circuit breakers and error budgets should share failure accounting.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — mesh-level circuit breaking
- [[wiki/infrastructure/retry-with-backoff|Retry with Backoff]] — the sibling pattern
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — full pattern mechanics
- [[wiki/infrastructure/bulkhead-pattern|Bulkhead Pattern]] — isolation complement
