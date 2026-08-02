---
type: "concept"
title: "Idempotency Keys"
description: "Idempotency-Key headers for retry-safe POST workflows"
tags: ["idempotency", "retries", "reliability", "payments", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://stripe.com/docs/api/idempotent_requests", "https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-idempotency-key-header"]
---

# Idempotency Keys

## Summary
An idempotency key is a client-generated identifier attached to a non-idempotent request so the server can recognize and replay duplicates. The client sends Idempotency-Key: <uuid>; the server stores the keyed outcome and returns the stored response for retries — the pattern that makes POST payments and order creation safe under network retries.

## Details
- Protocol: client generates a key per logical operation and sends it with POST; server keys its state transitions and response on that value.
- Server mechanics: a store mapping key -> (request hash, status, response) with a TTL (24-48h is common); a duplicate key with a different body is an error, not a new operation.
- Scope: one key per operation attempt — a retry of a new operation needs a new key; keys must be unique enough not to collide across users (UUIDs).
- Concurrency: simultaneous duplicates serialize on the key (lock or atomic insert) so both callers get the same result.
- Interaction: idempotency + retry + timeout is the reliable-POST triad; without it, a timeout-then-retry can charge a card twice.
- Extensions: the IETF draft (Idempotency-Key header) and Stripe's implementation are the de facto references; 409 or 422 on key conflicts, 200 with the replay for duplicates.
- Storage: keys need an index; purge expired keys in batch jobs, and never log full key-to-response mappings.

## Related
- [[wiki/api-protocols/idempotency|Idempotency]] — the concept keys implement over HTTP
- [[wiki/api-protocols/retry-policies|Retry Policies]] — retries are only safe with keys
- [[wiki/api-protocols/at-least-once-delivery|At-Least-Once Delivery]] — deduplication across delivery layers
- [[wiki/api-protocols/http-methods|HTTP Methods]] — POST needs keys because it is non-idempotent
- [[wiki/api-protocols/optimistic-concurrency|Optimistic Concurrency]] — conflict handling for concurrent writes
