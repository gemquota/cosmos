---
type: "concept"
title: "Authorization Models"
description: "The models for deciding what an authenticated party may do"
tags: ["authorization", "rbac", "abac", "access-control"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Authorization", "https://en.wikipedia.org/wiki/Role-based_access_control"]
---

# Authorization Models

## Summary
Authorization models decide what an authenticated identity may do: role-based access control (RBAC), attribute-based (ABAC), relationship-based (ReBAC), and policy-based (OPA-style). Choosing and centralizing the model is what keeps permissions auditable as systems grow.

## Details
- RBAC assigns roles to users and permissions to roles — simple, widely understood, prone to role explosion.
- ABAC evaluates attributes (user, resource, context) against policies — flexible, needs a policy engine.
- ReBAC (Google Zanzibar lineage) models relationships like owner and viewer — natural for collaborative systems.
- Centralize decisions: a policy engine or dedicated authorization service beats scattered if-statements.
- Auditability is the requirement: every decision should be explainable and logged.
- For the mykb bundle, authorization governs who may write, publish, or verify wiki content.
- Worked example — the wiki uses ReBAC: users own their articles, curators verify sources, and admins publish; the decision service answers 'can user X verify article Y?' consistently everywhere.

Worked example — the wiki uses ReBAC: users own their articles, curators verify sources, and admins publish; the decision service answers 'can user X verify article Y?' consistently everywhere.

## Related
- [[wiki/compositions/authentication-patterns|Authentication Patterns]]
- [[wiki/compositions/identity-management|Identity Management]]
- [[wiki/compositions/zero-trust-architecture|Zero-Trust Architecture]]
- [[wiki/security/rbac|RBAC]]
- [[wiki/security/abac|ABAC]]
- [[wiki/compositions/security-engineering|Security Engineering]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/compositions/distributed-locks|Distributed Locks]]
