---
type: "concept"
title: "Web Standards"
description: "The open specifications from W3C, WHATWG, and IETF that define how the web works"
tags: ["standards", "web", "w3c", "whatwg"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/standards/"]
---

# Web Standards

## Summary
Web standards are the open specifications — HTML, CSS, JavaScript, HTTP, and accessibility guidelines — developed by bodies like the W3C, WHATWG, and IETF so that the web works identically across browsers and devices. They are the reason a page written once runs everywhere.

## Details
- The core standards stack: WHATWG maintains the living HTML and DOM standards; the W3C publishes CSS, accessibility (WAI-ARIA), and web platform APIs; the IETF owns HTTP and TLS.
- Standards are developed in the open, with implementer feedback: browsers ship experimental features and the specs converge through interoperability testing.
- Interop is the goal: web-platform-tests (WPT) is a shared suite that browsers run to prove conformance.
- Living standards mean the web evolves continuously; features like WebSockets, Web Components, and service workers entered through this process.
- Progressive enhancement and graceful degradation let standards-based sites work on older or constrained clients.
- RSIS3 relevance: the mykb dashboard and any agent-facing web UI should target standards, not browser quirks.
- Worked example: a form using only HTML attributes (required, min, max) is accessible and works without JavaScript.

## Related
- [[wiki/web-platforms/browser-engines|Browser Engines]] — engines implement the standards
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — a standards-track requirement, not an add-on
- [[wiki/web-platforms/web-components|Web Components]] — the standard-based component mechanism
- [[wiki/web-platforms/web-apis|Web APIs]] — the standards-defined surface browsers expose
- [[wiki/security/https|HTTPS]] — the transport standard underneath
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — how the standards stack fits together
- [[wiki/security/tls|TLS]] — the encryption standard HTTPS relies on
