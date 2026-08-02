---
type: "concept"
title: "OpenID Connect"
description: "ID tokens, discovery, and userinfo endpoint"
tags: ["oidc", "openid-connect", "identity", "authentication", "oauth2"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://openid.net/connect/", "https://openid.net/specs/openid-connect-core-1_0.html"]
---

# OpenID Connect

## Summary
OpenID Connect (OIDC) is an identity layer on top of OAuth 2.0: the /token endpoint returns an ID token (a signed JWT with user claims) alongside access tokens, so clients learn who the user is, not just what they can access. Discovery and JWKS endpoints make verification automatic.

## Details
- ID token: a JWT with iss, aud, sub (user id), exp, and claims like name and email; signed by the IdP (JWS) and optionally encrypted.
- Discovery (RFC 8414/OIDC): /.well-known/openid-configuration publishes issuer, endpoints, and supported algorithms so clients configure themselves.
- JWKS: /.well-known/jwks.json serves the IdP's public keys; clients fetch keys and verify the ID token signature and audience.
- userinfo endpoint: returns identity claims on demand with the access token; complements claims embedded in the ID token.
- Flows: authorization code + PKCE is the recommended interactive flow; hybrid and implicit flows exist but are legacy.
- Logout: OIDC defines RP-initiated logout and front-channel/back-channel logout so sessions end everywhere.
- Verification checklist: validate signature, iss, aud, exp, nonce (replay protection), and use the nonce to bind the token to the original login.

## Related
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — OIDC builds on the OAuth framework
- [[wiki/api-protocols/json-web-tokens|JWT]] — ID tokens are signed JWTs
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — openid, profile, email scopes
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — the flow OIDC recommends
- [[wiki/security-auth/token-authentication|Token Authentication]] — validating ID and access tokens
