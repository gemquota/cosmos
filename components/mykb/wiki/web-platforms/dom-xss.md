---
type: "concept"
title: "DOM XSS"
description: "Injection sinks in client-side JavaScript instead of server HTML"
tags: ["security", "xss", "javascript", "attacks"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# DOM XSS

## Summary

DOM-based XSS occurs when untrusted data flows through JavaScript — location, postMessage, storage, DOM properties — into a sink like innerHTML, eval, or URL assignment, executing without ever touching the server. It is invisible to server-side filters.

## Details
- Mechanism: sources (location.hash, document.referrer, window.name, postMessage data, localStorage) feed sinks (innerHTML, outerHTML, insertAdjacentHTML, document.write, eval, new Function, script.src, location assignment, setTimeout with strings). A sanitizer on the server cannot see the flow because the attack payload never leaves the browser's own origin.
- Concrete example: a single-page app reading location.hash and writing it into innerHTML for a deep-link title executes <img src=x onerror=alert(1)> embedded in the hash; the payload is never in the URL sent to the server, so WAFs and server-side escaping miss it.
- Failure modes: sinks beyond innerHTML — attribute assignment (element.href from user data), javascript: URLs in links, postMessage handlers that trust event.origin, and JSON.parse followed by property access — are easy to miss in review; frameworks with dangerouslySetInnerHTML or v-html recreate the same sink.
- Operational tradeoffs: defense is layered: validate and encode at the sink (textContent, createElement, setAttribute where possible), keep a central allowlist for rich HTML, never eval strings, verify postMessage origins, and run DOM-XSS-aware scanners plus a CSP that blocks inline script as a backstop.
- RSIS3/mykb relevance: the wiki's markdown renderer would route untrusted HTML through the safe-rendering pipeline and CSP, and this node anchors the DOM-XSS checklist reviewed in loop passes.
- Browser-side detection: DOM-XSS scanners (static taint analysis in build, runtime instrumentation in dev) plus a strict CSP block the classes of sinks that code review misses; treat a CSP bypass report as a release blocker.
- Framework escape hatches: dangerouslySetInnerHTML, v-html, and template-string HTML builders re-open sinks; audit every occurrence and require a sanitizer review before merge.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/reflected-xss|Reflected XSS]]
- [[wiki/web-platforms/stored-xss|Stored XSS]]
- [[wiki/web-platforms/polyglot-xss|Polyglot XSS]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/web-apis|Web APIs]]
