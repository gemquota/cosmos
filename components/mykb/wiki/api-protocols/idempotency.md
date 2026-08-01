---
type: "concept"
title: "Idempotency"
description: "Guaranteeing repeated identical requests produce the same result, enabling safe client retries"
tags: ["idempotency", "api", "reliability", "retries", "distributed-systems"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://stripe.com/docs/api/idempotent_requests"]
---

# Idempotency

## Summary
An operation is idempotent if repeating it with the same input yields the same outcome as a single execution. HTTP methods like GET, PUT, and DELETE are idempotent by design, while POST is not. Because networks lose messages and clients retry, idempotency keys let servers deduplicate requests — the pattern Stripe popularized for payment APIs.

## Details
- Method semantics: GET/PUT/DELETE/HEAD idempotent; POST and PATCH not guaranteed (PATCH is often made idempotent with `If-Match`).
- Idempotency keys: the client sends a unique key header; the server stores the keyed result and replays it on duplicate submission.
- Server mechanics: a key-value store (Redis or a database table) records `{key, request-hash, status, response}` with a TTL; concurrent duplicates serialize on the key.
- Worked example: mykb session capture POSTs note chunks; a retry after a timeout would otherwise duplicate a note. A `Idempotency-Key: session-123-chunk-4` header fixes it.
- Interaction: idempotency plus [[wiki/api-protocols/retry-backoff|retry & backoff]] plus [[wiki/api-protocols/timeouts|timeouts]] is the reliability triad for API clients.
- Distributed note: exactly-once is impossible; idempotency gives effective-once semantics across at-least-once delivery.

## Related
- [[wiki/api-protocols/retry-backoff|Retry & Backoff]] — retries are only safe with idempotent operations
- [[wiki/api-protocols/rest-apis|REST APIs]] — method semantics define idempotency
- [[wiki/api-protocols/timeouts|Timeouts]] — what triggers the retry in the first place
- [[wiki/api-protocols/webhooks|Webhooks]] — delivery retries replay the same payload
- [[wiki/devops-infra/transactions|Transactions]] — database-level atomicity underpins dedup
- [[wiki/ops/gap-report|Gap Analysis Report]] — reliability gaps in daemon writes
- [[wiki/concepts/triad-architecture|Triad Architecture]] — retry semantics across the engine-memory bridge
