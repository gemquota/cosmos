---
type: "concept"
title: "Progressive Enhancement"
description: "Layering baseline functionality then enhancements"
tags: [progressive-enhancement", "html", "accessibility", "javascript", "architecture"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Progressive_Enhancement", "https://web.dev/articles/rendering-on-the-web"]
---

# Progressive Enhancement

## Summary
Progressive enhancement builds a working baseline with plain HTML and CSS, then layers JavaScript enhancements on top. Content and core function survive without scripting, network failures, or disabled JS. It is the resilient counterpart to JavaScript-first single-page apps and remains the standard for content-critical sites.

## Details
- Layers: semantic HTML for content, CSS for presentation, JavaScript for enhancement — each layer adds capability.
- No-JS behavior: forms submit server-side, links navigate, and content reads without any script executing.
- Feature detection: enhance only when APIs exist, avoiding feature-testing hacks and polyfill assumptions.
- Relationship to graceful degradation: degradation starts rich and strips back; enhancement starts minimal and adds.
- Modern fit: islands architecture and server-rendered HTML with optional hydration are enhancement in practice.
- Testing: verify key flows with JavaScript disabled, on slow networks, and with assistive technology.

## Related
- [[wiki/frontend/islands-architecture|Islands Architecture]] — enhancement applied to interactivity
- [[wiki/frontend/semantic-html|Semantic HTML]] — the baseline layer
- [[wiki/frontend/mobile-first-design|Mobile-First Design]] — same ordering for layout
- [[wiki/frontend/form-validation|Form Validation]] — server fallback for validation
- [[wiki/web-platforms/web-standards|Web Standards]] — the technology layers involved
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — why baselines must work for all
