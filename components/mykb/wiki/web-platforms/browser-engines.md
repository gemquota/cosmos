---
type: "concept"
title: "Browser Engines"
description: "The rendering engines that parse HTML, CSS, and JavaScript to display web pages"
tags: ["browsers", "engines", "rendering", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Glossary/Engine"]
---

# Browser Engines

## Summary
A browser engine is the core software that fetches documents, parses HTML and CSS, lays out pages, and executes JavaScript. The main engines are Blink (Chrome, Edge), Gecko (Firefox), WebKit (Safari), and their descendants; MDN defines them as the 'heart of the browser'.

## Details
- Engines have subcomponents: the rendering engine (HTML/CSS parsing, layout, paint) and the JavaScript engine (V8, SpiderMonkey, JavaScriptCore).
- Engine diversity is why the same code behaves differently: CSS prefixes, layout quirks, and API availability vary.
- Standardization and the web-platform-tests suite keep engines converging, but feature support still differs by release.
- Testing across engines is mandatory for serious web work; automated browsers (Playwright, Puppeteer) drive them.
- Engine evolution drives the platform: new CSS features and Web APIs ship when the engines agree.
- RSIS3 relevance: agent browser automation must know which engine it drives to write robust selectors and waits.
- Comparison: Blink/Gecko/WebKit share standards but differ in performance characteristics and niche features.

## Related
- [[wiki/web-platforms/web-standards|Web Standards]] — engines implement what standards define
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — engine internals determine what optimizations matter
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — the JS engines embedded in browsers and servers
- [[wiki/web-platforms/web-apis|Web APIs]] — the platform surface engines expose
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — engines sit in the middle of the stack
- [[wiki/testing/golden-tests|Golden Tests]] — cross-engine golden rendering catches drift
- [[wiki/agent-systems/agent-sandboxing|Agent Sandboxing]] — browser engines are also sandbox targets
