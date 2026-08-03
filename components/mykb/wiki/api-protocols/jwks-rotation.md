---
type: "concept"
title: "JWKS Rotation"
description: "Rolling signing keys published via JWK Sets without breaking verification"
tags: ["jwt", "security", "keys", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# JWKS Rotation

## Summary
JWKS rotation is the practice of replacing an authorization server's signing keys on a schedule and publishing the current set at a well-known URL. Done right, old tokens keep validating until expiry while new tokens use fresh keys; done wrong, every client breaks at once.

## Details
A JWK Set (JSON Web Key Set) is a JSON document listing the public keys an issuer currently uses to sign tokens, each with a kid (key id). Verifiers fetch the set (usually from /.well-known/jwks.json), select the key by kid, and validate signatures. Rotation means adding a new key to the set and, after a grace period, removing the old one.

The mechanism: the authorization server generates a new signing key pair, adds the public half to the JWKS with a fresh kid, and starts signing new tokens with it. Old tokens still carry signatures by the previous key, so the old key must remain in the set until every in-flight token has expired. Verifiers must handle multiple keys: pick by kid, and refresh their cached JWKS when the kid is unknown (or on a timer). Cache TTL is the load-bearing setting: too long, and clients validate against stale keys during rotation; too short, and the JWKS endpoint becomes hot.

Concrete example: an IdP rotates keys every 90 days with a 14-day overlap. On rotation day, the new key appears in the JWKS and new tokens use it; the old key stays for 14 days so tokens minted before rotation still verify. A verifier that caches the JWKS for 24 hours picks up the change within a day; one that caches for 30 days rejects new tokens as "unknown kid" until it refreshes — a classic rotation-induced outage.

Failure modes: removing the old key before token expiry invalidates every outstanding token; verifiers that treat an unknown kid as fatal instead of refetching fail hard during rotation; and rotation without a documented schedule leaves keys static until compromise, at which point the emergency rotation breaks everyone because the overlap period was never practiced. Kid collisions between the old and new sets cause wrong-key verification failures.

Operational tradeoffs: rotation schedules trade key hygiene against operational risk — frequent rotation reduces the value of a stolen signing key but demands disciplined overlap and monitoring. The baseline: automated rotation with a documented overlap longer than the max token lifetime, verifier-side kid-aware selection with JWKS refresh on unknown kid, and alerting on signature failures correlated with rotation events.

RSIS3/mykb relevance: the wiki's token validation should handle multi-key JWKS gracefully; documenting the rotation cadence and overlap rule keeps RSIS3's loops from caching keys past rotation.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/jti-claims|JWT ID Claims]] — related coverage in the same cluster
- [[wiki/api-protocols/scope-validation|Scope Validation]] — related coverage in the same cluster
- [[wiki/api-protocols/audience-claims|Audience Claims]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]] — related coverage in the same cluster
- [[wiki/identity/jwks|JWKS]] — related coverage in the same cluster
