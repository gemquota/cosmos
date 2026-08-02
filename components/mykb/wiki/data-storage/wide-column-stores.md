---
type: "concept"
title: "Wide-Column Stores"
description: "Cassandra/HBase-style column-family tables"
tags: ["wide-column", "cassandra", "hbase", "nosql"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html", "https://hbase.apache.org/book.html#datamodel"]
---

# Wide-Column Stores

## Summary
Wide-column stores organize data into tables with rows and columns, but each row can have different columns, and columns are grouped into column families stored contiguously. Cassandra, HBase, and ScyllaDB use this model to serve massive, write-heavy workloads with horizontal scaling.

## Details
- **Data model** — a table is keyed by a partition key (row key); columns are stored per column family; each cell is versioned by timestamp. In Cassandra, a row's columns are dynamic — a time-based column name (e.g., a sensor reading per hour) makes each row a wide, ordered set of values; HBase stores cells as `(row, column family, qualifier, timestamp)`.
- **Storage layout** — column families are stored separately and contiguously, which gives scan-friendly access per family; Cassandra runs on LSM trees with SSTables, HBase on HDFS-backed HFiles with a memstore — both append-oriented, write-optimized designs.
- **Query model** — reads are by partition key with optional range scans over clustered columns; there is no general join or ad-hoc secondary index (Cassandra supports limited secondary indexes and SASI/storage-attached indexes; HBase has coprocessors and Phoenix for SQL).
- **Distribution** — the data model is designed around sharding: Cassandra's consistent-hashing ring with tunable replication and consistency levels; HBase region servers serve sorted row ranges with HMaster coordination — a leader-based system.
- **Use cases** — time-series event logs, IoT telemetry, messaging history, and recommendation features where writes dominate and queries are known ahead of time; the price is that access patterns must be designed into the key structure.
- **Trade-offs** — brilliant write throughput and availability, weaker consistency and query flexibility than relational databases; choose it when the workload shape matches the model rather than forcing SQL semantics onto it.

## Related
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — Cassandra's replication model
- [[wiki/data-storage/lsm-trees|LSM Trees]] — the underlying storage engine
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — a natural workload fit
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — row-key distribution design
- [[wiki/data-storage/document-stores|Document Stores]] — the other flexible-schema NoSQL family
- [[wiki/data-storage/vacuuming-and-compaction|Vacuuming & Compaction]] — SSTable maintenance
