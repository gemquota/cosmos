---
type: "concept"
title: "Single Sign-On"
description: "One authentication event grants access across multiple applications via a shared identity provider"
tags: ["sso", "authentication", "oauth2", "oidc", "saml"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Single Sign-On

## Summary
Single Sign-On (SSO) lets users authenticate once with an identity provider (IdP) and access many applications. It centralizes credentials, MFA, and lifecycle management.

## Details
- Protocols: OIDC/OAuth 2.0 for modern web, SAML for enterprise federation.
- The IdP owns authentication; apps consume tokens or assertions (JWT, SAML).
- Benefits: fewer passwords, consistent MFA, centralized revocation — one security perimeter.

## Related
- [[wiki/security/oauth2|OAuth 2.0]] — protocol backbone
- [[wiki/security/saml|SAML]] — enterprise federation
- [[wiki/security/mfa|Multi-Factor Authentication]] — enforced centrally
- [[wiki/security/jwt|JWT]] — ID token format
- [[wiki/security/ldap|LDAP]] — legacy directory integration
