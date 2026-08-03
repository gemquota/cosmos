---
type: "concept"
title: "GitOps Bootstrap Processes"
description: "Booting a cluster from Git-managed state, starting with a seed"
tags: ["gitops", "bootstrap", "kubernetes", "argo"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# GitOps Bootstrap Processes

## Summary
GitOps bootstrap processes bring a cluster or environment from empty to fully managed — installing the GitOps operator, connecting it to the source repository, and verifying the first sync — entirely through declarative, reviewed artifacts. The bootstrap is itself GitOps: the tool that manages everything is installed by code, not by hand.

## Details
- Mechanism: the process starts with minimal secrets and a repo; the operator (Argo CD, Flux) is installed via a bootstrap manifest or its installer; it registers the repository and the target path; the first sync applies the declared apps, policies, and namespaces; successive steps promote more of the system into the repo until nothing is hand-managed.
- Concrete example: a new cluster runs `flux bootstrap github` — Flux installs itself, commits its manifests to the repo, and applies them; from then on, the cluster is reconstructed from the repo; Argo CD's bootstrap installs the controller and points it at an app-of-apps repo that defines everything else.
- Failure modes: bootstrap secrets (repo tokens, cloud credentials) embedded in manifests and committed — use sealed secrets, SOPS, or external secret stores from the start; a bootstrap that half-succeeds, leaving an operator installed but no sync (check the first reconciliation); ordering dependencies — the operator needs the repo reachable and credentials valid at first boot; idempotency — re-running bootstrap must converge, not duplicate resources.
- Tradeoffs: a fully bootstrapped, repo-managed cluster is reproducible and auditable but has a chicken-and-egg cost: you must carefully handcraft the bootstrap that then manages everything; the alternative — hand-provisioning — works but is unrepeatable; bootstrap code deserves the same review as production code.
- Operational notes: test bootstrap in a throwaway cluster, document the recovery path (rebuild from repo plus bootstrap), and rotate bootstrap credentials separately from runtime credentials.
- RSIS3 relevance: a fresh cosmos deployment should follow the same idea — one documented, scripted bootstrap that brings up the wiki daemon, dashboard build, and their config from the repo alone.

## Related
- [[wiki/devops-infra/gitops-argocd|GitOps & ArgoCD]]
- [[wiki/devops-infra/gitops-multi-env-patterns|GitOps Multi-Env Patterns]]
- [[wiki/infrastructure/dataset-release-processes|Dataset Release Processes]]
- [[wiki/os-shell/daemon-processes|Daemon Processes]]
