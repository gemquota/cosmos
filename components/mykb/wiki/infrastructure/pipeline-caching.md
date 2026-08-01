---
type: "concept"
title: "Pipeline Caching"
description: "Reusing dependencies and build outputs across CI runs to cut build time and cost"
tags: ["ci-cd", "caching", "pipelines", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
---

# Pipeline Caching

## Summary
Pipeline caching stores dependencies, layers, and build outputs so consecutive CI runs skip re-downloading and rebuilding. It is the highest-leverage speedup for slow pipelines.

## Details
- Cache scopes: package managers (npm, pip, Maven), container layers, and compiled outputs.
- Cache keys must change when inputs change — wrong keys serve stale artifacts.
- Caches are shared mutable state: corruption and poisoning are supply-chain risks.
- Open question: how to size and secure caches across many parallel builds.

## Related
- [[wiki/infrastructure/artifact-repositories|Artifact Repositories]] — the durable cache backend
- [[wiki/infrastructure/container-registries|Container Registries]] — layer caching for images
- [[wiki/devops-infra/github-actions|GitHub Actions]] — native action cache
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — cache poisoning risk
