---
type: "concept"
title: "Shared Nothing"
description: "An architecture where units own their state and coordinate only through messages or network calls"
tags: ["shared-nothing", "architecture", "concurrency", "scalability"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Shared Nothing

## Summary
Shared-nothing means each worker, process, or node owns its state entirely — no shared database, cache, or memory to contend over. It is how web tiers and distributed databases scale: add nodes, partition state, coordinate via messages.

## Details
- The web's stateless app tier over a shared DB is shared-nothing for compute but keeps the DB as the shared truth.
- Distributed databases (Bigtable, DynamoDB lineage) shard state across nodes with no cross-node sharing.
- Tradeoff: consistency and joins become distributed problems; that is what consensus and replication solve.
- mykb relevance: each worker in a parallel wiki pass should own its slug set and coordinate only at the end.

## Related
- [[wiki/software-engineering/message-passing|Message Passing]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/software-engineering/actor-model|Actor Model]]
- [[wiki/software-engineering/microservices-architecture|Microservices Architecture]]
- [[wiki/software-engineering/concurrency-models|Concurrency Models]]
