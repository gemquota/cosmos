---
type: "concept"
title: "Internationalization"
description: "Engineering apps so translation and locale adaptation is possible (i18n)"
tags: ["mobile", "internationalization", "unicode", "rtl"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Internationalization

Internationalization is the engineering side: Unicode throughout, locale-aware formatting, RTL layout support, and no hardcoded strings. A clean i18n base makes localization cheap.
- UTF-8 everywhere; format dates, numbers, and currencies per locale.
- Support RTL layouts for Arabic and Hebrew from day one.
- Plurals and gender-aware strings need locale-aware resources.
- Keyboards, fonts, and text input must follow locale.

## Related

- [[wiki/mobile-platform/localization|Localization]] — i18n enables l10n
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — RTL mirrors layout flow
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — reading order and locale interact
- [[wiki/frontend-frameworks/material-design|Material Design]] — the spec covers RTL and type scale
