---
type: "concept"
title: "Idempotent Writes and Upserts"
description: "Replaying the same write multiple times without corrupting state"
tags: ["idempotency", "upsert", "data-ingestion", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Idempotent Writes and Upserts

## Summary
An idempotent write produces the same final state no matter how many times it is applied, which makes retries safe. Upserts implement idempotency at the row level via primary keys; deduplication keys implement it at the event level — the precondition for at-least-once pipelines to behave like exactly-once.

## Details
- Mechanism: upserts use a primary key so re-applying a write overwrites instead of duplicating; event-level deduplication keys (a message ID, a natural business key) let a consumer recognize a replay; last-write-wins policies use operation timestamps; first-write-wins keeps the original; merge patterns combine incoming and existing state.
- Concrete example: a wiki event pipeline replays a batch after a failure; each article update upserts on slug, so re-processing converges to the same state; a payment event carries an idempotency key so a retried delivery does not double-charge; a merge pattern updates only changed fields, preserving concurrent edits.
- Failure modes: upserts on the wrong key (a mutable attribute), causing duplicate rows; timestamps with clock skew breaking last-write-wins; deduplication state lost, so replays duplicate; non-idempotent side effects (emails, external calls) firing on every attempt; retry logic that changes the payload between attempts, so the key no longer matches.
- Tradeoffs: idempotent writes cost a key design and dedup state but make retries and replays safe; the alternative — assume-once semantics — is simpler and corrupts under retries; the mature pattern is natural keys or idempotency keys, timestamped writes, and idempotent side effects.
- Operational notes: test replay behavior in CI, monitor dedup hit rates, and document the key per entity.
- RSIS3 relevance: RSIS3's state writes (checkpoints, registry updates) need idempotency so a retried loop step cannot corrupt state — the same upsert discipline as any ingestion pipeline.

## Related

- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — existing note on idempotent ingestion
- [[wiki/data-storage/deduplication|Deduplication]] — removing duplicate events before writes
- [[wiki/data-storage/merge-and-upsert-patterns|Merge And Upsert Patterns]] — how merges express idempotent writes
- [[wiki/data-storage/exactly-once-processing|Exactly Once Processing]] — idempotency as the engine guarantee
- [[wiki/api-services/idempotency-keys-in-apis|Idempotency Keys In Apis]] — API-level idempotency keys
