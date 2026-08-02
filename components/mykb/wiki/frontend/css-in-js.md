---
type: "concept"
title: "CSS-in-JS"
description: "Styling via JavaScript with runtime and compile-time strategies"
tags: [css", "css-in-js", "react", "styling", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://styled-components.com/docs/basics", "https://cssinjs.org/"]
---

# CSS-in-JS

## Summary
CSS-in-JS writes styles as JavaScript — strings, objects, or functions colocated with components. Runtime libraries such as styled-components and Emotion generate stylesheets while the app runs, while compile-time libraries such as vanilla-extract and Linaria extract CSS at build time. The trade-off centers on dynamic theming power versus bundle and runtime cost.

## Details
- Runtime model: styles are computed from props, injected into a style tag, and updated as props change; SSR requires extraction.
- Compile-time model: styles are evaluated at build time into static CSS files, with dynamic parts relegated to custom properties.
- Scoping: generated class names are unique, giving CSS Modules-style isolation without separate files.
- Theming: context or props pass tokens into style functions, enabling dark mode and per-instance variants cheaply.
- Cost concerns: runtime libraries add JavaScript weight and delay first paint unless styles are extracted for SSR.
- Modern direction: many teams move dynamic styling to CSS custom properties and reserve CSS-in-JS for static extraction.

## Related
- [[wiki/frontend/css-modules|CSS Modules]] — build-time scoping without JS
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — runtime values without runtime CSS
- [[wiki/frontend/theming|Theming]] — a core use case for dynamic styles
- [[wiki/frontend/design-tokens|Design Tokens]] — the values styles consume
- [[wiki/frontend/hydration|Hydration]] — SSR style extraction interacts with hydration
- [[wiki/web-platforms/web-frameworks|Web Frameworks]] — the component model CSS-in-JS targets
