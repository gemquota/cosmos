---
type: "concept"
title: "Content Security Policy"
description: "Directives restricting allowed resource origins"
tags: [security", "csp", "http", "headers", "web"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP", "https://web.dev/articles/csp"]
---

# Content Security Policy

## Summary
Content Security Policy is an HTTP header that tells the browser which origins and inline code a page may load. Directives like default-src, script-src, style-src, and img-src enumerate allowed sources; violations are blocked (or reported in report-only mode). CSP is the strongest browser-level mitigation against cross-site scripting.

## Details
- Directives: script-src controls scripts, style-src styles, img-src images, object-src plugins, and connect-src network targets.
- Inline handling: 'unsafe-inline' disables most protection; nonces and hashes allow specific inline scripts instead.
- report-only: Content-Security-Policy-Report-Only logs violations without blocking, enabling safe rollout.
- CSP3: strict-dynamic builds trust from already-approved scripts, improving compatibility with module bundlers.
- Common friction: eval, inline styles, and data: URIs conflict with strict policies; frameworks may need configuration.
- Value: CSP cannot stop all injection, but combined with encoding it sharply reduces what attackers can execute.

## Related
- [[wiki/frontend/cross-site-scripting|Cross-Site Scripting]] — the attack CSP mitigates
- [[wiki/security-auth/content-security-policy|Content Security Policy]] — the security-area article
- [[wiki/security-auth/same-origin-policy|Same-Origin Policy]] — the origin model CSP extends
- [[wiki/security-auth/cors-policy|CORS Policy]] — related cross-origin controls
- [[wiki/frontend/resource-hints|Resource Hints]] — preloads must obey CSP
- [[wiki/frontend/browser-caching|Browser Caching]] — serving headers with responses
