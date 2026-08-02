---
type: "concept"
title: "HTTP Cookies"
description: "Cookie attributes, scoping, SameSite, and API usage"
tags: ["http", "cookies", "session-management", "security", "web-platforms"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc6265", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies"]
---

# HTTP Cookies

## Summary
Cookies are small name-value pairs that a server sets with Set-Cookie and the browser returns on later requests, giving HTTP a stateful session layer over a stateless protocol. RFC 6265 defines their syntax and scoping, while SameSite and Secure attributes have tightened their security behavior in modern browsers.

## Details
- A Set-Cookie response sets attributes: Domain, Path, Max-Age or Expires, Secure, HttpOnly, and SameSite; the Cookie request header echoes matching pairs back.
- Scoping: a cookie is sent only to hosts that match Domain and URL paths under Path, which keeps sibling services from leaking state.
- SameSite=Strict, Lax, or None controls cross-site sending; Lax (the modern default) blocks cookies on cross-site subrequests but allows top-level GET navigation, mitigating CSRF.
- HttpOnly keeps the cookie out of document.cookie, blocking XSS payloads from reading session tokens; Secure forces transmission only over HTTPS.
- For APIs, cookies work well for browser-based sessions but poorly for mobile or service clients, which prefer Authorization headers and token storage.
- Partitioned cookies (CHIPS) give embedded iframes their own cookie jar, and the __Host- and __Secure- prefixes add name-based protections.

## Related
- [[wiki/api-protocols/csrf|CSRF]] — SameSite and cookie scoping are primary CSRF defenses
- [[wiki/security-auth/token-authentication|Token Authentication]] — header-based tokens replace cookies for API clients
- [[wiki/api-protocols/http-headers|HTTP Headers]] — Set-Cookie and Cookie are specialized header pairs
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — cookie scoping is rooted in origin semantics
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — authorization codes avoid exposing tokens to browser scripts
