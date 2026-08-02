---
type: "concept"
title: "Retry Policies"
description: "Retry budgets, caps, and idempotent retry design"
tags: ["retries", "retry-policies", "reliability", "backoff", "distributed-systems"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/", "https://cloud.google.com/architecture/exponential-backoff"]
---

# Retry Policies

## Summary
A retry policy decides when a failed call is retried, how fast attempts back off, and when to give up. The design space — retryable errors, exponential backoff with jitter, per-call and per-client budgets, and circuit breakers — separates resilient systems from ones that amplify outages.

## Details
- Retryable errors only: 429/503/504, connection resets, and gRPC Unavailable/DeadlineExceeded; never retry 4xx validation or auth failures.
- Backoff: exponential (1s, 2s, 4s ...) with full jitter (random between 0 and cap) to avoid synchronized retry storms after an outage.
- Budgets: cap attempts per call (3-5), cap total retry time relative to the deadline, and cap aggregate retry rate (percentage of original traffic) to avoid amplifying load.
- Idempotency prerequisite: retrying a non-idempotent POST needs an Idempotency-Key; otherwise retries double side effects.
- Circuit breaking: after repeated failures, stop trying for a cool-down window and fail fast — protects a struggling dependency from retry pressure.
- Retry-After and Retry-Once: honor server hints; Retry-Once prevents tight retry loops with 503s.
- Observe: instrument attempts, successes, and exhaustion; retry storms are a leading cause of cascading failures.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — the timing mechanics of retries
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]] — the growth schedule with jitter
- [[wiki/api-protocols/idempotency-keys|Idempotency Keys]] — retries require idempotent operations
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — failing fast instead of retrying a dead service
- [[wiki/api-protocols/deadline-propagation|Deadline Propagation]] — retries must respect the overall deadline
