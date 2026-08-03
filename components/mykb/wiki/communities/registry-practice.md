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
- Signing keys are the trust root of any registry: the private key should live outside CI and the registry itself, and consumers should pin the public key so a compromised build machine cannot forge artifacts.
- Scanning gates promotion, not just publication: vulnerability results should be recorded next to the artifact so the audit trail covers both the build and its findings, and known-critical findings should block the stable namespace.
- Private registries add access policy to the picture: read access for consumers, a small write set for publishers, and pull-through caching for upstream sources so supply-chain reach stays explicit and reviewable.
- Namespace hygiene matters: ownership controls, immutable tags, and digest pinning prevent squatting, accidental overwrites, and drift between what a lockfile says and what actually runs.
- A registry topology for the bundle would separate promoted artifacts from experimental ones, mirror critical dependencies, and define retention so old versions stay available while the catalog remains searchable.
- Retention policy closes the loop: old versions remain pullable for the window consumers need, and deprecation notices replace silent deletion so the catalog never lies about what still exists.
- The practice is only as strong as its weakest link: unsigned pushes, unscanned images, or wide write permissions each reintroduce the supply-chain risk the registry was meant to remove.
- mykb relevance: the wiki would publish signed bundles to a private registry with scans.

## Related
- [[wiki/dev-tools/package-management|Package Management]]
- [[wiki/communities/image-tagging|Image Tagging]]
- [[wiki/communities/image-scanning|Image Scanning]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
