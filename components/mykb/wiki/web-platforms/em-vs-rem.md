---
type: "concept"
title: "em vs rem"
description: "Relative font units: parent-scoped versus root-scoped sizing"
tags: ["css", "units", "typography", "layout"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# em vs rem

## Summary

rem units size relative to the root font size; em sizes relative to the current element's font size. The choice determines whether a component scales with user preferences and parent context, or stays globally consistent.

## Details
- Mechanism: 1rem = root font-size (16px by default, adjustable by user settings); 1em = the element's own computed font-size, so nested elements compound (0.8em inside 20px is 16px, inside another 0.8em it is 12.8px). Padding and margins in em scale with the element's text; rem values never compound.
- Concrete example: buttons using em for padding and border-radius scale the whole control when font-size changes, keeping proportion; a design system using rem for spacing tokens keeps rhythm consistent regardless of where a component lands in the tree. Mixing: font-size in rem for global scale, inner proportions in em.
- Failure modes: em compounding produces surprising sizes in deeply nested components (a 0.9em chain decays quickly); rem is relative to the root, so a component's size depends on a global knob — fine for accessibility zoom, bad for isolated previews; and hard-coded px in line-height or borders defeats the scaling intent.
- Operational tradeoffs: rem honors user font-size preferences (accessibility); em enables self-contained components. Many systems set html font-size to a fluid clamp and use rem everywhere for type and spacing, reserving em for component-internal proportions.
- RSIS3/mykb relevance: dashboard tokens define spacing in rem and component-internal padding in em so telemetry panels scale with the OS text-size setting, verified by a periodic accessibility check.
- Component scaling: em inside a component makes the whole control scale with its font-size — useful for buttons and badges; rem keeps global rhythm; the boundary between the two is a deliberate design decision, not an accident.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/px-vs-rem|px vs rem]]
- [[wiki/web-platforms/container-relative-units|Container Query Units]]
- [[wiki/web-platforms/responsive-units|Responsive Units]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]]
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]]
