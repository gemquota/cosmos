---
type: "concept"
title: "License Checking"
description: "Validating that dependencies' licenses fit your distribution model"
tags: ["licenses", "compliance", "dependencies", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# License Checking

## Summary
License checking audits every dependency's license against your distribution and legal requirements — copyleft obligations, attribution notices, and commercial-use constraints. Tools (license-checker, FOSSA, ScanCode) automate the inventory; humans review the edge cases.

## Details
- Know your obligations: GPL copyleft, LGPL dynamic-linking rules, MIT/BSD attribution.
- Automate inventory from lockfiles and SBOMs; gate on forbidden or unknown licenses.
- License changes between versions can break compliance — track them like vulnerabilities.
- mykb relevance: the wiki bundle publishes an SBOM with license attribution.

## Related
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/communities/dependency-graphs|Dependency Graphs]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/security/supply-chain-security|Supply Chain Security]]
- [[wiki/communities/package-pinning|Package Pinning]]
