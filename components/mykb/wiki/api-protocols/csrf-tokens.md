---
type: "concept"
title: "CSRF Tokens"
description: "Unpredictable per-session tokens that prove request intent"
tags: ["csrf", "security", "web", "forms"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# CSRF Tokens

## Summary
Unpredictable per-session tokens that prove request intent. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Unpredictable tokens prove the request originated from the app's own forms
- Tokens must be per-session and constant-time compared
- Open question — how do SPAs distribute CSRF tokens securely?

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/double-submit-cookie|Double-Submit Cookie]] — related coverage in the same cluster
- [[wiki/api-protocols/synchronizer-token|Synchronizer Token Pattern]] — related coverage in the same cluster
- [[wiki/api-protocols/sec-fetch-headers|Sec-Fetch Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
