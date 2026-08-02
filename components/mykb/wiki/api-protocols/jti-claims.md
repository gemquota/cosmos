---
type: "concept"
title: "JWT ID Claims"
description: "Unique token identifiers enabling replay detection and revocation"
tags: ["jwt", "security", "tokens", "claims"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# JWT ID Claims

## Summary
Unique token identifiers enabling replay detection and revocation. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- A unique jti per token enables replay detection and revocation lists
- Without storage, jti offers nothing beyond observability
- Open question — how do stateless verifiers check jti denylists?

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/scope-validation|Scope Validation]] — related coverage in the same cluster
- [[wiki/api-protocols/audience-claims|Audience Claims]] — related coverage in the same cluster
- [[wiki/api-protocols/issuer-validation|Issuer Validation]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — related coverage in the same cluster
- [[wiki/identity/jwks|JWKS]] — related coverage in the same cluster
