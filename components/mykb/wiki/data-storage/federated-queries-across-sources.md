---
type: "concept"
title: "Federated Queries Across Sources"
description: "Querying multiple databases and lakes in one statement"
tags: ["federated-queries", "trino", "sql", "integration"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Federated Queries Across Sources

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Engines like Trino expose many sources as SQL tables.
- Pushdown moves filters/aggregates to sources where possible.
- Data types, dialects, and statistics differ per connector.
- Federation is great for integration queries, not for big joins.

## Related

- [[wiki/data-storage/data-federation|Data Federation]] — federation
- [[wiki/data-storage/presto-and-trino|Presto And Trino]] — Trino
- [[wiki/data-storage/cross-database-joins|Cross-Database Joins]] — joins
- [[wiki/data-storage/distributed-query-engines|Distributed Query Engines]] — engine family
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
