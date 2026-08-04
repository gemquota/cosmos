---
type: "entity"
title: "ARIA"
description: "Roles, states, and properties for accessibility semantics"
tags: [accessibility", "aria", "a11y", "semantics", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/TR/wai-aria-1.2/", "https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA"]
---

# ARIA

## Summary
ARIA — Accessible Rich Internet Applications — adds semantics for assistive technology when native HTML cannot express the interaction model. Roles, states, and properties describe widgets, relationships, and live regions to the accessibility tree. The first rule of ARIA is to use native elements first, because built-in behavior is free and reliable.

## Details
- Roles: role="dialog", role="tablist", and role="switch" label the widget type; landmark roles mirror native sectioning elements.
- States and properties: aria-expanded, aria-checked, aria-controls, and aria-labelledby convey dynamic widget state and relationships.
- Live regions: aria-live and aria-atomic announce updates such as toasts and search results without moving focus.
- Name computation: aria-label, aria-labelledby, and fallback content determine the accessible name of a widget.
- Rules: do not override native roles (button stays button), keep state in sync with visible UI, and avoid redundant ARIA.
- Testing: inspect the accessibility tree in DevTools and verify with a real screen reader, since ARIA mistakes are silent.

## Related
- [[wiki/frontend/semantic-html|Semantic HTML]] — the native alternative ARIA supplements
- [[wiki/frontend/screen-readers|Screen Readers]] — consumers of ARIA semantics
- [[wiki/frontend/wcag|WCAG]] — the criteria ARIA helps satisfy
- [[wiki/frontend/keyboard-navigation|Keyboard Navigation]] — ARIA widget patterns require it
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — catching ARIA misuse
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — the platform discipline
