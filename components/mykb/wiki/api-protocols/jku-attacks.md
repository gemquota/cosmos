---
type: "concept"
title: "JKU Attacks"
description: "Abusing the jku header to point verification at attacker keys"
tags: ["jwt", "security", "attacks", "keys"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# JKU Attacks

## Summary
Abusing the jku header to point verification at attacker keys. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- The jku header points verification at a key URL
- Fetching keys from attacker-controlled URLs enables forgery
- Open question — should jku and x5u ever be honored automatically?

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/none-algorithm|JWT none Algorithm]] — related coverage in the same cluster
- [[wiki/api-protocols/weak-hash-jwt|Weak Hashes in JWT]] — related coverage in the same cluster
- [[wiki/api-protocols/algorithm-confusion|JWT Algorithm Confusion]] — related coverage in the same cluster
- [[wiki/api-protocols/json-web-tokens|JWT]] — related coverage in the same cluster
- [[wiki/identity/key-rotation|Key Rotation]] — related coverage in the same cluster
- [[wiki/api-protocols/mtls|mTLS]] — related coverage in the same cluster
