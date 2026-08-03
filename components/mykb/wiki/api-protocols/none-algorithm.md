---
type: "concept"
title: "JWT none Algorithm"
description: "The alg=none header that makes a JWT require no signature at all"
tags: ["jwt", "security", "attacks", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# JWT none Algorithm

## Summary
alg=none is the JWT signing algorithm that means "no signature." It exists for debugging and integrity-free contexts, and it is one of the first things attackers try: a verifier that accepts alg=none will trust a token with arbitrary claims and an empty signature.

## Details
JWT's algorithm header selects how the signature is computed. The none value (RFC 7519 and the JWA spec) indicates no signature: the token is header.payload. with an empty signature segment. It is meant for integrity-free or experimental use. The attack is trivial: send {"alg": "none", "typ": "JWT"} with claims like role=admin and an empty signature; a verifier that honors the header without checking an allowlist accepts it as valid.

The mechanism: verification must be configured with an explicit algorithm allowlist (for example HS256/RS256 only) and must reject none. Vulnerable libraries and misconfigured verifiers that accept any algorithm, including none, fail open. Variants include changing the case (None, NONE), which some parsers normalize and others don't, and setting alg=none with a valid-looking signature that the library skips verifying.

Concrete example: a test suite issues tokens with alg=none to speed up local development, and the same signing code path is used in production. An attacker registers, decodes a token's structure, and re-sends {"alg":"none"} with elevated claims. If production verification doesn't pin allowed algorithms, the forged token is accepted — full privilege escalation with a few bytes. The fix: a hard allowlist that excludes none at the verification layer, independent of the library's defaults.

Failure modes: libraries with lenient defaults that accept none unless explicitly disabled; verifiers that check the signature only when the header says an algorithm other than none; and copy-pasted validation code that omits the algorithm allowlist. Also, none is not the only unsigned path — some stacks accept missing signature segments or malformed base64 as "empty."

Operational tradeoffs: alg=none should never be enabled in production verification; where development convenience needs unsigned tokens, use a separate issuer and key space so the production verifier can't be reached. The verification checklist: pin allowed algorithms, reject none, reject missing signatures, and treat the header as untrusted data.

RSIS3/mykb relevance: JWT verification code in the wiki stack must reject none by construction; documenting the allowlist rule gives RSIS3's security reviews a first-line assertion.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]]
- [[wiki/api-protocols/weak-hash-jwt|Weak Hashes in JWT]]
- [[wiki/api-protocols/algorithm-confusion|JWT Algorithm Confusion]]
- [[wiki/api-protocols/jku-attacks|JKU Attacks]]
- [[wiki/api-protocols/json-web-tokens|JWT]]
- [[wiki/identity/key-rotation|Key Rotation]]
- [[wiki/api-protocols/mtls|mTLS]]
