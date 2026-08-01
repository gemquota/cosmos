---
type: "concept"
title: "Microsoft Entra ID"
description: "Microsoft's cloud identity and access management service (formerly Azure AD)"
tags: ["azure", "entra", "iam", "identity"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://learn.microsoft.com/en-us/entra/identity/"]
---

# Microsoft Entra ID

- Microsoft Entra ID (formerly Azure Active Directory) is Microsoft's multi-tenant identity service: users, groups, app registrations, and conditional access.
- It is the IdP behind Microsoft 365 and Azure, speaking OIDC, SAML, and WS-Fed.
- Conditional access policies combine identity, device, and location signals for risk-based access decisions.
- For mykb: Entra ID is the obvious enterprise IdP to federate with via OIDC.

## Related

- [[wiki/identity/identity-providers|Identity Providers]] — Entra ID is an enterprise IdP
- [[wiki/identity/openid-connect|OpenID Connect]] — the protocol Entra speaks
- [[wiki/identity/single-sign-on|Single Sign-On]] — SSO across Microsoft services
- [[wiki/api-services/cloud-security-posture|Cloud Security Posture]] — Azure tenant posture
