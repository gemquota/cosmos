---
type: "concept"
title: "Zero Trust Architecture"
description: "Security model that verifies every request regardless of origin, eliminating implicit network trust"
tags: ["zero-trust", "security", "architecture", "iam", "nist"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://csrc.nist.gov/pubs/sp/800/207/final"]
---

# Zero Trust Architecture

## Summary
Zero Trust (NIST SP 800-207) is a security model in which no entity is trusted by virtue of network location — every request is authenticated, authorized, and continuously verified. It replaces perimeter firewalls with per-request policy evaluation, micro-segmentation, and least-privilege access. "Never trust, always verify" is the operating principle.

## Details
- Core tenets: all data sources are resources, all traffic is encrypted, access is per-session and least-privileged, and policy decisions use identity plus device and environment signals.
- Components: policy decision/ enforcement points, identity providers, and continuous monitoring feed a dynamic access engine.
- Implementation layers: identity-aware proxies, mTLS service meshes (Istio), short-lived credentials, and device posture checks.
- Implicit trust zones disappear: internal networks, VPNs, and "trusted" subnets no longer grant blanket access.
- Worked example: a zero-trust mykb deployment puts every daemon call through an authenticated gateway with scoped tokens, mTLS between services, and audit logs on each access decision.
- Relationship: complements [[wiki/security/rbac|RBAC]]/[[wiki/security/abac|ABAC]] for authorization decisions and [[wiki/security/mfa|MFA]] for strong authentication.

## Related
- [[wiki/security/rbac|RBAC]] — role-based authorization policies
- [[wiki/security/abac|ABAC]] — attribute-driven policy decisions
- [[wiki/security/secrets-management|Secrets Management]] — secrets become identity material
- [[wiki/devops-infra/istio|Istio]] — mTLS and policy at the mesh layer
- [[wiki/security/mfa|Multi-Factor Authentication]] — strong factor for user access
- [[wiki/security/jwt|JWT]] — short-lived credentials per session
- [[wiki/concepts/triad-architecture|Triad Architecture]] — engine/memory bridge is a trust boundary
- [[wiki/ops/gap-report|Gap Analysis Report]] — trust-boundary gaps noted
