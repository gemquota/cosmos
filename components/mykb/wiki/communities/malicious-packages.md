---
type: "concept"
title: "Malicious Packages"
description: "Packages published deliberately to steal data or execute attacks"
tags: ["malicious-packages", "security", "supply-chain", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Malicious Packages

## Summary
Malicious packages are published with intentional payloads — credential theft, cryptomining, exfiltration — disguised as useful libraries. High-profile npm and PyPI incidents show detection is reactive: careful install hygiene is the real defense.

## Details
- Payloads often trigger on install or first import: postinstall scripts, __init__ execution.
- Watch for suspicious signs: brand-new maintainers, obfuscated code, unusual install scripts.
- Scan with tools that flag known-bad hashes and behaviors, not just CVEs.
- mykb relevance: the wiki installs from verified lockfiles and reviews install scripts.

## Related
- [[wiki/communities/typosquatting|Typosquatting]]
- [[wiki/communities/supply-chain-attacks|Supply-Chain Attacks]]
- [[wiki/communities/vulnerability-scanning-ci|Vulnerability Scanning in CI]]
- [[wiki/communities/package-pinning|Package Pinning]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
