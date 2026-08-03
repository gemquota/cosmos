---
type: "concept"
title: "Federation vs Hub-Spoke"
description: "Two models for coordinating application placement across clusters"
tags: ["federation", "hub-spoke", "kubernetes", "architecture"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Federation vs Hub-Spoke

## Summary
Two patterns dominate multi-cluster Kubernetes management. Federation (KubeFed) uses a central control plane that propagates and reconciles selected resources across member clusters, making them behave as one fleet. Hub-spoke keeps clusters independent and manages them from a central hub — Argo CD, ACM, or Fleet — that pushes configuration without owning the clusters' workloads.

## Details
- Federation (KubeFed): a federation control plane propagates chosen resources (deployments, ingresses, secrets) to member clusters and keeps them in sync; templated placement controls which clusters receive which resources. It suits fleets that must stay logically identical.
- Hub-spoke: the hub holds configuration and state (repositories, policies, app definitions) and pushes to spokes through GitOps agents; spokes stay autonomous and can run offline or with local overrides. It is the more common production pattern because failure domains remain isolated.
- Concrete example: Argo CD on a hub with registered cluster destinations; ApplicationSets generate apps per cluster; the hub is a control-plane tenant, not a workload tenant, so hub failure degrades management rather than runtime.
- Failure modes: federation's sync controller fighting local controllers that reconcile the same Deployment — reserve federated resources for truly global ones; credential sprawl in hub-spoke, where a hub holding kubeconfigs is a single compromise point — use short-lived tokens and audit who can add destinations; split-brain when spokes hold divergent overrides after a partial push.
- Tradeoffs: federation gives stronger consistency at the cost of coupling and coordinated upgrades; hub-spoke accepts eventual consistency for operational simplicity and per-cluster autonomy. A common hybrid federates identity and policies while running applications hub-spoke.
- RSIS3 relevance: RSIS3's multiple instances (dev versus prod knowledge bases) map naturally to hub-spoke — a central control repo pushes configuration to independent instances while each keeps local state.

## Related
- [[wiki/infrastructure/hub-spoke-vs-mesh-topologies|Hub-Spoke vs Mesh Topologies]]
- [[wiki/devops-infra/workload-identity-federation|Workload Identity Federation]]
- [[wiki/infrastructure/redis-cluster-and-sentinel|Redis Cluster And Sentinel]]
- [[wiki/devops-infra/multi-cluster-management|Multi-Cluster Management]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
