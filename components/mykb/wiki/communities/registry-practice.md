---
type: "concept"
title: "Registry Practice"
description: "Running and using package and image registries safely"
tags: ["registry", "packages", "images", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Registry Practice

## Summary
Registry practice covers publishing, pulling, scanning, and securing artifacts — package registries (npm, PyPI, Maven Central) and container registries (Docker Hub, GHCR, ECR). Immutability, signing, and scanning are the core disciplines.

## Details
- Treat published artifacts as immutable: republish under a new version, never overwrite.
- Sign artifacts (cosign, sigstore) and scan for vulnerabilities before promotion.
- Control publish rights tightly — registries are supply-chain trust boundaries.
- mykb relevance: the wiki publishes signed bundles to a private registry with scans.

## Related
- [[wiki/dev-tools/package-management|Package Management]]
- [[wiki/communities/image-tagging|Image Tagging]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
