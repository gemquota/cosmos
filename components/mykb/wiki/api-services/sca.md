---
type: "concept"
title: "Software Composition Analysis"
description: "Identifying and tracking vulnerabilities and licenses in third-party dependencies"
tags: ["sca", "dependencies", "sbom", "supply-chain"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/Component_Analysis", "https://en.wikipedia.org/wiki/Software_composition_analysis"]
---

# Software Composition Analysis

## Summary


## Details
- Software composition analysis (SCA) inventories the open-source components in a codebase and checks them against known-vulnerability databases.
- It tracks direct and transitive dependencies, licensing, and the fix availability for each advisory.
- The key metric is vulnerable-dependency reachability — a vulnerable library is only a risk if the vulnerable code path is actually used.
- SCA gates should fail on fixable, reachable, high-severity issues while allowing a policy-defined risk budget.
- **Worked example / comparison** — Worked example — a build reports 40 dependencies; SCA flags one CVE in a transitively included logging library, and the fix is a one-line upgrade.
- For mykb, SCA is the supply-chain half of appsec; freshness review matters because new advisories appear constantly.

## Related
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]]
- [[wiki/security/sbom|SBOM]]
- [[wiki/security-auth/patch-management|Patch Management]]
- [[wiki/security/supply-chain-security|Software Supply Chain Security]]
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
