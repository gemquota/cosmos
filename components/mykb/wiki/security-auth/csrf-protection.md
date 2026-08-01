---
type: "concept"
title: "CSRF Protection"
description: "Defenses against cross-site request forgery, which replays authenticated requests"
tags: ["csrf", "web-security", "attacks", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"]
---

# CSRF Protection

- CSRF tricks a victim's browser into sending an authenticated request (state change) to a site the victim trusts.
- Defenses: synchronizer tokens, SameSite cookies, double-submit cookies, and origin/Referer checks.
- Modern SameSite=Lax/Strict handling covers most cases, but tokens remain the robust baseline for state-changing endpoints.
- For mykb: API state changes should require CSRF tokens or rely on non-cookie authn like bearer tokens, which CSRF cannot replay.

## Related

- [[wiki/security-auth/security-headers|Security Headers]] — SameSite and cookie flags
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — XSS can steal CSRF tokens
- [[wiki/identity/session-management|Session Management]] — cookies and sessions are the CSRF surface
- [[wiki/api-protocols/rest-apis|REST APIs]] — state-changing endpoints need CSRF defense
