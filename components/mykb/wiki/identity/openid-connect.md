---
type: "concept"
title: "OpenID Connect"
description: "Identity layer on OAuth 2.0 that issues signed ID tokens describing the authenticated user"
tags: ["oidc", "openid-connect", "identity", "oauth2", "sso"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://openid.net/specs/openid-connect-core-1_0.html"]
---

# OpenID Connect

## Summary

OpenID Connect (OIDC) is a simple identity layer on top of OAuth 2.0. The authorization server (here called an OpenID Provider, OP) issues an ID token — a signed JWT carrying claims such as issuer, subject, audience, and expiry — that tells the client (RP) who the user is, while OAuth scopes tell it what the user allowed. It matters because it turned fragmented proprietary login into one interoperable protocol: 'Sign in with Google/GitHub/Microsoft' and most enterprise SSO now speak OIDC. For mykb, OIDC is the natural way to let RSIS3 authenticate to external services and to let humans authenticate to RSIS3 through a managed identity provider.

## Details

- ID token: a JWS-signed JWT with mandatory claims iss, sub, aud, exp, iat; the RP validates signature via JWKS and checks audience and expiry.
- Scopes: the openid scope is required; profile, email, and address scopes request additional claims, retrievable also from the UserInfo endpoint.
- Flows: authorization code flow with PKCE is the recommended interactive flow; client credentials for machine-to-machine; the implicit flow is deprecated in favour of code flow.
- Discovery: OPs publish an OpenID Provider Metadata document (/.well-known/openid-configuration) listing endpoints, supported scopes, and JWKS URI, enabling zero-config clients.
- OIDC vs OAuth: OAuth is authorization (what can the app do), OIDC adds authentication (who is the user) — a distinction RSIS3 must preserve when granting agents delegated access.
- Security considerations: ID tokens must be validated cryptographically, nonces prevent replay, and RPs should not use id_token for API authorization decisions.

## Related

- [[wiki/identity/oidc-clients|OIDC Clients]] — client configuration and registration on the OP
- [[wiki/identity/jwks|JWKS]] — the key set used to verify ID token signatures
- [[wiki/identity/single-sign-on|Single Sign-On]] — OIDC is the modern SSO protocol
- [[wiki/security/oauth2|OAuth 2.0]] — the authorization framework OIDC builds on
- [[wiki/security/jwt|JWT]] — the ID token format
- [[wiki/identity/refresh-tokens|Refresh Tokens]] — longer-lived credentials paired with ID tokens
- [[wiki/concepts/triad-architecture|Triad Architecture]] — OIDC fits the engine-to-service authn boundary
