---
type: "concept"
title: "Domain Cookies"
description: "Cookies scoped with Domain that travel across a domain and its subdomains"
tags: ["http", "cookies", "security", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Domain Cookies

## Summary
A cookie set with Domain=example.com is sent to example.com and every subdomain, and can be set by any subdomain. That cross-subdomain reach is convenient for shared auth and dangerous when any subdomain is less trusted than the rest.

## Details
The Domain attribute widens a cookie beyond the host that set it. A cookie set by app.example.com with Domain=example.com is sent to www.example.com, api.example.com, and user.example.com alike; it is also accepted in Set-Cookie from any of those hosts. Without the attribute, the cookie is host-only: only the setting host receives it and only that host can set it.

The mechanism: the browser matches the request host against the cookie's domain scope (public-suffix-aware: a cookie cannot be set for a public suffix like .com). The consequence of Domain=example.com is that every subdomain is inside the cookie's trust boundary: a subdomain with any XSS or cookie-setting ability can read, shadow, or overwrite the shared cookie. This is why security guidance treats a Domain-widened session cookie as "shared with every subdomain."

Concrete example: a dashboard on app.example.com sets a session cookie with Domain=example.com so the API on api.example.com can read it. A user-generated content host at user.example.com gets XSS; the attacker sets Domain=example.com; session=<forged value>, hijacking the session for the whole domain. With a host-only cookie on app.example.com, the XSS on user.example.com is out of scope entirely.

Failure modes: adding Domain=example.com for convenience silently widens the boundary and often goes unnoticed in review; public-suffix confusion (setting Domain=co.uk) causes browsers to reject the cookie, breaking sessions; and cookies with the __Host- prefix are incompatible with any Domain attribute, so mixing the two patterns creates inconsistent behavior across routes.

Operational tradeoffs: domain-wide cookies reduce friction for subdomain-based architectures — one login for app and api — but the security cost is real: the strongest subdomain determines the security of all. Alternatives: host-only cookies plus a token exchange, or a shared auth domain with dedicated auth cookies and an explicit, audited subdomain list. The default should be host-only; widen to Domain= only with a documented threat model.

RSIS3/mykb relevance: the wiki's services are single-host today, so the standing rule is host-only cookies; documenting the boundary prevents a future refactor from silently widening it.

## Related
- [[wiki/api-protocols/secure-cookies|Secure Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/path-cookies|Path Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/third-party-cookies|Third-Party Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/partitioned-cookies|Partitioned Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — related coverage in the same cluster
- [[wiki/api-protocols/csrf|CSRF]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
