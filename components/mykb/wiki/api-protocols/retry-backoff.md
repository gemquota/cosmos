---
type: "concept"
title: "Retry & Backoff"
description: "Re-attempting failed operations with increasing delays to ride out transient errors"
tags: ["retries", "backoff", "reliability", "resilience", "networking"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Retry & Backoff

## Summary
Retry with backoff re-attempts failed requests after increasing delays, distinguishing transient failures from permanent ones. It is the standard client-side response to 429, 503, and network errors.

## Details
- Only retry idempotent operations, or carry an idempotency key.
- Combine exponential backoff with jitter and a max retry cap; honor `Retry-After` headers.
- Log retry attempts; escalate to circuit breaking when retries keep failing.

## Related
- [[wiki/api-protocols/exponential-backoff|Exponential Backoff]] — the delay schedule
- [[wiki/api-protocols/jitter|Jitter]] — desynchronizes retry storms
- [[wiki/api-protocols/idempotency|Idempotency]] — makes retries safe
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — server-side counterpart
- [[wiki/api-protocols/circuit-breaker|Circuit Breaker]] — stops endless retrying
