---
type: "concept"
title: "Patch Management"
description: "Systematic process of tracking, testing, and deploying software updates"
tags: ["patching", "vulnerabilities", "lifecycle", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Patch_(computing)"]
---

# Patch Management

- Patch management is the discipline of applying vendor and security updates before attackers exploit known flaws.
- Time-to-patch is the metric that matters: most breaches exploit publicly known vulnerabilities that were patchable.
- A mature process inventories software, prioritizes by exploitability (CVE/CVSS, KEV catalog), tests, and deploys with rollback.
- For mykb: dependency and OS patching should be automated and monitored, with emergency paths for actively exploited CVEs.

## Related

- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — the vulnerability feed driving patches
- [[wiki/security-auth/cvss|CVSS]] — severity scoring for prioritization
- [[wiki/security-auth/endpoint-security|Endpoint Security]] — patch state as an endpoint control
- [[wiki/api-services/sca|Software Composition Analysis]] — tracking vulnerabilities in dependencies
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — patching is a baseline control
