---
type: "concept"
title: "Cross-Site Scripting (XSS)"
description: "Injection vectors and prevention techniques"
tags: [security", "xss", "injection", "web", "owasp"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/attacks/xss/", "https://developer.mozilla.org/en-US/docs/Web/Security/Types_of_attacks"]
---

# Cross-Site Scripting (XSS)

## Summary
Cross-site scripting injects executable scripts into pages viewed by other users. Stored XSS persists in data, reflected XSS bounces off the server, and DOM-based XSS happens entirely client-side. Because scripts run with the page's origin, they can steal cookies, tokens, and keystrokes — making XSS the highest-impact client-side vulnerability.

## Details
- Vectors: unescaped user input rendered into HTML, attribute, JavaScript, or URL contexts; innerHTML with untrusted data is a classic sink.
- Context matters: escaping must match the injection context — HTML, attribute, CSS, or URL — or an attacker breaks out.
- Prevention: framework auto-escaping (React, Vue), output encoding, sanitization libraries, and avoiding dangerous sinks.
- Defense in depth: Content Security Policy, Trusted Types, and HttpOnly cookies limit what a successful injection can do.
- Client storage: XSS can read localStorage and sessionStorage, so sensitive tokens belong in HttpOnly cookies.
- Testing: automated scanners plus manual review of sinks, and audit every third-party script in the page.

## Related
- [[wiki/frontend/content-security-policy|Content Security Policy]] — limiting XSS impact
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — the security-area deep dive
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the boundary XSS crosses
- [[wiki/frontend/web-storage|Web Storage]] — what XSS can read
- [[wiki/frontend/dom-api|DOM API]] — the sinks injection reaches
- [[wiki/frontend/frontend-testing|Frontend Testing]] — security regression tests
