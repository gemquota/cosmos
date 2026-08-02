---
type: "concept"
title: "etcd and Raft Consensus"
description: "Distributed key-value store providing consensus-based coordination state"
tags: ["etcd", "raft", "consensus", "coordination"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# etcd and Raft Consensus

## Summary

A stub to be expanded into a full article; frames the concept and open questions.

## Details

- etcd stores small amounts of critical configuration and coordination state with Raft consensus.
- It backs Kubernetes cluster state and service discovery; watch APIs enable reactive clients.
- Raft elects a leader, replicates logs, and guarantees linearizable reads with quorum.
- Keep etcd small, fast, and well-backuped; it is the source of truth for the control plane.

## Related

- [[wiki/data-storage/raft-consensus|Raft Consensus]] — Raft algorithm notes
- [[wiki/infrastructure/service-discovery-patterns|Service Discovery Patterns]] — discovery via etcd
- [[wiki/infrastructure/zookeeper-and-coordination|Zookeeper And Coordination]] — alternative coordination service
- [[wiki/data-storage/quorum-reads-and-writes|Quorum Reads And Writes]] — quorum mechanics
- [[wiki/data-storage/data-engineering-fundamentals|Data Engineering Fundamentals]] — core data engineering concepts
