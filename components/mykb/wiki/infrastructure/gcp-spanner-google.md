---
type: "concept"
title: "Google Cloud Spanner"
description: "Globally distributed relational database with external consistency"
tags: ["spanner", "gcp", "global", "distributed-sql"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Google Cloud Spanner

## Summary

Spanner is Google's globally distributed relational database: it combines the SQL model and transactions of a traditional RDBMS with the horizontal scaling and multi-region replication of a NoSQL system. Its headline guarantee is external consistency — linearizable transactions across the entire planet — delivered through a novel combination of Paxos replication and TrueTime (GPS/atomic-clock synchronized time). It is the flagship "NewSQL" managed service.

## Details

- Spanner combines SQL tables, synchronous replication across regions, and TrueTime for consistent reads. Data is partitioned into tablets, each replicated with Paxos across configurable regions; writes commit when a quorum of replicas acknowledge, giving strong durability and availability. The consistency story is where Spanner is unique: every transaction is assigned a TrueTime timestamp, and the commit-wait protocol ensures that a transaction's timestamp is always later than any transaction it could have been ordered after — so reads see a linearizable history, and multi-region transactions behave as if the planet were a single machine. That guarantee is what lets developers write normal transactional SQL against a globally replicated database, instead of dealing with conflict resolution.
- Interleaved tables and key-prefix design keep related rows co-located for low-latency access. The performance architecture rewards locality: interleaving places a parent row and its child rows on the same tablet, so a request that touches the whole hierarchy hits one tablet instead of scattering; key prefixes do the same for range scans. The design rule mirrors DynamoDB's: model for the access patterns, because cross-region reads are expensive and cross-tablet joins are slow. The failure mode is the hotspot: a monotonically increasing key (a timestamp, an auto-increment ID) concentrates writes on one tablet, which is why Spanner best practices use hash-prefixed or reversed keys for high-write tables.
- It offers external consistency (linearizable) transactions across the planet. This is the property that justifies Spanner's complexity: distributed transactions that behave like a single-node database, readable from any region with no stale reads. The price is latency — every multi-region transaction pays a round-trip to reach quorum — so the design discipline is to localize writes (put the primary replica near the users) and use read-only replicas where stale reads are acceptable.
- Schema changes and hotspots need careful key design; it is the flagship NewSQL managed service. Spanner made schema changes online (safe, non-blocking DDL) and handles huge scale, but its operational failure modes are all in the data model: bad key design creates hotspots and slow scans, and unbounded secondary-index churn can throttle the table.
- For mykb: the node anchors the distributed-SQL branch — distributed transactions, TrueTime, and consistency semantics connect to this concrete implementation.


## Related
- [[wiki/data-storage/distributed-transactions|Distributed Transactions]] — global transactions
- [[wiki/data-storage/hybrid-logical-clocks-and-true-time|Hybrid Logical Clocks And True Time]] — TrueTime underpins consistency
- [[wiki/data-storage/causal-consistency-and-strong-consistency|Causal Consistency And Strong Consistency]] — consistency guarantees
- [[wiki/data-storage/storage-engines|Storage Engines]] — underlying tablet storage
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
