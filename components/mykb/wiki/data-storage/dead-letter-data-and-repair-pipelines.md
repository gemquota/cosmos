---
type: "concept"
title: "Dead Letter Data and Repair Pipelines"
description: "Recovering bad records instead of losing them"
tags: ["dlq", "repair", "recovery", "data-quality"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dead Letter Data and Repair Pipelines

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Repair pipelines replay DLQ/quarantine records after fixing the cause.
- Preserve original payloads and error context for diagnosis.
- Replay must be idempotent to survive partial failures.
- Track DLQ age; stale records indicate unresolved root causes.

## Related

- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — DLQ
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues And Retries]] — retry policies
- [[wiki/data-storage/quarantine-and-bad-data-handling|Quarantine And Bad Data Handling]] — quarantine
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — safe replay
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
