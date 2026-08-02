---
type: "concept"
title: "AWS IAM"
description: "AWS's identity and access management service for users, roles, and policies"
tags: ["aws", "iam", "policies", "cloud"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html", "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html"]
---

# AWS IAM

## Summary


## Details
- AWS Identity and Access Management (IAM) controls who can access AWS resources: users, groups, roles, and policies combine into the authorization model.
- Policies are JSON documents granting or denying actions on resources; roles are the mechanism for temporary credentials, including for services and federated identities.
- The least-privilege principle drives policy design: grant the minimum actions and resources a workload needs, and review regularly.
- Common failures are overly broad wildcard policies, long-lived access keys, and roles assumed from untrusted identities.
- **Worked example / comparison** — Worked example — a CI job assumes a role with only the S3 PutObject action on one bucket prefix, so even a compromised job cannot touch other resources.
- For mykb, AWS IAM is the reference model for identity and access, contrasted with GCP IAM and Azure Entra ID in the same cluster.

## Related
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]]
- [[wiki/security-auth/least-privilege|Least Privilege]]
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]]
- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
