---
type: "concept"
title: "API Authentication Methods"
description: "Taxonomy of API authentication schemes"
tags: ["authentication", "api-security", "tokens", "taxonomy", "http"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://oauth.net/2/", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication"]
---

# API Authentication Methods

## Summary
API authentication proves who is calling; authorization decides what they may do. The common schemes — API keys, HTTP Basic, bearer tokens, OAuth 2.0 grants, JWT, mTLS, and signed requests — differ in where the credential lives, how it is issued, and what it can express. Most APIs use one primary scheme plus OAuth for delegated access.

## Details
- API keys: opaque shared secrets for simple client identification; easy but weak for security (no scopes by default, easy to leak).
- HTTP Basic: username:password base64-encoded; only acceptable over TLS, typically for legacy or machine bootstrap flows.
- Bearer tokens: Authorization: Bearer <token>; tokens are opaque to clients, carry scopes server-side, and are validated without user interaction.
- JWT: self-contained tokens with claims — handy across services but un-revocable until expiry, so keep them short-lived.
- OAuth 2.0: delegated authorization with grants (authorization code + PKCE for users, client credentials for machines); the modern default for third-party access.
- mTLS: certificate-based service identity; strong but operationally heavy, best for east-west traffic.
- Signed requests (HMAC, AWS SigV4): request signing proves possession of a secret and integrity of the request; used by cloud APIs.
- Choose by threat model: public web apps need OAuth + PKCE, internal services need tokens or mTLS, and partner integrations need API keys or OAuth.

## Related
- [[wiki/api-protocols/api-keys|API Keys]] — the simple shared-secret scheme
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — the delegated authorization framework
- [[wiki/api-protocols/json-web-tokens|JWT]] — self-contained bearer tokens
- [[wiki/api-protocols/mtls|mTLS]] — certificate-based machine identity
- [[wiki/security-auth/role-based-access-control|Role-Based Access Control]] — authentication feeds authorization
