---
type: "concept"
title: "Web Accessibility"
description: "Making web interfaces usable by everyone: semantics, keyboard support, ARIA, and WCAG"
tags: ["accessibility", "wcag", "aria", "a11y", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/fundamentals/accessibility-intro/", "https://developer.mozilla.org/en-US/docs/Web/Accessibility"]
---
# Web Accessibility

## Summary
Accessibility (a11y) ensures interfaces work for people with disabilities: screen-reader users, keyboard-only users, low-vision users, and more. WCAG organizes requirements into perceivable, operable, understandable, and robust principles. Native semantics plus correct ARIA beat hacks.

## Details
- **Semantics first** — use real buttons, headings, labels, and landmarks; assistive tech builds on the accessibility tree derived from the DOM.
- **Keyboard** — everything interactive must be reachable and operable by keyboard with visible focus.
- **ARIA** — roles, states, and properties fill gaps (tabs, modals, alerts) but never replace native elements when they exist.
- **Contrast and motion** — WCAG contrast ratios, `prefers-reduced-motion`, and text-resize-safe layouts.
- **Testing** — automated checks (axe) plus manual keyboard and screen-reader passes; mobile accessibility matters too.
- **Worked example** — the mykb dashboard ships with axe checks in CI and focus-visible styling on every control.
- **Relevance** — RSIS3's outputs (reports, dashboards) should meet the same bar so knowledge stays accessible to every reader.

## Related
- [[wiki/web-platforms/contrast-ratios|Contrast Ratios]] — adjacent concept in this wiki
- [[wiki/web-platforms/color-blind-considerations|Color Blind Accessibility]] — adjacent concept in this wiki
- [[wiki/web-platforms/prefers-contrast|prefers-contrast]] — adjacent concept in this wiki
- [[wiki/web-platforms/rtl-support|RTL Support]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — existing coverage
- [[wiki/web-platforms/web-standards|Web Standards]] — existing coverage
