---
type: "concept"
title: "CVSS"
description: "Common Vulnerability Scoring System: a standard for rating vulnerability severity"
tags: ["cvss", "scoring", "severity", "vulnerabilities"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.first.org/cvss/"]
---

# CVSS

- CVSS (FIRST) scores vulnerability severity on a 0-10 scale from vectors describing exploitability, impact, and context.
- Scores enable triage and prioritization, but raw scores ignore whether a vulnerability is reachable in your system.
- Best practice: combine CVSS with exploitability (KEV catalog, proof-of-concept) and business context.
- For mykb: severity thresholds should gate emergency patching and incident escalation.

## Related

- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — CVSS scores accompany CVEs
- [[wiki/security-auth/patch-management|Patch Management]] — scoring drives patch priority
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — high-severity CVEs escalate monitoring
- [[wiki/api-services/sca|Software Composition Analysis]] — dependency CVSS aggregation
