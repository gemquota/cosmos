---
type: "concept"
title: "JWT Algorithm Confusion"
description: "Switching signing algorithms to forge tokens when the verifier is lax"
tags: ["jwt", "security", "attacks", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# JWT Algorithm Confusion

## Summary
Algorithm confusion attacks trick a verifier into using an attacker-chosen algorithm or key type when validating a token or signature, most famously turning RS256 JWTs into HS256 forgeries.

## Details
Algorithm confusion (or key confusion) exploits verifiers that trust the algorithm declared inside a signed artifact instead of pinning it. In JWT land, the classic attack switches the alg header from RS256 (RSA, asymmetric) to HS256 (HMAC, symmetric). Libraries that look up the verification key by the header's alg or kid then treat the RSA public key as the HMAC shared secret — and since public keys are public, the attacker can compute a valid HMAC signature themselves.

The mechanism: verification should be a single, configured operation — verify with the key registered for this issuer and algorithm. Confused verifiers instead read alg from the token, select a key type, and coerce the key material. RSA public keys are just bytes (Modulus/Exponent), and HS256 accepts arbitrary bytes as a secret, so the same PEM parses as both. The 2015-2016 JWT confusion wave (CVE-2015-9235 and library variants) was exactly this.

Concrete example: an attacker obtains a service's RSA public key (it is public). They craft a token with alg=HS256, sign it with the public key bytes as the HMAC secret, and set claims like role=admin. A server that does not pin alg accepts it because the library loads the same JWK and happily interprets it as an HMAC secret. The fix: explicitly whitelist allowed algorithms at verification time and reject anything else, and never accept an embedded key (jku, x5c) without allow-listing the URL and validating trust.

Failure modes beyond JWT: similar confusion exists in CMS/PKCS#7 (choosing a weaker hash), SSH (algorithm downgrade), and TLS (export cipher downgrades). The common thread is allowing the artifact to select the security parameters. Failure also occurs at the library level: some frameworks have separate verify paths where forgetting to pass an algorithm parameter defaults to accepting any algorithm.

Operational tradeoffs: strict algorithm pinning breaks clients that rotate signing algorithms (for example migrating RS256 to PS256), so rollouts must overlap supported algorithms and pin per issuer via JWK kid metadata. Rotating keys and auditing logs for unexpected alg values are the monitoring half of the fix. Libraries that reject embedded keys outright remove jku/x5c flexibility, which some enterprise deployments need for key federation.

RSIS3/mykb relevance: algorithm confusion is a canonical "verify the verifier" failure; documenting the pinned-alg rule in mykb lets RSIS3-generated security reviews check token validation code mechanically.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]]
- [[wiki/api-protocols/jku-attacks|JKU Attacks]]
- [[wiki/api-protocols/none-algorithm|JWT none Algorithm]]
- [[wiki/api-protocols/weak-hash-jwt|Weak Hashes in JWT]]
- [[wiki/api-protocols/json-web-tokens|JWT]]
- [[wiki/identity/key-rotation|Key Rotation]]
- [[wiki/api-protocols/mtls|mTLS]]
