---
type: "concept"
title: "Font Fallbacks"
description: "Declaring font-family fallback stacks for missing glyphs and files"
tags: ["fonts", "css", "typography", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Font Fallbacks

## Summary

Font fallback stacks (font-family: "Inter", system-ui, sans-serif) decide what renders before and during web font loads. A well-built stack is metric-aware, keeps text readable, and minimizes the layout shift when the real font arrives.

## Details
- Mechanism: the browser walks the stack in order, using the first available family; system-ui maps to the platform's UI font, and generic families (serif/sans-serif/monospace) always resolve. Fallbacks apply during font loading, so their metrics determine pre-swap layout.
- Concrete example: font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif covers macOS/iOS, Windows, Android, and generic Linux; a mono stack for code lists ui-monospace, SFMono-Regular, Menlo, Consolas, monospace.
- Failure modes: omitting a generic family lets the browser pick an unexpected face; stacks ending in a serif generic change character; fallbacks with wildly different metrics (e.g. wide system font vs narrow web font) maximize CLS; and referencing a font that is never loaded but still first in the stack blocks rendering attempts.
- Operational tradeoffs: modern fallback tuning uses @font-face size-adjust and ascent/descent overrides to match fallback metrics to the web font, reducing swap shift to near zero; this is worth it for body text, while display fonts can accept a larger shift. Test fallbacks explicitly by blocking the web font in DevTools.
- RSIS3/mykb relevance: the dashboard's font stacks are documented with their metric-override values so chart digits and labels swap without shifting the layout.
- Unicode coverage: fallbacks must also cover glyphs the web font lacks (emoji, rare scripts); a bare generic can route those to a jarring default, so append "Apple Color Emoji", "Segoe UI Emoji" where needed.
- Self-hosting practice: pairing fallback tuning with self-hosted subsets avoids CDN font-flash variance and keeps the metric overrides consistent across environments.
- Fallback stack order: put the most likely system font first within the generic, so Linux, Windows, and macOS each get a native face; a single generic sans-serif is a readability gamble.

## Related
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]]
- [[wiki/web-platforms/variable-fonts|Variable Fonts]]
- [[wiki/web-platforms/web-fonts|Web Fonts]]
- [[wiki/web-platforms/font-display-swap|font-display: swap]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
