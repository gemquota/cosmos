---
type: "concept"
title: "Animation Performance"
description: "Compositor-friendly transform and opacity techniques"
tags: [performance", "animations", "css", "compositing", "javascript"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://web.dev/articles/animations", "https://developer.mozilla.org/en-US/docs/Web/CSS/will-change"]
---

# Animation Performance

## Summary
Fast animations run on the compositor thread by animating only transform and opacity. These properties skip layout and paint entirely, so frames stay smooth even when the main thread is busy. Animating width, height, or top forces per-frame layout work and is the classic source of jank.

## Details
- Compositor path: transform and opacity changes are promoted to layers and composited on the GPU thread, independent of main-thread work.
- What to animate: translate and scale for movement, opacity for fades, and transforms for rotations; keep layout properties still.
- will-change: hints the browser to promote an element ahead of time; use sparingly — every layer costs memory.
- FLIP: First-Last-Invert-Play measures layout once and animates transforms for position changes.
- Web Animations API: element.animate() gives scripted control while staying compositor-friendly.
- Accessibility: respect prefers-reduced-motion and keep essential feedback even when decorative motion is removed.

## Related
- [[wiki/frontend/reflow-repaint|Reflow and Repaint]] — the work compositor-friendly animation avoids
- [[wiki/frontend/prefers-reduced-motion|Reduced Motion]] — honoring user motion preferences
- [[wiki/frontend/long-tasks|Long Tasks]] — main-thread contention with animation
- [[wiki/frontend/core-web-vitals|Core Web Vitals]] — INP and CLS interaction with motion
- [[wiki/frontend/debouncing-throttling|Debouncing and Throttling]] — rAF-driven updates
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — frame budgets
