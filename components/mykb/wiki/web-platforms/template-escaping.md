---
type: "concept"
title: "Template Escaping"
description: "Auto-escaping values inside templating engines"
tags: ["security", "templates", "xss", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Template Escaping

## Summary

Template escaping is output encoding applied by the template layer: every interpolated value is escaped for its context (HTML text, attribute, URL, script, style) automatically. It is the primary XSS defense in server-rendered apps when used consistently.

## Details
- Mechanism: templating engines (Jinja2 autoescape, EJS <%= %>, Handlebars {{ }}, Vue/React interpolation) escape text by default; attribute, URL, and script contexts need context-aware escaping or dedicated helpers because HTML-escaping alone is insufficient there. The engine escapes at the output boundary, leaving data untouched.
- Concrete example: {{ user.name }} in Jinja2 renders <script> as &lt;script&gt; text; an href built as href="{{ url }}" still needs a URL/scheme filter because HTML-escaping does not stop javascript: URLs; a JS context like <script>var x = {{ data }};</script> needs JSON-escaped output or the </script> sequence terminates the script.
- Failure modes: disabling autoescape for "trusted" fields that later receive user data; using HTML-escaped values in JS/URL/CSS contexts; double-escaping (displaying &amp;lt; to users) when a value was already escaped upstream; and template injections via custom helpers that bypass the escaping layer.
- Operational tradeoffs: autoescaping is nearly free and defaults-on in modern engines; the remaining burden is auditing non-default contexts and helpers. Keep a context inventory per template and prefer structured output (JSON endpoints, DOM APIs) over building HTML strings.
- RSIS3/mykb relevance: the wiki's server templates would escape by default with an audited helper set; this node is the checklist the loop runs before adding new template surfaces.
- Context inventory: maintain a checklist of every template context — HTML text, attribute, URL, script, style — and the escape helper used for each; a value that was safe in one context is not automatically safe in another.
- Tooling: run a static scan for raw interpolations into HTML strings and for helpers that bypass autoescape; the scan catches the contexts developers forget, and it is cheap to run in CI.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/allowlist-validation|Allowlist Validation]]
- [[wiki/web-platforms/denylist-validation|Denylist Validation]]
- [[wiki/web-platforms/input-normalization|Input Normalization]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
