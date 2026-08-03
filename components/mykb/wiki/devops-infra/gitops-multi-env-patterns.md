---
type: "concept"
title: "GitOps Multi-Env Patterns"
description: "Reusing one repo across dev, staging, and prod environments"
tags: ["gitops", "environments", "kubernetes", "config"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# GitOps Multi-Env Patterns

## Summary
GitOps multi-environment patterns structure how one set of manifests becomes dev, staging, and production: environment overlays (Kustomize), templated values (Helm), or one-application-per-environment with promotion between them. The pattern decides where environment-specific values live, how promotion is reviewed, and how drift is prevented.

## Details
- Mechanism: the base manifests live once; per-environment overlays or values files layer differences (replicas, image tags, domains, secrets references); Argo CD or Flux syncs each environment's rendered output from its own path or branch; promotion is a change to the environment's image tag or values, reviewed via PR, often with approval gates between staging and prod.
- Concrete example: a repo with `base/` plus `overlays/dev|staging|prod` in Kustomize; a new image tag is bumped in staging's overlay, verified, then promoted to prod's overlay in a second PR; Flux multi-tenancy or Argo CD applications per environment keep sync scoped.
- Failure modes: overlay drift — a value added to prod but not staging means promotion surprises; promotion by copy-paste diverging from the base; image tags floating (`latest`) so environments run different code than reviewed; secrets in overlays; one environment failing sync while others succeed, hiding config errors until the next promotion.
- Tradeoffs: single-source-of-truth bases are DRY but make environment-specific quirks harder to express; fully duplicated per-environment repos are explicit but drift-prone; the middle path — shared base plus minimal overlays plus promotion gates — balances fidelity and reviewability.
- Operational notes: enforce image digest pinning, add diff checks between environments, and make promotion a recorded, reviewable artifact.
- RSIS3 relevance: cosmos's own environments (dev wiki, published dashboard) benefit from the same overlay structure so promoting a dashboard build or wiki update is a reviewed diff.

## Related
- [[wiki/devops-infra/gitops-argocd|GitOps & ArgoCD]] — related coverage in the same cluster
- [[wiki/cloud-infra/multi-cloud-hybrid-cloud|Multi-Cloud & Hybrid Cloud]] — related coverage in the same cluster
- [[wiki/devops-infra/nginx-configuration-patterns|NGINX Configuration Patterns]] — related coverage in the same cluster
- [[wiki/devops-infra/api-mesh-patterns|API Mesh Patterns]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
