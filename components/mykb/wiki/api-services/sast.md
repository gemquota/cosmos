---
type: "concept"
title: "Static Application Security Testing"
description: "Analyzing source code for security flaws without executing it"
tags: ["sast", "static-analysis", "code-scanning", "devsecops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/Source_Code_Analysis_Tools"]
---

# Static Application Security Testing

- SAST scans source code for vulnerability patterns — injection, insecure deserialization, hardcoded secrets — before code runs.
- It runs early in the pipeline (per commit), giving fast feedback, but produces false positives that need triage.
- OWASP maintains a list of open-source and commercial source code analysis tools.
- For mykb: SAST in CI gates merges on high-severity findings and catches injection patterns in agent tools.

## Related

- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — a class SAST detects
- [[wiki/api-services/dast|Dynamic Application Security Testing]] — the runtime complement
- [[wiki/api-services/secret-scanning|Secret Scanning]] — SAST's cousin for credentials
- [[wiki/devops-infra/github-actions|GitHub Actions]] — running SAST in CI
- [[wiki/security-auth/compliance-frameworks|Compliance Frameworks]] — SAST as a standard security control
