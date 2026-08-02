---
type: "concept"
title: "Build Caching & Artifacts"
description: "Reusing work and storing outputs across builds"
tags: ["build", "caching", "artifacts", "ci"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://bazel.build/remote/caching",
  "https://docs.gitlab.com/ci/",
]
---

# Build Caching & Artifacts

## Summary
Build caching reuses unchanged work across builds, while artifacts preserve outputs for later stages. Together they make pipelines fast and deterministic. Cache invalidation and artifact hygiene are the hard parts that teams must engineer carefully.

## Details
- Content-based caching keys outputs on inputs, so unchanged sources skip recompilation.
- Bazel's remote caching documentation describes the mechanism and tradeoffs.
- Job artifacts in GitLab preserve test reports and binaries between stages.
- Remote caches share work across machines and CI runs.
- Cache poisoning and correctness are managed with strict keying.
- In mykb, build caching connects to CI/CD and artifact repositories.
- Cache keys must include every input that affects the output, including toolchain versions.
- Artifact retention policies keep storage bounded while preserving auditability.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/http-caching-directives|HTTP Caching Directives]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/infrastructure/pipeline-caching|Pipeline Caching]]
- [[wiki/devops-infra/acid|ACID]]
