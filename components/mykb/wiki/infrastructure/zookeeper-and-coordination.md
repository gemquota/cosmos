---
type: "concept"
title: "ZooKeeper and Coordination"
description: "Legacy distributed coordination service with a hierarchical namespace"
tags: ["zookeeper", "coordination", "distributed-systems", "consensus"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# ZooKeeper and Coordination

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- ZooKeeper offers a tree of znodes with watches, ephemeral nodes, and sequential nodes for coordination.
- It underpins legacy Kafka and HBase deployments for metadata and leader election.
- ZAB protocol provides ordering; performance degrades with size, so it is being replaced by etcd/RAFT systems.
- Designs today prefer etcd or Kubernetes-native primitives; ZooKeeper remains in older stacks.

## Related

- [[wiki/data-storage/raft-consensus|Raft Consensus]] — modern consensus alternative
- [[wiki/data-storage/message-queues|Message Queues]] — legacy broker coordination
- [[wiki/infrastructure/etcd-and-raft-consensus|Etcd And Raft Consensus]] — replacement path
- [[wiki/infrastructure/service-discovery-patterns|Service Discovery Patterns]] — coordinating services
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
