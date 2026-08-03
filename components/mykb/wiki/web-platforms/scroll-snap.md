---
type: "concept"
title: "Scroll Snap"
description: "Aligning scroll positions to defined snap points"
tags: ["css", "scroll", "ux", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Scroll Snap

## Summary

CSS scroll snap makes scrolling rest on defined positions — whole slides, grid cells, or aligned sections — instead of arbitrary stops. It turns free scrolling into deliberate, gesture-friendly navigation for carousels, galleries, and paged interfaces.

## Details
- Mechanism: scroll-snap-type: x mandatory (or proximity) on the scroll container plus scroll-snap-align: start/center/end on children defines the snap points; mandatory forces a snap after every scroll, proximity only near a point. The container must actually scroll (overflow) for snapping to engage.
- Concrete example: an image gallery with scroll-snap-type: x mandatory and children scroll-snap-align: center always lands on a whole image; a vertical article reader snaps sections to the top. iOS momentum scrolling gains snap behavior for free via -webkit-overflow-scrolling plus snap properties.
- Failure modes: mandatory snap on large content makes users fight to reach middle content (prefer proximity or smaller snap areas); snapping inside nested scroll containers hijacks outer scrolling; content taller than the container cannot fully snap (snap-to-bottom unattainable); and keyboard/AT users get no equivalent unless focus and tab navigation are maintained.
- Operational tradeoffs: snap improves touch and trackpad UX but reduces free-scroll control; pair with scroll-padding-top to offset sticky headers, and gate smooth programmatic scrolling on prefers-reduced-motion. Test with trackpad momentum — some browsers still need explicit snap-stop behavior.
- RSIS3/mykb relevance: the OKF graph's card carousel uses horizontal snap; this note records the snap geometry so loop-generated galleries match the interaction pattern.
- Dynamic content: snap points re-evaluate after layout changes (image loads, fonts), so re-verify snapping after lazy content inserts inside a snap container.
- Proximity vs mandatory: proximity is the safer default for long content; mandatory suits short, discrete carousels where mid-state scrolling is meaningless.
- Snap and keyboard: ensure focus order matches snap order so keyboard users land on the same slides as gesture users; snap is visual, focus is functional.

## Related
- [[wiki/web-platforms/virtual-scrolling|Virtual Scrolling]]
- [[wiki/web-platforms/sticky-position|position: sticky]]
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]]
- [[wiki/web-platforms/scroll-snap|Scroll Snap]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/web-accessibility|Web Accessibility]]
- [[wiki/web-platforms/dom-manipulation|DOM Manipulation]]
