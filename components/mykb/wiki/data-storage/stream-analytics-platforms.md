---
type: "concept"
title: "Stream Analytics Platforms"
description: "Fully managed platforms for SQL stream processing"
tags: ["stream-analytics", "flink", "kinesis-analytics", "platforms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Stream Analytics Platforms

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Managed platforms (Kinesis Analytics, Confluent, Azure Stream Analytics, GCP Dataflow) run SQL over streams.
- They remove cluster operations but constrain topology and state control.
- Typical features: windows, joins, watermarks, and sink connectors.
- Evaluate against self-managed Flink/Spark when control matters.

## Related

- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engines
- [[wiki/data-storage/flink-stream-processing|Flink Stream Processing]] — Flink
- [[wiki/infrastructure/kinesis-and-kinesis-analytics|Kinesis And Kinesis Analytics]] — AWS option
- [[wiki/data-storage/stream-table-duality|Stream Table Duality]] — semantics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
