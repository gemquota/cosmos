---
type: "concept"
title: "Internationalization"
description: "Engineering apps so translation and locale adaptation is possible (i18n)"
tags: ["mobile", "internationalization", "unicode", "rtl"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Internationalization

Internationalization is the engineering side: Unicode throughout, locale-aware formatting, RTL layout support, and no hardcoded strings. A clean i18n base makes localization cheap.
- UTF-8 everywhere; format dates, numbers, and currencies per locale.
- Support RTL layouts for Arabic and Hebrew from day one.
- Plurals and gender-aware strings need locale-aware resources.
- Keyboards, fonts, and text input must follow locale.

## Engineering Layers

- **Encoding**: store and exchange text as Unicode, normalizing where needed, so every script round-trips safely.
- **Formatting**: use CLDR-based formatters for dates, times, numbers, and currencies instead of hand-rolled string concatenation.
- **Resources**: externalize user-facing strings into keyed catalogs; translate catalogs, never code.
- **Layout**: separate logical text direction from visual layout so RTL mirrors without special-casing.

## Mobile-Specific Notes

- Locale can change at runtime; configurations, caches, and formatted output must react to the new locale.
- Text input must follow the active locale: keyboard layout, autocomplete, and IME handling.
- Test with pseudo-locales and a short RTL language early, because layout bugs are cheaper to fix before translation begins.

## Locale Data and Testing

- CLDR (Common Locale Data Repository) supplies the canonical patterns for dates, numbers, and plural rules; rely on it instead of hand-maintained tables.
- Test early with pseudo-locales and a right-to-left language; layout and truncation bugs surface long before translation begins.
- Keep locale metadata in one place — a locale registry — so adding a language is a data change, not a code change.

## Related

- [[wiki/mobile-platform/localization|Localization]] — i18n enables l10n
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — RTL mirrors layout flow
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — reading order and locale interact
- [[wiki/frontend-frameworks/material-design|Material Design]] — the spec covers RTL and type scale
- [[wiki/frontend/internationalization|Frontend Internationalization]] — web counterpart
- [[wiki/frontend/rtl-layouts|RTL Layouts]] — direction-aware layout details

## Related

- [[wiki/mobile-platform/localization|Localization]] — i18n enables l10n
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — RTL mirrors layout flow
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — reading order and locale interact
- [[wiki/frontend-frameworks/material-design|Material Design]] — the spec covers RTL and type scale
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — layouts that follow locale and screen size
- [[wiki/frontend/accessibility-testing|Accessibility Testing]] — validating reading order and contrast
