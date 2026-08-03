---
type: "concept"
title: "Padding Oracle"
description: "Side-channel attacks that decrypt ciphertext through padding error feedback"
tags: ["security", "crypto", "attacks", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Padding Oracle

## Summary
A padding oracle is any endpoint that tells an attacker whether decrypted ciphertext had valid padding. With that yes/no signal, an attacker can decrypt any CBC-encrypted data byte by byte — and with chosen-ciphertext tricks, encrypt arbitrary plaintext.

## Details
Block ciphers in CBC mode pad plaintext to a block boundary (PKCS#7): the final block ends with N bytes of value N. On decryption, the padding must validate. If a server returns a different error for "bad padding" than for "bad MAC" or "valid," it leaks one bit per request: whether the manipulated ciphertext decrypted with valid padding. That single bit is a padding oracle.

The mechanism: the attacker flips bytes in a ciphertext block and observes the oracle's response, then solves for the plaintext of the adjacent block, one byte at a time (the classic Lucky13-era, Vaudenay's attack from 2002, and the 2016 POODLE predecessor). Each byte takes at most 256 oracle queries, so a full block is ~2048 queries and a whole message is linear in its length. The attack requires the ability to send many modified ciphertexts and read the difference between padding and MAC failures — exactly what encrypted cookies, encrypted session state, and some VPN protocols exposed.

Concrete example: an application encrypts session cookies with AES-CBC and a static key. On decrypt failure it returns 500 for bad padding and 400 for bad MAC. An attacker captures a valid cookie, then replays it with byte flips, reading the two responses to recover the plaintext — including the session secret — then forges an encrypted cookie by using the oracle to build valid ciphertext for chosen plaintext (admin=true). The fix: authenticate-then-encrypt with an AEAD (AES-GCM), or at minimum encrypt-then-MAC with constant-time, identical error handling.

Failure modes: any distinguishable error path (different HTTP status, different message, different timing) is an oracle; MAC-before-encrypt designs (MCO) leak; CBC with predictable IVs or reused keys compounds it; and libraries with padding-oracle-inherent modes (CBC with PKCS#7) must be replaced, not patched around.

Operational tradeoffs: switching to AEAD (AES-GCM or ChaCha20-Poly1305) removes the oracle class entirely and should be the standing default for any new encryption; legacy CBC ciphertext needs re-encryption with an explicit migration. Where CBC must remain, use encrypt-then-MAC, constant-time comparison, and identical errors for every failure. Detection: monitor for high volumes of decrypt failures from one source.

RSIS3/mykb relevance: any encrypted state in the wiki stack (cookies, cached secrets) should use AEAD; documenting the "no CBC without Encrypt-then-MAC, no distinguishable errors" rule gives RSIS3's crypto reviews a clear standard.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/hash-collision-dos|Hash Collision DoS]]
- [[wiki/api-protocols/regex-dos|ReDoS Attacks]]
- [[wiki/api-protocols/decompression-bombs|Decompression Bombs]]
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]]
- [[wiki/api-protocols/rate-limiting|Rate Limiting]]
- [[wiki/api-protocols/backpressure|Backpressure]]
