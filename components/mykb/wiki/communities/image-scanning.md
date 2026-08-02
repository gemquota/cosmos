---
type: "concept"
title: "Image Scanning"
description: "Checking container images for known vulnerabilities before they ship"
tags: ["image-scanning", "security", "containers", "ci"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Image Scanning

## Summary
Image scanning compares the packages inside a container image against vulnerability databases (Trivy, Grype, Clair, Snyk) and reports findings with severities and fixes. Scanning at build time keeps vulnerable images out of the registry.

## Details
- Scan base images and final images; gate promotion on fixable critical findings.
- Scans are point-in-time: re-scan on a schedule because the vulnerability DB grows.
- Pair with SBOMs so scans cover every layer, including distro packages and binaries.
- mykb relevance: wiki images gate promotion until critical CVEs are fixed or waived.

## Related
- [[wiki/communities/registry-practice|Registry Practice]]
- [[wiki/communities/image-tagging|Image Tagging]]
- [[wiki/compositions/dependency-scanning|Dependency Scanning]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
