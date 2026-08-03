---
type: "concept"
title: "Safe HTML Rendering"
description: "Rendering user content as text or through hardened HTML pipelines"
tags: ["security", "html", "xss", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Safe HTML Rendering

## Summary

Safe HTML rendering turns untrusted content into displayable HTML without executing scripts: parse, sanitize, escape, then insert as nodes. It is the composite of the wiki's rendering pipeline and the defense-in-depth story for user-generated content.

## Details
- Mechanism: the pipeline is strict: (1) parse markdown to a token tree, (2) render to HTML with every text node escaped and attribute values encoded, (3) sanitize the result by parsing into a DOM and dropping disallowed tags/attributes/URL schemes, (4) insert via node APIs (appendChild) rather than innerHTML so no re-parsing can resurrect payloads. A strict CSP is the final backstop.
- Concrete example: a wiki note containing <script>alert(1)</script> renders as literal text because the markdown renderer escapes it; a note containing [link](javascript:alert(1)) gets its href dropped by the scheme allowlist; an img with onerror is stripped during sanitization.
- Failure modes: sanitizing to a string and re-inserting with innerHTML (mutation re-parse risk); allowlists missing event attributes or URI schemes (data:, javascript:); sanitizer and browser parser disagreements (mXSS); and HTML in attribute contexts, JSON in script contexts, or URLs in CSS needing their own encodings.
- Operational tradeoffs: the pipeline adds complexity but converts rich-text features (tables, code blocks, images) into a safe default; keep the sanitizer updated and its test fixtures versioned, and never bypass the pipeline with "trusted" flags without review.
- RSIS3/mykb relevance: the wiki browser's renderer is this pipeline; safe-rendering rules are the first item on the loop's security checklist when new note types are added.
- Test fixtures: keep a corpus of known payloads (script tags, event handlers, javascript: URLs, mXSS vectors) and run it through the pipeline in CI after every sanitizer or renderer change.
- Schema-level defense: prefer explicit node construction (createElement, textContent) over string HTML in the renderer; the fewer string-to-DOM paths exist, the fewer mutation surfaces there are.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/template-escaping|Template Escaping]]
- [[wiki/web-platforms/allowlist-validation|Allowlist Validation]]
- [[wiki/web-platforms/denylist-validation|Denylist Validation]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
