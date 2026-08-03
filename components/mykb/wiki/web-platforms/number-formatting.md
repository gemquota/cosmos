---
type: "concept"
title: "Number Formatting"
description: "Locale-aware digit grouping, decimals, and currency display"
tags: ["i18n", "numbers", "formatting", "localization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Number Formatting

## Summary

Number formatting is locale-dependent: decimal separators, digit grouping, currency, percentages, and script-specific digits all differ. Intl.NumberFormat is the correct tool; toFixed and comma-splicing are locale bugs waiting to happen.

## Details
- Mechanism: Intl.NumberFormat(locale, {style, notation, maximumFractionDigits, ...}) uses CLDR data for grouping, separators, and digit systems; notation: "compact" renders 1.2M; currency style places symbols per locale (€10 vs 10 €). The same API handles unit formatting (kilometer, percent).
- Concrete example: (1234567.89).toLocaleString("de-DE") → "1.234.567,89" while "en-IN" → "12,34,567.89"; using a hard-coded comma in a finance app breaks German and Indian users immediately. Compact notation for chart axes must also be localized ("1,2 Mio." in German).
- Failure modes: assuming the browser default locale is the user's (it may be the server's or a default); formatting floats for money (use integer minor units or a decimal library); losing precision with toFixed for large values; and currency conversions — Intl formats, it does not convert, so label the currency explicitly.
- Operational tradeoffs: Intl is standard and tree-shakeable; per-locale data adds bundle weight, so lazy-load locales. Format at the display boundary only, keep canonical numeric values in data, and golden-test each locale's outputs.
- RSIS3/mykb relevance: dashboard metrics render via a shared NumberFormat pipeline; this node defines the locale set and precision rules the loop uses in generated charts.
- Digit systems: Intl renders Arabic-Indic, Devanagari, and other digit sets per locale automatically; manual toLocaleString call sites should all route through the shared formatter.
- Sign and units: negative numbers and unit placement also vary by locale — golden-test them, not just magnitudes.
- Compact notation: chart axes should use notation: compact with locale-aware units; a hard-coded "k" suffix is a localization bug that numbers formatting was built to avoid.
- Precision policy: set maximumFractionDigits per metric type (currency, percentage, raw count) so rounding is consistent across the UI.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/date-formatting|Date Formatting]]
- [[wiki/web-platforms/timezone-formatting|Timezone Handling]]
- [[wiki/web-platforms/i18n-web|Web Internationalization]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
