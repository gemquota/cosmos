---
type: "concept"
title: "Path Cookies"
description: "The Path attribute that limits which URLs a cookie is sent to"
tags: ["http", "cookies", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Path Cookies

## Summary
The Path attribute on a cookie limits which URL prefixes receive it. It is a routing convenience, not a security boundary: any same-host script can still reach a cookie by navigating to a URL under its path, so access control must come from Domain, Secure, SameSite, and HttpOnly.

## Details
A cookie with Path=/app is sent only to requests whose URL path starts with /app; Path=/ is the default and covers everything. The mechanism exists so servers can scope cookies to application areas — an admin panel cookie on /admin, a public-area cookie on /. But the browser treats Path as a send-rule only: a script running on /admin can make requests to /admin/../app or other paths, and can navigate frames to any path, carrying the cookie along.

The mechanism's limits: same-origin scripts are not constrained by cookie path. If a page at /app/index.html runs JavaScript, that script can request /admin/anything; the /admin cookie is attached because the browser's path-matching sees the request path, not the script's origin page. Path also doesn't restrict which server-side code can set or read the cookie — any same-host endpoint can read the cookie from the request. This is why path-scoped cookies must not be treated as a security control.

Concrete example: a wiki sets an admin cookie with Path=/admin believing it protects the session. An XSS on /wiki/page executes fetch('/admin/settings', {credentials: 'include'}) — the request path is under /admin, so the cookie is attached and the attack succeeds. HttpOnly would not have stopped this either (the browser attaches the cookie; the script doesn't need to read it); the real controls are authorization on the endpoint and CSRF protection.

Failure modes: treating Path as an authorization boundary; using Path to hide cookies from scripts (it doesn't); and inconsistent Path values causing cookies to be silently missing on some routes (a real functional bug when a cookie is set for /app but the session needs it on /). Path/ prefix cookies (__Host-/__Secure-) additionally require Path=/ for validation.

Operational tradeoffs: keep Path=/ for session and auth cookies — narrow paths add no security and cause missing-cookie bugs; the security attributes are Secure, HttpOnly, SameSite, and the __Host- prefix. Where different areas genuinely need different cookies, use different cookie names with explicit scoping decisions documented.

RSIS3/mykb relevance: the dashboard and wiki share a host; documenting that session cookies use Path=/ with security enforced elsewhere prevents a future "Path as security" mistake in code review.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/third-party-cookies|Third-Party Cookies]]
- [[wiki/api-protocols/partitioned-cookies|Partitioned Cookies]]
- [[wiki/api-protocols/cross-site-requests|Cross-Site Requests]]
- [[wiki/api-protocols/http-cookies|HTTP Cookies]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
