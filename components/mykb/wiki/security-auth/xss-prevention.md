---
type: "concept"
title: "XSS Prevention"
description: "Preventing injection of executable scripts into web pages viewed by other users"
tags: ["xss", "injection", "web-security", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html"]
---

# XSS Prevention

- Cross-site scripting (XSS) injects scripts into a page so they execute in another user's session, stealing cookies, tokens, and data.
- OWASP's cheat sheet: context-aware output encoding, safe APIs (no innerHTML), sanitization, and a strong Content Security Policy.
- Types: reflected, stored, and DOM-based XSS; each needs a different prevention focus.
- For mykb: any rendering of user content (notes, chat) must treat output encoding and CSP as non-negotiable.

## Related

- [[wiki/security-auth/content-security-policy|Content Security Policy]] — browser-level script control
- [[wiki/identity/session-hijacking|Session Hijacking]] — XSS is a cookie-stealing vector
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]] — sibling injection class
- [[wiki/security-auth/security-headers|Security Headers]] — header stack including CSP
- [[wiki/identity/session-management|Session Management]] — XSS steals the sessions CSP protects
