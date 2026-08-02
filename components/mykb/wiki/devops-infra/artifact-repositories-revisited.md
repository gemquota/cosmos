---
type: "concept"
title: "Artifact Repositories"
description: "Central stores for packages, images, and binaries"
tags: ["artifacts", "repository", "packages", "distribution"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.github.com/en/packages",
  "https://en.wikipedia.org/wiki/Binary_repository_manager",
]
---

# Artifact Repositories

## Summary
Artifact repositories store the packages, images, and binaries that pipelines produce and consume. Central repositories enable versioning, caching, and access control across teams. They are the connective tissue of the software supply chain and a key control point for security.

## Details
- Repositories host language packages, container images, and generic binaries with metadata.
- GitHub Packages and other hosted registries document their formats and authentication.
- Proxying upstream registries caches dependencies and controls what enters the build.
- Retention policies and signing protect against stale and tampered artifacts.
- Environment parity depends on promoting the same artifact, not rebuilding.
- In mykb, artifact repositories connect to registries, CI/CD, and supply-chain security.
- Repository promotion and tagging encode the maturity level of each artifact.
- Usage analytics reveal which artifacts are actually consumed and which can be retired.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/package-signing-and-repositories|Package Signing & Repositories]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]]
- [[wiki/devops-infra/acid|ACID]]
