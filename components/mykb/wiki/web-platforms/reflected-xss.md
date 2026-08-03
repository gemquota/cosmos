---
type: "concept"
title: "Reflected XSS"
description: "Injection echoed back in a single response without storage"
tags: ["security", "xss", "attacks", "http"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Reflected XSS

## Summary

Reflected XSS occurs when an application echoes request input — URL parameters, headers, search terms — into a response without safe encoding, letting an attacker craft a link that executes script in the victim's session. It is the classic XSS and the one server-side templates must prevent.

## Details
- Mechanism: the attack is reflected: attacker sends victim a URL containing a payload; the server includes that payload in the HTML response; the browser parses it as code. It differs from stored XSS (persisted on the server) and DOM XSS (never touches the server response).
- Concrete example: a search page rendering q={{ query }} unsafely executes <script>fetch('/api/keys')...</script> when the crafted URL is opened; the payload rides the same session cookies, so it can read the victim's data and exfiltrate it to the attacker's origin.
- Failure modes: escaping only some contexts (attribute values but not script contexts); frameworks' auto-escaping disabled for "rich" fields; reflected values in redirects (open redirect plus script via javascript:); and the payload surviving sanitization but breaking out through nesting (HTML in a JS string inside an attribute).
- Operational tradeoffs: prevention is output encoding at every reflection point — HTML-escape text, attribute-encode attributes, URL-encode and scheme-check URLs, JSON-escape script data — plus CSP and HttpOnly cookies as backstops; testing should include a fuzzed payload corpus of multi-context reflections.
- RSIS3/mykb relevance: the wiki server template-escapes every reflected value; this node anchors the encoding checklist and the regression fixtures the loop runs after template changes.
- CSP backstop: a strict script-src CSP converts a missed reflection into a blocked load instead of an infection; it is not a substitute for encoding but it bounds the damage of encoding mistakes.
- Review gate: any new reflection of request input into a response triggers a security review; grep-able templates make the audit cheap and the habit durable.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/stored-xss|Stored XSS]]
- [[wiki/web-platforms/polyglot-xss|Polyglot XSS]]
- [[wiki/web-platforms/mutation-xss|Mutation XSS]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/web-apis|Web APIs]]
