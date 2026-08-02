---
type: "concept"
title: "Stream-Table Duality"
description: "Streams and tables as two views of the same data"
tags: ["stream-table-duality", "kafka", "flink", "semantics"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kafka.apache.org/documentation/", "https://nightlies.apache.org/flink/flink-docs-stable/"]
---

# Stream-Table Duality

## Summary

A stream is an append-only log of events; a table is the current state derived from it.
Any stream can be materialized into a table, and any table's changelog is a stream.
The duality unifies batch and streaming programming.
The duality is why kappa architectures can rebuild state from logs alone.

## Details

- Changelog topics compact to tables (latest value per key).
- Flink dynamic tables run continuous SQL over streams.
- ksqlDB and Kafka Streams build on the duality directly.
- Joins between streams and tables mix both views.
- It simplifies reprocessing: rebuild tables from retained logs.
- Compacted topics and changelogs are the table side of the duality.
- Continuous SQL makes batch and streaming share one mental model.
- The duality is the intellectual foundation of kappa architectures and modern stream-table processing.

## Related

- [[wiki/data-storage/stream-table-duality|Stream-Table Duality]] — duality in ksqlDB
- [[wiki/data-storage/log-compaction-and-keys|Log Compaction And Keys]] — compact to table
- [[wiki/data-storage/stream-reprocessing-and-backfills|Stream Reprocessing And Backfills]] — replay
- [[wiki/data-storage/kappa-architecture|Kappa Architecture]] — log-first architecture
- [[wiki/data-storage/stream-processing-engines|Stream Processing Engines]] — engines

