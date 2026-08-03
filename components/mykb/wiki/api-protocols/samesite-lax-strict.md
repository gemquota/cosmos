---
type: "concept"
title: "SameSite Lax vs Strict"
description: "Cookie scoping that limits cross-site request sending"
tags: ["cookies", "http", "security", "csrf"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# SameSite Lax vs Strict

## Summary
The SameSite attribute tells the browser when a cookie may accompany cross-site requests. Lax permits cookies on top-level navigations such as link clicks, Strict blocks them on all cross-site requests, and browsers treat cookies without the attribute as Lax by default. Choosing between them is a direct tradeoff between CSRF resistance and cross-site usability.

## Details
- Mechanism: SameSite values are computed from the site (scheme plus registrable domain), not the origin, so `app.example.com` and `api.example.com` are the same site while `example.com` and `evil.example.net` differ. Lax allows the cookie on same-site requests and on top-level navigations with safe methods (GET, HEAD, OPTIONS), which covers normal link-following and address-bar entry. Strict allows the cookie only on same-site requests, so any request whose site differs arrives without it, including top-level GET navigations from other sites.
- Concrete examples: a banking app using Lax keeps sessions working when users click a link from email or a search engine, while still blocking the POST-based CSRF attacks that classic forged forms rely on. Strict protects a session even against top-level GET-based state changes, but breaks the common flow where a user clicks a link to your app from a partner site and appears logged out; the fix is often a redirect through the login origin so the next request is same-site.
- Failure modes: the biggest failure is treating SameSite as a complete CSRF defense: a Lax cookie still rides along on top-level GETs, so any state-changing GET endpoint (logout links, cache-busting URLs) remains exploitable, and same-site subdomains are out of scope entirely. Strict causes confusing "logged out" experiences on embedded widgets and third-party integrations because every cross-site entry lands cold; teams then silently downgrade to None without `Secure`, recreating the cross-site cookie leak the attribute was meant to stop.
- Operational tradeoffs: Lax is the right default for most session cookies because it preserves navigation flows while neutralizing the highest-volume CSRF vector; Strict fits high-security contexts (financial, admin consoles) where the usability cost of cross-site cold starts is acceptable. For embedded widgets that genuinely need cross-site cookies, use `SameSite=None; Secure` and pair it with CSRF tokens, frame-ancestor restrictions, and scope checks, because None is the least safe setting.
- RSIS3/mykb relevance: the SameSite decision parallels memory-layer trust boundaries: treat cookies like session state in MyKB's daemon, scope them tightly, and never rely on a single header for authorization — defense in depth (SameSite plus tokens plus origin checks) mirrors how RSIS3 gates cross-loop writes.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-prefixes|Cookie Prefixes]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-scoping|Cookie Scoping]] — related coverage in the same cluster
- [[wiki/api-protocols/domain-cookies|Domain Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
