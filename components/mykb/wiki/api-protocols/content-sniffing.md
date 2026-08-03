---
type: "concept"
title: "Content Sniffing"
description: "Browser MIME sniffing and the X-Content-Type-Options defense"
tags: ["security", "http", "headers", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Content Sniffing

## Summary
Content sniffing lets browsers guess a response's MIME type from its bytes when the declared type is missing or ambiguous. Guessing wrong turns text into executable content; X-Content-Type-Options: nosniff stops it.

## Details
When a response lacks a Content-Type or declares a generic one (text/plain, application/octet-stream), browsers historically sniff the bytes to decide how to render it — and sometimes upgrade to a more dangerous type. The classic failure is a user-uploaded file served as text/plain that the browser sniffs as text/html and executes, enabling stored XSS from an "image" or "plain text" file.

The mechanism: browsers apply type-sniffing heuristics: HTML starts with <html or <!DOCTYPE, XML with <?xml, JPEG with 0xFFD8, and so on. When a plausible script or HTML signature appears, the browser may override the declared type. X-Content-Type-Options: nosniff instructs the browser to trust the declared Content-Type and never sniff, and modern browsers additionally refuse to treat nosniff'd resources as scripts or styles when the type doesn't match.

Concrete example: a forum allows text attachments served from /uploads at a path like /uploads/avatar.txt with Content-Type: text/plain. An attacker uploads a file containing <script>alert(document.cookie)</script> and gets victims to open it. Without nosniff, an old browser sniffs HTML and executes the script; with X-Content-Type-Options: nosniff, the browser renders it as plain text. The defense-in-depth pair is nosniff plus Content-Disposition: attachment for untrusted uploads.

Failure modes: nosniff alone doesn't fix missing or wrong Content-Type — a server that declares text/html for user content is still XSS-able; JSON endpoints hit with text/html accept types and served as HTML can execute; and some legacy browsers ignore nosniff, so serving untrusted bytes with the correct, explicit type remains necessary. Sniffing also breaks on download endpoints that stream with the wrong type.

Operational tradeoffs: nosniff is a one-line, zero-cost header with broad modern support and should be on every response; it breaks the rare legit case of content-type-less downloads, which should instead declare application/octet-stream explicitly. Combined with correct Content-Type at every endpoint and Content-Disposition for attachments, it closes a whole class of stored-XSS and mime-confusion bugs.

RSIS3/mykb relevance: the wiki would host generated HTML snapshots; ensuring the static host sends nosniff plus correct types is a standing check in the deployment practice.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/api-protocols/template-injection|Template Injection]]
- [[wiki/api-protocols/sql-injection-practice|SQL Injection]]
- [[wiki/api-protocols/xml-injection|XML Injection]]
- [[wiki/security-auth/sql-injection-prevention|SQL Injection Prevention]]
- [[wiki/security-auth/command-injection|Command Injection]]
- [[wiki/security-auth/ldap-injection|LDAP Injection]]
