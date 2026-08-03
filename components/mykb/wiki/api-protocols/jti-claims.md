---
type: "concept"
title: "JWT ID Claims"
description: "The jti claim that gives a token a unique identifier for replay and audit"
tags: ["jwt", "security", "claims", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# JWT ID Claims

## Summary
The jti (JWT ID) claim is a unique identifier for a token. It enables replay detection, revocation by id, and correlation of a token with audit logs — capabilities that signature and expiry checks alone cannot provide.

## Details
jti is an optional registered claim (RFC 7519) holding a unique string per token. Its purpose is to identify the token itself, not the subject: the same user can hold many tokens, each with its own jti. Verifiers and authorization servers use it to implement single-use tokens, detect replay, maintain a denylist ("revoke jti X"), and match a presented token to issuance records.

The mechanism: the authorization server mints jti as a random UUID or an incrementing server-side identifier and stores it with issuance metadata (subject, client, scopes, issued-at, expiry). For replay-sensitive grants — authorization codes, refresh tokens, one-time tokens — the server records used jtis and rejects repeats. For access tokens, a revocation list keyed by jti gives immediate invalidation without waiting for expiry, complementing short lifetimes.

Concrete example: a payments API uses short-lived access tokens plus refresh tokens. Each refresh token has a jti; on refresh, the server marks the old jti as used. If an attacker replays a stolen refresh token, the server sees a used jti and rejects it — and can flag the event as a likely theft, triggering rotation of the whole token family. The same jti appears in audit logs, so a support ticket citing the jti finds every use of that token.

Failure modes: jti values that are predictable (sequential integers) allow forgery of the identifier space and weaken denylist semantics; jti reused across tokens defeats replay detection entirely; and a denylist that never expires grows without bound — entries must be pruned after token expiry. Verifiers that ignore jti cannot participate in revocation or replay detection, so the claim only helps when the server stores and checks it.

Operational tradeoffs: storing jtis adds a small write per token and a lookup per verification (or a cache), the standard cost of revocation capability. Pairing jti with refresh-token rotation and reuse detection is the strongest practical anti-theft posture. The baseline: random jti, recorded at issuance, denylist with TTL tied to token expiry, and jti in every audit log line.

RSIS3/mykb relevance: RSIS3 loops that issue or validate tokens should include jti in their audit trail; documenting the claim contract lets the loop correlate a token's use across services.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]]
- [[wiki/api-protocols/scope-validation|Scope Validation]]
- [[wiki/api-protocols/audience-claims|Audience Claims]]
- [[wiki/api-protocols/issuer-validation|Issuer Validation]]
- [[wiki/api-protocols/json-web-tokens|JWT]]
- [[wiki/api-protocols/oauth2-scopes|OAuth Scopes]]
- [[wiki/identity/jwks|JWKS]]
