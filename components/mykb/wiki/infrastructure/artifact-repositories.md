---
type: "concept"
title: "Artifact Repositories"
description: "Central stores for build outputs — images, packages, binaries — with versioning and access control"
tags: ["artifacts", "repositories", "ci-cd", "supply-chain"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Artifact Repositories

## Summary
Artifact repositories store and version every build output — container images, language packages, binaries — so deployments consume known, immutable artifacts. They are the bridge between CI and production.

## Details
- Repositories hold immutable artifacts with provenance: digests, signatures, and metadata.
- Proxy and cache upstreams (Maven, npm, PyPI) for supply-chain control and reliability.
- Access control and retention policies turn the repo into a governance point.
- Open question: how artifact immutability and vulnerability patching should interact.

## Related
- [[wiki/infrastructure/container-registries|Container Registries]] — the image-specific repository
- [[wiki/infrastructure/pipeline-caching|Pipeline Caching]] — repositories speed up pipelines
- [[wiki/infrastructure/container-scanning|Container Scanning]] — scanning at the repository gate
- [[wiki/security/sbom|SBOM]] — provenance metadata in repositories
