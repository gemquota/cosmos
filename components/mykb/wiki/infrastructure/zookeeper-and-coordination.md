---
type: "concept"
title: "ZooKeeper and Coordination"
description: "Legacy distributed coordination service with a hierarchical namespace"
tags: ["zookeeper", "coordination", "distributed-systems", "consensus"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# ZooKeeper and Coordination

## Summary
ZooKeeper is a distributed coordination service that provides a hierarchical namespace of znodes with watches, ephemeral nodes, and sequential nodes — the primitives distributed systems need for leader election, configuration, group membership, and metadata. It popularized the coordination pattern that etcd and Kubernetes-native primitives now fill, and it still underpins many legacy Kafka, HBase, and Solr deployments.

## Details
- Data model: znodes form a tree like a filesystem; each znode can hold a small payload, and nodes can be persistent, ephemeral (deleted when the session ends), or sequential (server-assigned monotonically increasing suffix). Watches notify clients when a znode changes, enabling reactive coordination.
- Coordination patterns: leader election via ephemeral sequential nodes (the lowest-numbered node wins); group membership by having each member create an ephemeral node under a group path; distributed locks with the same sequential-node recipe; and configuration storage where clients watch a path and reload on change.
- Consistency: ZooKeeper uses the ZAB protocol to order updates across its ensemble (odd number of servers, typically 3 or 5); reads may go to any server with optional sync to the leader, and writes are ordered by the leader. Session timeouts and heartbeats drive failure detection.
- Failure modes: a misbehaving client that does not close sessions leaks ephemeral nodes; ensemble partitions can cause the minority side to lose the quorum and stop serving writes; session timeouts that are too short flap leaders during GC pauses; and znodes that accumulate without cleanup grow the tree and slow startup.
- Tradeoffs: ZooKeeper is mature and battle-tested but is a Java service with its own operational burden, and its API is low-level — every pattern is hand-built. etcd/RAFT covers most of the same ground with a simpler key-value model, and Kubernetes-native primitives (Lease, ConfigMap) replace many classic use cases; ZooKeeper remains where deep integration (Kafka, HBase) already exists.
- Operational practice: run an odd-sized ensemble on dedicated nodes, keep znode payloads small, tune session timeouts to expected GC pauses, monitor watches and sessions, and plan an upgrade path if the stack is on a modern platform.
- RSIS3/mykb relevance: coordination services embody the quorum and ordering rules any self-improvement loop needs when multiple agents share state; this node keeps the ZAB-vs-Raft comparison retrievable for distributed design.

## Related
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — modern consensus alternative
- [[wiki/data-storage/message-queues|Message Queues]] — legacy broker coordination
- [[wiki/infrastructure/etcd-and-raft-consensus|Etcd And Raft Consensus]] — replacement path
- [[wiki/infrastructure/service-discovery-patterns|Service Discovery Patterns]] — coordinating services
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
