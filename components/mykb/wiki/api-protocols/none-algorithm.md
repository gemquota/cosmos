---
type: "concept"
title: "JWT none Algorithm"
description: "Exploiting the none signing algorithm on misconfigured verifiers"
tags: ["jwt", "security", "attacks", "algorithms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# JWT none Algorithm

## Summary
Exploiting the none signing algorithm on misconfigured verifiers. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- alg: none tokens are unsigned and trivially forgeable
- Strict libraries reject none unless explicitly configured
- Open question — do embedded verifiers still accept none in 2026?

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/weak-hash-jwt|Weak Hashes in JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/algorithm-confusion|JWT Algorithm Confusion]] — related coverage in the same cluster
- [[wiki/api-protocols/jku-attacks|JKU Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/identity/key-rotation|Key Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
