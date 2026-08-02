---
type: "concept"
title: "Change Data Capture"
description: "Capturing row-level changes for replication and streaming"
tags: ["cdc", "replication", "debezium", "event-streaming"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://debezium.io/documentation/reference/stable/index.html", "https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html"]
---

# Change Data Capture

## Summary
Change data capture (CDC) captures row-level inserts, updates, and deletes as they happen and streams them to consumers — replicas, warehouses, search indexes, or event buses. Reading the database's own transaction log (binlog, WAL) avoids poll queries and gives near-real-time fidelity.

## Details
- **Log-based CDC** — Debezium and AWS DMS parse the source's change log: MySQL binlog, Postgres WAL (via logical decoding), SQL Server change streams; events carry before/after values plus metadata (LSN, timestamp, table).
- **Why not polling** — `SELECT ... WHERE updated_at > watermark` adds source load, misses deletes, and lags; log-based CDC has low overhead and captures every committed change exactly once per log position.
- **Event shape** — each change is an envelope (create/update/delete, before/after, source metadata); consumers dedupe by log position since redelivery is possible.
- **Initial snapshot + stream** — pipelines start with a snapshot of existing rows, then continue from the log offset; Debezium coordinates this automatically with its snapshot phase.
- **Targets** — streaming into Kafka for analytics, mirroring into a warehouse via streaming tables, updating search indexes (Elasticsearch), and keeping a denormalized read model warm.
- **Operational caveats** — schema changes on the source break decoders; ALTER TABLE needs coordinated handling (Debezium schema evolution modes), and retention of the log bounds how far a lagging consumer can catch up.

## Related
- [[wiki/data-storage/event-streaming-platforms|Event Streaming Platforms]] — where CDC events land
- [[wiki/data-storage/incremental-loading|Incremental Loading]] — watermark-based alternative
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — log-based replication
- [[wiki/data-storage/schema-evolution|Schema Evolution]] — decoder compatibility
- [[wiki/data-storage/exactly-once-semantics|Exactly-Once Semantics]] — end-to-end guarantees
