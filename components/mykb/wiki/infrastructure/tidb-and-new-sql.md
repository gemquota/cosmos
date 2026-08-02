---
type: "concept"
title: "TiDB and NewSQL"
description: "MySQL-compatible distributed database with TiKV storage and MPP analytics"
tags: ["tidb", "newsql", "mysql", "distributed-sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# TiDB and NewSQL

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- TiDB splits SQL (stateless TiDB servers) from storage (TiKV, a Raft-based row store) and analytics (TiFlash columnar replicas).
- It speaks MySQL protocol, making migration from MySQL relatively smooth.
- Online DDL, auto-scaling, and HTAP-style TiFlash replicas are headline features.
- NewSQL means OLTP semantics (ACID, SQL) with NoSQL-scale horizontal scaling.

## Related

- [[wiki/data-storage/raft-consensus|Raft Consensus]] — Raft replication in TiKV
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — ACID across shards
- [[wiki/infrastructure/cockroachdb-and-yugabytedb|Cockroachdb And Yugabytedb]] — comparable distributed SQL
- [[wiki/data-storage/singlestore-htap|Singlestore Htap]] — TiFlash HTAP role
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
