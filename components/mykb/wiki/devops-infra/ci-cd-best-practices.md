---
type: "concept"
title: "CI/CD Best Practices"
description: "Fast feedback, hermetic builds, and safe promotion"
tags: ["ci-cd", "best-practices", "pipelines", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://docs.gitlab.com/ci/",
  "https://docs.github.com/en/actions",
]
---

# CI/CD Best Practices

## Summary
CI/CD best practices make pipelines fast, reliable, and safe: fast feedback, hermetic builds, and safe promotion. Pipelines are themselves code that must be reviewed and tested. These practices are the foundation of developer velocity and delivery reliability.

## Details
- Fast feedback keeps builds under minutes so failures reach developers immediately.
- Hermetic builds pin dependencies and run in clean environments for reproducibility.
- GitLab CI documentation details pipeline configuration and best practices.
- Cache and artifact management separate reusable work from outputs.
- Safe promotion moves artifacts through environments with gates, not rebuilds.
- In mykb, CI/CD connects to build caching, artifact repositories, and deployment strategies.
- Pipeline stages should fail fast and cache aggressively to keep developer loops short.
- Secrets are passed to jobs via vaults or masked variables, never committed to the repo.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/cloud-infra/security-group-best-practices|Security Group Best Practices]]
- [[wiki/devops-infra/envoy-data-plane|Envoy Data Plane]]
- [[wiki/devops-infra/entities/ci-cd-patterns|CI/CD Patterns]]
- [[wiki/infrastructure/ci-cd-for-data|Ci Cd For Data]]
