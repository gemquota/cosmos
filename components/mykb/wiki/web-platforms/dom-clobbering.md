---
type: "concept"
title: "DOM Clobbering"
description: "HTML attributes shadowing DOM globals to confuse scripts"
tags: ["security", "xss", "dom", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DOM Clobbering

## Summary

DOM clobbering is an attack where HTML elements with id/name collide with global JavaScript references or built-in DOM APIs, letting injected markup hijack code that trusted the DOM namespace. It is a client-side XSS cousin that sanitizers often miss.

## Details
- Mechanism: elements with id="foo" become window.foo; forms and named inputs create nested properties (form.foo.input); certain ids shadow prototype properties (e.g. an element id="toString" or name="location") so code reading window.location or element properties gets an element instead. Libraries that do var x = document.something or walk forms by name are the usual victims.
- Concrete example: a comment system renders user-controlled HTML where <img id="onerror" name="attributes"> can replace references the script expects; classic payloads use <a id="defaultView"> or <form><input name=body> to clobber window properties that a sanitizer's own logic reads, turning sanitization into exploitation.
- Failure modes: sanitizers that strip script but keep id/name attributes; code reading global names without hasOwnProperty or typeof guards; frameworks copying DOM properties into options objects; and clobbering via the HTMLCollection of form controls, which stringifies differently.
- Operational tradeoffs: defenses include using const/let shadows? No — the fix is not using undeclared globals: read via window["name"] after checking typeof, use symbols or Map for name storage, and strip id/name from untrusted markup. Server-side templating must also avoid building globals from user input.
- RSIS3/mykb relevance: the wiki viewer renders markdown to HTML; its sanitizer strips id/name attributes on untrusted elements, and this note feeds the safe-rendering checklist used by the acquisition pipeline.
- Defense in depth: freeze critical globals, use Object.create(null) for name maps, and strip id/name from untrusted markup at the sanitizer; each layer covers the failure mode the others miss.
- Framework note: DOM clobbering also hits frameworks that read named form elements; audit any code that does document.forms or window[name] access and route it through safe lookups.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/prototype-pollution-web|Prototype Pollution on the Web]]
- [[wiki/web-platforms/xs-leaks|XS-Leaks]]
- [[wiki/web-platforms/dom-clobbering|DOM Clobbering]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
