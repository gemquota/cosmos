---
type: "concept"
title: "Localization"
description: "Translated content, pluralization, and locale formatting"
tags: [l10n", "localization", "translation", "i18n", "content"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.i18next.com/", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules"]
---

# Localization

## Summary
Localization (l10n) adapts an internationalized application to a specific locale: translated strings, locale-correct plurals, date and number formats, and region conventions. Where i18n builds the plumbing, l10n fills it with content. Translation files, locale catalogs, and tooling keep the two sides synchronized.

## Details
- Resource files: JSON or gettext catalogs map keys to translations per locale; fallback chains keep missing keys safe.
- Pluralization: ICU message syntax selects forms by count; Intl.PluralRules classifies the number for the active locale.
- Locale data: CLDR-driven Intl handles dates, currencies, and sorting; collation differs from simple string comparison.
- Quality: machine translation helps, but cultural fit, units, and idioms need human review; pseudolocalization exposes truncation.
- Delivery: loading locale bundles on demand keeps initial payload small; language switchers persist the choice.
- Testing: verify each locale for truncation, encoding, RTL layout, and number/date correctness — not just translation presence.

## Related
- [[wiki/frontend/internationalization|Internationalization]] — the plumbing localization fills
- [[wiki/frontend/rtl-layouts|RTL Layouts]] — script direction in localized UIs
- [[wiki/mobile-platform/localization|Localization]] — the mobile counterpart
- [[wiki/frontend/frontend-testing|Frontend Testing]] — locale-aware test coverage
- [[wiki/web-platforms/web-standards|Web Standards]] — encoding and language standards
- [[wiki/frontend/design-tokens|Design Tokens]] — text expansion-aware spacing
