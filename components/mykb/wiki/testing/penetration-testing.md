---
type: "concept"
title: "Penetration Testing"
description: "Authorized simulated attacks to validate security defenses"
tags: ["penetration-testing", "testing", "security", "red-team"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-project-web-security-testing-guide/", "https://owasp.org/www-project-penetration-testing-knowledge-base/"]
---

# Penetration Testing

## Summary
Penetration testing performs authorized simulated attacks to validate security defenses end to end. Pentesters think like attackers, chaining flaws, to demonstrate real exploitability and business impact beyond what scanners report.

## Details
- Types: black-box with no internal knowledge, white-box with full access, and gray-box mixed.
- Methodology: reconnaissance, enumeration, exploitation, privilege escalation, persistence, and reporting.
- OWASP WSTG and PTES guide scope, technique, and reporting formats.
- Scoped and authorized: rules of engagement define targets, timing, and limits.
- Deliverables: proof-of-concept exploits, severity ratings, and remediation guidance.
- Combine with automated scanning: pentesting adds human creativity and flaw chaining.
- Run after major changes and on a cadence; integrate with bug bounty programs.

## Related
- [[wiki/testing/security-testing|Security Testing]] — the discipline pentesting belongs to
- [[wiki/testing/vulnerability-scanning|Vulnerability Scanning]] — automated baseline pentests build on
- [[wiki/security-auth/bug-bounty|Bug Bounty]] — crowdsourced pentest coverage
- [[wiki/security-auth/mitre-attack-framework|MITRE ATT&CK]] — tactics pentests map to
- [[wiki/security-auth/kill-chain|Kill Chain]] — stages simulated in engagements
- [[wiki/security-auth/responsible-disclosure|Responsible Disclosure]] — reporting found vulnerabilities
