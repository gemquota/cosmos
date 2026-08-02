---
type: "concept"
title: "Partition Pruning"
description: "Skipping irrelevant partitions using query predicates"
tags: ["partitioning", "query-optimization", "partition-pruning", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/ddl-partitioning.html", "https://dev.mysql.com/doc/refman/8.4/en/partitioning-pruning.html"]
---

# Partition Pruning

## Summary
Partition pruning is an optimizer technique that examines a query's predicates and skips partitions that cannot contain matching rows. Instead of scanning every partition, the planner restricts the scan to a small subset — often a single partition — turning a full-table scan into a targeted read.

## Details
- **How it works** — the planner matches range, equality, and list predicates against partition bounds: a `WHERE created_at BETWEEN ...` on a range-partitioned table by date visits only the partitions overlapping the interval; MySQL calls this partition pruning and Postgres implements it both at plan time and at execution time.
- **Plan-time vs runtime pruning** — plan-time pruning uses constants known when the query is planned; runtime (execution-time) pruning handles parameters and correlated values discovered during execution, such as Postgres's `executor pruning` and partition-wise joins.
- **What defeats pruning** — non-sargable predicates (functions or arithmetic on the partition key, e.g., `WHERE date(created_at) = ...`), OR-ed predicates that span bounds, and casts that prevent bound comparison; writing predicates directly against the partition column keeps pruning effective.
- **The enabling condition** — pruning only works when the partition key appears in the query and bounds are comparable; that is why choosing the partition key to match the dominant query filter (usually time) is the first design rule.
- **Analytical impact** — in data warehouses and time-series workloads, pruning converts "scan the whole history" into "scan this month," often the single largest win after correct indexing; Hive-style partition folders and Iceberg partition metadata apply the same idea to object storage.
- **Verification** — `EXPLAIN` output shows the pruned partition set; a plan that still lists every partition signals a predicate or key mismatch worth fixing.

## Related
- [[wiki/data-storage/table-partitioning|Table Partitioning]] — the structure pruning relies on
- [[wiki/data-storage/query-tuning|Query Tuning]] — using EXPLAIN to verify pruning
- [[wiki/data-storage/time-series-databases|Time-Series Databases]] — the canonical pruning workload
- [[wiki/data-storage/open-table-formats|Open Table Formats]] — partition metadata in lakehouses
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — complementary scan efficiency
