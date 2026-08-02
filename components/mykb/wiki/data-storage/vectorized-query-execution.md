---
type: "concept"
title: "Vectorized Query Execution"
description: "Batch-at-a-time columnar processing for analytical workloads"
tags: ["vectorized-execution", "columnar", "olap", "query-execution"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://duckdb.org/docs/internals/vector.html", "https://clickhouse.com/docs/en/development/architecture"]
---

# Vectorized Query Execution

## Summary
Vectorized execution processes tuples in fixed-size batches (typically 1024 rows) instead of one row at a time. The batch model amortizes dispatch overhead, exposes data to SIMD-friendly loops, and pairs naturally with columnar storage.

## Details
- **Tuple-at-a-time vs batch** — classic Volcano iterators call `next()` per row, paying virtual-dispatch and pipeline overhead; batch operators process a whole vector per call, often with specialized per-type kernels.
- **Columnar synergy** — columns of a single type in contiguous memory make tight loops and SIMD (AVX2/NEON) practical; analytical engines like DuckDB, ClickHouse, and Apache DataFusion all rely on this pairing.
- **Operator specialization** — compilers and hand-written kernels avoid null-checks and type switches per element; some engines (Umbra, Hyper) JIT-compile whole pipelines.
- **Cache locality** — smaller working sets per operator stage reduce cache misses; late materialization reads only needed columns until late in the pipeline.
- **Parallelism** — batches partition naturally across cores and nodes, which is why vectorization and MPP scale together.
- **mykb relevance** — any aggregation over the wiki corpus (term frequency, tag counts) maps directly to vectorized scans in DuckDB, where per-row Python loops are orders of magnitude slower.

## Related
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — the layout vectorized engines consume
- [[wiki/data-storage/olap-vs-oltp|OLAP vs OLTP]] — the workload split that motivated batching
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — where the executor fits
- [[wiki/data-storage/massively-parallel-processing|Massively Parallel Processing]] — batch parallelism across nodes
- [[wiki/data-storage/compression-codecs|Compression Codecs]] — compression that vectorized loops can decode inline
- [[wiki/devops-infra/duckdb|DuckDB]] — a reference vectorized engine in this stack
