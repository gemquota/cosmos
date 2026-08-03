---
type: "concept"
title: "Secure Cookies"
description: "Cookie attributes, scoping, and session protection against theft, CSRF, and cross-site abuse"
tags: ["cookies", "security", "http", "sessions", "csrf"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies", "https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html"]
---
# Secure Cookies

## Summary
Cookies are the classic browser session mechanism, and their security hinges on attributes. Secure, HttpOnly, SameSite, and Path jointly decide when a cookie is sent and whether JavaScript can read it. Modern defaults — Secure + SameSite=Lax — plus CSRF tokens cover most web apps.

## Details
- **Attribute roles** — Secure restricts to HTTPS; HttpOnly blocks JS reads (blunting XSS theft); SameSite bounds cross-site sending; Path and Domain scope delivery.
- **SameSite semantics** — Lax permits top-level GET navigations; Strict blocks cross-site entirely; None requires Secure and enables third-party contexts.
- **CSRF defense** — SameSite alone is not enough for state-changing endpoints; synchronizer tokens or double-submit cookies add intent proof.
- **Partitioning** — third-party cookies are being partitioned or blocked; embedded sessions must move to partitioned (CHIPS) or first-party storage.
- **Worked example** — mykb's session cookie would use Secure, HttpOnly, and Lax with a rotating CSRF token served to the SPA.
- **Relevance** — RSIS3's dashboard login is a cookie-based flow; the wiki records the flag matrix so hardening is auditable.

## Related
- [[wiki/api-protocols/session-invalidation|Session Invalidation]] — adjacent concept in this wiki
- [[wiki/api-protocols/cookie-flags|Cookie Flags]] — adjacent concept in this wiki
- [[wiki/api-protocols/secure-flag|Secure Cookie Flag]] — adjacent concept in this wiki
- [[wiki/api-protocols/httponly-flag|HttpOnly Cookie Flag]] — adjacent concept in this wiki
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — existing coverage
- [[wiki/identity/session-management|Session Management]] — existing coverage
- [[wiki/identity/session-hijacking|Session Hijacking]] — existing coverage
