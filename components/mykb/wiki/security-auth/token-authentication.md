---
type: "concept"
title: "Token Authentication"
description: "Using bearer tokens issued by an authorization server to authenticate API and web requests"
tags: ["tokens", "bearer", "authentication", "oauth2", "apis"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6750"]
---

# Token Authentication

## Summary

Token authentication presents a token — an opaque or structured credential — to a resource server, which validates it before granting access. RFC 6750 defines the bearer token: a string that whoever holds it may use, presented in the Authorization header as Bearer <token>. Tokens matter because they let authentication and authorization be delegated to an authorization server and carried across stateless APIs without re-sending credentials. RSIS3's service-to-service calls and user-facing API boundaries both run on token authentication, so its lifecycle rules are security-critical.

## Details

- Bearer token rules: the token must be transmitted only over TLS, and possession alone grants access — hence short lifetimes and tight scoping.
- Token forms: opaque tokens require server-side lookup or introspection; JWT tokens are self-contained and verified via signature (JWKS).
- Validation pipeline: check signature, issuer, audience, expiry, and scope claims; treat any validation failure as an authentication failure.
- Lifecycle: tokens are issued by an authorization server after an OAuth grant, refreshed via refresh tokens, and revoked through RFC 7009 revocation endpoints.
- Threats: token theft from logs or referrers, replay across services, and over-broad scopes; mitigations are TLS, scopes, expiry, and binding to client context.
- For mykb, a validation policy shared by all resource servers prevents drift: same checks, same clocks, same revocation feed.

## Related

- [[wiki/identity/refresh-tokens|Refresh Tokens]] — renewing access without re-authentication
- [[wiki/identity/jwks|JWKS]] — keys that verify signed tokens
- [[wiki/identity/token-revocation|Token Revocation]] — invalidating tokens before expiry
- [[wiki/security/oauth2|OAuth 2.0]] — the framework that issues access tokens
- [[wiki/security/jwt|JWT]] — self-contained token format
- [[wiki/security/secrets-management|Secrets Management]] — protecting token signing keys
- [[wiki/concepts/triad-architecture|Triad Architecture]] — token-protected boundaries between engine and memory
