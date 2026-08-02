---
type: "concept"
title: "Cross-Database Joins"
description: "Joining data that lives in different systems"
tags: ["cross-database", "joins", "federation", "sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cross-Database Joins

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Options: federated engine (Trino), ETL into one store, or materialized copies.
- Joins across systems lose statistics and pushdown; expect slower plans.
- Volume matters: joining small lookup tables remotely is fine; large joins are not.
- Consider data products: copy what you join repeatedly.

## Related

- [[wiki/data-storage/join-algorithms|Join Algorithms]] — join algorithms
- [[wiki/data-storage/federated-queries-across-sources|Federated Queries Across Sources]] — federation
- [[wiki/data-storage/data-federation-and-virtualization|Data Federation And Virtualization]] — virtualization
- [[wiki/data-storage/warehouse-optimization|Warehouse Optimization]] — local joins
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
