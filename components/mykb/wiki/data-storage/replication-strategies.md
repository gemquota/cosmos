---
type: "concept"
title: "Replication Strategies"
description: "Primary-replica replication and failover behavior"
tags: ["replication", "primary-replica", "failover", "high-availability"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/warm-standby.html", "https://dev.mysql.com/doc/refman/8.4/en/replication.html"]
---

# Replication Strategies

## Summary
Replication keeps copies of data on multiple nodes to survive failures, serve reads, and keep data near users. The dominant topology is primary-replica: one node accepts writes and streams changes to replicas, which can be promoted if the primary fails.

## Details
- **Topologies** — primary-replica (single leader) is the default; multi-leader adds writable replicas across sites; leaderless (Dynamo-style) lets any node accept writes. Most relational databases and managed services start with primary-replica.
- **Synchronous vs asynchronous** — asynchronous replicas accept writes immediately and may lag or lose recent commits on failover; synchronous replication commits only after a replica confirms, trading latency for durability — Postgres `synchronous_commit`, MySQL semi-synchronous, and InnoDB Cluster illustrate the spectrum.
- **Delivery mechanisms** — Postgres streams WAL (physical) or logical replication streams decoded changes; MySQL uses the binary log; MongoDB and managed clouds replicate oplog/commit logs. Change data capture consumes the same streams.
- **Read scaling** — replicas serve read traffic and reporting, offloading the primary; stale reads are the cost, so applications either accept bounded lag or route consistent reads to the primary.
- **Failover** — when the primary dies, a replica is promoted (manually, by a manager like Patroni, or by the cloud service); automated failover trades faster recovery for the risk of split-brain, which fencing and quorum devices mitigate.
- **Operational reality** — replication lag monitoring, replica drift, and backfill after replica rebuilds are the recurring tasks; a replica is not a backup because it replicates errors too — logical errors and accidental deletes propagate.

## Related
- [[wiki/data-storage/multi-leader-replication|Multi-Leader Replication]] — writable replicas everywhere
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — the no-leader alternative
- [[wiki/data-storage/write-ahead-logging|Write-Ahead Logging]] — the replicated log stream
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — consuming replication streams
- [[wiki/data-storage/consistency-models|Consistency Models]] — what replicas let you read
- [[wiki/data-storage/disaster-recovery|Disaster Recovery]] — failover at site scale
