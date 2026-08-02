---
type: "concept"
title: "Dependency Scanning"
description: "Checking dependencies for known vulnerabilities continuously"
tags: ["dependency-scanning", "security", "supply-chain", "automation"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-project-dependency-check/", "https://en.wikipedia.org/wiki/Software_bill_of_materials"]
---

# Dependency Scanning

## Summary
Dependency scanning matches the packages in your project against vulnerability databases and flags known issues with severity and remediation. Run in CI and on a schedule, it turns the dependency graph from a blind spot into a managed risk surface.

## Details
- Scanners (OWASP Dependency-Check, Trivy, Grype, OSV-Scanner, Snyk) compare versions and hashes against advisories.
- Scan the resolved graph from lockfiles, not just declared ranges — transitive dependencies dominate.
- Gate on severity with owners and waivers; unmanaged scan output becomes noise fast.
- Scans are point-in-time: re-run on schedule and after advisories, not just at release.
- Pair with SBOMs and license checks for the full supply-chain picture.
- For the mykb bundle, dependency scans run in CI and weekly against the tooling's lockfiles.
- Worked example — a weekly wiki scan flags a transitive npm package with a critical advisory; the update bot opens a fix PR the same day, and CI verifies it.

Worked example — a weekly wiki scan flags a transitive npm package with a critical advisory; the update bot opens a fix PR the same day, and CI verifies it.

## Related
- [[wiki/tooling/sbom-practice|Dependency Scanning]]
- [[wiki/tooling/sbom-practice|SBOM Practice]]
- [[wiki/communities/dependency-updates|Dependency Updates]]
- [[wiki/compositions/shift-left-security|Shift-Left Security]]
- [[wiki/communities/supply-chain-attacks|Supply-Chain Attacks]]
- [[wiki/tooling/secure-sdlc|Secure SDLC]]
- [[wiki/communities/dependabot-practice|Dependabot Practice]]
- [[wiki/communities/renovate-bot|Renovate Bot]]
- [[wiki/testing/vulnerability-scanning|Vulnerability Scanning]]
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
