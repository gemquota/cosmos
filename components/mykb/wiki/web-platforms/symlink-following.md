---
type: "concept"
title: "Symlink Following"
description: "Attacks that traverse symbolic links during file operations"
tags: ["security", "filesystem", "paths", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Symlink Following

## Summary
Attacks that traverse symbolic links during file operations. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Symlinks let filesystem writes escape their intended directory
- O_NOFOLLOW and canonical-path checks prevent traversal
- Open question — how do archive extractors handle symlink entries?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/sanitization-practice|Sanitization Practice]] — related coverage in the same cluster
- [[wiki/web-platforms/output-encoding|Output Encoding]] — related coverage in the same cluster
- [[wiki/web-platforms/safe-html-rendering|Safe HTML Rendering]] — related coverage in the same cluster
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — related coverage in the same cluster
