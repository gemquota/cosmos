---
type: "concept"
title: "Environment Promotion Models"
description: "Promoting artifacts and config through environment tiers"
tags: ["promotion", "environments", "delivery", "artifacts"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Environment Promotion Models

## Summary
Environment promotion models define how configuration and artifacts move from development through staging to production. The spectrum runs from copy-and-paste (drift-prone) through scripted promotion (environment-specific rendering) to artifact promotion (one immutable artifact promoted with per-environment config).

## Details
- Artifact promotion: one build artifact (image, binary, release) is built once, verified, and promoted unchanged; environments differ only in injected configuration; this kills "compiled differently in prod" bugs and makes rollback a matter of redeploying an older artifact.
- Config promotion: the same config set moves through environments with per-environment values overlaid (Helm values, Kustomize overlays, Terraform workspaces); review happens at the diff between environments.
- Concrete example: CI builds and signs an image once; staging runs it with staging values; the same digest runs in production after approval; a promotion pipeline (GitHub Environments with approvals, Argo CD sync waves) moves the artifact and records the promotion decision.
- Failure modes: environment-specific build artifacts that mask issues until prod; config that exists only in production (ambient drift) breaking the next promotion; promotion steps done by hand and skipped or mis-ordered; secrets injected at the wrong environment; rollback promoting an old artifact against new schema, creating version skew.
- Tradeoffs: strict promotion pipelines add process and waiting time but make releases predictable and auditable; loose models ship faster but accumulate drift and surprises; the key trade is per-environment customization versus fidelity to production.
- Operational notes: promote the same digest everywhere, keep promotion logs, and rehearse rollback as part of every promotion runbook.
- RSIS3 relevance: RSIS3's own releases (loop versions, dashboard builds) should follow artifact promotion — the same generated dashboard bundle promoted to preview and production with only config differing.

## Related
- [[wiki/devops-infra/kubernetes-networking-models|Kubernetes Networking Models]] — related coverage in the same cluster
- [[wiki/devops-infra/progressive-delivery-models|Progressive Delivery Models]] — related coverage in the same cluster
- [[wiki/infrastructure/data-maturity-models|Data Maturity Models]] — related coverage in the same cluster
- [[wiki/infrastructure/t-shirt-sizing-and-resource-models|T Shirt Sizing And Resource Models]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
