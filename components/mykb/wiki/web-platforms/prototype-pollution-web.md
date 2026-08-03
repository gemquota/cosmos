---
type: "concept"
title: "Prototype Pollution on the Web"
description: "Mutating Object.prototype via merge operations to alter app behavior"
tags: ["security", "javascript", "attacks", "objects"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Prototype Pollution on the Web

## Summary

Prototype pollution lets an attacker add or modify properties on Object.prototype (or other prototypes) through unsafe merge/assign logic, corrupting every object in the page and enabling XSS or logic bypasses. It is a JS-specific injection class.

## Details
- Mechanism: operations that recursively merge user-controlled objects — JSON.parse then Object.assign({}, userInput), lodash.merge with __proto__/constructor.prototype keys, query-string parsers with dot/bracket syntax — can set Object.prototype.polluted = value; code reading obj.polluted then finds the polluted value everywhere, including security checks.
- Concrete example: a config loader merging user JSON with defaults via lodash.merge lets {"__proto__": {"isAdmin": true}} set a prototype property that a later authorization check reads from a fresh object — privilege escalation without touching stored data. Browser extensions and SSR pipelines are common targets.
- Failure modes: sanitizing top-level keys but recursing into nested objects where __proto__/constructor.prototype live; frameworks cloning with unsafe merge paths; prototype writes surviving into serialization (JSON.stringify drops them, hiding the issue until runtime); and pollution via URL parameters in older query parsers.
- Operational tradeoffs: defense is structural: never merge untrusted data (use Object.assign with Object.create(null) targets, structuredClone, or explicit key allowlists), freeze prototypes in high-security contexts, and CSP/SSR sandboxes as backstops. Audit dependency chains for unsafe merge libraries.
- RSIS3/mykb relevance: the wiki ingestion JSON pipeline whitelists schema keys and rejects __proto__/constructor keys, a rule this note anchors for all JSON parsing in loop tooling.
- Runtime defense: Object.freeze(Object.prototype) or a Proxy guard is a blunt but effective backstop in high-security contexts; combine with CSP and code review of merge sites.
- Detection: log and reject __proto__, constructor, and prototype keys during parsing, and add a fuzz test that feeds nested pollution payloads to every merge/parse path.
- Dependency audit: scan transitive dependencies for unsafe merge patterns; the vulnerability often lives in a tiny utility a framework pulls in, not in your own code.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/xs-leaks|XS-Leaks]]
- [[wiki/web-platforms/dom-clobbering|DOM Clobbering]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]]
