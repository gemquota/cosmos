---
type: "concept"
title: "Dynamic Application Security Testing"
description: "Testing running applications for vulnerabilities through their external interfaces"
tags: ["dast", "dynamic-analysis", "pentest", "devsecops"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-project-web-security-testing-guide/"]
---

# Dynamic Application Security Testing

- DAST probes a running application — HTTP endpoints, APIs, UIs — the way an attacker would, finding runtime flaws SAST misses.
- OWASP's Web Security Testing Guide is the methodology reference for what to test and how.
- DAST is slower and needs deployed environments, so it fits staging/release gates rather than per-commit.
- For mykb: DAST against the API gateway exercises authn, injection, and access-control paths end to end.

## Related

- [[wiki/api-services/sast|Static Application Security Testing]] — the static complement
- [[wiki/security-auth/ssrf-prevention|SSRF Prevention]] — a flaw DAST surfaces
- [[wiki/security-auth/security-headers|Security Headers]] — DAST validates header posture
- [[wiki/api-protocols/openapi|OpenAPI]] — API surface DAST targets
- [[wiki/security-auth/audit-logging|Audit Logging]] — DAST verifies security events are logged
