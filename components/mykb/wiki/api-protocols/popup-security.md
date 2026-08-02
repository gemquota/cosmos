---
type: "concept"
title: "Popup Security"
description: "Controlling window.open behavior, opener relationships, and popup abuse"
tags: ["security", "browsers", "javascript", "web-platforms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Popup Security

## Summary
Controlling window.open behavior, opener relationships, and popup abuse. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- window.opener grants the opened page a reference back to its opener
- rel=noopener and COOP sever that link
- Open question — do popups still carry meaningful privilege in modern browsers?

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/clickjacking-defense|Clickjacking Defense]] — related coverage in the same cluster
- [[wiki/api-protocols/iframe-sandboxing|iframe Sandboxing]] — related coverage in the same cluster
- [[wiki/api-protocols/popup-security|Popup Security]] — related coverage in the same cluster
- [[wiki/api-protocols/cors|CORS]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
