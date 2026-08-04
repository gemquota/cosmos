---
type: "entity"
title: "SingleStore and HTAP"
description: "One engine for transactions and analytics (hybrid transactional/analytical processing)"
tags: ["singlestore", "htap", "olap", "oltp"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# SingleStore and HTAP

## Summary
HTAP systems run operational and analytical workloads on one database, avoiding dual-copy pipelines. SingleStore keeps row-based tables for writes and columnar tables for scans, syncing internally — fresher analytics and simpler architecture at the cost of tuning that compromises both workload types.

## Details
- Mechanism: rowstore tables serve point writes and lookups; columnstore tables serve scans and aggregations; the engine syncs data between the two forms automatically, so analytical queries see recent writes without an ETL hop; memory-optimized rowstores and disk-based columnstores share one SQL surface.
- Concrete example: a real-time personalization service writes user events to rowstore tables and runs aggregate queries on columnstore tables in the same database; an operational dashboard reads the same data the transactional API writes, with seconds of freshness; no nightly copy pipeline.
- Failure modes: workload interference — a heavy analytical query stealing resources from transactions; columnstore refresh lag making analytics stale; tuning compromises that leave both workloads mediocre; schema choices (row vs column placement) made wrong and hard to change later; scale surprises where the unified engine underperforms specialized systems.
- Tradeoffs: HTAP trades dual-system operational complexity for a compromise in each workload — one engine, fresher data, simpler ops, at the cost of peak OLTP or OLAP performance; the alternative, separate OLTP and OLAP systems with replication, is the traditional split; the mature pattern is HTAP where freshness and simplicity matter more than peak performance on either side.
- Operational notes: monitor rowstore/columnstore sync lag, isolate heavy queries, and benchmark both workload classes before committing.
- RSIS3 relevance: wiki writes (captures) and reads (dashboards, analytics) could share one HTAP engine — fresh telemetry without a pipeline between.


## Related
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — the split HTAP tries to bridge
- [[wiki/data-storage/real-time-personalization|Real Time Personalization]] — HTAP-powered feature
- [[wiki/data-storage/read-replicas-and-scaling|Read Replicas And Scaling]] — alternative separation of workloads
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — columnar side of SingleStore
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
