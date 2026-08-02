---
type: "concept"
title: "Tabs Patterns"
description: "Tab interfaces: semantics, keyboard navigation, lazy loading, and content switching"
tags: ["tabs", "patterns", "ux", "accessibility", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/WAI/ARIA/apg/patterns/tabs/", "https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles/tab_role"]
---
# Tabs Patterns

## Summary
Tabs switch between related content panes without navigation. The ARIA tabs pattern defines role=tab/tablist/tabpanel with arrow-key navigation and roving focus. Tabs should be used for sibling views, not wizard steps; each panel's content loads with the tab.

## Details
- **Semantics** — tablist/tab/tabpanel roles with aria-selected and aria-controls; ids must match panel ids.
- **Keyboard** — Arrow keys move focus between tabs; Home/End jump; activate on Enter/Space (or on focus per pattern).
- **Activation** — automatic (focus) vs manual (click); automatic suits small panels, manual prevents surprises.
- **Lazy content** — load panels on first activation; preserve scroll and state per tab or reset deliberately.
- **Worked example** — the mykb wiki editor uses tabs for Write/Preview/Diff with lazy diff computation on first open.
- **Relevance** — tab semantics are a core primitive in RSIS3's UI component vocabulary.
- **Tab stop design** — either the whole tablist is one tab stop with arrow-key movement, or tabs are in the tab order with automatic activation; pick one and stay consistent.

## Related
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-snap|Scroll Snap]] — adjacent concept in this wiki
- [[wiki/web-platforms/content-visibility|content-visibility CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/contain-property|CSS Containment]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/frontend-frameworks/material-design|Material Design]] — existing coverage
