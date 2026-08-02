---
type: "concept"
title: "Bitmap Indexes"
description: "Compressed bitmaps for low-cardinality predicate filtering"
tags: ["bitmap-index", "indexing", "query-optimization", "analytics"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/indexes-bitmap-scans.html", "https://docs.oracle.com/en/database/oracle/oracle-database/23/cncpt/indexes-and-index-organized-tables.html"]
---

# Bitmap Indexes

## Summary
A bitmap index stores one bitmap per distinct value, where each bit position maps to a row. Bitwise AND/OR operations then answer multi-predicate queries without touching the table, which makes bitmaps fast for low-cardinality columns and complex boolean filters.

## Details
- **Layout** — for each value in a low-cardinality column, a bitmap of length N marks which rows hold that value; storage scales with distinct values times row count, so it suits columns like status, region, or gender.
- **Predicate evaluation** — `status = 'active' AND region = 'eu'` becomes a bitwise AND of two bitmaps; OR conditions use bitwise OR. This turns predicate evaluation into vectorized CPU work.
- **Compression** — run-length encoding collapses long runs of zeros, keeping bitmaps small even for sparse matches; Oracle's implementation compresses bitmaps and merges them during scans.
- **PostgreSQL variant** — Postgres does not ship bitmap indexes; instead its planner builds a Bitmap Index Scan and ORs together multiple ordinary index scans into a bitmap before fetching heap pages, giving similar multi-index benefits.
- **Trade-offs** — writes become expensive because every insert/update must maintain per-value bitmaps; high-cardinality columns explode in size. Analytical warehouses with rare updates benefit most.

## Related
- [[wiki/data-storage/b-tree-indexing|B-Tree Indexing]] — the ordered default used where bitmaps fit poorly
- [[wiki/data-storage/hash-indexes|Hash Indexes]] — another specialized access method
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — run-length encoding that makes bitmaps compact
- [[wiki/data-storage/cost-based-query-optimization|Cost-Based Query Optimization]] — how planners choose scan paths
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — why warehouses favor bitmap scans
