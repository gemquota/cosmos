---
type: "entity"
title: "Local"
description: "Localization (l10n): adapting software for language and regional conventions"
tags: ["entity", "localization", "l10n", "i18n", "frontend"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# Local

## Summary

Local, in the localization sense, is the practice of adapting software to a target language, region, and culture — translating text, formatting dates and numbers, and handling direction and plural rules. It matters because products ship to users worldwide, and unlocalized software breaks trust. Localization sits on top of internationalization, the engineering that makes adaptation possible.

## Details

- **Definition** — Localization (l10n) adapts an internationalized product: user-visible strings, formats, and conventions become appropriate for a specific locale.
- **Internationalization first** — I18n prepares code with externalized strings, locale-aware formatting, and layout flexibility; l10n then fills in translations and regional data.
- **Formatting** — Dates, times, numbers, currencies, and units differ by locale; libraries such as Intl handle these without hand-rolled logic.
- **Plurals and gender** — Languages have different plural categories and agreement rules; message formats with plural selectors handle the complexity.
- **Right-to-left** — Arabic and Hebrew need mirrored layouts; CSS logical properties and bidirectional isolation prevent text-order bugs.
- **Worked example** — A shopping app shows dates as DD/MM/YYYY in the UK, MM/DD/YYYY in the US, and ٢٠٢٦-٠٨-٠٣ in an Arabic locale, all from one format call.
- **Common failure modes** — Concatenated sentences that break grammar, hard-coded strings, images with embedded text, and missing locale fallbacks are classic issues.
- **Practical relevance** — Localization quality affects adoption; regression tests with locale-specific fixtures keep it from decaying.
- **Telemetry note** — The stub explicitly resolves Local to localization, matching the Android and backend sessions where locale bugs surface.
- **Translation workflow** — Extracted strings flow to translators, return as locale files, and load lazily so untranslated locales fall back gracefully.
- **Testing** — Locale fixtures and snapshot tests catch format regressions; automated checks verify every string key resolves in every supported language.
- **Worked example** — A settings screen switches locale at runtime: dates, currencies, and sort order change with the language, and the layout mirrors for RTL locales.

## Related

- [[wiki/frontend/localization|Localization]] — frontend l10n practice
- [[wiki/mobile-platform/localization|Localization]] — mobile l10n specifics
- [[wiki/web-platforms/i18n-web|I18n Web]] — web internationalization
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/frontend-logic|Frontend Logic]] — client-side locale handling
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/next-2|Next 2]] — framework with i18n routing
- [[wiki/testing/api-testing|API Testing]] — locale-aware payload checks
