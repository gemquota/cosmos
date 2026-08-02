---
type: "concept"
title: "OLAP vs OLTP"
description: "Workload classification and why engine design diverges"
tags: ["olap", "oltp", "workloads", "databases", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing-vs-online-analytical-processing", "https://clickhouse.com/docs/en/introduction"]
---

# OLAP vs OLTP

## Summary
OLTP and OLAP describe opposite workload poles: many short, concurrent point transactions versus few long, scanning-heavy analytical queries. Because the two stress different resources, engines optimize for one and retrofit the other.

## Details
- **OLTP profile** — high write rates, small transactions touching few rows by primary key, row-oriented storage with indexes, strong consistency, and concurrency control; examples are order entry, account balances, and session state.
- **OLAP profile** — large scans and aggregations over millions of rows, columnar layout, heavy compression, vectorized execution, and modest concurrency; examples are revenue reports and cohort analysis.
- **Why design diverges** — row stores make single-row reads cheap but scans fetch full rows; column stores read only needed columns and compress well, at the cost of slower point updates.
- **HTAP** — hybrid engines (TiDB, SingleStore, ClickHouse) serve both via replicas or separate row and column stores, accepting freshness or performance trade-offs.
- **Choosing** — the same logical table rarely lives in both regimes; most systems extract OLTP data into an OLAP warehouse for analysis.
- **mykb relevance** — wiki writes are OLTP-like but tiny; corpus analysis (TF-IDF, embeddings similarity sweeps) is OLAP-like, so the stack keeps Postgres for state and DuckDB/vector stores for analysis.

## Related
- [[wiki/data-storage/vectorized-query-execution|Vectorized Query Execution]] — the OLAP execution model
- [[wiki/data-storage/columnar-storage|Columnar Storage]] — the OLAP physical layout
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — the canonical OLAP destination
- [[wiki/data-storage/transaction-isolation-levels|Transaction Isolation Levels]] — OLTP concurrency semantics
- [[wiki/data-storage/in-memory-databases|In-Memory Databases]] — latency-focused engines for OLTP
- [[wiki/data-storage/etl-vs-elt|ETL vs ELT]] — moving data between the two regimes
