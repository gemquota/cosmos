---
type: "concept"
title: "Double-Submit Cookie"
description: "CSRF defense that compares a cookie value with a submitted form value"
tags: ["security", "csrf", "http", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Double-Submit Cookie

## Summary
The double-submit cookie pattern defends against CSRF by setting a random token in a cookie and requiring the same token in a request parameter or header; the server compares the two. It needs no server-side token store, which is both its appeal and its weakness.

## Details
The pattern works because a cross-site attacker cannot read the victim's cookies (same-origin policy) and therefore cannot include the cookie's value in a forged request body or header. The server sets csrf_token=<random> as a cookie; the application embeds the same value in forms (hidden field) or as a custom header on AJAX calls; on each state-changing request, the server compares the submitted value with the cookie value and rejects mismatches.

The mechanism: no session store is consulted, which makes the pattern stateless and horizontally scalable — attractive for microservices and CDN-served frontends. But the cookie must be readable by the server, so it cannot be HttpOnly; and any subdomain that can set cookies for the parent domain can set both the cookie and the form value (or an attacker who can inject into the page can read both), defeating the control. Binding the cookie value to the session id (signed or hashed) closes part of that gap.

Concrete example: a wiki's AJAX comment form sends a custom header X-CSRF-Token: ab12... while the server set cookie csrf_token=ab12... with SameSite=Lax. A cross-site forged POST from an attacker page cannot set the custom header (browsers block cross-origin custom headers without CORS preflight) and cannot read the cookie, so the request fails. A cross-site form POST also fails because the attacker can't know the hidden field value.

Failure modes: cookies without the Secure flag or with overly broad Domain scope undermine the pattern; the token being guessable or non-random defeats it; and a CSRF token cookie that is also sent to subdomains allows a subdomain attacker to forge both halves. The pattern is weaker than the synchronizer token when subdomain compromise is in scope.

Operational tradeoffs: double-submit is the cheapest scalable CSRF defense and works well for cookie-based SPAs, but it trades the synchronizer pattern's server-side binding for statelessness. The upgrade path is a signed token derived from the session, or moving to SameSite=Strict plus the synchronizer pattern where server state is acceptable.

RSIS3/mykb relevance: if the dashboard ships a cookie-based SPA, double-submit with a session-bound token is the documented baseline; RSIS3's security checks can assert the comparison exists on every state-changing route.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/synchronizer-token|Synchronizer Token Pattern]] — related coverage in the same cluster
- [[wiki/api-protocols/sec-fetch-headers|Sec-Fetch Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf-tokens|CSRF Tokens]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/csrf-protection|CSRF Protection]] — related coverage in the same cluster
- [[wiki/api-protocols/http-headers|HTTP Headers]] — related coverage in the same cluster
