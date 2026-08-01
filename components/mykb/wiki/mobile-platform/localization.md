---
type: "concept"
title: "Localization"
description: "Adapting app content to languages and locales (l10n)"
tags: ["mobile", "localization", "i18n", "languages"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Localization

Localization adapts an app strings, plurals, dates, and layout to target locales. Android string resources and iOS .strings/String Catalogs keep translated text out of code.
- Extract all user-visible strings into resource catalogs.
- Handle plural rules per locale - they are not always plural+s.
- Text length changes break layouts; design flexible containers.
- Localize store listings and screenshots for each market.

## Related

- [[wiki/mobile-platform/internationalization|Internationalization]] — l10n builds on i18n foundations
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — locale affects reading order and font choice
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — translated text must reflow
- [[wiki/mobile-platform/app-store-optimization|App Store Optimization]] — localized listings convert better
