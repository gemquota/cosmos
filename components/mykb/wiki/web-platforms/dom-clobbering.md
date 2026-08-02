---
type: "concept"
title: "DOM Clobbering"
description: "HTML attributes shadowing DOM globals to confuse scripts"
tags: ["security", "xss", "dom", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# DOM Clobbering

## Summary
HTML attributes shadowing DOM globals to confuse scripts. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- id and name attributes can shadow DOM globals
- Clobbered globals break security checks in scripts
- Open question — how do frameworks protect against clobbering today?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/prototype-pollution-web|Prototype Pollution on the Web]] — related coverage in the same cluster
- [[wiki/web-platforms/xs-leaks|XS-Leaks]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-clobbering|DOM Clobbering]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — related coverage in the same cluster
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — related coverage in the same cluster
