---
type: "concept"
title: "Toast Notifications"
description: "Transient, non-blocking feedback messages and their placement, stacking, and dismissal"
tags: ["toast", "notifications", "ux", "feedback", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-live", "https://m3.material.io/components/snackbar/overview"]
---
# Toast Notifications

## Summary
Toasts (snackbars) show brief, non-blocking feedback: "Saved", "Copied", or error summaries. They auto-dismiss, never require action, and must not obscure critical information. Accessibility, stacking, and dismissal timing are the details that separate good from annoying toasts.

## Details
- **Placement and stacking** — bottom (mobile) or top-right (desktop); multiple toasts stack without overlapping controls.
- **Timing** — long enough to read (4-6s typical), longer for errors; never rely on auto-dismiss for critical outcomes.
- **Actions** — optional single action ("Undo", "Retry") but never require one; keyboard dismissal via Esc.
- **Accessibility** — announce via aria-live; avoid flashing and pure-color status cues.
- **Worked example** — the mykb editor shows "Note saved" with an Undo action, replacing it on the next save.
- **Relevance** — agent-generated confirmations should follow the same transient-feedback rules.
- **Stacking and priority** — high-priority errors replace or pin toasts; queues prevent overlap; each toast carries a single action at most, keeping the pattern non-blocking.

## Related
- [[wiki/web-platforms/z-index-management|Z-Index Management]] — adjacent concept in this wiki
- [[wiki/web-platforms/stacking-contexts|Stacking Contexts]] — adjacent concept in this wiki
- [[wiki/web-platforms/pointer-events-css|pointer-events CSS]] — adjacent concept in this wiki
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/frontend-frameworks/material-design|Material Design]] — existing coverage
