---
type: "concept"
title: "HSTS in Practice"
description: "Strict-Transport-Security header that forces HTTPS and blocks downgrade"
tags: ["security", "https", "headers", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# HSTS in Practice

## Summary
HTTP Strict Transport Security (HSTS) tells browsers to use HTTPS only for a domain for a stated period, blocking protocol-downgrade and cookie-hijacking attacks like sslstrip. It is a one-header policy with operational requirements: HTTPS must already work, and the max-age must be raised carefully.

## Details
The Strict-Transport-Security header (Strict-Transport-Security: max-age=31536000; includeSubDomains; preload) instructs the browser to remember that the domain must be contacted only over HTTPS for max-age seconds. Once cached, plain-HTTP requests are rewritten to HTTPS before being sent, and certificate errors become hard failures instead of click-through warnings. The header is only honored when the response itself arrived over HTTPS.

The mechanism: the browser stores the HSTS policy per host (and subdomains if includeSubDomains is set). The preload directive is a separate submission to browser-maintained lists that ship the policy even before first visit — closing the initial-request gap. HSTS does not protect the very first request if the user types http:// or the site has no preload entry, which is why preloading and redirect-only HTTPS are complementary.

Concrete example: a wiki site enables HSTS with max-age=31536000 and includeSubDomains. An attacker on the same Wi-Fi runs sslstrip, intercepting an http://wiki.example request and downgrading it; the browser, remembering the policy, refuses to send plain HTTP and upgrades to HTTPS itself — the attack fails. Without HSTS, the first request can be downgraded and the login cookie harvested.

Failure modes: enabling HSTS on a site where some subdomains still serve HTTP bricks those subdomains in returning browsers (includeSubDomains is dangerous until everything is HTTPS); a long max-age cannot be quickly undone if a certificate breaks — clients keep hard-failing until expiry; and a header served over HTTP is ignored, so misconfigured CDNs that serve mixed content give false confidence.

Operational tradeoffs: the safe rollout is incremental: serve HTTPS everywhere first, ship HSTS with a short max-age (hours to days), monitor, then raise to months and add includeSubDomains, then submit for preload. HSTS plus Secure cookies and CSP upgrade-insecure-requests makes the HTTPS boundary load-bearing. The cost is operational discipline: certificate expiry or mixed content becomes an outage, not a warning.

RSIS3/mykb relevance: the deployed dashboards run behind GitHub Pages which already forces HTTPS; documenting the HSTS policy (and its max-age rollout) gives RSIS3's deployment checks a concrete header assertion.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/csp-headers|CSP Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/referrer-policy|Referrer Policy]] — related coverage in the same cluster
- [[wiki/api-protocols/x-frame-options|X-Frame-Options]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
