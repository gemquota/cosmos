---
type: "concept"
hub: true
title: "Web Security (OWASP)"
description: "The OWASP Top 10 and cheat sheets as the baseline threat model for web applications"
tags: ["security", "owasp", "xss", "injection", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-project-top-ten/", "https://cheatsheetseries.owasp.org/"]
---
# Web Security (OWASP)

## Summary
OWASP publishes the Top 10 web application risks and a series of practical cheat sheets. The current list leads with broken access control, cryptographic failures, and injection, and it is the de facto checklist for security reviews. Teams use it to prioritize fixes and to frame penetration testing.

## Details
- **Broken access control** — IDOR, missing object-level checks, and privilege escalation top the list; fix with consistent authorization middleware and audits.
- **Injection** — SQL, XSS, and command injection persist; parameterized queries, context-aware output encoding, and safe APIs close the classes.
- **Cryptographic failures** — weak hashing, missing TLS, and hardcoded secrets; use modern algorithms and secret managers.
- **SSRF and deserialization** — server-side request forgery and untrusted deserialization are recurring criticals.
- **Cheat sheets** — OWASP's cheat sheet series gives concrete defenses per vulnerability class, from CSRF to file upload.
- **Worked example** — the mykb wiki has a security cluster that maps each OWASP category to stubs (XSS variants, injection, SSRF, deserialization) for review checklists.
- **Relevance** — RSIS3's acquisition workers fetch and validate external content, so SSRF and injection defenses apply directly to tool input handling.

## Related
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — adjacent concept in this wiki
- [[wiki/api-protocols/csp-headers|CSP Headers]] — adjacent concept in this wiki
- [[wiki/api-protocols/referrer-policy|Referrer Policy]] — adjacent concept in this wiki
- [[wiki/api-protocols/x-frame-options|X-Frame-Options]] — adjacent concept in this wiki
- [[wiki/security-auth/security-headers|Security Headers]] — existing coverage
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — existing coverage
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — existing coverage
