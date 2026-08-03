---
type: "concept"
title: "Sync Policies & Waves"
description: "Ordering ArgoCD syncs and handling automated or manual sync"
tags: ["sync", "argocd", "gitops", "ordering"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Sync Policies & Waves

## Summary
Sync policies and waves control how Argo CD and Flux apply changes to a cluster: sync policies decide when and how (automated, self-heal, prune, retry), and sync waves order resources within an apply (CRDs before controllers, namespaces before workloads). Together they make GitOps reconciliation safe, ordered, and drift-free.

## Details
- Sync policy mechanics: automated sync applies changes continuously from git; selfHeal reverts manual drift back to git; prune deletes resources removed from git; retry controls failed-sync behavior; policies are per-application, so the same cluster can have different reconciliation guarantees per app.
- Wave mechanics: resources declare an annotation (sync.argocd.argoproj.io/instance and sync-waves; Flux uses dependency ordering); Argo CD applies wave 0 first (CRDs, namespaces), then wave 1 (controllers), then wave 2 (workloads), waiting for health between waves.
- Concrete example: an app with wave 0 CRDs and Namespaces, wave 1 the operator Deployment, wave 2 the CustomResources; automated sync with prune enabled keeps the cluster exact; selfHeal reverts a hand-scaled Deployment within minutes.
- Failure modes: waves misordered — workloads syncing before their CRDs exist, failing in a retry loop; prune deleting resources whose deletion is destructive (never enable prune without reviewing); selfHeal fighting emergency manual changes; automated sync applying a broken commit fleet-wide before review; wave health checks that never become healthy, stalling all later waves.
- Tradeoffs: automation guarantees consistency but removes the human gate — pair it with strong CI (manifest validation, smoke tests) and review; waves add ordering safety at the cost of complexity; the alternative, manual sync, is controllable and slow; the mature pattern is automated sync with reviewed, tested git as the only write path.
- Operational notes: test waves in staging, monitor sync status and health, and log every sync action.
- RSIS3 relevance: cosmos's deployments benefit from ordered, automated sync — the same discipline as RSIS3 applying state changes in dependency order.

## Related
- [[wiki/devops-infra/ingress-egress-policies|Ingress & Egress Policies]]
- [[wiki/devops-infra/network-policies-kubernetes|Kubernetes Network Policies]]
- [[wiki/devops-infra/escalation-policies|Escalation Policies]]
- [[wiki/cloud-infra/snapshot-lifecycle-policies|Snapshot Lifecycle Policies]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
- [[wiki/devops-infra/observability-pillars|Observability Pillars]]
