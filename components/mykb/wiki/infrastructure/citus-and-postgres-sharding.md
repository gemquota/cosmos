---
type: "concept"
title: "Citus and Postgres Sharding"
description: "Distributing Postgres tables across nodes with transparent SQL"
tags: ["citus", "postgres", "sharding", "distributed-sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Citus and Postgres Sharding

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Citus is a Postgres extension that shards tables across worker nodes using hash or reference distribution.
- Queries are pushed down to workers; the coordinator merges results, preserving Postgres semantics.
- Reference tables replicate to all nodes for fast joins with distributed tables.
- Best for multi-tenant SaaS and time-series workloads where the distribution key aligns with queries.

## Related

- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — distribution strategies
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — Postgres engine underneath
- [[wiki/infrastructure/vitess-and-sharded-mysql|Vitess And Sharded Mysql]] — MySQL-based alternative
- [[wiki/data-storage/cross-database-joins|Cross Database Joins]] — join semantics across shards
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
