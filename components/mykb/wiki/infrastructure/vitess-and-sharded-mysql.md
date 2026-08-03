---
type: "concept"
title: "Vitess and Sharded MySQL"
description: "Database clustering middleware that shards MySQL behind a SQL-compatible front end"
tags: ["vitess", "mysql", "sharding", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Vitess and Sharded MySQL

## Summary
Vitess is database clustering middleware that turns many MySQL instances into one horizontally scalable database behind a SQL-compatible front end. Built to scale YouTube's MySQL, it layers connection pooling, query routing, sharding, and online resharding onto MySQL, and it now runs natively on Kubernetes through operators.

## Details
- Architecture: VTGate is the stateless front end that accepts MySQL-protocol connections, parses and routes queries; VTTablet runs alongside each MySQL instance, managing replication, serving, and health; and a topo service (etcd or ZooKeeper) stores the shard map and cluster state. Clients talk to VTGate as if it were a single MySQL server.
- Sharding: data is split by a shard key — for example a `user_id` hash or range — so each shard owns a disjoint keyspace slice. Queries that include the shard key route to one shard; queries without it scatter to all shards and merge, which is the main cost to design around.
- Concrete example: a user service with 100 million rows across 8 shards by `user_id`; `SELECT ... WHERE user_id = 42` hits one shard in a few milliseconds, while an analytics query that aggregates across all users fans out to every shard and pays coordination cost.
- Lifecycle: resharding (splitting one shard into more) runs online with filtered replication — the old shards keep serving while data copies to new ones — then traffic switches over; Vitess also provides online schema migrations (gh-ost-style VReplication) so DDL does not lock production.
- Failure modes: a hot shard key (a celebrity user) overloads one shard while others idle; schema changes that must run on every shard and drift between them; cross-shard transactions that need 2PC and are slower; and misconfigured topology that routes queries to the wrong shard.
- Tradeoffs: Vitess gives scale and operational tooling at the cost of complexity — every query must be written with the shard key in mind, and the middleware itself is a system to operate. It is the right answer for very large MySQL workloads, overkill for databases that fit one node.
- RSIS3/mykb relevance: sharding decisions are a standing pattern when the knowledge store outgrows one node; this node keeps the query-routing and resharding tradeoffs retrievable for scale planning.

## Related
- [[wiki/data-storage/sharding-strategies|Sharding Strategies]] — sharding fundamentals
- [[wiki/infrastructure/kubernetes-operators|Kubernetes Operators]] — Vitess runs as K8s operators
- [[wiki/infrastructure/citus-and-postgres-sharding|Citus And Postgres Sharding]] — Postgres-side sharding alternative
- [[wiki/data-storage/sharding-and-partitioning-revisited|Sharding And Partitioning Revisited]] — design tradeoffs
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
