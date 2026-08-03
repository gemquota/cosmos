---
type: "concept"
title: "Stateful Application Patterns"
description: "Running databases and queues on Kubernetes with stable identity"
tags: ["stateful", "kubernetes", "databases", "storage"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Stateful Application Patterns

## Summary
Stateful application patterns cover how workloads with persistent data run on Kubernetes: StatefulSets for stable identity and ordering, PVCs for durable storage, headless services for stable network identity, and the operational patterns (backup, restore, scale-down safety, node-pinned storage) that make stateful apps reliable.

## Details
- Mechanism: a StatefulSet gives each replica a stable name (app-0, app-1), stable storage via volumeClaimTemplates (a PVC per replica), and ordered startup/shutdown; a headless service exposes stable DNS names; scaling down is ordered and the operator decides whether to keep or delete PVCs; controllers (operators) handle the app-specific lifecycle on top.
- Concrete example: a three-node database StatefulSet with one PVC per replica; pod app-0 resolves via DNS and its data survives rescheduling; scaling down from 3 to 2 must be safe (data on app-2 may be removed); an operator manages backups, failover, and rebalancing.
- Failure modes: scaling down accidentally deleting the PVC (and data) when the volumeClaimTemplate is removed; node loss stranding local volumes — data pinned to a dead node; rescheduling races where two replicas briefly share a volume; ordered startup making rollouts slow when startup is sequential; stateful sets with no backup plan, where PVC deletion means data loss.
- Tradeoffs: StatefulSets buy stable identity and storage at the cost of operational complexity — scaling, upgrades, and failure recovery are all harder than for stateless Deployments; the alternative, stateless-plus-external-store (database-as-a-service, object storage), trades control for simplicity; the decision is whether the workload truly needs node-local, ordered state or can outsource it.
- Operational notes: protect PVCs with explicit reclaim policies, back up statefully, test scale-down and node-loss scenarios, and prefer operators for complex lifecycles.
- RSIS3 relevance: the wiki store and checkpoint volume are exactly the stateful workload — stable identity, durable PVCs, and a rehearsed recovery path.

## Related
- [[wiki/devops-infra/web-application-firewalls|Web Application Firewalls]]
- [[wiki/cloud-infra/serverless-computing-patterns|Serverless Computing Patterns]]
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]]
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
