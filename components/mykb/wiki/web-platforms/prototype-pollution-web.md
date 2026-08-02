---
type: "concept"
title: "Prototype Pollution on the Web"
description: "Mutating Object.prototype via merge operations to alter app behavior"
tags: ["security", "javascript", "attacks", "objects"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Prototype Pollution on the Web

## Summary
Mutating Object.prototype via merge operations to alter app behavior. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Merge and assignment functions can poison Object.prototype
- Polluted prototypes alter property lookups app-wide
- Open question — how do JSON parsers and stores resist pollution?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/xs-leaks|XS-Leaks]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-clobbering|DOM Clobbering]] — related coverage in the same cluster
- [[wiki/web-platforms/prototype-pollution-web|Prototype Pollution on the Web]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
