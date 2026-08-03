---
type: "concept"
title: "Color Blind Accessibility"
description: "Designing palettes that work without relying on hue alone"
tags: ["accessibility", "color", "design", "inclusion"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Color Blind Accessibility

## Summary

Color blindness affects roughly 8% of men and 0.5% of women, so interfaces must not rely on hue alone to convey meaning. Redundancy, contrast, and pattern support make designs work for everyone.

## Details
- Mechanism: the common forms are deuteranopia/protanopia (red-green) and tritanopia (blue-yellow); color perception differs, not sharpness. Simulators recolor screenshots through these transforms so designers can audit their own work.
- Concrete example: a status badge that is green for success and red for failure fails the deuteranopic user when the two look identical; adding a check/cross icon, or a text label, preserves the signal. Charts should encode series with dash patterns or shapes in addition to color.
- Failure modes: relying on a single hue channel for data series; using low-contrast pastel fills that also fail contrast checks; assuming grayscale simulation covers all forms (it does not — tritanopia needs its own filter); and forgetting that color vision varies with age, displays, and night modes.
- Operational tradeoffs: redundant encoding adds visual noise; pick the highest-signal redundancy (icon, label, position) rather than adding all. Contrast and color-vision fixes usually improve readability for everyone, so treat them as quality, not accommodation.
- Tooling: WCAG 2.x contrast ratios do not directly test hue-dependence, so pair contrast checks with a simulator and a manual review of every color-meaning pairing.
- RSIS3/mykb relevance: the dashboard's pulse charts use color-plus-shape series and WCAG-checked palettes so telemetry remains readable to the whole team, and the wiki documents the palette decision as a design note.
- Palette audit: check every color-meaning pairing with a simulator and in grayscale; charts that survive both keep their signal for deuteranopic and tritanopic users alike.
- Documentation: record color-meaning pairs in the design tokens so future palette edits cannot silently break the encoding.

## Related
- [[wiki/web-platforms/css-variables-theming|CSS Variables and Theming]]
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]]
- [[wiki/web-platforms/srgb-vs-p3|sRGB vs Display P3]]
- [[wiki/web-platforms/color-mix|color-mix() CSS]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
