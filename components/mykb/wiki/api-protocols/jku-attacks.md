---
type: "concept"
title: "JKU Attacks"
description: "Abusing the jku header to make a verifier fetch an attacker's key set"
tags: ["jwt", "security", "attacks", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# JKU Attacks

## Summary
The jku (JWK Set URL) header in a JWT tells the verifier where to fetch the signing keys. If the verifier honors an attacker-controlled jku, the attacker can point it at their own JWKS and mint valid-looking tokens — the whole signature is attacker-signed and trusted.

## Details
JWTs can carry key-fetching hints in headers: jku (a URL to a JWKS), jwk (an embedded public key), x5u (a URL to an X.509 certificate chain), and kid (a key id into a known set). These exist for flexibility — decentralized issuers can advertise their keys. The attack: the attacker sets jku to https://evil.example.com/jwks.json, where their own key set lists a key they control, and sets kid to match. A verifier that fetches from the URL without an allowlist happily verifies the attacker's signature.

The mechanism: the verifier's trust model must be "keys are only fetched from configured, pinned locations." jku handling that dereferences any https URL converts the verifier into a tool for the attacker. The same problem applies to x5u and to OpenID discovery URLs, and to kid alone when the key set includes attacker-registered keys. The URL fetch is also an SSRF vector: a jku pointing at internal hosts (169.254.169.254 metadata, internal services) makes the verifier issue requests into its own network.

Concrete example: an API verifies JWTs and supports jku for a multi-tenant setup. An attacker sends a token with alg=RS256, jku=https://evil.example.com/keys.json, kid=attacker-key, and signs it with the matching private key. The verifier fetches the attacker's JWKS, finds the kid, verifies the signature against the attacker's public key — it all checks out, and the token's role=admin claim is accepted. The fix: an explicit allowlist of jku URLs per issuer, or rejecting jku/jwk/x5u entirely.

Failure modes: allowing jku with any https URL; fetching with redirects enabled (the allowlisted URL redirects to the attacker's host); caching attacker-supplied JWKS responses; and treating kid as sufficient trust when the key set is attacker-influenced. Also, jku fetches add a network dependency — if the attacker's server is slow, the verifier blocks, a minor DoS vector.

Operational tradeoffs: supporting jku requires per-issuer URL allowlists, redirect blocking, TLS validation, and SSRF protections on the fetch; for most services the simpler and safer contract is to reject jku, jwk, and x5u and rely on a pinned JWKS per issuer. If federated key advertisement is genuinely needed, validate the fetched JWKS against a trusted issuer discovery document.

RSIS3/mykb relevance: JWT verification code should default to reject-on-jku; documenting that rule gives RSIS3's security reviews a concrete header policy to check.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/none-algorithm|JWT none Algorithm]] — related coverage in the same cluster
- [[wiki/api-protocols/weak-hash-jwt|Weak Hashes in JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/algorithm-confusion|JWT Algorithm Confusion]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/identity/key-rotation|Key Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
