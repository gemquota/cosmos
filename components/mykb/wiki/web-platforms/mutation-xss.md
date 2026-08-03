---
type: "concept"
title: "Mutation XSS"
description: "Browsers mutating markup into executable script during parsing"
tags: ["security", "xss", "attacks", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Mutation XSS

## Summary

Mutation XSS (mXSS) exploits the gap between what a sanitizer sees and what the DOM ends up containing: HTML parsing or DOM APIs mutate markup in ways that resurrect dangerous elements after sanitization. It is a leading sanitizer-bypass class.

## Details
- Mechanism: browsers parse HTML with forgiving, idiosyncratic rules (implied tags, foster parenting, namespace handling); a string that looks safe as text — e.g. <math><mtext></mtext><img src=x onerror=1></math> or <svg><p><style><img src=x onerror=alert(1)></style></p></svg> — can re-parse into an active element after being inserted via innerHTML. Sanitizers that serialize and re-parse mutate the payload differently than the live DOM.
- Concrete example: the classic mXSS vector uses </style> or </title> inside foreign content to escape the raw-text element after sanitization; DOMPurify's mXSS patches and browser-behavior tests exist precisely because blacklists of tags/attributes keep missing mutation paths.
- Failure modes: sanitizing to a string and re-inserting via innerHTML (the parse boundary changes the tree); relying on regex-based filtering; treating sanitizer versions as stable — mXSS fixes are security patches that must be updated; and sanitizing server-side with a different parser than the client browser, so the two disagree.
- Operational tradeoffs: robust defense is sanitize into a detached DOM (parsed once, same engine as the browser), then insert nodes — or use a maintained sanitizer with an active mXSS test suite; add CSP as a backstop. Mutation after sanitization is the signal: log and re-check.
- RSIS3/mykb relevance: the wiki markdown renderer sanitizes into a template element and inserts nodes, with mXSS regression fixtures tracked in this cluster's safe-rendering checklist.
- Sanitizer hygiene: pin the sanitizer version and update it as a security dependency; mXSS bypasses ship as patches, and a stale sanitizer is a standing vulnerability.
- Detection: log re-parse differences between sanitized output and the live DOM; divergence is the mXSS signal worth alerting on.

## Related
- [[wiki/api-protocols/web-security-owasp|Web Security (OWASP)]]
- [[wiki/web-platforms/dom-xss|DOM XSS]]
- [[wiki/web-platforms/reflected-xss|Reflected XSS]]
- [[wiki/web-platforms/stored-xss|Stored XSS]]
- [[wiki/security-auth/xss-prevention|XSS Prevention]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
- [[wiki/web-platforms/web-apis|Web APIs]]
