---
type: "concept"
title: "Shared Nothing"
description: "An architecture where units own their state and coordinate only through messages or network calls"
tags: ["shared-nothing", "architecture", "concurrency", "scalability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Shared Nothing

## Summary

Shared-nothing architecture partitions state so each worker owns its data exclusively and communicates only by messages — no shared memory, no shared database writes, no locks. It is the scalability doctrine behind web workers, sharded databases, and horizontally-scaled services.

## Details
- Mechanism: each instance owns a partition of data (shard, region, task); requests route to the owning instance; coordination happens via messages (queues, events), not shared state; the design eliminates lock contention and cache-coherency costs because nothing is shared. In databases, sharding keys partition rows; in compute, workers claim tasks atomically.
- Concrete example: a chat service shards rooms across servers by room id — a server owns its rooms' state; an event-processing pool claims jobs from a queue with lease-based locks, so no two workers process the same job; a cache cluster partitions keys by hash so each node owns its keys.
- Failure modes: hidden shared state (a shared cache or database column that reintroduces contention); hot partitions (one shard takes most traffic — pick partition keys by access pattern); rebalancing complexity when adding nodes; and cross-shard queries that silently become expensive scatter-gathers.
- Operational tradeoffs: shared-nothing scales linearly and fails independently at the cost of data partitioning design and cross-partition operations; the discipline is partition by the hot access path, keep cross-partition work rare, and design rebalancing as a first-class operation.
- RSIS3/mykb relevance: the wiki's workers would partition their queues and state by domain, so loop jobs scale horizontally without distributed locks.
- Partition key choice: model the access path before choosing the shard key; a key chosen by convenience becomes the hot-shard regret.
- Rebalancing: plan for adding and removing nodes with background migration and double-write windows so scaling is boring, not an incident.
- Consistency across partitions: operations spanning partitions need explicit coordination (idempotent messages, compensation); never assume cross-partition reads are cheap or consistent.
- Failure independence: because workers share nothing, a crashed worker's partition must be reassigned cleanly — design claim/release semantics so recovery is automatic.

## Related
- [[wiki/software-engineering/message-passing|Message Passing]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/software-engineering/actor-model|Actor Model]]
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
