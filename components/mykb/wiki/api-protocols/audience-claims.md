---
type: "concept"
title: "Audience Claims"
description: "Verifying the aud claim so tokens minted elsewhere are rejected"
tags: ["jwt", "security", "claims", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Audience Claims

## Summary
Verifying the aud claim so tokens minted elsewhere are rejected. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- aud declares which services the token targets
- Missing audience checks let tokens minted for A call B
- Open question — how do multi-service APIs share audience values?

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/issuer-validation|Issuer Validation]] — related coverage in the same cluster
- [[wiki/api-protocols/introspection-endpoint|Token Introspection]] — related coverage in the same cluster
- [[wiki/api-protocols/jwks-rotation|JWKS Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — related coverage in the same cluster
- [[wiki/identity/jwks|JWKS]] — related coverage in the same cluster
