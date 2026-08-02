---
type: "concept"
title: "JWT in Practice"
description: "JSON Web Tokens: structure, signing, validation, and the attacks that follow misuse"
tags: ["jwt", "tokens", "security", "auth", "claims"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7519", "https://jwt.io/introduction"]
---
# JWT in Practice

## Summary
A JWT is a compact, URL-safe token with a header, claims, and a signature. Signatures prove issuer authenticity; claims carry identity, expiry, audience, and scopes. Stateless verification is convenient, but revocation is hard and algorithm confusion is a classic forgery path.

## Details
- **Structure** — base64url header (`alg`, `typ`), payload claims (`iss`, `sub`, `aud`, `exp`, `iat`, `jti`), and signature (HMAC or asymmetric).
- **Verification checklist** — pin algorithms, validate signature against JWKS, check issuer and audience exactly, enforce expiry, and require unique jti where replay matters.
- **Stateless trade-off** — no server lookup per request, but tokens survive until expiry unless denylists or introspection are added.
- **Common attacks** — alg none, RS256-to-HS256 confusion, JKU pointing at attacker keys, and weak HMAC secrets.
- **Worked example** — mykb's service issues short-lived JWTs with aud scoped per service and rotates signing keys via JWKS.
- **Relevance** — RSIS3's tool sessions mint scoped JWTs; the wiki's token cluster records validation rules and attack notes.

## Related
- [[wiki/api-protocols/introspection-endpoint|Token Introspection]] — adjacent concept in this wiki
- [[wiki/api-protocols/jwks-rotation|JWKS Rotation]] — adjacent concept in this wiki
- [[wiki/api-protocols/jti-claims|JWT ID Claims]] — adjacent concept in this wiki
- [[wiki/api-protocols/scope-validation|Scope Validation]] — adjacent concept in this wiki
- [[wiki/api-protocols/json-web-tokens|JWT]] — existing coverage
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — existing coverage
- [[wiki/identity/jwks|JWKS]] — existing coverage
