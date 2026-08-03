---
type: "concept"
title: "Retry with Backoff"
description: "Retrying transient failures with growing delays and jitter to avoid retry storms"
tags: ["retry", "backoff", "resilience", "patterns"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
---

# Retry with Backoff

## Summary
Retry with backoff retries failed operations after delays that grow with each attempt, adding jitter so retries desynchronize. It turns transient failures into blips instead of cascades: the first retry comes quickly, later retries wait progressively longer, and jitter keeps thousands of clients from retrying in lockstep — the pattern that turns a small outage into a thundering-herd collapse.

## Details
- Exponential backoff doubles the delay per attempt; jitter randomizes it to avoid thundering herds. The canonical schedule: base delay (say 100ms) × 2^attempt, capped at a maximum (say 30s), with random jitter applied (the standard is "full jitter": a random delay between 0 and the computed value, per AWS's guidance). The reasoning: transient failures need quick retries (the first retry catches the blip), but sustained failures must not be hammered — the growing delay gives the dependency time to recover, and jitter breaks the synchronization that would otherwise make every client retry at the same instant. Without jitter, exponential backoff actually amplifies the problem: all retries align, the dependency gets slammed exactly when it is most vulnerable, and recovery is pushed further out.
- Budget total retry time: retries consume deadline budgets and can mask real problems. A retry loop that runs forever delays the user's failure response, burns the request's deadline, and hides the underlying issue from monitoring (the system looks "slow but working" while every request is actually failing and retrying). The discipline: cap the retry count and the total backoff time, and make the final failure visible — a request that exhausted its retries must surface as a failure, not as an eternal "pending".
- Combine with circuit breakers: stop retrying once the dependency is clearly down. Retries and circuit breakers are designed as a pair: while the dependency looks healthy, retry transient failures; when the failure rate crosses the breaker's threshold, the breaker opens and retries stop — because retrying into a known-down dependency is wasted work that adds load to a system already struggling. The composition rule: retry with backoff in the closed state, respect the open state as a stop signal.
- Open question: which failures are transient enough to retry at all. The retry decision is a classification problem: connection timeouts and 429/503s are retryable; 4xx client errors and validation failures are not (retrying them is guaranteed failure); and the dangerous middle — idempotency — a retry of a non-idempotent operation (a payment, a counter increment) duplicates the effect unless the operation is designed to be safe to repeat.
- For mykb: retry-with-backoff is the sibling of the circuit-breaker pattern — the pair forms the foundation of the resilience-pattern cluster, with service mesh providing the enforcement layer.

## Related
- [[wiki/infrastructure/service-mesh|Service Mesh]] — retries enforced by the mesh
- [[wiki/infrastructure/circuit-breaker-pattern|Circuit Breaker Pattern]] — the stop condition for retries
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]] — the delay schedule
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — full pattern reference
