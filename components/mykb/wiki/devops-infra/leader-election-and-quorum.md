---
type: "concept"
title: "Leader Election & Quorum"
description: "Choosing one active replica and agreeing on cluster membership"
tags: ["leader-election", "quorum", "consensus", "distributed"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Leader Election & Quorum

## Summary
Leader election and quorum decide who acts in a distributed system: leader election picks a single active node among replicas, and quorum determines how many nodes must agree for a decision to be safe. Together they prevent split-brain — two nodes acting as leader — and underpin HA for databases, controllers, and coordination services.

## Details
- Mechanism: candidates contend for a lease (etcd, ZooKeeper, Consul); the winner holds the lease and renews it; on expiry or loss of connectivity, a new leader is elected; quorum-based systems (Raft, Paxos) require a majority of nodes to agree before committing, so a minority partition can neither elect nor commit.
- Concrete example: a Kubernetes controller uses leader election so only one replica reconciles; Patroni uses etcd quorum to choose the Postgres primary; etcd itself needs a majority to serve writes — with 3 nodes, 2 must agree; with 5, at least 3.
- Failure modes: split-brain when leases do not fence — the old leader, still alive but partitioned, keeps writing because fencing mechanisms (epoch numbers, lease checks) are missing; flapping leadership under network jitter, thrashing failovers; quorum loss — an even number of nodes can tie, so odd counts are the norm; slow leaders holding leases while unable to act, blocking failover.
- Tradeoffs: strong quorum guarantees safety at the cost of availability — losing a majority stops writes; single-leader designs are simple and linearizable but concentrate write load and need election on failure; leaderless (quorum-read) designs trade consistency guarantees; the choice is about whether split-brain or brief unavailability is worse for the workload.
- Operational notes: monitor lease duration, election churn, and quorum health; test partition scenarios in game days.
- RSIS3 relevance: any HA deployment of the wiki daemon or shared state needs explicit leader election and fencing — otherwise a failed node may keep writing while its replacement runs.

## Related
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
