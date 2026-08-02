---
type: "concept"
title: "Web Animations API"
description: "Animating DOM elements from JavaScript with keyframes, timing, and playback control"
tags: ["animation", "waapi", "javascript", "css", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API", "https://www.w3.org/TR/web-animations-1/"]
---
# Web Animations API

## Summary
The Web Animations API (WAAPI) drives CSS-style animations from JavaScript: `element.animate(keyframes, options)` returns an Animation with play, pause, reverse, and seek. It unifies CSS transitions, CSS animations, and JS-driven effects under one timing model.

## Details
- **Keyframes and options** — keyframe arrays with offsets and easings; options set duration, delay, iterations, direction, and fill.
- **Playback control** — `play()`, `pause()`, `cancel()`, `finish()`, and `currentTime` give script-level control CSS lacks.
- **Compositor friendliness** — animating transform and opacity stays off the main thread; WAAPI animations run on the compositor where possible.
- **Reduced motion** — check `prefers-reduced-motion` and scale or skip animations accordingly.
- **Worked example** — a toast notification in the mykb UI animates in via WAAPI with a composited translate, then reverses out.
- **Relevance** — RSIS3's interface polish should use WAAPI rather than rAF loops for declarative, pausable motion.
- **Composite order** — animations compose in document order with higher composite order winning; `animation.composite` and `iterationComposite` control how effects layer, matching the CSS cascade.

## Related
- [[wiki/web-platforms/sprite-sheets|Sprite Sheets]] — adjacent concept in this wiki
- [[wiki/web-platforms/inline-svg|Inline SVG]] — adjacent concept in this wiki
- [[wiki/web-platforms/svg-animation|SVG Animation]] — adjacent concept in this wiki
- [[wiki/web-platforms/css-transforms|CSS Transforms]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/css-layout|CSS Layout]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
