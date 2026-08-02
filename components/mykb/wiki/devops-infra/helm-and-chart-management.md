---
type: "concept"
title: "Helm & Chart Management"
description: "Packaging and templating Kubernetes applications"
tags: ["helm", "charts", "kubernetes", "packaging"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://helm.sh/docs/",
  "https://helm.sh/docs/topics/charts/",
]
---

# Helm & Chart Management

## Summary
Helm packages Kubernetes applications as charts: templated manifests with values, hooks, and versioning. Charts make complex applications installable and upgradeable in one command. Helm is the dominant packaging tool in the ecosystem.

## Details
- A chart is a directory of templates rendered with user-supplied values, producing the concrete Kubernetes manifests to apply.
- Releases track install and upgrade history, enabling rollback to any previously deployed chart version.
- The official Helm documentation covers chart structure, values files, and the release lifecycle in detail.
- Hooks such as pre-install and post-upgrade coordinate sequenced actions during the release lifecycle.
- Repository-based distribution makes charts shareable, with provenance and signing available for supply-chain safety.
- In mykb, Helm connects to GitOps, registries, and continuous delivery articles across the cluster.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/cloud-infra/quota-management|Quota Management]]
