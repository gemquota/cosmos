---
type: "concept"
title: "Content Security Policy"
description: "CSP headers that restrict which scripts, styles, and resources a page may load"
tags: ["security", "headers", "csp", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Content Security Policy

## Summary
Content-Security-Policy is a response header that tells the browser which origins and types of content the page may load, making XSS dramatically harder. It is one of the highest-value security headers a site can ship.

## Details
CSP is a set of directives: default-src sets the fallback policy, and script-src, style-src, img-src, frame-src, connect-src, and others set per-type rules. The browser enforces them as the page loads: a script from an origin not in script-src is blocked, an inline handler when 'unsafe-inline' is absent is blocked, and a form submission to a non-listed endpoint is blocked. A violation triggers the report-only or enforcement reporting endpoint.

The mechanism: the header is parsed into source lists, each entry an origin, scheme, or keyword ('self', 'none', 'unsafe-inline', 'unsafe-eval', nonces, hashes). Nonces and hashes allow specific inline scripts while blocking the rest. Because enforcement happens in the browser before execution, a successful XSS payload that loads an external script is dead on arrival unless the payload itself is covered by an allowed source.

Concrete example: a wiki dashboard sets script-src 'self' 'nonce-abc123'; each response embeds a fresh nonce in its inline scripts. An attacker's stored <script src="https://evil.example/x.js"> is blocked because evil.example is not allowed, and inline script injection without the correct nonce is blocked too. A strict policy like this converts most XSS from exploitable to merely present.

Failure modes: 'unsafe-inline' or 'unsafe-eval' in script-src neutralizes most of the protection; policies built by trial-and-error drift into permissive allowlists (adding https: or *); inline event handlers and javascript: URLs bypass policies without those keywords only when not blocked; and a policy that blocks legitimate CDNs or analytics breaks the page, which is why sites ship report-only first.

Operational tradeoffs: strict CSP is the strongest single XSS mitigation and can be layered with nonces for inline scripts, but it requires inventorying every resource the page loads and updating the policy with the release. The migration path: report-only mode, collect violations, tighten, then enforce. CSP also pairs with frame-ancestors (frame embedding) and object-src 'none' to shrink the attack surface further.

RSIS3/mykb relevance: the dashboard loads Tailwind and Chart.js; its CSP contract — self plus a couple of trusted CDNs, nonce for inline config — is a concrete policy RSIS3's deployment checks can assert.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/referrer-policy|Referrer Policy]]
- [[wiki/api-protocols/x-frame-options|X-Frame-Options]]
- [[wiki/api-protocols/mime-sniffing|MIME Sniffing]]
- [[wiki/security-auth/security-headers|Security Headers]]
- [[wiki/security-auth/content-security-policy|Content Security Policy]]
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]]
