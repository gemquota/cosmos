---
type: "concept"
title: "Cassandra and ScyllaDB"
description: "Wide-column, leaderless, eventually consistent databases for write-heavy scale"
tags: ["cassandra", "scylladb", "wide-column", "nosql"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Cassandra and ScyllaDB

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- Cassandra distributes rows by partition key across a ring with configurable replication factor.
- It is leaderless and eventually consistent, with tunable consistency per query (QUORUM, ALL, ONE).
- ScyllaDB is a C++ reimplementation with the same protocol and higher per-node throughput.
- Best for time-series, IoT, and messaging workloads that tolerate eventual consistency.

## Related

- [[wiki/data-storage/wide-column-stores|Wide-Column Stores]] — data model basics
- [[wiki/data-storage/leaderless-replication|Leaderless Replication]] — replication model
- [[wiki/data-storage/consistent-hashing|Consistent Hashing]] — ring distribution
- [[wiki/data-storage/quorum-reads-and-writes|Quorum Reads And Writes]] — tunable consistency
- [[wiki/data-storage/hint-handoff-and-repair-paths|Hint Handoff And Repair Paths]] — repair mechanics
