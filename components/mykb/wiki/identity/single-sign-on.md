---
type: "concept"
title: "Single Sign-On"
description: "One primary authentication event grants access to many applications without repeated credential prompts"
tags: ["sso", "authentication", "saml", "oidc", "enterprise"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/what-is-single-sign-on"]
---

# Single Sign-On

## Summary

Single sign-on (SSO) lets a user authenticate once to a central identity provider and then access many applications without re-entering credentials. The IdP issues an assertion or token (SAML assertion, OIDC ID token, Kerberos ticket) that each service provider accepts via a trust relationship. It matters because it collapses hundreds of passwords into one managed identity, centralizes policy and audit, and improves the security posture: fewer stored credentials, faster revocation, and consistent MFA enforcement. For RSIS3, SSO is the pattern for giving agents and humans one identity that spans mykb services, external APIs, and the development environment.

## Details

- Protocols: SAML 2.0 for enterprise web apps, OIDC for modern apps and SPAs, Kerberos for on-premises networks; WS-Fed remains in legacy stacks.
- Session topology: the IdP session is the root; SP sessions are derived via assertions, so logout must fan out (single logout) to be effective.
- Benefits: reduced password fatigue, centralized password policies and MFA, single audit trail, faster onboarding and offboarding.
- Risks: the IdP is a single point of failure and a prime attack target — if it is compromised, every connected app is exposed; session hygiene and key management at the IdP become critical.
- Deployment patterns: IdP-initiated vs SP-initiated SSO, federated trust via metadata exchange, and just-in-time user provisioning from assertions.
- In mykb terms, SSO keeps RSIS3's identity graph consistent: one subject record, many service-specific sessions.

## Related

- [[wiki/identity/identity-providers|Identity Providers]] — the central component SSO depends on
- [[wiki/identity/openid-connect|OpenID Connect]] — the modern SSO protocol
- [[wiki/identity/saml-assertions|SAML Assertions]] — the classic SSO assertion format
- [[wiki/identity/session-management|Session Management]] — managing the sessions SSO creates
- [[wiki/security/sso|Single Sign-On]] — existing article on SSO
- [[wiki/identity/session-hijacking|Session Hijacking]] — the attack SSO sessions must resist
- [[wiki/identity/session-fixation|Session Fixation]] — fixation attacks target SSO session IDs
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — SSO feeds the central identity system
