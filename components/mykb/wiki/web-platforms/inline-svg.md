---
type: "concept"
title: "Inline SVG"
description: "Embedding SVG markup directly in HTML for styleable graphics"
tags: ["svg", "images", "web", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Inline SVG

## Summary

Inline SVG embeds vector graphics directly in HTML, giving CSS and script access to every part of the image. It is the best tool for logos, icons, charts, and any graphic that must scale, style, or animate.

## Details
- Mechanism: an <svg> element in the DOM is styled and scripted like any element; shapes, paths, gradients, and text respond to CSS, and SMIL/Web Animations can animate parts independently. Unlike <img> SVG, inline SVG participates in the accessibility tree and can be cached only as part of the page.
- Concrete example: a logo inline so a hover swaps its fill via CSS; a loading spinner drawn as an SVG circle with a stroke-dashoffset animation; a donut chart built from circle stroke-dasharray — all without raster images or canvas redraws.
- Failure modes: massive inline SVGs bloat HTML and defeat caching (use sprites or external files for reused art); untrusted SVG can execute scripts when injected — sanitize or render as <img> to neutralize scripts; viewBox vs width/height mismatch causes scaling surprises; and text in SVG needs the same font considerations as HTML.
- Operational tradeoffs: inline SVG is interactable and styleable but not cacheable per asset; <img src> SVG is cacheable and safe but opaque to CSS and scripts. Choose by need: static art via <img>/sprite, interactive or themeable art inline.
- RSIS3/mykb relevance: the OKF graph and dashboard diagrams are inline SVG so the loop can animate and annotate graph nodes with the same styling tokens as the rest of the UI.
- Security: inline SVG can carry scripts and external references; sanitize untrusted SVG or load it via <img> where scripts are inert, and strip href/xlink:href javascript: schemes.
- Accessibility: give inline SVGs a role and accessible name (title/aria-label) where they carry meaning, and aria-hidden decorative ones; unlabeled SVGs are read as noise by assistive tech.

## Related
- [[wiki/web-platforms/web-animations|Web Animations API]]
- [[wiki/web-platforms/svg-animation|SVG Animation]]
- [[wiki/web-platforms/sprite-sheets|Sprite Sheets]]
- [[wiki/web-platforms/inline-svg|Inline SVG]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
