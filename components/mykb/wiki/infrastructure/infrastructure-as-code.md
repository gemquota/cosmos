---
type: "concept"
title: "Infrastructure as Code"
description: "Managing infrastructure through declarative, versioned, reviewable definition files instead of manual changes"
tags: ["iac", "terraform", "declarative", "automation", "devops"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.hashicorp.com/terraform/intro"]
---

# Infrastructure as Code

## Summary
Infrastructure as code (IaC) treats infrastructure as versioned, reviewable artifacts: definitions in a repository replace click-ops and undocumented changes. Declarative tools like Terraform compute the difference between desired and actual state and apply only what changed. This makes environments reproducible, auditable, and testable.

## Details
- Declarative vs imperative: declarative files describe the end state (a VPC with these subnets), and the tool figures out the steps; imperative scripts encode the steps themselves.
- Terraform workflow: write HCL, run plan to preview changes, apply to converge, and store state to track real-world resources — state management is the hard part.
- Idempotency: re-running apply on an unchanged configuration produces no changes, which enables safe retries and drift detection.
- IaC pairs with CI/CD: pull requests change infrastructure the same way they change code, with plan output as the review artifact.
- Scope: provisioning (Terraform, CloudFormation, Pulumi) is often split from configuration management of the software inside servers.
- Worked example: a mykb environment as a Terraform module — VPC, database, and cluster — with separate workspaces for staging and production, gated by plan reviews.
- Failure mode: state corruption or hand-edited resources create drift; import, locking, and state backends are the mitigations.

## Related
- [[wiki/devops-infra/tfstate-management|Terraform State Management]] — the state backend problem in practice
- [[wiki/infrastructure/configuration-drift|Configuration Drift]] — what happens when state and reality diverge
- [[wiki/cloud-infra/cloud-emulators|Cloud Emulators]] — testing IaC locally without a cloud
- [[wiki/devops-infra/terraform|Terraform]] — the reference IaC tool
- [[wiki/devops-infra/github-actions|GitHub Actions]] — running plan/apply in CI
- [[wiki/infrastructure/configuration-management|Configuration Management]] — software state inside provisioned servers
