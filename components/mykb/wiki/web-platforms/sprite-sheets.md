---
type: "concept"
title: "Sprite Sheets"
description: "Combining many small images into one file to cut requests"
tags: ["images", "performance", "css", "sprites"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Sprite Sheets

## Summary

Sprite sheets pack many images into one file so a page loads one request and positions sub-images via background-position or clip. They shine for many small fixed assets (icons, animation frames) and fight the cache when assets change together.

## Details
- Mechanism: one bitmap holds a grid of frames; CSS background-position offsets reveal the desired cell (sprite coordinates), or an animation steps through frames by shifting position. Icon sprites cut HTTP requests and compress better as one image than many.
- Concrete example: a classic icon sprite with 30 icons served as one 16KB PNG; an animated character using steps(10) over a 10-frame strip; a game texture atlas packing hundreds of tiles for WebGL. Modern variants: SVG sprite sheets (<symbol> + <use>) for vectors, and CSS mask/sprites for multi-color needs.
- Failure modes: adding/changing one sprite invalidates the whole cache (frequent bumps waste bandwidth); background-position math errors show wrong cells; DPR — a 1x sprite blurs on retina unless scaled or 2x variants exist; and sprite sheets hurt inlining and accessibility (each icon needs its own markup semantics).
- Operational tradeoffs: for a handful of images, separate files with HTTP/2 multiplexing are often better than a sprite; sprites win for many tiny, rarely-changing assets. Keep generation scripted (a build step), and prefer SVG symbols for UI icons to sidestep DPR entirely.
- RSIS3/mykb relevance: the wiki's chart legends and status icons use an SVG symbol sprite; bitmap sprite sheets are reserved for animation frames, per the asset rules in this note.
- Maintenance trigger: regenerate sprites from a source directory in the build; hand-edited sprite coordinates are the top source of wrong-icon bugs, and a build step makes the sheet a derived artifact.
- HTTP/2 note: with connection multiplexing, many small files compete with one sprite on bytes, not requests; measure before assuming the sprite is faster on modern transports.

## Related
- [[wiki/web-platforms/web-animations|Web Animations API]]
- [[wiki/web-platforms/inline-svg|Inline SVG]]
- [[wiki/web-platforms/svg-animation|SVG Animation]]
- [[wiki/web-platforms/sprite-sheets|Sprite Sheets]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
