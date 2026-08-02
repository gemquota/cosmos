---
type: "concept"
title: "Double-Submit Cookie"
description: "CSRF defense comparing a cookie with a mirrored request value"
tags: ["csrf", "security", "cookies", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Double-Submit Cookie

## Summary
CSRF defense comparing a cookie with a mirrored request value. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- The cookie value must match a submitted request value
- It needs no server storage but is weaker than synchronizer tokens
- Open question — which CSRF defenses survive SameSite defaults?

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/synchronizer-token|Synchronizer Token Pattern]] — related coverage in the same cluster
- [[wiki/api-protocols/sec-fetch-headers|Sec-Fetch Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf-tokens|CSRF Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
