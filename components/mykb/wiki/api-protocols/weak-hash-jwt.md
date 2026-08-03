---
type: "concept"
title: "Weak Hashes in JWT"
description: "HS256 tokens signed with guessable or weak secrets"
tags: ["jwt", "security", "attacks", "hashing"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Weak Hashes in JWT

## Summary
Weak-hash JWT failures are tokens signed with HMAC algorithms such as HS256 whose secret is guessable or reused. Because HMAC verification is a pure function of header, payload, and secret, an attacker who can guess the secret can forge tokens offline — no network interaction needed — and mint tokens with arbitrary claims.

## Details
- Mechanism: with HS256, the JWT is signed as `HMAC-SHA256(base64url(header) + "." + base64url(payload), secret)` and the signature travels in the token. Verification recomputes the HMAC and compares. The attack is offline brute force: take a captured token, try candidate secrets from wordlists or derived from leaked data, and check whether the recomputed signature matches. HS256 is only as strong as the secret's entropy — a passphrase like `secret` or a key reused across environments falls in seconds, after which the attacker can sign any claims they like.
- Concrete examples: a Django SECRET_KEY committed to a public repo and used as the JWT secret; a shared "jwt_secret" hardcoded in microservice configs; a token signed with HS256 where the issuer intended to use RS256, so the same "public" value is doing symmetric duty. Tools like `jwt_tool` and `hashcat` automate the guessing, and leaked keys in container images or CI logs are a favorite source of candidate secrets.
- Failure modes: the algorithm-confusion variant — where a server expecting an asymmetric RS256 public key is tricked into verifying an HS256 token with that same public key as the HMAC secret — turns a public value into a signing capability. Weak secrets also compound with other JWT failures: a guessable secret makes `none`-algorithm and JKU attacks unnecessary. Reused secrets across services mean one compromise forges tokens everywhere, and secrets that never rotate leave a long exploitation window even after discovery.
- Operational tradeoffs: prefer asymmetric algorithms (RS256/ES256) so the signing key is never shared with verifiers and token verification cannot double as forgery; if symmetric HS256 is required, generate a 256+ bit random secret, store it in a secrets manager, never in code or config, and rotate on a schedule with overlapping old/new keys during transition. Auditing in CI — scanning for hardcoded secrets, checking that signing keys are not in the repo, and testing that token forgery fails — catches the weak-hash class before it ships.
- RSIS3/mykb relevance: RSIS3 and MyKB issue tokens across loop components; the standing rule is that any HMAC secret must be generated randomly, stored outside code, and rotated, with a test that verifies a token signed with the wrong secret is rejected.

## Related
- [[wiki/api-protocols/jwt-practice|JWT in Practice]]
- [[wiki/api-protocols/algorithm-confusion|JWT Algorithm Confusion]]
- [[wiki/api-protocols/jku-attacks|JKU Attacks]]
- [[wiki/api-protocols/none-algorithm|JWT none Algorithm]]
- [[wiki/api-protocols/json-web-tokens|JWT]]
- [[wiki/identity/key-rotation|Key Rotation]]
- [[wiki/api-protocols/mtls|mTLS]]
