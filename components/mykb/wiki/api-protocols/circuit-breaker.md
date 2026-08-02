---
type: "concept"
title: "Circuit Breaker"
description: "Failing fast when a downstream service degrades, preventing cascading failures"
tags: ["circuit-breaker", "resilience", "distributed-systems", "failures"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://martinfowler.com/bliki/CircuitBreaker.html", "https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern"]
---

# Circuit Breaker

## Summary
A circuit breaker wraps calls to a dependency and trips open when failures exceed a threshold, failing fast instead of waiting on timeouts. It half-opens after a cooldown to test recovery.

## Details
- States: closed (normal), open (fail fast), half-open (probe with limited traffic).
- Track failure rates, not just errors; respect dependency health and recovery time.
- Envoy and Istio implement it at the mesh layer; libraries exist per language.
- A circuit breaker wraps a failing dependency and trips open after a threshold of failures, so callers fail fast instead of waiting on a dead service.
- It has three states: closed (normal), open (fail fast), and half-open (allow a probe request to test recovery); the half-open window decides when to close again.
- Timeouts, failure counts, and success thresholds tune how aggressively the breaker trips; a good breaker also surfaces its state for observability.
- It differs from retry: retries assume transient failure, while a breaker assumes the dependency is down and stops hammering it.
- **Worked example / comparison** — Worked example — the wiki's search service breaker trips after five 5-second timeouts; subsequent requests fail in milliseconds until a half-open probe succeeds.
- For mykb, circuit breakers are documented as the sibling of retry-backoff for protecting the wiki's external dependencies.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]]
- [[wiki/api-protocols/timeouts|Timeouts]]
- [[wiki/devops-infra/istio|Istio]]
- [[wiki/devops-infra/envoy|Envoy]]
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
