---
type: "concept"
title: "Content Security Policy"
description: "Browser mechanism restricting which scripts, styles, and origins a page may load"
tags: ["csp", "xss", "browsers", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP"]
---

# Content Security Policy

- CSP lets servers declare allowed content sources, blocking inline scripts, unsafe eval, and unexpected origins.
- A strict CSP (no unsafe-inline, explicit source allowlists) neutralizes most XSS even if encoding fails.
- Implementation: start with report-only mode, tune against real traffic, then enforce.
- For mykb: the web UI should ship a strict CSP with a reporting endpoint wired into monitoring.

## Related

- [[wiki/security-auth/xss-prevention|XSS Prevention]] — CSP is the safety net
- [[wiki/security-auth/security-headers|Security Headers]] — CSP within the header stack
- [[wiki/security-auth/subresource-integrity|Subresource Integrity]] — verifying loaded script integrity
- [[wiki/devops-infra/nginx|Nginx]] — serving CSP at the edge
- [[wiki/identity/session-management|Session Management]] — CSP protects sessions from script theft
