---
type: "concept"
title: "Circuit Breaker"
description: "Failing fast when a downstream service degrades, preventing cascading failures"
tags: ["circuit-breaker", "resilience", "distributed-systems", "failures"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Circuit Breaker

## Summary
A circuit breaker wraps calls to a dependency and trips open when failures exceed a threshold, failing fast instead of waiting on timeouts. It half-opens after a cooldown to test recovery.

## Details
- States: closed (normal), open (fail fast), half-open (probe with limited traffic).
- Track failure rates, not just errors; respect dependency health and recovery time.
- Envoy and Istio implement it at the mesh layer; libraries exist per language.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — retries belong before tripping
- [[wiki/api-protocols/timeouts|Timeouts]] — bound per-call latency
- [[wiki/devops-infra/istio|Istio]] — mesh-level circuit breaking
- [[wiki/devops-infra/envoy|Envoy]] — proxy-level resilience
- [[wiki/api-protocols/graceful-shutdown|Graceful Shutdown]] — clean degradation at exit
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — both protect services from overload
