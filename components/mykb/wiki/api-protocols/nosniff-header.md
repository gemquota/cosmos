---
type: "concept"
title: "X-Content-Type-Options nosniff"
description: "The header that stops browsers from MIME-sniffing responses"
tags: ["security", "headers", "http", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# X-Content-Type-Options nosniff

## Summary
X-Content-Type-Options: nosniff tells browsers to trust the declared Content-Type and never MIME-sniff a response. It is the cheapest and most effective fix for the stored-XSS-through-upload class of bugs.

## Details
When a response's Content-Type is missing, generic (text/plain), or octet-stream, browsers historically inspect the bytes and may upgrade to a more dangerous type — text to HTML, image to script. X-Content-Type-Options: nosniff disables that inference: the browser must use the declared type. Modern browsers additionally use the header to refuse loading a resource as a script or stylesheet when its declared type doesn't match, which makes the header meaningful beyond sniffing.

The mechanism: the header is a simple response header (X-Content-Type-Options: nosniff) with a single value. It applies per response; setting it centrally on all responses is the norm. When present, a text/plain response containing <script> renders as text, not HTML, and a resource declared image/png is not executed as a script even if its bytes look like one. The header composes with correct Content-Type declarations and Content-Disposition: attachment for untrusted files.

Concrete example: a wiki hosts user-uploaded files at /uploads with Content-Type: text/plain and sends nosniff. An attacker uploads a polyglot file starting with <script>; a victim's browser renders it as plain text instead of executing it — the stored-XSS chain is broken at the render step. Without nosniff, the same bytes execute in the origin's context, and the wiki is compromised.

Failure modes: nosniff is ignored by a few legacy browsers, so it must pair with correct, explicit Content-Type; a server that itself declares text/html for user content is still vulnerable (nosniff trusts the declaration); and applying nosniff to cross-origin resources without fixing their types can break legitimate embeds, which surfaces as a compatibility issue, not a security one.

Operational tradeoffs: the header costs nothing, has no meaningful downside for normal sites, and should be on every response — HTML pages, JSON, assets, and error pages alike. The companion practices: accurate Content-Type everywhere, attachments for untrusted files, and CSP as a second layer. Security checkers (headers.dev-style tools) flag its absence precisely because it is so cheap.

RSIS3/mykb relevance: the dashboard and wiki hosting should send nosniff on all responses; documenting the header as a standing assertion lets RSIS3's deployment checks fail the build when it's missing.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/csp-headers|CSP Headers]] — related coverage in the same cluster
- [[wiki/api-protocols/referrer-policy|Referrer Policy]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
