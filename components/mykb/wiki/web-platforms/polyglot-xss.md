---
type: "concept"
title: "Polyglot XSS"
description: "Payloads valid in multiple contexts to defeat filters"
tags: ["security", "xss", "attacks", "payloads"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Polyglot XSS

## Summary

Polyglot XSS crafts a single payload that works in multiple parsing contexts — HTML, URL, JavaScript, CSS — exploiting ambiguous encodings and parser differentials to slip past filters that check only one interpretation.

## Details
- Mechanism: a payload that is harmless-looking HTML but executable in another context (e.g. an attribute value that also terminates a script, or a CSS url() that injects a javascript: fetch); combined encodings (HTML entity inside a URL inside JS) let a filter see one form while the parser executes another.
- Concrete example: "\x3cscript\x3e" inside a JS string where the HTML parser re-enters; "javascript&#58;alert(1)" in an href where the filter decodes entities but the browser's URL parser does not; and UTF-7/overlong-encoding payloads that older parsers misread — each bypasses a single-context check.
- Failure modes: validating per-context with the wrong decoder; assuming one sanitization pass covers nested contexts (it must be applied per context, outermost to innermost); regex filters that see one encoding; and differential parsers between the filter, the DOM, and URL/JS engines.
- Operational tradeoffs: defense requires context-aware encoding at every boundary plus a strict CSP that blocks script execution even if a payload slips through; treat polyglot payloads as a permanent test fixture in your XSS corpus and fuzz the sanitizer against them.
- RSIS3/mykb relevance: the wiki's safe-rendering pipeline would keep polyglot fixtures in its regression suite, so sanitizer updates cannot silently regress multi-context handling.
- Parser differentials: keep the sanitizer on the same engine as the consumer — a Node-side HTML parser that disagrees with the browser is itself a polyglot risk, so re-parse client-side or use the DOM as the sanitizer.
- Test corpus: maintain polyglot fixtures (nested contexts, entity+URL+JS combos) and run them through every sanitizer upgrade in CI.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/mutation-xss|Mutation XSS]]
- [[wiki/web-platforms/dom-xss|DOM XSS]]
- [[wiki/web-platforms/reflected-xss|Reflected XSS]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/web-apis|Web APIs]]
