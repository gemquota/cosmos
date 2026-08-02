---
type: "concept"
title: "Reduced Motion"
description: "Respecting user motion preferences in animations"
tags: [accessibility", "css", "animations", "motion", "a11y"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion", "https://web.dev/articles/prefers-reduced-motion"]
---

# Reduced Motion

## Summary
The prefers-reduced-motion media query lets sites honor a user's system-level request to minimize animation. People with vestibular disorders can be sickened by parallax, marquees, and large transitions, so WCAG 2.2 includes a criterion for reducing motion. Respecting the preference is a small CSS change with significant comfort impact.

## Details
- Query: @media (prefers-reduced-motion: reduce) gates styles; the no-preference value is the default for most users.
- Scope: scale down transitions, scroll-triggered effects, autoplaying carousels, and decorative animation; keep essential feedback.
- Technique: set a custom property such as --duration or --motion-scale and swap its value inside the query for global effect.
- Animation libraries: CSS animation shorthand resets, JavaScript motion libraries, and CSS-in-JS all need the same guard.
- Semantics: reduced motion does not mean no motion — fade and opacity changes are generally gentler than transforms.
- Testing: emulate the setting in DevTools and on-device; verify that content is not hidden by motion suppression.

## Related
- [[wiki/frontend/media-queries|Media Queries]] — the feature family this belongs to
- [[wiki/frontend/animation-performance|Animation Performance]] — building motion well
- [[wiki/frontend/wcag|WCAG]] — the reduced-motion success criterion
- [[wiki/frontend/css-custom-properties|CSS Custom Properties]] — gating animation values
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — motion sensitivity as a11y
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — verifying reduced-motion behavior
