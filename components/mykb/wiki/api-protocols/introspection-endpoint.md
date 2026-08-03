---
type: "concept"
title: "Token Introspection"
description: "OAuth endpoint that reports whether a token is active and its metadata"
tags: ["oauth2", "tokens", "security", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Token Introspection

## Summary
The introspection endpoint (RFC 7662) lets a resource server query the authorization server about a token it received: is it active, who owns it, what scopes does it have? It is the OAuth way to validate opaque tokens without sharing a signing key.

## Details
An opaque access token is a random string only the authorization server can interpret. A resource server that receives one calls POST /introspect with the token and its own client credentials, and the authorization server answers {"active": true, "scope": "read write", "client_id": "...", "username": "...", "exp": 1234567890, ...}. The active field is the verdict; the rest is metadata the resource server can use for authorization decisions.

The mechanism: introspection is a protected, authenticated endpoint — the resource server must present its own credentials so the authorization server knows who is asking and can enforce that the resource server is allowed to introspect. The response should never be cached for long (tokens can be revoked), and the resource server should treat active:false as reject. Introspection replaces shared-secret verification for opaque tokens and is the counterpart to local JWT verification for structured tokens: JWT validation is faster (no round trip) but cannot see revocation; introspection sees revocation but costs a network call.

Concrete example: a payments API issues opaque tokens; the analytics service (a different resource server) receives one in a header. It introspects at the authorization server, learns the token is active with scope=analytics:read and an expiry, checks its own policy, and serves the data. If the user revokes the token mid-session, the next introspection returns active:false and access stops immediately — something a stateless JWT could not do until expiry.

Failure modes: introspecting with the wrong endpoint or without authentication (some implementations accept unauthenticated calls, leaking token metadata); caching introspection responses too aggressively, which undoes revocation; treating a network error from the introspection endpoint as active:false (fail-open versus fail-closed decisions); and mixing opaque-token introspection with JWT local verification without a clear per-token strategy.

Operational tradeoffs: introspection adds latency per request and load on the authorization server, so resource servers typically cache results briefly (seconds) and only for high-frequency tokens. JWT local verification is cheaper and offline-friendly but requires trusting the signing key and accepting revocation lag. Many systems use JWTs for hot paths and introspection for revocation-sensitive ones. The failure mode must be fail-closed: when the introspection endpoint is unreachable, reject.

RSIS3/mykb relevance: RSIS3 service-to-service calls should verify tokens consistently — either local JWT checks or introspection; documenting which services introspect and their cache TTL keeps the authorization model auditable.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/jwks-rotation|JWKS Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/jti-claims|JWT ID Claims]] — related coverage in the same cluster
- [[wiki/api-protocols/scope-validation|Scope Validation]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — related coverage in the same cluster
- [[wiki/identity/jwks|JWKS]] — related coverage in the same cluster
