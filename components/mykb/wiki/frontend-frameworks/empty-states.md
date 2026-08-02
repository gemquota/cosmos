---
type: "concept"
title: "Empty States"
description: "Designing for no data: guidance, onboarding, and next actions in blank screens"
tags: ["empty-states", "ux", "onboarding", "design", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://uxdesign.cc/empty-states-2ea0e7d6d4b3", "https://uxdesign.cc/empty-states-2ea0e7d6d4b3"]
---
# Empty States

## Summary
An empty state is the screen users see when a list or page has no data: a first-run welcome, an all-done moment, or a search that matched nothing. Good empty states explain why the space is blank and point to the next action. They are onboarding moments, not dead ends.

## Details
- **Kinds** — first-run (show the value and a starting action), empty-after-clearing (all done), and no-results (adjust the query).
- **Ingredients** — a clear message, a relevant illustration or icon, and one primary action (create, clear filters, explore).
- **Tone** — informative and encouraging; never blame the user or imply failure.
- **Worked example** — the mykb wiki's "no pulses yet" view explains the pass workflow and links to the acquisition guide.
- **Relevance** — RSIS3's empty data surfaces should guide users to the first meaningful action.
- **Search-specific empty states** — no-results views should offer query suggestions, clear-filter actions, and alternative searches instead of a bare message; typo tolerance reduces these moments.

## Related
- [[wiki/frontend-frameworks/async-state|Async State]] — adjacent concept in this wiki
- [[wiki/api-protocols/error-codes-api|Error Codes in APIs]] — adjacent concept in this wiki
- [[wiki/api-protocols/404-vs-410|404 vs 410]] — adjacent concept in this wiki
- [[wiki/api-protocols/retry-after-web|Retry-After]] — adjacent concept in this wiki
- [[wiki/web-platforms/component-architecture|Component Architecture]] — existing coverage
- [[wiki/web-platforms/state-management|State Management]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
