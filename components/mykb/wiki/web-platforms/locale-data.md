---
type: "concept"
title: "Locale Data"
description: "CLDR datasets powering number, date, and plural rules per locale"
tags: ["i18n", "locale", "cldr", "data"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Locale Data

## Summary

Locale data is the CLDR-backed dataset — number formats, calendars, plural rules, collation, timezones — that Intl APIs rely on. Its size, loading strategy, and correctness determine whether formatting code is accurate and affordable.

## Details
- Mechanism: browsers embed ICU/CLDR; Intl.NumberFormat, DateTimeFormat, PluralRules, and Collator read that data per locale. In Node, ICU coverage can be partial (small-icu), silently degrading formatting; bundlers must decide how much locale data ships to the client.
- Concrete example: Node's default builds include full ICU, but minimal builds (NODE_ICU_DATA or small-icu) format dates in English only — a subtle production bug. In the browser, importing @formatjs/intl-locale with only the needed locale data keeps bundles small while toLocaleString stays correct.
- Failure modes: assuming every runtime has full locale data; shipping all locales (megabytes) when users need three; data version drift between server and client producing different formats for the same input; and locale identifiers that alias (zh vs zh-Hans vs zh-CN) resolving to different datasets.
- Operational tradeoffs: correctness wants full data; performance wants subsets. Load per-locale data lazily, pin ICU versions across serverless environments, and write golden tests per supported locale so formatting regressions are caught at build time.
- RSIS3/mykb relevance: the wiki dashboard formats timestamps and numbers with a pinned Intl setup; this node records the ICU/CLDR loading strategy so future loops reuse it instead of rediscovering small-icu surprises.
- Golden tests: snapshot Intl output for every supported locale at build time so ICU upgrades or data drift fail CI instead of production.
- Server-client parity: format on one tier when possible; if both format, pin the same ICU version so a timestamp shown in an email matches the page.
- Node builds: confirm full-icu in the runtime image or bundle the locale data explicitly; a small-icu Node silently formats dates in English for every locale.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/message-formatting|Message Formatting]]
- [[wiki/web-platforms/plural-rules|Plural Rules]]
- [[wiki/web-platforms/number-formatting|Number Formatting]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
