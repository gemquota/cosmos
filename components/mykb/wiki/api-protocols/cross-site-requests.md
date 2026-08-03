---
type: "concept"
title: "Cross-Site Requests"
description: "How browsers send requests across origins and what CSRF defenses must cover"
tags: ["security", "http", "csrf", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cross-Site Requests

## Summary
Cross-site requests are requests a browser sends to one origin from a page on another origin. The browser sends many of them automatically — cookies included — which is exactly what CSRF attacks exploit and what SameSite, CSRF tokens, and CORS are designed to control.

## Details
When a page at evil.example triggers a request to bank.example (a form submit, an img src, a fetch), the browser sends it with the target's cookies when the cookie scope allows. The classic CSRF primitive is a cross-site POST: the attacker's form submits to a state-changing endpoint, and the victim's session cookie rides along, so the request is authenticated. The server cannot distinguish it from a legitimate click without additional signals.

The mechanism: browsers attach cookies to cross-site requests according to SameSite and the cookie's Secure and Domain attributes; they attach Origin and Sec-Fetch-Site headers that reveal the request's true context. CORS governs whether the response is readable, but it does not stop the request from being sent — so a cross-site GET with side effects or a cross-site form POST is still delivered even when the browser blocks the response. This asymmetry is why CSRF defense must be server-side.

Concrete example: an attacker page contains <form action="https://bank.example/transfer" method="POST"><input name="to" value="attacker"><input name="amount" value="1000"></form> and auto-submits it. The victim's bank session cookie (SameSite=None or old default) is attached, and the transfer executes. With SameSite=Lax on the session cookie, the cross-site POST is not sent — the cookie stays home — and with a CSRF token, even SameSite=None cookies can't forge the required token.

Failure modes: relying on CORS to stop cross-site requests is the classic mistake — CORS only stops reads; relying on the Referer header is fragile because referrer-policy and privacy tools strip it; and SameSite=None sessions, login CSRF, and top-level navigation CSRF (link clicks that trigger actions) remain even with Lax. Server-side CSRF tokens or custom headers are the reliable layer.

Operational tradeoffs: SameSite=Lax is the cheap baseline that kills most CSRF while preserving link-in navigation; CSRF tokens (synchronizer or double-submit) add complexity but are the defense when cookies must be sent cross-site or when strict SameSite breaks flows; Sec-Fetch-Site checks add a signal but are bypassed by some legacy browsers. The robust stack is SameSite=Lax plus token validation on all state-changing endpoints.

RSIS3/mykb relevance: any wiki automation that POSTs with cookies must understand this asymmetry; documenting the "CORS stops reads, SameSite/tokens stop writes" rule keeps RSIS3's web-automation security notes consistent.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/cookie-flags|Cookie Flags]] — related coverage in the same cluster
- [[wiki/api-protocols/secure-flag|Secure Cookie Flag]] — related coverage in the same cluster
- [[wiki/api-protocols/httponly-flag|HttpOnly Cookie Flag]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
