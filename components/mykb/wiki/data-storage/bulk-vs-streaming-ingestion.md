---
type: "concept"
title: "Bulk vs Streaming Ingestion"
description: "Choosing how data enters the platform"
tags: ["ingestion", "batch", "streaming", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Data_pipeline", "https://kafka.apache.org/documentation/"]
---

# Bulk vs Streaming Ingestion

## Summary

Bulk ingestion loads data in scheduled batches; streaming ingests continuously.
The choice sets freshness, complexity, and cost.
Many platforms run both for different data classes.
The real question is freshness economics: how much are minutes of latency worth?

## Details

- Bulk: simpler, cost-efficient, bounded; freshness by schedule.
- Streaming: low latency, event-driven, operationally complex.
- CDC is streaming for databases; files are bulk for lakes.
- Hybrid patterns: batch backfill plus streaming catch-up.
- Match ingestion mode to consumer latency needs.
- Reuse one pipeline codebase for both modes where possible.
- CDC streaming plus nightly batch covers most patterns.
- Ingestion mode is a latency and cost decision, not an ideology.

## Related

- [[wiki/data-storage/streaming-data-pipelines|Streaming Data Pipelines]] — streaming
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental
- [[wiki/data-storage/change-data-capture|Change Data Capture]] — CDC
- [[wiki/data-storage/batch-vs-stream-processing|Batch vs Stream Processing]] — existing note
- [[wiki/data-storage/data-import-export-patterns|Data Import Export Patterns]] — exchange
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — data contracts
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

