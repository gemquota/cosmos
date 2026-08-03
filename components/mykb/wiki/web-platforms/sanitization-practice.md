---
type: "concept"
title: "Sanitization Practice"
description: "Cleaning untrusted input while preserving intended structure"
tags: ["security", "sanitization", "input", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Sanitization Practice

## Summary

Sanitization rewrites untrusted HTML into a safe subset, preserving formatting while removing executable content. Good practice uses a maintained, allowlist-based sanitizer, applies it at the last parseable moment, and treats it as one layer among several.

## Details
- Mechanism: an allowlist sanitizer (DOMPurify, sanitize-html) parses input into a DOM, walks the tree, removes disallowed tags/attributes and dangerous URL schemes, and serializes the clean result. It differs from escaping (which changes how text renders) — sanitization keeps formatting but deletes risk.
- Concrete example: a comment box accepting basic HTML strips <script>, event attributes (onclick), and javascript: hrefs but keeps <b>, <a>, <code>; a markdown renderer sanitizes its output so users cannot smuggle raw HTML through. A CSP that blocks inline script would catch what slips through.
- Failure modes: regex-based or hand-rolled sanitizers missing edge cases; blacklist approaches (strip script only) beaten by mXSS and obfuscation; sanitizing too early (before other transforms re-introduce markup) or too late (after insertion into a dangerous context); and stale sanitizer versions missing published bypass fixes.
- Operational tradeoffs: sanitization alone cannot guarantee safety — pair with context-aware escaping, CSP, and the principle of never trusting sanitized output across a new context boundary; update the sanitizer as a security dependency and run its known-bypass corpus in CI.
- RSIS3/mykb relevance: the wiki's sanitizer configuration (allowed tags/attributes/schemes) is documented here and would be reviewed whenever a new rich-text feature is enabled.
- Context inventory: document every sink that receives sanitized output (innerHTML, attribute assignment, URL navigation) so a sanitizer change cannot silently reach an unsafe context.
- Policy review: the allowed tag/attribute set is a policy decision — review additions with security and product together, and prefer dropping features over broadening the allowlist.
- Input vs output: sanitize rich text at render time, not just at input; data written before a sanitizer fix remains dangerous until it is re-processed on the way out.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/output-encoding|Output Encoding]]
- [[wiki/web-platforms/safe-html-rendering|Safe HTML Rendering]]
- [[wiki/web-platforms/template-escaping|Template Escaping]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
