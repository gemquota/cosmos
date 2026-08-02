---
type: "concept"
title: "Auth Flows on the Web"
description: "OAuth 2.0 and OpenID Connect grant flows for browser, native, and machine clients"
tags: ["oauth2", "oidc", "auth", "security", "tokens"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6749", "https://openid.net/connect/"]
---
# Auth Flows on the Web

## Summary
Web authentication follows OAuth 2.0 grants and OpenID Connect for identity. The authorization code flow with PKCE is the recommended browser and mobile path; client credentials serve machine-to-machine calls; device flow covers constrained devices. Tokens carry scopes, audiences, and expiry that every service must validate.

## Details
- **Authorization code + PKCE** — the app redirects to the provider, receives a code, and exchanges it with a verifier proof; PKCE protects public clients from code interception.
- **Client credentials** — confidential clients authenticate directly and get tokens for their own identity, not a user's.
- **Device flow** — the client polls while the user approves on another device; suited to TVs and CLI tools.
- **OpenID Connect** — OIDC layers an ID token and userinfo endpoint on OAuth for sign-in.
- **Validation checklist** — verify issuer, audience, expiry, signature via JWKS, and scopes on every request.
- **Worked example** — the mykb dashboard uses OIDC with PKCE; the wiki records each flow and validation rule for the auth layer.
- **Relevance** — RSIS3's tool grants are OAuth flows too; agents must refresh and validate without exposing secrets.

## Related
- [[wiki/api-protocols/api-keys-vs-tokens|API Keys vs Tokens]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-basic-auth|API Basic Auth]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-digest-auth|API Digest Auth]] — adjacent concept in this wiki
- [[wiki/api-protocols/bearer-tokens|Bearer Tokens]] — adjacent concept in this wiki
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — existing coverage
- [[wiki/api-protocols/api-keys|API Keys]] — existing coverage
- [[wiki/api-protocols/basic-authentication|Basic Authentication]] — existing coverage
