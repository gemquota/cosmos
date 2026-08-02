---
type: "concept"
title: "Semantic HTML"
description: "Choosing native elements for meaning and behavior"
tags: [html", "semantics", "accessibility", "a11y", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Semantics", "https://html.spec.whatwg.org/multipage/dom.html#semantics"]
---

# Semantic HTML

## Summary
Semantic HTML chooses elements for their meaning rather than their appearance: header, nav, main, article, section, aside, and footer describe structure, while button, a, input, and table carry built-in behavior. Browsers, search engines, and assistive technology all read these semantics, which is why semantic markup is the cheapest accessibility feature available.

## Details
- Landmarks: header, nav, main, and footer create navigation regions screen readers jump between; article and section nest content.
- Native behavior: button gives Enter and Space activation, form controls give labels and validation, a gives links — all for free.
- Headings: one h1 and a logical heading hierarchy (h1-h6 without skips) structure document outline for all users.
- Lists and tables: ul/ol/li and proper table semantics (th, scope, caption) beat divs for structure and announcement.
- Anti-patterns: divs with click handlers, span buttons, and heading-styled paragraphs all require ARIA and JS to approximate what natives give.
- Performance and SEO: semantic markup is smaller, more maintainable, and signals content meaning to crawlers.

## Related
- [[wiki/frontend/aria|ARIA]] — supplements semantics when natives fall short
- [[wiki/frontend/wcag|WCAG]] — criteria that reward semantic structure
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — native elements are keyboard-ready
- [[wiki/frontend/html-forms|HTML Forms]] — the semantic form model
- [[wiki/frontend/screen-readers|Screen Readers]] — consumers of element semantics
- [[wiki/web-platforms/web-standards|Web Standards]] — where these semantics are defined
