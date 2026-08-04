---
type: "entity"
title: "Helm"
description: "Kubernetes package manager templating, versioning, and deploying applications as charts"
tags: ["helm", "kubernetes", "charts", "packaging", "devops"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Helm

## Summary
Helm packages Kubernetes applications as charts: templated manifests plus values, versioned and shareable. `helm install` and `helm upgrade` manage releases with rollback, giving operators a package-manager experience on top of raw YAML.

## Details
- A chart is a directory layout containing `Chart.yaml`, templates, values, and optional dependencies; `helm create` scaffolds the standard structure.
- `values.yaml` parameterizes templates; charts nest subcharts for dependencies. Values cascade from release-level overrides down through parent and child charts, with explicit precedence rules.
- Templating uses Go templates plus Sprig functions, letting manifests inject names, labels, and resource settings. `helm template` renders locally for review, and `helm lint` checks for common mistakes.
- Release history enables `helm rollback` after bad upgrades. Each `helm install` or `upgrade` records a revision, and history shows what changed between revisions.
- Repositories (such as Artifact Hub) distribute charts; lockfiles and signatures address supply-chain risk. Charts should be pinned to versions, and signed charts let operators verify provenance.
- Lifecycle hooks (pre-install, post-install, and so on) run Jobs at the right moment, while the test hooks in a chart run validation checks against a deployed release.

## Workflow
A typical flow is: author a chart, render and lint it locally, commit it, publish it to a repository, then install it into a cluster with a values file that captures the environment's settings. Upgrades reuse the release name, so rollback always has a previous revision to return to. Because charts are declarative and versioned, the same chart can promote an application from staging to production with different values and no template changes.


Helm is declarative the way Kubernetes is: the desired state lives in charts and values, and the tool reconciles the cluster toward it. This makes environments reviewable, since a pull request can change a values file instead of hand-editing live manifests. The main risks are template complexity and drift — rendered output can be hard to read, and direct kubectl edits can diverge from the chart — so teams review rendered manifests and treat the chart as the source of truth.


## Related
- [[wiki/devops-infra/kubernetes|Kubernetes]] — charts deploy to clusters
- [[wiki/devops-infra/kustomize|Kustomize]] — overlay alternative to templating
- [[wiki/security/supply-chain-security|Supply Chain Security]] — chart signing and provenance
- [[wiki/devops-infra/terraform|Terraform]] — cluster-level IaC complement
