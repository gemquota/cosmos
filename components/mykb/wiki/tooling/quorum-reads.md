---
type: "concept"
title: "Quorum Reads"
description: "Reading from enough replicas to satisfy consistency requirements"
tags: ["quorum", "reads", "replication", "consistency"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Quorum Reads

## Summary
Quorum reads fetch from multiple replicas and use the latest version among the responses, giving stronger consistency than reading one replica. Combined with quorum writes (W+R > N), they bound staleness and detect failed writes.

## Details
- W + R > N blocks overlapping quorums from serving stale data (in the quorum model).
- Quorum reads cost latency and load; choose R to balance consistency and speed.
- Read-repair and hinted handoff are the supporting mechanisms in Dynamo-style systems.
- mykb relevance: wiki index reads can use quorum when consistency beats speed.

## Related
- [[wiki/tooling/read-replicas|Read Replicas]]
- [[wiki/tooling/replication-lag|Replication Lag]]
- [[wiki/tooling/distributed-consistency|Distributed Consistency]]
- [[wiki/tooling/failover-practice|Failover Practice]]
- [[wiki/tooling/consensus-algorithms|Consensus Algorithms]]
