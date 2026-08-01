---
type: "concept"
title: "Threat Intelligence"
description: "Curated information about adversaries, tactics, and indicators used to guide defense"
tags: ["threat-intel", "cti", "indicators", "adversaries"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://oasis-open.github.io/cti-documentation/"]
---

# Threat Intelligence

- Threat intelligence (CTI) describes adversaries, their campaigns, tactics, and technical indicators, structured in standards like STIX/TAXII.
- It feeds detection rules, risk scoring, and incident response with evidence beyond local telemetry.
- Intelligence is only useful when operationalized: indicators age fast, so automation and context matter.
- For mykb: a small CTI feed (CVE, KEV, IoC lists) can sharpen monitoring without a full intel program.

## Related

- [[wiki/security-auth/indicators-of-compromise|Indicators of Compromise]] — the technical artifacts intel shares
- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK Framework]] — the behavior taxonomy for intel
- [[wiki/security-auth/security-incident-monitoring|Security Incident Monitoring]] — intel improves detection
- [[wiki/security-auth/cve-disclosures|CVE Disclosures]] — vulnerability intel
