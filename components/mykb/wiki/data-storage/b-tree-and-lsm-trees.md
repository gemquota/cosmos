---
type: "concept"
title: "B-Trees and LSM Trees"
description: "The two dominant data structures for database storage engines"
tags: ["b-tree", "lsm", "storage-engines", "databases"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/B-tree", "https://en.wikipedia.org/wiki/Log-structured_merge-tree"]
---

# B-Trees and LSM Trees

## Summary

B-trees keep data sorted in pages with low read amplification, ideal for reads.
LSM trees buffer writes and flush sorted runs, trading write speed for read/compaction cost.
Storage engine choice is a read/write workload tradeoff.
The structure choice is a workload statement: B-trees favor readers, LSM trees favor writers.

## Details

- B-trees: in-place page updates, good point/range reads, random write cost.
- LSM: append-only writes, batched compaction, excellent write throughput.
- LSM read path needs memtable, bloom filters, and run merging.
- Compaction (size-tiered vs leveled) shapes write and read amplification.
- Examples: Postgres/MySQL use B-trees; Cassandra/RocksDB/Scylla use LSM.
- Compaction tuning in LSM systems is a top performance lever.
- Hybrid engines and storage classes blur the line further.
- Understand both structures well enough to predict storage behavior from write patterns alone.

## Related

- [[wiki/data-storage/indexing-strategies-revisited|Indexing Strategies Revisited]] — indexes on both
- [[wiki/data-storage/bloom-filters-and-skipping|Bloom Filters And Skipping]] — LSM read acceleration
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — B-tree note
- [[wiki/data-storage/lsm-trees|LSM Trees]] — LSM note
- [[wiki/data-storage/storage-engines|Storage Engines]] — engines
- [[wiki/data-storage/data-quality-dimensions|Data Quality Dimensions]] — quality dimensions
- [[wiki/data-storage/data-observability-and-monitoring|Data Observability And Monitoring]] — observability
- [[wiki/data-storage/data-testing-frameworks|Data Testing Frameworks]] — testing
- [[wiki/data-storage/feature-stores-and-ml-features|Feature Stores And Ml Features]] — ML features
- [[wiki/data-storage/data-contracts-and-agreements|Data Contracts And Agreements]] — data contracts
- [[wiki/data-storage/incremental-loading-strategies|Incremental Loading Strategies]] — incremental loading
- [[wiki/data-storage/schema-evolution-in-streams|Schema Evolution In Streams]] — schema evolution
- [[wiki/data-storage/streaming-sinks-and-sources|Streaming Sinks And Sources]] — streams

