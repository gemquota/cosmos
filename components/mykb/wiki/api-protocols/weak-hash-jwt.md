---
type: "concept"
title: "Weak Hashes in JWT"
description: "HS256 tokens signed with guessable or weak secrets"
tags: ["jwt", "security", "attacks", "hashing"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Weak Hashes in JWT

## Summary
HS256 tokens signed with guessable or weak secrets. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- HS256 with a guessable secret permits offline brute force
- Long random secrets or asymmetric algorithms are required
- Open question — how do tools audit token secrets in CI?

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/algorithm-confusion|JWT Algorithm Confusion]] — related coverage in the same cluster
- [[wiki/api-protocols/jku-attacks|JKU Attacks]] — related coverage in the same cluster
- [[wiki/api-protocols/none-algorithm|JWT none Algorithm]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/identity/key-rotation|Key Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
