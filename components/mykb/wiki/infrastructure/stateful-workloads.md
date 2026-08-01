---
type: "concept"
title: "Stateful Workloads"
description: "Applications with durable data and identity — databases, queues, caches — that resist ephemeral scheduling"
tags: ["stateful", "kubernetes", "databases", "operators"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Stateful Workloads

## Summary
Stateful workloads need stable identity, ordered deployment, and durable storage — databases, caches, and message brokers. They are the hardest things to run on Kubernetes, which is why operators exist.

## Details
- StatefulSets give stable network identity and ordered scaling; PersistentVolumes provide durable state.
- Backup, restore, and upgrade are operational problems that operators encode.
- Not everything belongs on Kubernetes: evaluate managed databases first.
- Open question: how far to push stateful workloads before managed services win.

## Related
- [[wiki/infrastructure/kubernetes-operators|Kubernetes Operators]] — automates stateful lifecycle
- [[wiki/infrastructure/persistent-volumes|Persistent Volumes]] — durable storage for state
- [[wiki/infrastructure/storage-classes|Storage Classes]] — volume performance tiers
- [[wiki/devops-infra/replication|Replication]] — data redundancy for state
