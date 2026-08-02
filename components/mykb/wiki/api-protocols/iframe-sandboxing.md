---
type: "concept"
title: "iframe Sandboxing"
description: "Restricting embedded content capabilities through the sandbox attribute"
tags: ["security", "iframe", "browsers", "web-platforms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# iframe Sandboxing

## Summary
Restricting embedded content capabilities through the sandbox attribute. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- The sandbox attribute drops scripts, forms, popups, and top navigation
- allow-scripts plus allow-same-origin re-creates risk and must be deliberate
- Open question — which sandbox flags do third-party embeds truly need?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/popup-security|Popup Security]] — related coverage in the same cluster
- [[wiki/api-protocols/clickjacking-defense|Clickjacking Defense]] — related coverage in the same cluster
- [[wiki/api-protocols/iframe-sandboxing|iframe Sandboxing]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
