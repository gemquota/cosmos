---
type: "concept"
title: "Dead Letter Topics and DLQ"
description: "Kafka topics that hold undeliverable or unprocessable records"
tags: ["dlq", "kafka", "dead-letter", "reliability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Dead Letter Topics and DLQ

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- A DLQ topic captures records that failed processing after retries, preserving the payload.
- Consumers write poison messages (deserialization failures, repeated errors) to the DLQ.
- Operators replay DLQ records after fixing the cause; headers can carry error context.
- Monitor DLQ growth as a health signal; unbounded growth hides real problems.

## Related

- [[wiki/data-storage/dead-letter-queues|Dead Letter Queues]] — DLQ fundamentals
- [[wiki/data-storage/dead-letter-queues-and-retries|Dead Letter Queues and Retries]] — retry policies
- [[wiki/data-storage/dead-letter-data-and-repair-pipelines|Dead Letter Data and Repair Pipelines]] — repair flows
- [[wiki/infrastructure/etl-observability-and-alerting|Etl Observability And Alerting]] — alerting on DLQ
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
