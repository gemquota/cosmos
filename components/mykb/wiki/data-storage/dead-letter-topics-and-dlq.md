---
type: "concept"
title: "Dead Letter Topics and DLQ"
description: "Kafka topics that hold undeliverable or unprocessable records"
tags: ["dlq", "kafka", "dead-letter", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Dead Letter Topics and DLQ

## Summary
A DLQ topic captures records that failed processing after retries, preserving the payload for inspection and replay. Consumers write poison messages — deserialization failures, repeated errors — to the DLQ with error context in headers, so the main stream keeps flowing and nothing is silently lost.

## Details
- Mechanism: the consumer processes records with a retry policy; after max attempts or on non-retryable errors, the record is produced to a DLQ topic with headers carrying error class, attempts, and the last failure reason; operators monitor DLQ growth and replay records after fixing the cause; replay re-injects into the pipeline, ideally through the same ingestion path for validation.
- Concrete example: a Kafka consumer of wiki events fails to parse a record; retries with backoff exhaust; the record lands in wiki.dlq with an error-type header; an alert fires when DLQ lag grows; after the parser fix, a replay job re-sends the record, and idempotent downstream writes make the re-processing safe.
- Failure modes: DLQ topics without retention or compaction limits, growing unboundedly; no alerting on DLQ depth, so failures hide until data is needed; replay without idempotency, duplicating side effects; DLQ records lacking headers, so triage requires re-deriving the error; poison messages replayed in a loop by automation, re-poisoning the pipeline.
- Tradeoffs: DLQ topics trade pipeline simplicity for durability — a record is never dropped, only deferred; the alternative, dropping after retries, is simpler and loses data; the mature pattern is bounded retries, header-rich DLQs, depth alerting, and a rehearsed, idempotent replay path.
- Operational notes: monitor DLQ depth and age, cap DLQ retention deliberately, and test the replay path in drills.
- RSIS3 relevance: RSIS3's ingestion pipeline benefits from the same quarantine — a malformed article should be inspectable and replayable, not a silent loss.

## Related

- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — DLQ fundamentals
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues and Retries]] — retry policies
- [[wiki/data-storage/dead-letter-data-and-repair-pipelines|Dead Letter Data and Repair Pipelines]] — repair flows
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — alerting on DLQ
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
