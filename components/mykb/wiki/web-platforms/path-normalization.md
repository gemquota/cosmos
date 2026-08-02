---
type: "concept"
title: "Path Normalization"
description: "Resolving dot segments and traversal before filesystem access"
tags: ["paths", "security", "filesystem", "normalization"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Path Normalization

## Summary
Resolving dot segments and traversal before filesystem access. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Dot-segments and traversal must resolve before filesystem access
- Realpath-style checks stop symlink and .. escapes
- Open question — how do sandboxes virtualize path resolution?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/web-platforms/symlink-following|Symlink Following]] — related coverage in the same cluster
- [[wiki/web-platforms/sanitization-practice|Sanitization Practice]] — related coverage in the same cluster
- [[wiki/web-platforms/output-encoding|Output Encoding]] — related coverage in the same cluster
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — related coverage in the same cluster
- [[wiki/web-platforms/web-apis|Web APIs]] — related coverage in the same cluster
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]] — related coverage in the same cluster
