---
type: "concept"
title: "Internationalization"
description: "Message extraction and i18n framework plumbing"
tags: [i18n", "internationalization", "javascript", "intl", "web-platform"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl", "https://www.w3.org/International/"]
---

# Internationalization

## Summary
Internationalization (i18n) is the engineering that lets an application support multiple languages and regions without code changes. It covers message extraction, plural and gender rules, date, number, and currency formatting, and text expansion headroom. The Intl API provides locale-aware formatting natively, and i18n libraries add message management.

## Details
- Message extraction: UI strings move to resource files with ICU placeholders — {name} — instead of concatenation.
- Plural rules: locales differ (English has two forms, Polish has four); Intl.PluralRules and ICU plurals handle them.
- Formatting: Intl.DateTimeFormat, NumberFormat, and RelativeTimeFormat apply locale conventions for dates, numbers, and units.
- Text expansion: translations run 30-50% longer; UI must reserve space and avoid fixed widths.
- Locale selection: accept-language headers, stored preferences, or URL prefixes determine the active locale.
- Dates and text: avoid storing localized strings in code; treat them as data loaded at runtime.

## Related
- [[wiki/frontend/localization|Localization]] — applying i18n to content and translations
- [[wiki/frontend/rtl-layouts|RTL Layouts]] — layout for right-to-left scripts
- [[wiki/mobile-platform/internationalization|Internationalization]] — the mobile counterpart
- [[wiki/web-platforms/web-standards|Web Standards]] — language and encoding standards
- [[wiki/web-platforms/web-apis|Web APIs]] — the Intl API family
- [[wiki/frontend/frontend-testing|Frontend Testing]] — locale-specific test coverage
