---
type: "concept"
title: "Single Sign-On"
description: "One authentication event grants access across multiple applications via a shared identity provider"
tags: ["sso", "authentication", "oauth2", "oidc", "saml"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Single Sign-On

## Summary
Single Sign-On (SSO) lets users authenticate once with an identity provider (IdP) and access many applications. It centralizes credentials, MFA, and lifecycle management.

## Details
- Protocols: OIDC/OAuth 2.0 for modern web, SAML for enterprise federation.
- The IdP owns authentication; apps consume tokens or assertions (JWT, SAML).
- Benefits: fewer passwords, consistent MFA, centralized revocation — one security perimeter.

## How It Works

- The IdP owns the authentication ceremony and issues a signed token or assertion to the requesting application.
- OIDC uses a discovery document to advertise endpoints; the app validates the ID token's signature, issuer, audience, and expiry, often with JWKS-fetched keys.
- SAML follows a similar trust model for enterprise federation, with XML assertions exchanged between IdP and service provider.
- Session state lives at the IdP, so logout and revocation take effect centrally rather than per application.

## Implementation Notes

- Validate tokens on every request, not just at login, and tolerate clock skew with explicit leeway.
- Handle key rotation by caching JWKS with a short TTL and re-fetching on unknown `kid`.
- Use refresh tokens with rotation and reuse detection to limit the blast radius of a leaked token.
- Design single logout carefully: RP-initiated logout varies by protocol and not every app supports it.

## Operational Considerations

- The IdP is a single point of failure for every connected app; monitor its availability and cache what you safely can.
- Plan for incidents: rate-limited login, fail-open vs fail-closed decisions, and a communication channel for users.
- Favor phishing-resistant methods such as WebAuthn/passkeys for high-value accounts.


## Related
- [[wiki/security/oauth2|OAuth 2.0]] — protocol backbone
- [[wiki/security/saml|SAML]] — enterprise federation
- [[wiki/security/mfa|Multi-Factor Authentication]] — enforced centrally
- [[wiki/security/jwt|JWT]] — ID token format
- [[wiki/security/ldap|LDAP]] — legacy directory integration

## Related Concepts

- [[wiki/api-protocols/oauth2-authorization-code|OAuth2 Authorization Code]] — the flow that issues ID and access tokens
- [[wiki/api-protocols/openid-connect|OpenID Connect]] — the identity layer over OAuth 2.0
- [[wiki/api-protocols/oauth2-refresh-tokens|OAuth2 Refresh Tokens]] — long-lived session maintenance
- [[wiki/security/webauthn|WebAuthn]] — phishing-resistant authentication
- [[wiki/security/passkeys|Passkeys]] — the modern credential replacement

