---
type: "concept"
title: "Output Encoding"
description: "Encoding dynamic values for the context they are emitted into"
tags: ["security", "encoding", "xss", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Output Encoding

## Summary

Output encoding transforms data into the safe form for its context — HTML entities in markup, percent-encoding in URLs, JSON escaping in scripts — so untrusted input cannot become code. It is the flip side of input validation and is context-specific.

## Details
- Mechanism: each context has its own escaping rules: HTML text needs & < > " ' encoded; attributes need the same plus context-specific handling; URLs need percent-encoding with scheme allowlisting (javascript: is the classic escape); script contexts need JSON escaping plus no </script sequence; CSS and XML have their own rules.
- Concrete example: a username rendered as <div>Hello <b>${name}</b></div> becomes safe only when name is HTML-escaped — <script> in the input renders as text. Building a URL with user input requires encodeURIComponent per segment plus a scheme check, because encodeURIComponent alone does not stop javascript: URLs.
- Failure modes: encoding for the wrong context (HTML-escaping inside a JS string still allows injection through </script>); double-encoding that displays &amp;lt; to users; encoding only at some layers while a framework re-interprets the string; and skipping encoding because "the input was sanitized" — sanitization and encoding are complements, not substitutes.
- Operational tradeoffs: encode at the output boundary for every dynamic value, using framework-native auto-escaping where available (React, Vue) and explicit helpers elsewhere; keep a context-type list (HTML text, attribute, URL, JS, CSS) and a lint rule that flags raw interpolations.
- RSIS3/mykb relevance: the wiki renderer HTML-escapes all text nodes and attribute values at the boundary; this node anchors the encoding checklist reviewed during loop passes.
- Layering: encode at the boundary for every context and keep the original data intact; encoding is lossless and reversible, so it belongs at output, never as a data-mangling transform.
- Never-encode-twice rule: track which values are already encoded and encode once at the boundary; double-encoding is the other common rendering bug.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/safe-html-rendering|Safe HTML Rendering]]
- [[wiki/web-platforms/template-escaping|Template Escaping]]
- [[wiki/web-platforms/allowlist-validation|Allowlist Validation]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
