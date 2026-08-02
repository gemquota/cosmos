---
type: "concept"
title: "Dead Letter Queues and Retries"
description: "Routing failed messages to a quarantine queue after retries are exhausted"
tags: ["dlq", "retries", "messaging", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dead Letter Queues and Retries

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A DLQ holds messages that repeatedly fail processing so they do not block the main pipeline or get silently dropped.
- Retry policies wrap each attempt: immediate retries, exponential backoff, and a max-attempts threshold before DLQ routing.
- DLQ handling needs monitoring, replay tooling, and a repair path back into the pipeline once the root cause is fixed.
- For data pipelines the DLQ is often a topic, table, or object-store prefix with original payload plus error metadata.

## Related

- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — foundational note on DLQ mechanics
- [[wiki/data-storage/backpressure|Backpressure]] — how slow consumers trigger failures upstream
- [[wiki/data-storage/idempotent-writes-and-upserts|Idempotent Writes And Upserts]] — safe replay of DLQ records
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — alerting when DLQ volume grows
- [[wiki/data-storage/dead-letter-data-and-repair-pipelines|Dead Letter Data and Repair Pipelines]] — repair flows for quarantined records
- [[wiki/api-services/retry-strategies-and-backoff-jitter|Retry Strategies And Backoff Jitter]] — API-side retry design
