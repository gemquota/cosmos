---
type: "concept"
title: "Presto and Trino"
description: "Open-source distributed SQL engines for interactive analytics"
tags: ["presto", "trino", "sql", "federation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://trino.io/docs/current/", "https://prestodb.io/docs/current/"]
---

# Presto and Trino

## Summary

Presto and Trino are distributed SQL engines for interactive queries over large datasets.
Trino forked from Presto in 2019 with a focus on the query engine.
Both excel at querying lakes and federated sources.
Trino's community focus on the engine itself keeps it fast and SQL-standard.

## Details

- SQL over Hive/Iceberg/Delta, object storage, and JDBC sources.
- Coordinator + worker architecture with pushdown.
- Trino adds cost-based optimization and fault-tolerant execution.
- Used for interactive BI and data lake analytics.
- Not a transactional store: read-mostly workloads.
- Fault-tolerant execution handles long, heavy queries.
- Catalog and connector management is the main ops surface.
- Trino is the go-to engine for federated SQL and lakehouse ad-hoc queries.

## Related

- [[wiki/data-storage/distributed-query-engines|Distributed Query Engines]] — family
- [[wiki/data-storage/sql-on-lakehouse|Sql On Lakehouse]] — lake access
- [[wiki/data-storage/federated-queries-across-sources|Federated Queries Across Sources]] — federation
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — existing note
- [[wiki/data-storage/cross-database-joins|Cross Database Joins]] — joins
- [[wiki/data-storage/data-warehouse|Data Warehouse]] — warehouse reference

