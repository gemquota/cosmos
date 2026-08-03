---
type: "concept"
title: "JWKS"
description: "JSON Web Key Sets publishing the public keys used to verify signed JWTs"
tags: ["jwks", "jwt", "keys", "oidc"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc7517"]
---

# JWKS

## Summary
A JSON Web Key Set (JWKS, RFC 7517) is a JSON document of public keys that verifiers use to check JWT signatures. It is how identity providers publish their signing keys without out-of-band configuration: a client fetches the JWKS from a well-known URI, selects the key by its `kid` (key ID), and verifies the token's signature.

## Details
- A JSON Web Key Set (JWKS, RFC 7517) is a JSON document of public keys that verifiers use to check JWT signatures. Each key in the set carries its type, algorithm, use, key ID, and the key material itself (for RSA, the modulus and exponent; for EC, the curve and coordinates).
- OIDC providers publish JWKS at a well-known URI so clients can fetch signing keys without out-of-band configuration. The OpenID Connect discovery document points at `jwks_uri`, and clients fetch the set on demand or on a cache schedule — no manual key exchange is needed when a provider rotates keys.
- Best practice: cache keys briefly, rotate keys on a schedule, and honor the kid (key ID) claim to pick the right key. Caching avoids a fetch per token while keeping the window short enough that a rotation is picked up promptly; rotation keeps each key's exposure bounded; and `kid` selection means a token signed with the previous key still verifies during the rotation overlap.
- Concrete example: a provider rotates its signing key weekly. On rotation, the JWKS contains both the old and new keys; tokens issued before rotation carry the old `kid` and verify with the old key; tokens issued after carry the new `kid`. Clients that hardcode the key instead of fetching the JWKS break every rotation — a classic integration failure.
- Key confusion attacks occur when verifiers accept attacker-chosen keys or ignore the alg — validation must pin allowed algorithms. The `alg:none` and algorithm-confusion (RS256 vs HS256) attacks succeed when the verifier trusts header claims instead of a configured allowlist; the fix is to pin the algorithm set and validate that the key used matches the key source.
- Failure modes: fetching JWKS from an unauthenticated or attacker-influenced URI; caching the set forever so rotation never takes effect; and libraries that verify signatures but not issuer, audience, or expiry, which leaves the door open for tokens from the wrong tenant.
- For mykb: JWKS fetching and caching should live in one shared library used by every token-validating service, with pinned algorithms and a short cache TTL — the same configuration everywhere, so rotation cannot break one consumer.

## Related
- [[wiki/identity/openid-connect|OpenID Connect]] — OIDC providers publish JWKS
- [[wiki/security-auth/token-authentication|Token Authentication]] — signature verification uses JWKS
- [[wiki/security/jwt|JWT]] — the tokens the keys verify
- [[wiki/identity/key-rotation|Key Rotation]] — rotating the keys in the set
