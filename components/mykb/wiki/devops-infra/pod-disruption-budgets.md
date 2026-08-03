---
type: "concept"
title: "Pod Disruption Budgets"
description: "Limiting voluntary evictions to protect availability"
tags: ["pdb", "disruption", "kubernetes", "availability"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Pod Disruption Budgets

## Summary
PodDisruptionBudgets (PDBs) cap how many pods of a workload may be voluntarily evicted at once — node drains, cluster upgrades, autoscaling. They do not protect against node crashes or application failures; they protect availability during planned maintenance by guaranteeing a minimum number of replicas stay up.

## Details
- Mechanism: a PDB specifies minAvailable (or maxUnavailable) as a number or percentage; during voluntary disruptions (kubectl drain, Descheduler, cluster upgrades), the eviction API rejects requests that would violate the budget; controllers and drain tools retry or reorder; involuntary disruptions (node death) are unaffected.
- Concrete example: a Deployment with 3 replicas and minAvailable: 2 — a node drain can evict one pod at a time; draining two nodes concurrently blocks the second eviction until the first replacement is ready; a PDB on the database StatefulSet keeps quorum during upgrades.
- Failure modes: PDBs set too tight (minAvailable equal to replicas) that block all maintenance indefinitely — cluster upgrades stall; PDBs that ignore readiness, so the budget counts not-ready pods and disruption still causes downtime; percentage rounding that permits zero available; eviction storms when the drain tool retries aggressively against a full budget.
- Tradeoffs: PDBs are cheap insurance for planned disruption but only as good as the replica count and readiness they assume; the alternative — no PDBs — lets maintenance tools evict everything at once, turning an upgrade into an outage; pair PDBs with anti-affinity so evictions land on distinct nodes.
- Operational notes: size PDBs from real capacity, watch PDB status (currentHealthy, desiredHealthy), and test drain behavior in staging.
- RSIS3 relevance: if the wiki daemon runs replicated, a PDB keeps retrieval available during node maintenance — a small config that prevents a big outage.

## Related
- [[wiki/devops-infra/slo-and-error-budgets|SLOs & Error Budgets]] — related coverage in the same cluster
- [[wiki/devops-infra/pod-to-pod-communication|Pod-to-Pod Communication]] — related coverage in the same cluster
- [[wiki/devops-infra/error-budgets|Error Budgets]] — related coverage in the same cluster
- [[wiki/infrastructure/pod-lifecycle|Pod Lifecycle]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
