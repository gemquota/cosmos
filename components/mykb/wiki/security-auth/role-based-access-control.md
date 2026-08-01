---
type: "concept"
title: "Role-Based Access Control"
description: "Authorization model where users receive permissions through assigned roles"
tags: ["rbac", "authorization", "access-control", "nist"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://csrc.nist.gov/projects/role-based-access-control"]
---

# Role-Based Access Control

## Summary

Role-based access control (RBAC) grants permissions not directly to users but to roles, and users receive roles. Because permissions change with the role rather than per-user, administration scales and separation of duties becomes expressible. NIST standardized RBAC in INCITS 359-2012 with flat, hierarchical, and constrained models; the NIST RBAC project page is the canonical reference. RBAC is the default authorization model for mykb's files, APIs, and admin surfaces, so its role inventory needs deliberate design.

## Details

- Core elements: users, roles, permissions, and sessions; a user-role assignment plus role-permission assignment yields effective permissions.
- Role hierarchies: senior roles inherit permissions of junior roles, simplifying administration while preserving least privilege at the leaves.
- Constraints: separation of duty (no user may hold conflicting roles) and cardinality (limits on role membership) enforce business and audit rules.
- RBAC vs ACLs: ACLs attach permissions directly to resources per user; RBAC centralizes them in roles, which is easier to audit and provision.
- Limits: RBAC is static — it struggles with context like time, location, or data sensitivity, which is where ABAC extends it.
- For RSIS3, roles map cleanly onto agent personas: reader, curator, operator, and admin roles bound the blast radius of each agent session.

## Related

- [[wiki/security-auth/least-privilege|Least Privilege]] — the principle role design should satisfy
- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]] — dynamic alternative and complement
- [[wiki/security/rbac|RBAC]] — existing article on RBAC
- [[wiki/security/zero-trust|Zero Trust Architecture]] — RBAC supplies the authorization decision
- [[wiki/api-services/aws-iam|AWS IAM]] — cloud-native RBAC implementation
- [[wiki/api-services/azure-ad|Microsoft Entra ID]] — enterprise role and group management
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — roles bound to RSIS3 identities
