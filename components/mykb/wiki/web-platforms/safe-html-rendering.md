---
type: "concept"
title: "Safe HTML Rendering"
description: "Rendering user content as text or through hardened HTML pipelines"
tags: ["security", "html", "xss", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Safe HTML Rendering

## Summary
Rendering user content as text or through hardened HTML pipelines. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Rendering untrusted content as text is always safer than as HTML
- Hardened pipelines and DOMPurify-style sanitizers render rich content
- Open question — how do agent UIs render tool output safely?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/template-escaping|Template Escaping]] — related coverage in the same cluster
- [[wiki/web-platforms/allowlist-validation|Allowlist Validation]] — related coverage in the same cluster
- [[wiki/web-platforms/denylist-validation|Denylist Validation]] — related coverage in the same cluster
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — related coverage in the same cluster
