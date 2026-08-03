---
type: "concept"
title: "Web Internationalization"
description: "Designing web apps for multiple languages, scripts, and regions"
tags: ["i18n", "web", "localization", "design"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Web Internationalization

## Summary

Internationalization (i18n) on the web means engineering for locales from the start: locale-aware data handling, flexible layout, and text that is not hard-coded. It is the architecture; localization (l10n) is the translation that fills it.

## Details
- Mechanism: i18n covers resource loading per locale, number/date/plural formatting (Intl), text direction (LTR/RTL) via logical properties, and layout elasticity for longer or shorter strings. Locale identifiers (en-US, zh-Hans, ar-EG) select formatting rules and translation catalogs.
- Concrete example: a dashboard that formats 12,345.67 as "12,345.67" in en-US, "12 345,67" in de-DE, and "١٢٬٣٤٥٫٦٧" in ar-EG uses Intl.NumberFormat rather than toFixed/commas; a sidebar using width: 200px breaks with German strings, while flex + logical properties reflows.
- Failure modes: string concatenation ("Hello, " + name) that breaks word order in other languages; hard-coded English in JS; images with embedded text; encoding bugs from assuming UTF-8 input; and pseudo-localization skipped, so long translations blow up layouts late.
- Operational tradeoffs: i18n is cheaper to retrofit early — the painful part is finding every hard-coded assumption, not the plumbing. Ship pseudo-locales and test RTL mirrors; keep source strings in one catalog and treat user-visible text as data.
- RSIS3/mykb relevance: wiki notes store locale-sensitive fields with Intl at render time, and the dashboard runs a pseudo-locale pass to catch layout breaks before release.
- Bundle strategy: load locale data lazily per region instead of shipping every Intl dataset; tree-shaken CLDR keeps startup fast while coverage stays complete for served locales.
- String discipline: keep templates free of literals (except structural punctuation), use ICU message syntax for plurals/gender, and give translators character-limit metadata so long translations are caught in review.
- Locale selection: resolve the user's locale from accept-language with a curated allowlist and a documented fallback chain; serving an unsupported locale with broken formatting is worse than a clean fallback.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/l10n-practice|Localization Practice]]
- [[wiki/web-platforms/locale-data|Locale Data]]
- [[wiki/web-platforms/message-formatting|Message Formatting]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
