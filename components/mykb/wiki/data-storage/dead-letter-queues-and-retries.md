---
type: "concept"
title: "Dead Letter Queues and Retries"
description: "Routing failed messages to a quarantine queue after retries are exhausted"
tags: ["dlq", "retries", "messaging", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dead Letter Queues and Retries

## Summary
A DLQ holds messages that repeatedly fail processing so they do not block the main pipeline or get silently dropped. Retry policies wrap each attempt — immediate retries, exponential backoff, a max-attempts threshold — and only after they are exhausted does the message route to the quarantine.

## Details
- Mechanism: a consumer tries the message with a retry policy (backoff schedule, max attempts); failures beyond the threshold route the message to a DLQ with the original payload plus error metadata (attempts, error class, last failure reason); the main queue keeps flowing; the DLQ is monitored, replayed, and repaired.
- Concrete example: an order event fails JSON validation; retries with backoff exhaust after 5 attempts; the message lands in the DLQ tagged with the validation error; an alert fires on DLQ depth; after the schema fix, a replay tool re-injects the message into the pipeline; a poison message (permanently unprocessable) stays quarantined for inspection.
- Failure modes: retry storms — immediate retries hammering a broken dependency (add backoff and jitter); DLQs that fill silently because no alerting or depth monitoring exists; replaying without idempotent processing, duplicating side effects; repair paths that do not exist, so quarantined data rots; DLQ messages without error metadata, making triage guesswork.
- Tradeoffs: DLQs trade pipeline simplicity for durability and debuggability — a message is never lost, only deferred; the alternative, dropping after retries, is simpler and loses data; the mature pattern is bounded retries with backoff, DLQ routing with metadata, alerting on depth, and a rehearsed replay path.
- Operational notes: monitor DLQ depth and age, document the replay procedure, and make consumers idempotent so replay is safe.
- RSIS3 relevance: RSIS3's ingestion pipeline needs the same quarantine — a malformed article should not block the batch, and its error metadata should survive for repair and learning.

## Related

- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — foundational note on DLQ mechanics
- [[wiki/data-storage/backpressure|Backpressure]] — how slow consumers trigger failures upstream
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — safe replay of DLQ records
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — alerting when DLQ volume grows
- [[wiki/data-storage/dead-letter-data-and-repair-pipelines|Dead Letter Data and Repair Pipelines]] — repair flows for quarantined records
- [[wiki/api-services/retry-strategies-and-backoff-jitter|Retry Strategies And Backoff Jitter]] — API-side retry design
