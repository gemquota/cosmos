---
type: "concept"
title: "Cookie Flags"
description: "Secure, HttpOnly, SameSite, and prefix attributes on cookies"
tags: ["http", "cookies", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cookie Flags

## Summary
Cookie flags — Secure, HttpOnly, SameSite — are the security attributes that decide who can read, send, and receive a cookie. Getting them wrong turns session cookies into XSS and CSRF fuel.

## Details
Each cookie can carry four security-relevant attributes: Secure (only sent over HTTPS), HttpOnly (invisible to JavaScript), SameSite (Lax, Strict, or None; controls cross-site sending), and the newer __Host- and __Secure- prefixes. Together they define the cookie's trust boundary: Secure controls transport, HttpOnly controls script access, SameSite controls cross-site inclusion, and prefixes bind the cookie to its host and secure context.

The mechanism: the browser enforces the flags at set and send time. HttpOnly keeps document.cookie from seeing the value, so XSS can't read the session directly. Secure drops the cookie on plain HTTP, blocking downgrade interception. SameSite=Lax sends the cookie on top-level navigations but not cross-site subrequests or fetches, killing most CSRF; SameSite=Strict also suppresses it on top-level navigations (which can break link-in login flows); SameSite=None requires Secure and sends everywhere, opting out of the protection.

Concrete example: a wiki session cookie set with Secure; HttpOnly; SameSite=Lax; Path=/ protects against the three standard attacks at once: script exfiltration (HttpOnly), HTTP downgrade theft (Secure), and cross-site form POSTs from attacker pages (SameSite=Lax). Removing SameSite makes a login CSRF or comment-POST CSRF possible; removing HttpOnly makes any stored XSS able to hijack the session.

Failure modes: SameSite=None without Secure is rejected by modern browsers, breaking sessions; SameSite=Strict on a site that receives cross-site navigations (email links to a dashboard) appears to log users out; the Secure flag without HSTS still allows the initial plain-HTTP request to be downgraded unless the site redirects before cookies are set; and defaulting to same-site-everywhere breaks embedded third-party widgets that legitimately need cookies.

Operational tradeoffs: the secure baseline is Secure plus HttpOnly plus SameSite=Lax on every session and auth cookie, with Strict only where the UX cost is acceptable and None only for cross-site iframes with explicit justification. The __Host- prefix should be used on session cookies to prevent domain-scoped override attacks. These flags are cheap, but they must be set centrally, not per-route, or pockets of exposure remain.

RSIS3/mykb relevance: the dashboard's session handling should follow the Secure+HttpOnly+SameSite=Lax baseline; documenting the flag policy gives RSIS3's security checks a concrete assertion to verify.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/secure-flag|Secure Cookie Flag]]
- [[wiki/api-protocols/httponly-flag|HttpOnly Cookie Flag]]
- [[wiki/api-protocols/samesite-lax-strict|SameSite Lax vs Strict]]
- [[wiki/api-protocols/http-cookies|HTTP Cookies]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
