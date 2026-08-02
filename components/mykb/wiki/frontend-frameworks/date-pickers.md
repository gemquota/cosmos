---
type: "concept"
title: "Date Pickers"
description: "Choosing dates and times: native inputs, calendars, ranges, and timezones"
tags: ["date-picker", "forms", "ux", "accessibility", "frontend"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date", "https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/"]
---
# Date Pickers

## Summary
Date picking ranges from native `<input type="date">` to rich calendar widgets with ranges and timezones. Native inputs bring mobile pickers and keyboard support free; custom calendars add ranges, quick picks, and formatting control at the cost of accessibility reimplementation.

## Details
- **Native inputs** — date, time, datetime-local, and week/month types: free UX and validation, limited styling.
- **Custom calendars** — grid semantics (role=grid), arrow-key navigation, focus management, and text input fallback.
- **Ranges** — start/end pairing with validation (end >= start); quick selections (last 7 days) reduce friction.
- **Timezones** — store instants in UTC; render in the user's zone; never store local strings ambiguously.
- **Worked example** — the mykb pulse filter uses native date inputs for simple ranges and a custom calendar for quick presets.
- **Relevance** — date handling connects to the i18n and timezone stubs in RSIS3's wiki.
- **Date-only vs datetime** — pickers must distinguish all-day dates from instants; month grids need disabled-date and min/max semantics communicated to assistive tech.

## Related
- [[wiki/web-platforms/date-formatting|Date Formatting]] — adjacent concept in this wiki
- [[wiki/web-platforms/timezone-formatting|Timezone Handling]] — adjacent concept in this wiki
- [[wiki/web-platforms/locale-data|Locale Data]] — adjacent concept in this wiki
- [[wiki/web-platforms/number-formatting|Number Formatting]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-accessibility|Web Accessibility]] — existing coverage
- [[wiki/mobile-platform/internationalization|Internationalization]] — existing coverage
