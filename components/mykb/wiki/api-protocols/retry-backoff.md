---
type: "concept"
title: "Retry & Backoff"
description: "Re-attempting failed operations with increasing delays to ride out transient errors"
tags: ["retries", "backoff", "reliability", "resilience", "networking"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://cloud.google.com/storage/docs/retry-strategy", "https://learn.microsoft.com/en-us/dotnet/architecture/microservices/implement-resilient-applications/implement-http-call-retries-exponential-backoff-polly"]
---

# Retry & Backoff

## Summary
Retry with backoff re-attempts failed requests after increasing delays, distinguishing transient failures from permanent ones. It is the standard client-side response to 429, 503, and network errors.

## Details
- Only retry idempotent operations, or carry an idempotency key.
- Combine exponential backoff with jitter and a max retry cap; honor `Retry-After` headers.
- Log retry attempts; escalate to circuit breaking when retries keep failing.
- Retry with backoff re-attempts failed calls while respecting the failure class: transient errors retry, permanent errors do not.
- Backoff grows the delay between attempts so a struggling dependency gets room to recover without being flooded.
- Retry counts, per-attempt timeouts, and circuit-breaker state must all be coordinated or retries make outages worse.
- The protocol matters: idempotent operations are safe to retry; non-idempotent ones need request IDs or exactly-once semantics.
- **Worked example / comparison** — Worked example — a wiki sync worker would retry a failed fetch up to five times with doubling delays, stopping immediately on a 4xx because retrying a bad request will not help.
- For mykb, retry-backoff would be the standard resilience layer for the wiki's source checks and sync jobs.

- Coordination: retry counts, per-attempt timeouts, and circuit-breaker state must all be coordinated or retries make outages worse; the standard pattern is bounded retries with exponential backoff plus jitter, escalating to a breaker.
- Failure classification: transient errors (429, 503, network blips) retry; permanent errors (4xx) do not — the classification is what keeps retries from hammering a target or masking a bug.
- Idempotency requirement: only idempotent operations should be retried, or the request should carry an idempotency key, so a duplicated attempt cannot double-apply a side effect.
- Observability: every retry should be logged with the attempt number and delay, so retry storms are visible in telemetry rather than silent.
## Related
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]]
- [[wiki/api-protocols/jitter|Jitter]]
- [[wiki/api-protocols/idempotency|Idempotency]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
