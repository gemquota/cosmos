---
type: "concept"
title: "Retry with Backoff"
description: "Retrying transient failures with growing delays and jitter to avoid retry storms"
tags: ["retry", "backoff", "resilience", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Retry with Backoff

## Summary
Retry with backoff retries failed operations after delays that grow with each attempt, adding jitter so retries desynchronize. It turns transient failures into blips instead of cascades.

## Details
- Exponential backoff doubles the delay per attempt; jitter randomizes it to avoid thundering herds.
- Budget total retry time: retries consume deadline budgets and can mask real problems.
- Combine with circuit breakers: stop retrying once the dependency is clearly down.
- Open question: which failures are transient enough to retry at all.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — retries enforced by the mesh
- [[wiki/infrastructure/circuit-breaker-pattern|Circuit Breaker Pattern]] — the stop condition for retries
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]] — the delay schedule
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — full pattern reference
