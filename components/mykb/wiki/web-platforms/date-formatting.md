---
type: "concept"
title: "Date Formatting"
description: "Locale-aware date and time presentation"
tags: ["i18n", "dates", "formatting", "localization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Date Formatting

## Summary

Dates are locale-specific: order, separators, calendars, and era conventions differ. Correct formatting uses Intl.DateTimeFormat or a well-maintained library instead of hand-rolled strings, and stores dates in a timezone-free interchange format.

## Details
- Mechanism: Intl.DateTimeFormat(locale, options) formats from a Date or epoch using CLDR data for the given locale; toLocaleString is the quick form. The key options are dateStyle/timeStyle, hour12, timeZone, and the many field options; timeZone: "UTC" or the user's zone is chosen explicitly, never assumed.
- Concrete example: new Intl.DateTimeFormat("en-GB", { dateStyle: "medium" }).format(d) yields "3 Aug 2026" while "en-US" yields "Aug 3, 2026"; "ar-EG" uses Arabic-Indic digits and a different calendar. The same instant renders differently everywhere by design.
- Failure modes: formatting local time when the stored value is UTC (or vice versa); parsing with new Date("2026-08-03") treating it as UTC while new Date("2026/08/03") is local — inconsistent parsers; locale fallback chains rendering in the wrong language when ICU data is trimmed; and serializing formatted strings back into storage, corrupting round-trips.
- Operational tradeoffs: shipping full CLDR data costs bundle size (tree-shake locales); hand-rolled templates are smaller but wrong in subtle ways. Prefer the platform Intl API, serialize ISO 8601 with timezone (or UTC with an explicit convention), and format only at the display boundary.
- RSIS3/mykb relevance: the wiki's log and synthesis timestamps are stored as ISO-8601 UTC and would be rendered with Intl per reader locale, keeping acquisition records comparable across timezones.
- Relative time: Intl.RelativeTimeFormat handles "3 days ago" with correct plural rules per locale; hand-rolled versions get the units and grammar wrong.
- Timezones in storage: store instants, not wall-clock strings; if a local wall time is meaningful (appointments), store it with its offset or IANA zone explicitly.
- Validation: golden-test each locale's output at build time; a locale whose formatting silently changes (CLDR updates) then surfaces as user-visible inconsistency.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/timezone-formatting|Timezone Handling]]
- [[wiki/web-platforms/i18n-web|Web Internationalization]]
- [[wiki/web-platforms/l10n-practice|Localization Practice]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
