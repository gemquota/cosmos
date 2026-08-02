---
type: "concept"
title: "SBOM Practice"
description: "Producing and consuming software bills of materials for transparency"
tags: ["sbom", "supply-chain", "inventory", "security"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Software_bill_of_materials", "https://en.wikipedia.org/wiki/Dependency_management"]
---

# SBOM Practice

## Summary
A software bill of materials (SBOM) is a machine-readable inventory of a product's components — packages, versions, licenses, and hashes. Practice means generating one per release, sharing it with consumers, and using it for vulnerability and license analysis.

## Details
- Formats: SPDX and CycloneDX are the standards; both encode components, relationships, and hashes.
- Generate SBOMs from lockfiles and container images at build time; embed them in release artifacts.
- SBOMs enable consumer-side response: when an advisory lands, matching against SBOMs finds affected products.
- An SBOM is only as good as its generation and freshness — regenerate per release and verify contents.
- Sign SBOMs like any artifact so they cannot be tampered with.
- For the mykb bundle, each wiki release ships an SBOM of its tooling and content dependencies.
- Worked example — a wiki release ships a CycloneDX SBOM; when a markdown library advisory appears, the team queries the SBOM, finds the affected release, and schedules the update.

Worked example — a wiki release ships a CycloneDX SBOM; when a markdown library advisory appears, the team queries the SBOM, finds the affected release, and schedules the update.

## Related
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/communities/registry-practice|Registry Practice]]
- [[wiki/communities/license-checking|License Checking]]
- [[wiki/security/sbom|SBOM]]
- [[wiki/communities/supply-chain-attacks|Supply-Chain Attacks]]
- [[wiki/tooling/secure-sdlc|Secure SDLC]]
- [[wiki/communities/checksums|Checksums]]
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
