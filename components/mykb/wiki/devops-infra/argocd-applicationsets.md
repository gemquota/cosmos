---
type: "concept"
title: "ArgoCD ApplicationSets"
description: "Template-driven generation of ArgoCD applications at scale"
tags: ["argocd", "applicationset", "gitops", "kubernetes"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# ArgoCD ApplicationSets

## Summary
ApplicationSets generate ArgoCD Application resources from templates, replacing hand-maintained app definitions and sprawling app-of-apps manifests. Generators supply parameters — a git directory, a cluster list, a matrix of values — and the template renders one Application per combination, so adding a cluster or service no longer requires editing dozens of YAML files by hand.

## Details
- Generators: the List generator renders fixed parameters; the Git generator produces one app per directory or file pattern; the Cluster generator produces one app per registered cluster; Matrix and Merge generators combine outputs; the Pull Request generator builds per-PR previews automatically.
- Concrete example: a Git generator watching `apps/*/` combined with a Cluster generator across dev, staging, and prod creates the same services on every cluster; `goTemplate` interpolation turns `apps/{{path.basename}}` into app name, namespace, and source path.
- Failure modes: a generator returning zero matches silently stops deploying with no apps and no errors — alert on the generated app count; a bad template renders invalid Application specs that ArgoCD repeatedly fails to apply; `automated: selfHeal` plus a generator change can create or delete dozens of apps in one pass, so diff or dry-run before merging.
- Tradeoffs: ApplicationSets reduce boilerplate and centralize configuration but hide the per-app detail operators used to review; debugging which generator produced an app needs `argocd appset list` and label selectors. Very large sets strain the app controller's reconciliation loop, so batch operations and refresh intervals matter.
- Operational notes: pin the ApplicationSet controller to the ArgoCD release, make `preserveResourcesOnDeletion` explicit, and keep the template in git so the merge diff is the reviewable source of truth.
- Generator tuning: `requeueAfterSeconds` and revision polling decide how fast new directories and clusters appear — short intervals hammer the git host and cluster API, long ones delay rollout, so tune them per source.
- RSIS3 relevance: the same template-and-generate discipline applies to RSIS3's batch telemetry renders — generate dashboards and checkpoints from a declarative spec instead of hand-maintaining each artifact.

## Related
- [[wiki/devops-infra/gitops-argocd|GitOps & ArgoCD]]
