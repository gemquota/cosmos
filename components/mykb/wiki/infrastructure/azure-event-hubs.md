---
type: "entity"
title: "Azure Event Hubs"
description: "Azure's high-throughput event ingestion service with Kafka compatibility"
tags: ["event-hubs", "azure", "event-streaming", "ingestion"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Azure Event Hubs

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Event Hubs ingests millions of events per second into partitions with retention windows.
- It exposes an AMQP API and Kafka-compatible endpoints for ecosystem reuse.
- Consumer groups and checkpointing mirror Kafka consumer semantics.
- Events age out by retention unless forwarded to storage or stream analytics.

## Related

- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — event streaming concepts
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — downstream processing
- [[wiki/data-storage/consumer-groups-and-offsets|Consumer Groups And Offsets]] — consumer group model
- [[wiki/infrastructure/azure-synapse|Azure Synapse]] — analytics destination in Azure
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
