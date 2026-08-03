---
type: "concept"
title: "Circuit Breaker Pattern"
description: "Failing fast when a dependency degrades, protecting callers from cascading failure"
tags: ["circuit-breaker", "resilience", "patterns", "microservices"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Circuit Breaker Pattern

## Summary
A circuit breaker trips when a dependency's failure rate crosses a threshold, short-circuiting calls instead of letting them pile up. It converts dependency outages into fast, controlled failures. The pattern is named for the electrical circuit breaker because it plays the same role: when the downstream is overloaded, cut the flow rather than feeding the fault.

## Details
- States: closed (normal), open (failing fast), half-open (probing recovery). In the closed state, calls flow normally and failures are counted; when the failure rate (or consecutive-failure count) exceeds a threshold, the breaker opens. In the open state, calls fail immediately with a fast error — no attempt to reach the dependency — protecting both the caller (no timeout waiting) and the dependency (no load from a system that is already struggling). After a cooldown period, the breaker moves to half-open: it lets a small probe of traffic through, and if the probes succeed, it closes; if they fail, it reopens. This is the recovery loop that makes the pattern self-healing.
- Thresholds, timeouts, and probe intervals are tuned per dependency — the api-protocols article has the full mechanics. The tuning knobs: the failure-rate threshold (how much degradation tolerates), the timeouts that define "failure" (a dependency that hangs for 30s is failing even if it eventually answers), the open-state cooldown (how long to wait before probing), and the half-open probe count. Each depends on the dependency's characteristics — a flaky-but-essential dependency needs a higher threshold than a critical one — and the tuning is operational work, not a one-time setting.
- Pair with retries and backoff carefully: retrying into an open circuit makes everything worse. The retry and breaker patterns interact: if a caller retries aggressively and the breaker is open, the retries are wasted work (fast failures, but multiplied); if the breaker is closed and the dependency is failing, retries add load to a system that is already down. The correct composition: retry with backoff on the closed state, and respect the breaker's open state as a signal to stop retrying — which is why the two patterns are always documented together.
- Open question: how circuit breakers and error budgets should share failure accounting — the breaker protects one dependency; the error budget governs a service's overall reliability, and coordinating the two (when does a breaker trip count against the budget?) is an unsolved operational design question.
- For mykb: the node anchors the resilience-pattern cluster, with service mesh, retry/backoff, and bulkhead as its siblings.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — mesh-level circuit breaking
- [[wiki/infrastructure/retry-with-backoff|Retry with Backoff]] — the sibling pattern
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — full pattern mechanics
- [[wiki/infrastructure/bulkhead-pattern|Bulkhead Pattern]] — isolation complement
