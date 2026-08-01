---
type: "concept"
title: "RBAC"
description: "Role-based access control: permissions granted through roles assigned to users"
tags: ["rbac", "authorization", "iam", "access-control", "security"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# RBAC

## Summary
RBAC (Role-Based Access Control) assigns permissions to roles and roles to users, instead of granting each user permissions directly. It is the most common authorization model.

## Details
- Core entities: users, roles, permissions (or role hierarchies); NIST INCITS 359 formalizes it.
- Reduces administration: manage roles, not individuals; audit via role memberships.
- Limits: roles can be coarse; ABAC adds attributes for fine-grained policy.

## Related
- [[wiki/security/abac|ABAC]] — attribute-based extension
- [[wiki/security/zero-trust|Zero Trust Architecture]] — least-privilege enforcement
- [[wiki/security/sso|Single Sign-On]] — role source via IdP
- [[wiki/security/oauth2|OAuth 2.0]] — scoped tokens as roles
- [[wiki/security/ldap|LDAP]] — group-based role assignment
