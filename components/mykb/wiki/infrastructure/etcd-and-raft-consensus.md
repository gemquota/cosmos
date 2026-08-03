---
type: "concept"
title: "etcd and Raft Consensus"
description: "Distributed key-value store providing consensus-based coordination state"
tags: ["etcd", "raft", "consensus", "coordination"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# etcd and Raft Consensus

## Summary

etcd is a distributed key-value store that uses the Raft consensus algorithm to give a cluster of machines one shared, consistent source of truth for small but critical state. It is best known as the brain of Kubernetes — the cluster's control-plane state, configuration, and service discovery all live in etcd — and its design reflects that job: small data, strong consistency, high reliability.

## Details

- etcd stores small amounts of critical configuration and coordination state with Raft consensus. The "small" constraint is architectural, not cosmetic: every write is committed through a consensus round (a majority of the cluster must acknowledge it), so throughput is bounded by the network round-trip between nodes and the fsync latency of the disk. etcd is tuned for a few thousand writes per second, not high-volume data — the design rule is to keep configuration and metadata in etcd, and everything else in a real database.
- It backs Kubernetes cluster state and service discovery; watch APIs enable reactive clients. Kubernetes stores its entire desired state (deployments, pods, secrets, configmaps) in etcd — the API server is essentially a translation layer between the Kubernetes API and etcd — which is why "restore etcd" is the Kubernetes disaster-recovery procedure. The watch API is the other pillar: clients can subscribe to changes on a key or prefix and react immediately (a service mesh watching for endpoint changes, a scheduler watching for pending pods), turning etcd into an event bus as well as a store.
- Raft elects a leader, replicates logs, and guarantees linearizable reads with quorum. Raft's structure: the cluster elects a single leader; all writes go through the leader, which appends them to its log and replicates to followers; a write is committed when a majority (quorum) of nodes have durably stored it; reads are linearizable when they also go through the leader (or with quorum reads). The design's virtue is understandability — Raft was created to be the teachable consensus algorithm — and its failure modes are the ones any quorum system has: losing quorum (fewer than a majority of nodes alive) stops all writes; split-brain is prevented by the quorum requirement itself.
- Keep etcd small, fast, and well-backed-up; it is the source of truth for the control plane. The operational rules: place it on fast disks (fsync latency is the write bottleneck), keep it on dedicated nodes or at least dedicated resources (its disk and network contention starve the control plane), size the cluster at 3 or 5 nodes (odd numbers maximize fault tolerance per node), and back it up — because if etcd is lost, the entire Kubernetes cluster's state is lost with it.
- For mykb: the node anchors the coordination cluster — Raft mechanics, quorum, and Zookeeper as the alternative.


## Related
- [[wiki/data-storage/raft-consensus|Raft Consensus]] — Raft algorithm notes
- [[wiki/infrastructure/service-discovery-patterns|Service Discovery Patterns]] — discovery via etcd
- [[wiki/infrastructure/zookeeper-and-coordination|Zookeeper And Coordination]] — alternative coordination service
- [[wiki/data-storage/quorum-reads-and-writes|Quorum Reads And Writes]] — quorum mechanics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
