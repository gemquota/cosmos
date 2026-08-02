---
type: "concept"
title: "Physical Replication"
description: "Replicating database files or storage blocks to identical copies"
tags: ["physical-replication", "standby", "wal", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://dev.mysql.com/doc/refman/8.0/en/replication.html", "https://www.postgresql.org/docs/current/hot-standby.html"]
---

# Physical Replication

## Summary

Physical replication copies storage-level data: WAL records, files, or blocks.
Replicas are byte-identical, making failover and read scaling simple.
It is how databases ship built-in high availability.
Physical replicas are the fastest path to high availability, but they demand identical environments.

## Details

- Postgres streaming replication ships WAL to hot standbys.
- MySQL semi-synchronous and group replication ship binlog or redo data.
- Physical replicas cannot diverge in schema or data format.
- Failover promotes a replica; RPO depends on sync configuration.
- Physical replication is the backbone of managed database failover.
- Promote-and-failback drills should be part of routine operations.
- Synchronous replication costs latency; choose sync depth by RPO.
- Physical replication gives the strongest fidelity and is the backbone of managed database high availability.

## Related

- [[wiki/data-storage/wal-and-consistency|Wal And Consistency]] — WAL basis
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — read scale-out
- [[wiki/data-storage/replication-mechanisms|Replication Mechanisms]] — family
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — strategies
- [[wiki/data-storage/disaster-recovery|Disaster Recovery]] — DR
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability and Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores and ML Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts and Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

