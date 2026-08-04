---
type: "entity"
title: "Kafka Connect and Connector Pools"
description: "The framework for running Kafka source/sink connectors at scale"
tags: ["kafka-connect", "connectors", "kafka", "integration"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Kafka Connect and Connector Pools

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Kafka Connect runs connectors as workers in standalone or distributed mode.
- Connector pools let multiple pipelines share workers with controlled parallelism.
- Tasks, offsets, and configuration are managed via REST API and config topics.
- Single Message Transforms (SMTs) handle light routing/filtering without processors.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — Kafka ecosystem
- [[wiki/data-storage/connectors|Connectors]] — connector patterns
- [[wiki/data-storage/debezium-and-cdc-tools|Debezium And Cdc Tools]] — CDC via Connect
- [[wiki/data-storage/dead-letter-topics-and-dlq|Dead Letter Topics And Dlq]] — Connect DLQ handling
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
