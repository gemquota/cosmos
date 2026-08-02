---
type: "concept"
title: "Terraform State Management"
description: "The state file as Terraform's source of truth"
tags: ["terraform", "state", "iac", "backend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: [
  "https://developer.hashicorp.com/terraform/language/state",
  "https://developer.hashicorp.com/terraform/language/backend",
]
---

# Terraform State Management

## Summary
Terraform state records the mapping between configuration and real resources, making it the tool's source of truth. State must be stored remotely, locked, and handled carefully. State problems are the most common Terraform failure mode.

## Details
- State stores resource attributes so Terraform can plan accurate diffs and destroy resources correctly.
- Remote backends such as S3, GCS, or Azure Storage keep state shared across the team and enable locking.
- State locking prevents concurrent modifications from corrupting the mapping between config and resources.
- Sensitive values in state are stored in plaintext, so backend access control and encryption at rest matter.
- Workspaces and modules affect how state files are organized, shared, and reused across teams.
- In mykb, state management connects to backend configuration, locking, workspaces, and drift detection.
- Operationally, alerting thresholds and runbook steps for this concept belong in the SLO, incident, and runbook articles of this cluster.
- Pipelines and GitOps practices in the delivery articles show how this concept is deployed and promoted safely.

## Related
- [[wiki/infrastructure/ssh-key-management|SSH Key Management]]
- [[wiki/infrastructure/security-information-and-event-management|SIEM]]
- [[wiki/cloud-infra/dns-management|DNS Management]]
- [[wiki/cloud-infra/quota-management|Quota Management]]
