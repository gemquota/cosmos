---
type: "concept"
title: "Vitess and Sharded MySQL"
description: "Database clustering middleware that shards MySQL behind a SQL-compatible front end"
tags: ["vitess", "mysql", "sharding", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Vitess and Sharded MySQL

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Vitess gives MySQL horizontal sharding, connection pooling, and query routing via VTGate.
- It was built to scale YouTube's MySQL and runs on Kubernetes with operators.
- Shard keys, resharding, and online schema change tooling manage the sharding lifecycle.
- SQL compatibility is preserved, but cross-shard queries and transactions pay coordination costs.

## Related

- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — sharding fundamentals
- [[wiki/infrastructure/kubernetes-operators|Kubernetes Operators]] — Vitess runs as K8s operators
- [[wiki/infrastructure/citus-and-postgres-sharding|Citus And Postgres Sharding]] — Postgres-side sharding alternative
- [[wiki/data-storage/sharding-and-partitioning-revisited|Sharding And Partitioning Revisited]] — design tradeoffs
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
