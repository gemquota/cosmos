---
type: "concept"
title: "Multi-Leader Replication"
description: "Writable replicas with cross-site conflict handling"
tags: ["multi-leader", "replication", "conflict-resolution", "active-active"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.postgresql.org/docs/current/logical-replication.html", "https://dev.mysql.com/doc/refman/8.4/en/group-replication.html"]
---

# Multi-Leader Replication

## Summary
Multi-leader replication lets several nodes (leaders) accept writes, each propagating its changes to the others. It enables active-active deployments across data centers, low-latency local writes for distributed teams, and offline-tolerant apps — at the cost of handling concurrent writes to the same data, which can conflict.

## Details
- **The topology** — each leader applies local writes and asynchronously ships them to peer leaders; PostgreSQL logical replication supports bidirectional setups with two publishers/subscribers, MySQL Group Replication provides multi-primary mode, and MongoDB, DynamoDB global tables, and Cosmos DB offer managed multi-region write support.
- **Why multi-leader** — writes are served near their region (lower latency), a data-center outage does not stop writes, and multi-datacenter failover becomes symmetric; single-leader replication must route all writes through one primary, which is slow across regions and a single point of failure.
- **Conflict problem** — two leaders can accept conflicting writes to the same row or key concurrently; without resolution, replicas diverge. Last-write-wins (by timestamp), merge strategies, conflict-free replicated data types, and application-level resolution are the standard responses.
- **Conflict detection** — synchronous conflict detection (abort one write at commit) requires coordination that erodes the latency win; asynchronous detection is common, surfacing conflicts in logs or storing conflicting versions for manual/app-level resolution.
- **Costs and operations** — monotonically increasing IDs, unique constraints, and auto-increment columns need per-node offsets or UUIDs; monitoring replication lag in both directions and testing failover are essential because a stuck multi-leader pair silently splits the system.
- **When to choose it** — cross-region active-active services and collaborative apps; for a single region, single-leader replication is simpler and usually sufficient.

## Related
- [[wiki/data-storage/replication-strategies|Replication Strategies]] — the full topology landscape
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — conflict-prone replication, no leaders
- [[wiki/data-storage/crdts|CRDTs]] — convergent merge structures for conflicts
- [[wiki/data-storage/consistency-models|Consistency Models]] — what writes you can observe
- [[wiki/data-storage/cdc-change-data-capture|Change Data Capture]] — logical replication streams
