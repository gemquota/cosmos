---
type: "concept"
title: "Mutation XSS"
description: "Browsers mutating markup into executable script during parsing"
tags: ["security", "xss", "attacks", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Mutation XSS

## Summary
Browsers mutating markup into executable script during parsing. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- HTML parsers rewrite markup, turning inert input executable
- Sanitizers must account for parser mutation
- Open question — how do mXSS-resistant parsers handle unknown tags?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-xss|DOM XSS]] — related coverage in the same cluster
- [[wiki/web-platforms/reflected-xss|Reflected XSS]] — related coverage in the same cluster
- [[wiki/web-platforms/stored-xss|Stored XSS]] — related coverage in the same cluster
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
