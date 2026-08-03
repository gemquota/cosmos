---
type: "concept"
title: "Cookie Scoping"
description: "Domain, Path, Secure, and SameSite attributes that bound cookie reach"
tags: ["http", "cookies", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cookie Scoping

## Summary
Cookie scoping — Domain, Path, Secure, and SameSite — decides which requests carry a cookie and which sites can set or read it. Correct scoping is the difference between a session and a credential leak.

## Details
A cookie's scope is defined by its attributes: Domain (which hosts receive it), Path (which URL prefixes), Secure (HTTPS only), and SameSite (cross-site behavior). The browser sends the cookie only on requests matching all the scoping attributes and the cookie's host-only rule, and honors Set-Cookie only from hosts that match the Domain scope.

The mechanism: without a Domain attribute the cookie is host-only — sent only to the exact host that set it. With Domain=example.com it is sent to example.com and all subdomains, and can be set by any subdomain (a subdomain can issue cookies for its parent domain, which is both a feature and an attack surface). Path scoping is advisory to the browser only and provides no security boundary — any same-host script or redirect can still reach cookies by crafting URLs under the path. Secure restricts to HTTPS; SameSite restricts cross-site sends.

Concrete example: a dashboard at app.example.com sets session with no Domain and Path=/ — the cookie never leaves app.example.com, so a compromised user.example.com can't read or shadow it. If someone later adds Domain=example.com for convenience, every subdomain, including attacker-controlled ones, can now both receive and overwrite the session cookie — a silent widening of the trust boundary.

Failure modes: Domain=example.com on a multi-tenant host exposes cookies to every tenant; Path=/admin does not protect cookies from an XSS on /admin/../other; omitting Secure lets an HTTPS-set cookie be re-set or intercepted over HTTP; and SameSite=None plus Secure cookies are sent to every cross-site context, including attacker iframes, which turns any CSRF-able endpoint into a cookie-bearing target.

Operational tradeoffs: the narrowest scope (host-only, Path=/, Secure, SameSite=Lax, __Host- prefix) is the security baseline but breaks legitimate subdomain sharing; sharing cookies across subdomains is sometimes needed — auth on one subdomain, API on another — and then should use a dedicated auth cookie with Domain set explicitly and a documented list of subdomains. The rule: widen scope deliberately and only as far as the threat model allows.

RSIS3/mykb relevance: the wiki's auth boundary is a single host, so the standing rule is host-only cookies; documenting the scope contract prevents future "convenience" widening during refactors.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/domain-cookies|Domain Cookies]]
- [[wiki/api-protocols/path-cookies|Path Cookies]]
- [[wiki/api-protocols/third-party-cookies|Third-Party Cookies]]
- [[wiki/api-protocols/http-cookies|HTTP Cookies]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
