---
type: "concept"
title: "Modals in Practice"
description: "Dialog design: focus trapping, dismissal, scroll, and when not to use modals"
tags: ["modals", "dialogs", "ux", "accessibility", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog", "https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/"]
---
# Modals in Practice

## Summary
Modals focus the user on one task: confirm, enter, or inspect without leaving context. The native `<dialog>` element plus correct ARIA (role=dialog, aria-modal) handles focus and semantics. Modals interrupt; reserve them for tasks that genuinely need focus, and manage dismissal carefully.

## Details
- **Focus management** — focus moves into the dialog on open and returns to the trigger on close; Tab cycles within (focus trap).
- **Dismissal** — Esc, overlay click, and an explicit close button; confirm before losing unsaved work.
- **Scrolling** — tall dialogs scroll internally; the background locks (scrollbar-gutter prevents layout shift).
- **Alternatives** — confirm dialogs, inline expansion, and non-modal popovers often serve better than a modal.
- **Worked example** — the mykb delete-confirmation uses the native dialog element with a focus trap and Esc handling.
- **Relevance** — RSIS3's generated UIs should default to non-interruptive patterns and reserve modals.

## Related
- [[wiki/web-platforms/z-index-management|Z-Index Management]] — adjacent concept in this wiki
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]] — adjacent concept in this wiki
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/scroll-behavior|scroll-behavior CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/web-platforms/component-architecture|Component Architecture]] — existing coverage
