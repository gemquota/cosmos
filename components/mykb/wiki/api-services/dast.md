---
type: "concept"
title: "Dynamic Application Security Testing"
description: "Testing running applications for vulnerabilities through their external interfaces"
tags: ["dast", "dynamic-analysis", "pentest", "devsecops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/Vulnerability_Scanning_Tools", "https://en.wikipedia.org/wiki/Dynamic_application_security_testing"]
---

# Dynamic Application Security Testing

## Summary


## Details
- Dynamic application security testing (DAST) probes a running application the way an attacker would, sending malicious payloads and observing responses.
- It tests the deployed system end-to-end, including configuration and framework behavior, catching issues static analysis cannot see.
- DAST needs a running environment and careful scoping so scans do not corrupt data or trigger destructive endpoints.
- Scan results require triage: automated scanners report many findings that need a human to judge real exploitability.
- **Worked example / comparison** — Comparison — SAST flags the unsafe query in source at commit time; DAST confirms whether the deployed app actually reflects the injection in its responses.
- For mykb, DAST is documented as the runtime half of the appsec testing pair, complementing SAST in the same cluster.

## Related
- [[wiki/api-services/sast|Static Application Security Testing]]
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]]
- [[wiki/security-auth/security-headers|Security Headers]]
- [[wiki/api-protocols/openapi|OpenAPI]]
- [[wiki/security-auth/audit-logging|Audit Logging]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/concepts/decision-guides|Decision Guides]]
