---
type: "concept"
title: "Infrastructure Drift Detection"
description: "Finding and reconciling config that diverged from the desired state"
tags: ["drift", "iac", "terraform", "gitops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Infrastructure Drift Detection

## Summary
Infrastructure drift is the difference between declared configuration (Terraform, Helm, GitOps manifests) and the actual running state. Drift detection continuously compares the two, reports divergence, and optionally reconciles; it turns "I think production matches the repo" into a checked, measurable fact.

## Details
- Mechanism: a detector compares desired state (repo) with observed state (cloud API, cluster, live resources) — `terraform plan` diff, Argo CD's sync status, Flux drift detection, cloud config rules; results classify resources as in-sync, out-of-sync, or unknown; policy decides whether to alert, auto-reconcile, or require a human fix.
- Concrete example: Argo CD shows an out-of-sync app because someone scaled a Deployment by hand; Flux detects and reverts it within a minute (or flags it); Terraform drift runs in CI nightly and files a ticket when state diverges; cloud rules flag a security group opened out-of-band.
- Failure modes: auto-reconcile fighting legitimate out-of-band actions (emergency scaling, manual data migration) — create an explicit "bypass with review" path; detectors that cannot see certain resources, giving false confidence; alert fatigue when drift is noisy but benign; drift detection itself drifting (detector credentials stale, checks disabled).
- Tradeoffs: continuous reconciliation enforces the repo as truth but can stomp intentional manual changes; detection-only preserves flexibility but lets drift accumulate until it matters; the mature pattern is detection with alerting plus reconciliation for known-safe resource classes and manual approval for the rest.
- Operational notes: separate drift alerts by severity, keep detector credentials least-privileged, and periodically reconcile known drift back into the repo so the repo stays the source of truth.
- Coverage: detect drift in managed resources and in unmanaged ones — periodic full inventory scans catch out-of-band edits and unknown resources that config tools never see.
- RSIS3 relevance: RSIS3's state files can drift from their schemas the same way — a drift check on registry invariants and checkpoints catches loops that mutated state outside the declared format.

## Related
- [[wiki/devops-infra/infrastructure-as-code-revisited|Infrastructure as Code]]
- [[wiki/infrastructure/intrusion-detection-systems|Intrusion Detection Systems]]
- [[wiki/infrastructure/gpu-compute-infrastructure|GPU Compute Infrastructure]]
- [[wiki/infrastructure/configuration-drift|Configuration Drift]]
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]]
