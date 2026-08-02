---
type: "concept"
title: "Checksums"
description: "Hash values that verify artifacts are intact and untampered"
tags: ["checksums", "hashes", "integrity", "supply-chain"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Checksums

## Summary
Checksums are hash values (SHA-256 and up) that let consumers verify an artifact matches its published content. They catch corruption and tampering in transit, and they are the load-bearing primitive behind lockfiles, signatures, and content-addressed storage.

## Details
- Use strong hashes: SHA-256 or better; SHA-1 and MD5 are broken for integrity claims.
- Checksums verify integrity; signatures (cosign, GPG) add authenticity — do not confuse the two.
- Content-addressed systems (Nix store, OCI digests) make the hash the identity.
- mykb relevance: the wiki verifies every fetched artifact against a pinned hash.

## Related
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/dev-tools/lockfiles|Lockfiles]]
- [[wiki/tooling/backup-verification|Backup Verification]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/communities/hermetic-builds|Hermetic Builds]]
