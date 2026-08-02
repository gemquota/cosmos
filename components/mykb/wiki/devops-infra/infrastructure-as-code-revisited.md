---
type: "concept"
title: "Infrastructure as Code"
description: "Managing infrastructure with versioned, reviewable definitions"
tags: ["iac", "terraform", "automation", "devops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://developer.hashicorp.com/terraform/docs",
  "https://opentofu.org/docs/",
]
---

# Infrastructure as Code

## Summary
Infrastructure as code manages compute, network, and storage through versioned, reviewable definitions instead of manual clicks. Declarative tools converge the world to a desired state, enabling review, reproducibility, and automation. It is the foundation of modern platform engineering.

## Details
- Declarative configuration describes the end state; the tool plans and applies the changes needed to reach it.
- HashiCorp Terraform is the most widely used IaC tool, and OpenTofu provides an open-source fork.
- Review flows treat infrastructure changes like code changes: diffs, tests, and approvals.
- State tracks what the tool manages; drift between state and reality is the central operational risk.
- IaC enables ephemeral environments, disaster recovery, and audit of every change.
- In mykb, IaC connects to Terraform state, drift detection, GitOps, and CI/CD pipelines.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/devops-infra/gatekeeper-and-policy-as-code|Gatekeeper & Policy as Code]]
- [[wiki/devops-infra/development-environments-as-code|Development Environments as Code]]
- [[wiki/infrastructure/infrastructure-as-code|Infrastructure as Code]]
- [[wiki/cloud-infra/function-as-a-service|Function-as-a-Service]]
