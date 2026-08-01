---
type: "concept"
title: "ABAC"
description: "Attribute-based access control: policies evaluated over subject, resource, action, and context attributes"
tags: ["abac", "authorization", "iam", "access-control", "policy"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# ABAC

## Summary
ABAC (Attribute-Based Access Control) authorizes requests by evaluating policies against attributes: subject (user), resource (note), action (read), and environment (time, location). It enables fine-grained, context-aware rules.

## Details
- Policies are expressions like `subject.team == resource.owner_team AND env.time within business_hours`.
- XACML and OPA (Rego) are common engines; policies live outside application code.
- Trade-off: expressive and dynamic but requires careful policy management and evaluation performance.

## Related
- [[wiki/security/rbac|RBAC]] — simpler role-based baseline
- [[wiki/security/zero-trust|Zero Trust Architecture]] — attribute-driven decisions
- [[wiki/security/oauth2|OAuth 2.0]] — scopes as attributes
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — per-note access rules
- [[wiki/ops/gap-report|Gap Analysis Report]] — access-control gaps
