---
type: "concept"
title: "Same-Origin Policy"
description: "Browser rule preventing cross-origin reads of documents and resources"
tags: ["same-origin", "browsers", "web-security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy"]
---

# Same-Origin Policy

- The same-origin policy confines scripts to reading resources from their own origin (scheme + host + port), blocking cross-site data theft.
- It is the browser's core isolation primitive; CORS and postMessage are the controlled exceptions.
- Origin checks are exact — subdomains and different ports count as different origins.
- For mykb: sensitive APIs should refuse non-CORS cross-origin reads by default and rely on origin-aware tokens.

## Related

- [[wiki/security-auth/cors-policy|CORS Policy]] — the deliberate exception mechanism
- [[wiki/security-auth/security-headers|Security Headers]] — hardening around origin isolation
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — SOP limits XSS damage
- [[wiki/identity/session-management|Session Management]] — cookie scoping by origin
