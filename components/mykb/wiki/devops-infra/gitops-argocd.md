---
type: "concept"
title: "GitOps & ArgoCD"
description: "Git as the source of truth for cluster state"
tags: ["gitops", "argocd", "kubernetes", "git"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://argo-cd.readthedocs.io/en/stable/",
  "https://www.gitops.tech/",
]
---

# GitOps & ArgoCD

## Summary
GitOps makes Git the single source of truth for cluster state, with tools like Argo CD continuously reconciling the cluster to the repo. Declarative state plus automated sync gives auditable, reversible operations. It is the standard deployment model for Kubernetes.

## Details
- GitOps practices define the repo as the desired state and the operator as the reconciler.
- Argo CD watches Git repositories and applies manifests to the cluster, reporting sync and health status continuously.
- Diffing shows drift between the repo and the cluster before sync.
- Rollbacks are just reverting a commit and letting the tool reconcile the cluster back to the previous state.
- The CNCF GitOps principles formalize the model's guarantees: declarative, versioned, and automated.
- In mykb, GitOps connects to Argo CD ApplicationSets, sync policies, and progressive delivery.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/gitops-bootstrap-processes|GitOps Bootstrap Processes]]
- [[wiki/devops-infra/argocd-applicationsets|ArgoCD ApplicationSets]]
- [[wiki/devops-infra/acid|ACID]]
- [[wiki/devops-infra/alert-fatigue|Alert Fatigue]]
