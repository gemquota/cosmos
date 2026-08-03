---
type: "concept"
title: "MIME Sniffing"
description: "Browser heuristics that guess content type from bytes and the nosniff fix"
tags: ["security", "http", "mime", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# MIME Sniffing

## Summary
MIME sniffing is the browser behavior of guessing a resource's type from its leading bytes when the declared Content-Type is missing or generic. The guess can upgrade text to HTML or script, enabling stored XSS; X-Content-Type-Options: nosniff disables it.

## Details
When a server sends Content-Type: text/plain or application/octet-stream — or no Content-Type at all — the browser examines the payload's bytes and infers a more specific type: a file beginning with <html or <!DOCTYPE is treated as HTML, one starting with <script as script, JPEG and PNG have magic numbers, and so on. The inference is a compatibility feature for misconfigured servers, and it is exactly what attackers abuse.

The mechanism: browsers apply per-format signatures in order (HTML, XML, images, archives). If a text/plain response contains HTML, the browser may render it as HTML; if an image response is actually HTML, it may render that too. The nosniff header (X-Content-Type-Options: nosniff) instructs the browser to trust the declared type and never upgrade, and modern browsers also use it to refuse treating a resource as script or style when the type mismatches — the header has real teeth beyond sniffing.

Concrete example: a file-sharing API serves user uploads with Content-Type: text/plain from /uploads. An attacker uploads a file whose content starts with <script>...</script>; a victim opens the URL; the browser sniffs HTML and executes the script in the origin's context — stored XSS through an "innocent" text file. With nosniff, the browser renders it as plain text, and with Content-Disposition: attachment, it never renders inline at all.

Failure modes: nosniff does not fix a server that declares the wrong type itself (text/html for user content); JSON endpoints served with HTML-friendly types can still execute; some legacy browsers ignore nosniff, so correct, explicit Content-Type remains necessary; and download endpoints that stream with the wrong type can trigger sniffing or break attachments.

Operational tradeoffs: nosniff is zero-cost and should be universal; the companion discipline is declaring accurate Content-Type on every response and serving untrusted files as attachments. The combination — correct types, nosniff, attachment disposition — closes the stored-XSS-via-upload class. Testing should include polyglot files and uppercase or BOM-prefixed signatures.

RSIS3/mykb relevance: the wiki's snapshot hosting must send nosniff and accurate types; documenting the header set gives RSIS3's deployment checks a fixed assertion.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]] — related coverage in the same cluster
- [[wiki/api-protocols/nosniff-header|X-Content-Type-Options nosniff]] — related coverage in the same cluster
- [[wiki/api-protocols/hsts-practice|HSTS in Practice]] — related coverage in the same cluster
- [[wiki/api-protocols/csp-headers|CSP Headers]] — related coverage in the same cluster
- [[wiki/security-auth/security-headers|Security Headers]] — related coverage in the same cluster
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — related coverage in the same cluster
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — related coverage in the same cluster
