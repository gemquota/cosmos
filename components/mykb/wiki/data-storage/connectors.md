---
type: "concept"
title: "Connectors"
description: "Reusable source/sink adapters that move data between systems"
tags: ["connectors", "ingestion", "kafka-connect", "integration"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Connectors

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Connectors wrap a source or sink's API into a standard sync contract (e.g., Kafka Connect).
- Good connectors handle schema, retries, checkpointing, and incremental state.
- Connector sprawl is a governance problem: catalog, test, and version them.
- Frameworks: Kafka Connect, Airbyte CDK, Flink connectors, and vendor SDKs.

## Related

- [[wiki/data-storage/data-pipeline-orchestration|Data Pipeline Orchestration]] — pipeline management
- [[wiki/data-storage/kafka-connect-and-connector-pools|Kafka Connect And Connector Pools]] — Kafka Connect specifics
- [[wiki/data-storage/fivetran-and-airbyte|Fivetran And Airbyte]] — managed connector libraries
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — sink/source patterns
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
