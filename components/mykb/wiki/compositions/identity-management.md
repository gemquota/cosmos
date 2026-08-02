---
type: "concept"
title: "Identity Management"
description: "Establishing and governing who and what can access systems"
tags: ["identity", "iam", "management", "access"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Identity_management", "https://en.wikipedia.org/wiki/Authentication"]
---

# Identity Management

## Summary
Identity management (IAM) covers the lifecycle of digital identities: creation, verification, provisioning, credentialing, and deprovisioning. It answers who someone is, and it feeds every authorization decision in the system.

## Details
- Identity lifecycle: join (onboarding), maintain (credentials, roles), leave (deprovisioning) — the last is where breaches happen.
- Federated identity (SSO via OIDC/SAML) centralizes identity while systems rely on claims.
- Provisioning automation keeps accounts in sync; orphaned accounts are a top audit finding.
- Identities extend to services and devices, not just people — machine identities need the same discipline.
- The principle of least privilege applies per identity: grants are scoped and time-bound.
- For the mykb bundle, identity management covers contributors, agents, and service accounts touching the wiki.
- Worked example — a wiki contributor joins via SSO, gets scoped write access to the curation API, and is deprovisioned in the same pass when they leave — enforced by the provisioning automation.

Worked example — a wiki contributor joins via SSO, gets scoped write access to the curation API, and is deprovisioned in the same pass when they leave — enforced by the provisioning automation.

## Related
- [[wiki/compositions/authentication-patterns|Authentication Patterns]]
- [[wiki/compositions/authorization-models|Authorization Models]]
- [[wiki/compositions/zero-trust-architecture|Zero-Trust Architecture]]
- [[wiki/identity/identity-providers|Identity Providers]]
- [[wiki/security/oauth2|OAuth 2.0]]
- [[wiki/compositions/security-engineering|Security Engineering]]
- [[wiki/compositions/fencing-tokens|Fencing Tokens]]
- [[wiki/tooling/leader-election|Leader Election]]
- [[wiki/security/sso|Single Sign-On]]
