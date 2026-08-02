---
type: "concept"
title: "CockroachDB and YugabyteDB"
description: "Distributed SQL databases with Postgres compatibility and strong consistency"
tags: ["cockroachdb", "yugabytedb", "distributed-sql", "postgres"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# CockroachDB and YugabyteDB

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Both are NewSQL systems: SQL on top of a replicated, sharded key-value store with Raft consensus.
- CockroachDB offers serializable transactions, geo-partitioning, and automatic rebalancing.
- YugabyteDB uses a similar architecture with docDB storage and compatibility layers for Postgres/Cassandra.
- They trade operational complexity for horizontal scale, high availability, and strong consistency.

## Related

- [[wiki/data-storage/raft-consensus|Raft Consensus]] — consensus underpinning
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — transaction machinery
- [[wiki/infrastructure/tidb-and-new-sql|Tidb And New Sql]] — same category, different storage
- [[wiki/data-storage/consistent-hashing-and-ring-topology|Consistent Hashing And Ring Topology]] — data placement
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
