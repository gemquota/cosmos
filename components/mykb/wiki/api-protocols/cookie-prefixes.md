---
type: "concept"
title: "Cookie Prefixes"
description: "__Host- and __Secure- name prefixes enforced by the browser"
tags: ["http", "cookies", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Cookie Prefixes

## Summary
The __Host- and __Secure- cookie prefixes make the browser enforce cookie security properties that flags alone cannot, preventing domain- and scheme-scoped cookie confusion attacks.

## Details
A cookie named __Secure- is only accepted by the browser if it was set with the Secure flag; __Host- is stricter — it additionally requires Secure, no Domain attribute (host-only), and Path=/ . These are not flags the server sets but name-based contracts the browser enforces, so a compromised or confused Set-Cookie path cannot downgrade them.

The mechanism: without prefixes, a Set-Cookie for name=value; Domain=example.com; Secure can be re-issued from any subdomain or via a path override, and a session cookie scoped to a subdomain can be shadowed or clobbered by an attacker-controlled subdomain that can set cookies for the parent domain. __Host- prevents this by construction: the browser refuses any Set-Cookie with that prefix unless it is Secure, host-only, and path-rooted, so the cookie can only be set by the exact host serving the response.

Concrete example: a wiki runs app.example.com and lets users host content on user.example.com. Without prefixes, a user page could set a Domain=example.com cookie named session and shadow the real session (session-fixation-adjacent confusion). With __Host-session, the Set-Cookie from user.example.com is rejected because the prefix demands host-only binding to user.example.com — the app's session is unreachable.

Failure modes: using the prefix with any Domain attribute causes the browser to drop the cookie entirely (silent logout at worst); behind CDNs and proxies that rewrite Host, a __Host- cookie may not be set, breaking sessions; and prefixes protect the name, not the value — a leaked value is still usable. Libraries and frameworks must also not strip or mutate cookie names that begin with __.

Operational tradeoffs: __Host- is the strongest, safest choice for session and auth cookies and costs nothing when the cookie is genuinely host-only and path-rooted; __Secure- is a lighter-weight option when Domain or Path scope is required. The tradeoff is strictness versus flexibility — prefix-enforced cookies can't be shared across subdomains, which is usually exactly what you want for security.

RSIS3/mykb relevance: prefixing session cookies is a concrete, checkable rule for the dashboard; encoding it here means RSIS3 security reviews can assert cookie names rather than debate flag settings.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]]
- [[wiki/api-protocols/cookie-scoping|Cookie Scoping]]
- [[wiki/api-protocols/domain-cookies|Domain Cookies]]
- [[wiki/api-protocols/path-cookies|Path Cookies]]
- [[wiki/api-protocols/http-cookies|HTTP Cookies]]
- [[wiki/api-protocols/csrf|CSRF]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
