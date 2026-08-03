---
type: "concept"
title: "Referrer Policy"
description: "Referrer-Policy header that controls what URL data leaves the page"
tags: ["security", "headers", "privacy", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Referrer Policy

## Summary
Referrer-Policy controls how much of the current URL is sent in the Referer header on navigations and requests. Without it, full URLs — including tokens, ids, and query parameters — leak to other origins through the Referer.

## Details
Browsers send a Referer header on navigations and subresource loads, containing the referring URL. The default behavior historically leaked the full URL, path included, to every destination. Referrer-Policy (default-referrer, no-referrer, origin, same-origin, strict-origin-when-cross-origin, unsafe-url, and others) tells the browser what to send. The modern default in browsers is strict-origin-when-cross-origin: full URL same-origin, origin only cross-origin, nothing on downgrade.

The mechanism: the policy is set via the Referrer-Policy header or a <meta name="referrer"> tag, and applies per document. The dangerous cases are URLs with sensitive query parameters (?token=..., ?id=..., ?next=...) — if the policy permits full-URL referral, every external link and image request leaks them into the destination's logs. Even without tokens, the Referer reveals browsing behavior and internal paths.

Concrete example: a wiki page at https://wiki.example/notes/42?share=abc123 links to an external site. With the default strict-origin-when-cross-origin, the external site sees Referer: https://wiki.example/ — no path, no token. With unsafe-url or an old default, it sees the full URL including share=abc123, leaking the share secret into third-party logs. Login flows that put one-time tokens in URLs are the classic casualty.

Failure modes: setting Referrer-Policy on the landing page but not on deep-linked pages; policies that still leak on same-origin (harmless) or on downgrade (https to http — should always send nothing); and Referer leaking through redirect chains even when the original page sets a policy. Also, the meta tag is ignored when the header is present, and meta tags in HTML loaded via fetch don't apply.

Operational tradeoffs: strict-origin-when-cross-origin is the right default — it preserves useful analytics (the origin) without leaking paths and tokens; no-referrer maximizes privacy but breaks referrer-based analytics and some CSRF checks that relied on it (which should be replaced anyway). The baseline: the header on every response, tokens never in URLs, and redirect handling that strips query parameters on external jumps.

RSIS3/mykb relevance: the dashboard's links and any share URLs should follow the strict-origin policy; documenting it lets RSIS3's header checks assert the policy on all responses.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/x-frame-options|X-Frame-Options]] — related coverage in the same cluster
- [[wiki/api-protocols/mime-sniffing|MIME Sniffing]] — related coverage in the same cluster
- [[wiki/api-protocols/nosniff-header|X-Content-Type-Options nosniff]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
