---
type: "concept"
title: "AWS IAM"
description: "AWS's identity and access management service for users, roles, and policies"
tags: ["aws", "iam", "policies", "cloud"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html"]
---

# AWS IAM

- AWS IAM manages users, groups, roles, and policies that grant permissions on AWS resources.
- Best practice: roles over users, least-privilege policies, no long-lived access keys, and MFA on privileged principals.
- Policies are JSON statements with effect, action, resource, and condition — a real-world RBAC/ABAC blend.
- For mykb: if hosting on AWS, IAM roles for services replace static credentials entirely.

## Related

- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — the model IAM implements
- [[wiki/security-auth/least-privilege|Least Privilege]] — the policy design principle
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]] — assessing IAM misconfigurations
- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]] — condition keys as attributes
