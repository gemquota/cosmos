---
type: "concept"
title: "JWT"
description: "Compact, signed JSON tokens for transmitting verified claims between parties (RFC 7519)"
tags: ["jwt", "tokens", "authn", "security", "json"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7519"]
---

# JWT

## Summary
JSON Web Tokens (RFC 7519) are compact, URL-safe tokens carrying signed claims: header, payload, and signature. The signature (HS256, RS256, or EdDSA) proves the token was issued by a trusted party and has not been altered. JWTs are widely used for access tokens, ID tokens, and stateless session data.

## Details
- Structure: `header.payload.signature`, each part base64url-encoded; payload claims include `iss`, `sub`, `aud`, `exp`, `iat`, and `jti`.
- Signing: HMAC (HS256, shared secret) vs asymmetric (RS256/ES256/EdDSA, private key signs, public key verifies) — asymmetric suits multi-party verification.
- Stateless verification: a resource server validates signature, `exp`, and `aud` without a session store — but revocation requires a blocklist or short expiry.
- Pitfalls: storing secrets in payloads (JWTs are signed, not encrypted — use JWE if confidential), `alg=none` downgrades, and long `exp` windows.
- Comparison: opaque tokens are revocable server-side; JWTs are introspectable offline. Hybrids (short JWT + refresh token) get the best of both.
- Worked example: the mykb daemon issues an RS256 JWT to the dashboard with `scope: read` and 15-minute expiry; the hub validates with the published public key.
- Relationship: OAuth 2.0 access tokens are often JWTs; WebAuthn assertions are separate signed structures.

## Related
- [[wiki/security/oauth2|OAuth 2.0]] — JWT as access/ID token format
- [[wiki/security/secrets-management|Secrets Management]] — where signing keys must live
- [[wiki/security/sso|Single Sign-On]] — ID tokens carry identity claims
- [[wiki/api-protocols/rest-apis|REST APIs]] — bearer-token authorization header
- [[wiki/security/zero-trust|Zero Trust Architecture]] — short-lived credentials fit continuous verification
- [[wiki/concepts/mykb-analysis|Mykb Analysis]] — session capture includes token flows
- [[wiki/security/passkeys|Passkeys]] — passwordless alternative to token sessions
- [[wiki/concepts/triad-architecture|Triad Architecture]] — token issuance for bridge calls
