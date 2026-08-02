---
type: "concept"
title: "Synchronizer Token Pattern"
description: "Server-stored CSRF tokens validated against session state"
tags: ["csrf", "security", "web", "forms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Synchronizer Token Pattern

## Summary
Server-stored CSRF tokens validated against session state. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Server-stored tokens are compared against request tokens
- Session binding and constant-time comparison are essential
- Open question — how do stateless backends persist synchronizer state?

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/sec-fetch-headers|Sec-Fetch Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf-tokens|CSRF Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/double-submit-cookie|Double-Submit Cookie]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
