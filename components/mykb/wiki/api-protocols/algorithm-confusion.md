---
type: "concept"
title: "JWT Algorithm Confusion"
description: "Switching signing algorithms to forge tokens when the verifier is lax"
tags: ["jwt", "security", "attacks", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# JWT Algorithm Confusion

## Summary
Switching signing algorithms to forge tokens when the verifier is lax. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Verifiers trusting the alg header accept attacker-chosen algorithms
- Pinning algorithms and key types prevents RS256-to-HS256 swaps
- Open question — how do libraries harden default algorithm selection?

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/jku-attacks|JKU Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/none-algorithm|JWT none Algorithm]] — related coverage in the same cluster
- [[wiki/api-protocols/weak-hash-jwt|Weak Hashes in JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/identity/key-rotation|Key Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
