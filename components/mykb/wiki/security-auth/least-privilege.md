---
type: "concept"
title: "Least Privilege"
description: "Security principle granting subjects only the minimum permissions needed for their function"
tags: ["least-privilege", "authorization", "security", "principle"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html"]
---

# Least Privilege

## Summary

Least privilege is the principle that every subject — user, service, or agent — should receive only the permissions necessary to perform its function, and only for as long as needed. It is the single most effective way to limit the blast radius of a compromised credential. OWASP's Authorization Cheat Sheet treats least privilege as the core rule of access-control design: default deny, grant minimal, review continuously. For RSIS3, least privilege is not a nicety but an operating requirement: agent sessions with write access to memory are the crown jewels.

## Details

- Implementation: default-deny policies, permission minimization at design time, and per-session rather than standing grants.
- Just-in-time and just-enough access: elevate privileges temporarily for a task and expire them automatically (JIT/JEA, privileged access management).
- Apply at every layer: IAM policies, database roles, filesystem ACLs, API scopes, and container privileges.
- Separation of duties: split sensitive actions across roles so one compromised identity cannot complete an abuse chain.
- Continuous review: permission discovery, unused-role cleanup, and access reviews keep standing grants from accumulating.
- For mykb, each agent capability list should be reviewed like a firewall rule set: what can this agent touch, and why does it need it?

## Related

- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — roles are the vehicle for least privilege
- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]] — dynamic conditions keep grants minimal
- [[wiki/api-services/api-key-management|API Key Management]] — scoped keys limit service blast radius
- [[wiki/security/rbac|RBAC]] — existing article on role-based authorization
- [[wiki/security/zero-trust|Zero Trust Architecture]] — least privilege is a zero-trust tenet
- [[wiki/security/secrets-management|Secrets Management]] — credential access should follow least privilege
- [[wiki/api-services/aws-iam|AWS IAM]] — scoped cloud policies
- [[wiki/api-services/secret-scanning|Secret Scanning]] — finding credentials that exceed their scope
- [[wiki/concepts/triad-architecture|Triad Architecture]] — engine-to-memory access minimized
