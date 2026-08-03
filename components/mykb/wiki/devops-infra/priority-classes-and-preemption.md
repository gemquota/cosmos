---
type: "concept"
title: "Priority Classes & Preemption"
description: "Scheduling precedence and evicting lower-priority pods"
tags: ["priority", "preemption", "scheduling", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Priority Classes & Preemption

## Summary
PriorityClasses and preemption govern which pods win when resources are scarce: priority classes assign numeric priorities, and preemption lets a higher-priority pod evict lower-priority ones so it can schedule. They protect critical workloads (control planes, databases) during oversubscription, at the cost of evicting everything below the line.

## Details
- Mechanism: a PriorityClass declares a value (and optional globalDefault); pods reference it; when a pod cannot schedule due to insufficient resources, the scheduler may preempt running pods with lower priority (subject to PodDisruptionBudgets and defaulting); preemption is a last resort, so the scheduler first tries normal scheduling on available nodes.
- Concrete example: system-critical pods at priority 1,000,000; batch jobs at 0; during a resource crunch, a critical pod preempts batch pods to schedule; the batch controller requeues the evicted work; a PDB on a database prevents its eviction even at lower priority.
- Failure modes: priority inflation — every team sets max priority, so the ordering is meaningless and preemption fights itself (govern the range); preemption storms where evicted pods immediately reschedule and re-preempt; priority without quotas — a greedy priority-100 workload squeezes everyone; batch jobs losing progress repeatedly to preemption; preemption ignoring PDBs in some configurations, violating availability guarantees.
- Tradeoffs: priorities give critical workloads scheduling guarantees under scarcity but add a governance burden and a failure mode (mass eviction) that is hard to debug; the alternative — overprovisioning or quotas — is simpler but wasteful; the mature pattern is a small, governed priority ladder plus quotas and PDBs.
- Operational notes: audit priority assignments, monitor preemption events, and keep the priority ladder documented.
- RSIS3 relevance: if cosmos runs time-critical jobs (dashboard builds, telemetry collection) alongside batch work, priorities keep the critical path scheduled when nodes fill up.

## Related
- [[wiki/infrastructure/priority-queuing-and-dscp|Priority Queuing & DSCP]] — related coverage in the same cluster
- [[wiki/devops-infra/storage-classes-and-provisioners|Storage Classes & Provisioners]] — related coverage in the same cluster
- [[wiki/infrastructure/storage-classes|Storage Classes]] — related coverage in the same cluster
- [[wiki/cloud-infra/coldline-and-archive-storage-classes|Coldline & Archive Storage Classes]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
