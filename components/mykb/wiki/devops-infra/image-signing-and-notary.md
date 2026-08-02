---
type: "concept"
title: "Image Signing & Notary"
description: "Cryptographic signatures that authenticate container images"
tags: ["image-signing", "notary", "containers", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Image Signing & Notary

## Summary
Cryptographic signatures that authenticate container images. This stub frames the concept and its place in the mykb Systems & Infrastructure cluster; expand it into a full article with worked examples, failure modes, and verified sources.

## Details
- Definition anchor: Cryptographic signatures that authenticate container images.
- Open questions: how this interacts with adjacent delivery, reliability, and Kubernetes operations topics, the failure modes that matter, and the operational tradeoffs to document.
- Ties to RSIS3/mykb: keeping this node discoverable makes it easier to surface from related protocols and tooling during retrieval.
- Next step: verify sources and promote to a growing article with protocol or configuration detail.

## Related
- [[wiki/devops-infra/trivy-and-image-scanning|Trivy & Image Scanning]] — related coverage in the same cluster
- [[wiki/devops-infra/package-signing-and-repositories|Package Signing & Repositories]] — related coverage in the same cluster
- [[wiki/infrastructure/docker-image-optimization|Docker Image Optimization]] — related coverage in the same cluster
- [[wiki/devops-infra/golden-images-and-image-baking|Golden Images & Image Baking]] — related coverage in the same cluster
- [[wiki/devops-infra/kubernetes-control-plane|Kubernetes Control Plane]] — related coverage in the same cluster
- [[wiki/devops-infra/observability-pillars|Observability Pillars]] — related coverage in the same cluster
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
