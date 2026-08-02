---
type: "concept"
title: "Web Storage"
description: "localStorage, sessionStorage, and cookies"
tags: [web-storage", "localstorage", "cookies", "javascript", "browser"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies"]
---

# Web Storage

## Summary
Web Storage provides key-value persistence in the browser: localStorage survives restarts, sessionStorage lasts for the tab session, and cookies travel with HTTP requests. localStorage and sessionStorage store strings synchronously with a roughly 5MB quota per origin; cookies hold a few KB and are sent to the server on every request.

## Details
- localStorage: origin-scoped, synchronous, string-only values; survives browser restarts; storage events fire across tabs.
- sessionStorage: per-tab lifetime, ideal for ephemeral wizard state and drafts that should not leak between tabs.
- Cookies: 4KB limits, sent automatically with requests; SameSite, Secure, and HttpOnly attributes control exposure.
- Quotas and errors: writes can throw QuotaExceededError in private browsing or when full; always wrap writes in try/catch.
- Security: any XSS can read localStorage and sessionStorage — never store tokens there without compensating controls.
- Alternatives: IndexedDB for large structured data; server-side session storage for anything sensitive.

## Related
- [[wiki/frontend/indexeddb|IndexedDB]] — the larger structured storage sibling
- [[wiki/frontend/cross-site-scripting|Cross-Site Scripting]] — the threat model for client storage
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the boundary storage respects
- [[wiki/identity/session-management|Session Management]] — server-side session counterparts
- [[wiki/frontend/fetch-api|Fetch API]] — cookie behavior on requests
- [[wiki/web-platforms/web-apis|Web APIs]] — the API family storage belongs to
