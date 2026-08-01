---
type: "concept"
title: "Helm"
description: "Kubernetes package manager templating, versioning, and deploying applications as charts"
tags: ["helm", "kubernetes", "charts", "packaging", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Helm

## Summary
Helm packages Kubernetes applications as charts: templated manifests plus values, versioned and shareable. `helm install`/`upgrade` manage releases with rollback.

## Details
- `values.yaml` parameterizes templates; charts nest subcharts for dependencies.
- Release history enables `helm rollback` after bad upgrades.
- Repositories (Artifact Hub) distribute charts; lockfiles and signatures address supply-chain risk.

## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — charts deploy to clusters
- [[wiki/devops-infra/kustomize|Kustomize]] — overlay alternative to templating
- [[wiki/security/supply-chain-security|Supply Chain Security]] — chart signing and provenance
- [[wiki/devops-infra/terraform|Terraform]] — cluster-level IaC complement
