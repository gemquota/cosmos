---
type: "concept"
title: "Tooltips in Practice"
description: "Hover/ focus-accessible hints: trigger, delay, placement, and dismissal"
tags: ["tooltips", "ux", "accessibility", "frontend", "patterns"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/ARIA/apg/patterns/tooltip/", "https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/tooltip_role"]
---
# Tooltips in Practice

## Summary
Tooltips provide short, supplemental information on hover or focus. They must be keyboard-reachable (focus triggers), dismissible, and never required to complete a task — critical information belongs in content, not hover. The ARIA tooltip pattern defines the contract.

## Details
- **Triggers** — hover, focus, and optionally touch; keyboard users must reach every tooltip source.
- **Timing** — small delay on show (200-500ms) prevents flicker; hide on mouse-out, Esc, or when the target loses focus.
- **Placement** — avoid viewport edges and pointer-obscured spots; flip and offset adaptively.
- **Content** — one or two lines; icons with aria-describedby announce the hint.
- **Worked example** — the mykb dashboard's chart controls show keyboard-reachable tooltips describing each metric.
- **Relevance** — tooltips are a pattern RSIS3's agent UI library should ship as an accessible component.
- **Rich content caution** — tooltips must stay short; interactive content inside them belongs in popovers, because tooltips close on hover-out and cannot reliably hold focus.

## Related
- [[wiki/web-platforms/z-index-management|Z-Index Management]] — adjacent concept in this wiki
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]] — adjacent concept in this wiki
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/frontend-frameworks/material-design|Material Design]] — existing coverage
