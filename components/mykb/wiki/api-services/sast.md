---
type: "concept"
title: "Static Application Security Testing"
description: "Analyzing source code for security flaws without executing it"
tags: ["sast", "static-analysis", "code-scanning", "devsecops"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/Source_Code_Analysis_Tools", "https://en.wikipedia.org/wiki/Static_application_security_testing"]
---

# Static Application Security Testing

## Summary


## Details
- Static application security testing (SAST) analyzes source code without running it, looking for vulnerability patterns, taint flows, and unsafe API use.
- It finds issues early in the pipeline — before code reaches production — and integrates with CI as a gate on pull requests.
- SAST produces false positives because static analysis approximates runtime behavior; triage rules and baselining keep the signal usable.
- It complements DAST: SAST sees the code, DAST sees the running system, and they catch different bug classes.
- **Worked example / comparison** — Worked example — a SAST rule flags an unescaped query string concatenation in a search endpoint as a SQL-injection candidate before the PR merges.
- For mykb, SAST is documented in the security-services cluster; the wiki's own check scripts use the same gate idea for practices verification.

## Related
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/api-services/dast|Dynamic Application Security Testing]]
- [[wiki/api-services/secret-scanning|Secret Scanning]]
- [[wiki/devops-infra/github-actions|GitHub Actions]]
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/global-link-check|Global Link Check]]
- [[wiki/concepts/decision-guides|Decision Guides]]
