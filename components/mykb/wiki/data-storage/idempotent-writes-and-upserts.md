---
type: "concept"
title: "Idempotent Writes and Upserts"
description: "Replaying the same write multiple times without corrupting state"
tags: ["idempotency", "upsert", "data-ingestion", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Idempotent Writes and Upserts

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- An idempotent write produces the same final state no matter how many times it is applied, which makes retries safe.
- Upserts implement idempotency at the row level via primary keys; deduplication keys implement it at the event level.
- Natural keys plus operation timestamps allow 'last write wins' or first-write-wins policies.
- Idempotent ingestion is a precondition for at-least-once pipelines to behave like exactly-once.

## Related

- [[wiki/data-storage/idempotent-ingestion|Idempotent Ingestion]] — existing note on idempotent ingestion
- [[wiki/data-storage/deduplication|Deduplication]] — removing duplicate events before writes
- [[wiki/data-storage/merge-and-upsert-patterns|Merge And Upsert Patterns]] — how merges express idempotent writes
- [[wiki/data-storage/exactly-once-processing|Exactly Once Processing]] — idempotency as the engine guarantee
- [[wiki/api-services/idempotency-keys-in-apis|Idempotency Keys In Apis]] — API-level idempotency keys
