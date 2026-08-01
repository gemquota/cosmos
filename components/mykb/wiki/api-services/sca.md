---
type: "concept"
title: "Software Composition Analysis"
description: "Identifying and tracking vulnerabilities and licenses in third-party dependencies"
tags: ["sca", "dependencies", "sbom", "supply-chain"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/Component_Analysis"]
---

# Software Composition Analysis

- SCA inventories open-source dependencies and matches them against vulnerability databases (CVE, OSV) and license policies.
- Modern stacks are mostly third-party code, so dependency risk is a first-class concern.
- SCA output feeds SBOMs, patch prioritization, and policy gates on vulnerable versions.
- For mykb: SCA in CI should fail builds on known-vulnerable direct dependencies and flag transitive risk.

## Related

- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — the vulnerability data SCA matches
- [[wiki/security/sbom|SBOM]] — the inventory SCA produces
- [[wiki/security-auth/patch-management|Patch Management]] — updating what SCA flags
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — the broader program
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — dependency compliance
