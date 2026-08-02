---
type: "concept"
title: "Security Testing"
description: "Discovering vulnerabilities through systematic testing techniques"
tags: ["security-testing", "testing", "vulnerabilities", "owasp"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-project-web-security-testing-guide/", "https://owasp.org/Top10/"]
---

# Security Testing

## Summary
Security testing discovers vulnerabilities, injection, auth bypass, and data exposure, through a mix of automated scanning, manual review, and adversarial techniques. It validates that security controls actually work under attack-like conditions.

## Details
- OWASP WSTG provides a structured methodology and checklist for web apps.
- Families: SAST for static analysis, DAST at runtime, dependency scanning, secret scanning, and penetration testing.
- Focus areas: authentication, authorization, session handling, input validation, and cryptography.
- Automate scans in CI; run deep reviews before release and for high-risk changes.
- Threat-model first: know the attack surface and trust boundaries.
- Triage findings by CVSS severity and fix criticals before shipping.
- Combine with red teaming and bug bounty programs for outside perspective.

## Related
- [[wiki/testing/penetration-testing|Penetration Testing]] — human adversarial validation
- [[wiki/testing/vulnerability-scanning|Vulnerability Scanning]] — automated known-vuln checks
- [[wiki/testing/authentication-testing|Authentication Testing]] — identity attack surface
- [[wiki/testing/api-testing|API Testing]] — security cases in API suites
- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK]] — tactics security tests model
- [[wiki/security-auth/threat-intelligence|Threat Intelligence]] — drives what to test
