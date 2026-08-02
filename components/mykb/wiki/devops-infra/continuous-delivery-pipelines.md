---
type: "concept"
title: "Continuous Delivery Pipelines"
description: "Automating the path from commit to production"
tags: ["cd", "pipelines", "automation", "delivery"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://continuousdelivery.com/",
  "https://docs.github.com/en/actions",
]
---

# Continuous Delivery Pipelines

## Summary
Continuous delivery pipelines automate the path from commit to deployable artifact and beyond. Pipelines run builds, tests, and deployments with gates and approvals at every stage. CD turns deployment from a risky event into a routine, repeatable process.

## Details
- The CD model requires artifacts that are built once and promoted through environments.
- Pipelines compose stages: checkout, build, test, package, deploy, verify.
- GitHub Actions and GitLab CI document their pipeline models.
- Deployment strategies (blue-green, canary) are pipeline stages, not manual steps.
- Artifact provenance ties the deployed version back to its source commit.
- In mykb, CD connects to CI/CD best practices, GitOps, and deployment verification.
- Pipeline definitions in the repository make the delivery process reviewable like code.
- Environment promotion reuses the same artifact, keeping testing and production identical.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/infrastructure/openflow-pipelines|OpenFlow Pipelines]]
- [[wiki/devops-infra/progressive-delivery-models|Progressive Delivery Models]]
- [[wiki/cloud-infra/content-delivery-networks|Content Delivery Networks]]
- [[wiki/os-shell/text-processing-pipelines|Text Processing Pipelines]]
