---
type: "concept"
title: "Client-Side Retries"
description: "Retries initiated by the client for failed or timed-out requests"
tags: ["retries", "clients", "reliability", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Client-Side Retries

## Summary
Client-side retries re-attempt failed requests automatically — with backoff and jitter — to ride out transient failures. They work well for idempotent calls; for others they need idempotency keys or careful design.

## Details
- Retry only on transient failures: timeouts, 5xx, connection resets — not 4xx.
- Budget total retry time so the user is not stuck behind an endless loop.
- Add jittered backoff and honor Retry-After to stay a good citizen.
- mykb relevance: the fetcher retries sources on transient failures with backoff caps.

## Related
- [[wiki/software-engineering/exponential-backoff-practice|Exponential Backoff Practice]]
- [[wiki/tooling/client-side-timeouts|Client-Side Timeouts]]
- [[wiki/software-engineering/retry-after|Retry-After]]
- [[wiki/software-engineering/retry-patterns|Retry Patterns]]
- [[wiki/tooling/idempotency-design|Idempotency Design]]
