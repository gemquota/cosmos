---
type: "concept"
title: "GCP IAM"
description: "Google Cloud's identity and access management with roles and policies"
tags: ["gcp", "iam", "roles", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://cloud.google.com/iam/docs/overview", "https://cloud.google.com/iam/docs/understanding-roles"]
---

# GCP IAM

## Summary


## Details
- Google Cloud IAM binds principals (users, groups, service accounts) to roles on resources: the role defines allowed permissions, the binding defines who gets them.
- Roles are either predefined (curated by Google), basic (owner/editor/viewer), or custom (user-defined permission sets).
- Service accounts provide machine identity, and the resource hierarchy (organization, folders, projects) controls where bindings apply.
- The principle of least privilege applies per binding, and policy analysis tools can show effective access and over-permission.
- **Worked example / comparison** — Worked example — a Cloud Run service runs as a service account with a custom role that can only write to its own bucket; the deployment pipeline holds broader permissions separately.
- For mykb, GCP IAM is documented as the role-and-binding model, compared against AWS IAM and Azure Entra ID.

## Related
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]]
- [[wiki/security-auth/least-privilege|Least Privilege]]
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]]
- [[wiki/security/secrets-management|Secrets Management]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
