---
type: "concept"
title: "JWKS"
description: "JSON Web Key Sets publishing the public keys used to verify signed JWTs"
tags: ["jwks", "jwt", "keys", "oidc"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.rfc-editor.org/rfc/rfc7517"]
---

# JWKS

- A JSON Web Key Set (JWKS, RFC 7517) is a JSON document of public keys that verifiers use to check JWT signatures.
- OIDC providers publish JWKS at a well-known URI so clients can fetch signing keys without out-of-band configuration.
- Best practice: cache keys briefly, rotate keys on a schedule, and honor the kid (key ID) claim to pick the right key.
- Key confusion attacks occur when verifiers accept attacker-chosen keys or ignore the alg — validation must pin allowed algorithms.
- For mykb: JWKS fetching and caching should live in one shared library used by every token-validating service.

## Related

- [[wiki/identity/openid-connect|OpenID Connect]] — OIDC providers publish JWKS
- [[wiki/security-auth/token-authentication|Token Authentication]] — signature verification uses JWKS
- [[wiki/security/jwt|JWT]] — the tokens the keys verify
- [[wiki/identity/key-rotation|Key Rotation]] — rotating the keys in the set
