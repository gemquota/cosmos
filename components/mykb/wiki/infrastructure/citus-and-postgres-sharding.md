---
type: "concept"
title: "Citus and Postgres Sharding"
description: "Distributing Postgres tables across nodes with transparent SQL"
tags: ["citus", "postgres", "sharding", "distributed-sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Citus and Postgres Sharding

## Summary

Citus is a Postgres extension that turns a cluster of Postgres instances into a distributed database: tables are sharded across worker nodes, and the coordinator presents the cluster as a single Postgres database to the client. It matters because it scales out Postgres — the world's most-used relational engine — without changing the SQL interface, giving multi-tenant and time-series workloads horizontal capacity while keeping transactions, joins, and the Postgres ecosystem.

## Details

- Citus is a Postgres extension that shards tables across worker nodes using hash or reference distribution. When you create a distributed table, Citus picks a distribution column and hashes its values to place rows into shards, each shard living on one worker (with replication if configured). The distribution column is the design decision that decides everything: queries that filter on it can be routed to exactly the shards that hold the relevant rows (co-located pushdown), while queries that do not filter on it become scatter queries that touch every shard. Multi-tenant SaaS is the canonical fit — tenant_id as the distribution column gives each tenant's queries single-shard locality.
- Queries are pushed down to workers; the coordinator merges results, preserving Postgres semantics. The coordinator parses the SQL, rewrites it into per-shard queries, sends them to the workers in parallel, and merges the results — aggregations are pushed down (each worker computes partial sums), and the coordinator combines them. The semantics stay Postgres because the workers are Postgres: the extension does not reimplement the engine, it orchestrates it. The tradeoff is that cross-shard operations (joins that are not co-located, transactions spanning shards) are slower and more limited than single-node Postgres — the distributed SQL ceiling is set by the distribution design.
- Reference tables replicate to all nodes for fast joins with distributed tables. Small, frequently joined tables (countries, status enums, tenant metadata) are marked as reference tables: every worker holds a full copy, so joins between distributed and reference tables happen locally on each worker with no cross-shard data movement. This is the practical trick that makes the multi-tenant model work — the hot small tables are everywhere, the big tenant tables are sharded.
- Best for multi-tenant SaaS and time-series workloads where the distribution key aligns with queries. The failure mode is a distribution key that does not align with the workload: then every query scatters, the coordinator becomes a bottleneck, and the cluster is slower than a single well-tuned Postgres instance. The operational discipline: profile query patterns before choosing the distribution column, and monitor coordinator CPU and scatter-query rates after.
- For mykb: the node connects sharding strategies, SQL engine internals, and cross-database joins to a concrete Postgres implementation, and contrasts with Vitess for MySQL.

## Related

- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — distribution strategies
- [[wiki/data-storage/sql-engines|SQL Engine Architecture]] — Postgres engine underneath
- [[wiki/infrastructure/vitess-and-sharded-mysql|Vitess And Sharded Mysql]] — MySQL-based alternative
- [[wiki/data-storage/cross-database-joins|Cross Database Joins]] — join semantics across shards
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
