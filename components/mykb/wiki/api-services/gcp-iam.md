---
type: "concept"
title: "GCP IAM"
description: "Google Cloud's identity and access management with roles and policies"
tags: ["gcp", "iam", "roles", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cloud.google.com/iam/docs/overview"]
---

# GCP IAM

- GCP IAM grants permissions through roles (primitive, predefined, custom) bound to principals (users, groups, service accounts).
- Policies bind roles to principals at the project, folder, or organization level, evaluated with deny rules taking precedence.
- Service accounts and Workload Identity reduce long-lived key usage for applications.
- For mykb: GCP service accounts with scoped roles are the clean way to give agents cloud access.

## Related

- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — roles are GCP's model
- [[wiki/security-auth/least-privilege|Least Privilege]] — custom minimal roles
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]] — governing GCP configuration
- [[wiki/security/secrets-management|Secrets Management]] — short-lived cloud credentials
