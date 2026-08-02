---
type: "concept"
title: "JWT"
description: "Token structure, claims, and verification"
tags: ["jwt", "tokens", "authentication", "security", "json"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7519", "https://jwt.io/introduction"]
---

# JWT

## Summary
JSON Web Tokens (RFC 7519) are compact, URL-safe tokens encoding claims in a base64url header.payload.signature structure. Signed with JWS (HMAC or asymmetric algorithms), a JWT lets any service verify its issuer and integrity offline — which makes it the default format for access tokens and ID tokens, and a common source of auth bugs.

## Details
- Structure: header (alg, typ), payload (claims), signature; three base64url segments separated by dots.
- Claims: iss (issuer), sub (subject), aud (audience), exp (expiry), nbf, iat, and custom claims; exp is mandatory in practice.
- Signature: HMAC (HS256, shared secret) or asymmetric (RS256/ES256/EdDSA, public key verification) — asymmetric lets any resource server verify without the secret.
- Verification: decode, check alg is expected (never 'none'), verify signature with the right key, then validate iss/aud/exp/nbf.
- Common vulnerabilities: alg confusion (accepting HS256 with an RSA public key), missing exp checks, and accepting unsigned 'none' tokens.
- Revocation problem: a valid JWT cannot be revoked before exp — mitigate with short lifetimes, refresh tokens, or an allow/denylist.
- Storage: keep JWTs out of localStorage in browsers (XSS risk); use httpOnly cookies or in-memory storage with a BFF.

## Related
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — access tokens are often JWTs
- [[wiki/api-protocols/openid-connect|OpenID Connect]] — ID tokens are JWTs with identity claims
- [[wiki/api-protocols/oauth2-refresh-tokens|Refresh Tokens]] — revocable companions to JWTs
- [[wiki/api-protocols/api-authentication-methods|API Authentication Methods]] — JWT in the auth taxonomy
- [[wiki/security-auth/token-authentication|Token Authentication]] — server-side token validation
