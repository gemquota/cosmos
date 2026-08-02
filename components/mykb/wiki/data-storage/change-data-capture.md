---
type: "concept"
title: "Change Data Capture"
description: "Capturing row-level changes from database transaction logs"
tags: ["cdc", "replication", "streaming", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Change_data_capture", "https://debezium.io/documentation/reference/stable/"]
---

# Change Data Capture

## Summary

Change data capture (CDC) reads database transaction logs and turns row changes into events.
It gives low-latency, reliable change streams without taxing the source with queries.
CDC powers streaming ETL, event-driven architectures, and cache/warehouse synchronization.
CDC turns databases into event producers, enabling event-driven architectures without source changes.

## Details

- Log-based CDC (Postgres WAL, MySQL binlog) captures inserts, updates, deletes, and DDL.
- Tools: Debezium, Maxwell, and native replication protocols.
- CDC events carry before/after images plus metadata for exactly-once downstream handling.
- Initial snapshot plus continuous capture is the standard bootstrap.
- Combine with the outbox pattern for reliable event publication.
- Monitor CDC lag and slot usage; stalled consumers grow logs and degrade sources.
- Schema changes (DDL) need handling policies in any CDC pipeline.
- CDC pipelines should be treated as first-class streaming citizens with monitoring, schema governance, and replay capability.

## Related

- [[wiki/data-storage/debezium-and-cdc-tools|Debezium And Cdc Tools]] — tooling
- [[wiki/data-storage/transactional-outbox-and-cdc-relay|Transactional Outbox And Cdc Relay]] — outbox + CDC
- [[wiki/data-storage/streaming-data-pipelines|Streaming Data Pipelines]] — downstream
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — existing note
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — replication

