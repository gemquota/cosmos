---
type: "concept"
title: "CSRF"
description: "Cross-site request forgery and defenses"
tags: ["csrf", "security", "web", "same-site", "attacks"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://owasp.org/www-community/attacks/csrf", "https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html"]
---

# CSRF

## Summary
Cross-Site Request Forgery (CSRF) tricks a victim's browser into sending a forged state-changing request to a site where the victim is authenticated: a malicious page triggers POST /transfer with the victim's session cookie, and the server cannot tell the request was not intended. Defenses make forged requests fail at the browser or server layer.

## Details
- The exploit: cookies are sent automatically with cross-site requests, so any cookie-authenticated endpoint is a target; GETs must never change state.
- SameSite cookies: SameSite=Lax (default) blocks cookies on cross-site subrequests; Strict blocks more but hurts legit linking; None + CSRF tokens is the legacy pattern.
- CSRF tokens: the server embeds an unguessable token in forms/headers (X-CSRF-Token); the server rejects requests without a matching token.
- Double-submit cookies and origin checks: verify Origin/Referer headers match — cheap and effective when tokens are impractical.
- Modern baseline: SameSite=Lax/Strict + custom-header requirement for APIs (cross-site requests cannot set custom headers without CORS preflight) renders most CSRF moot.
- Why APIs still care: cookie-based auth (sessions) is the vulnerable path; token-in-header auth (Bearer) is CSRF-immune because the token is not auto-sent.
- Testing: send forged cross-site requests from a separate origin in QA and assert rejection.

## Related
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — SameSite attributes are the first CSRF defense
- [[wiki/api-protocols/cors|CORS]] — CORS controls reading, not sending — CSRF needs separate fixes
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the boundary CSRF exploits
- [[wiki/api-protocols/oauth2-authorization-code|Authorization Code Flow]] — state parameter prevents login CSRF
- [[wiki/security-auth/xss-prevention|XSS Prevention]] — XSS bypasses CSRF defenses entirely
