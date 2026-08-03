---
type: "concept"
title: "Localization Practice"
description: "Translating, adapting, and testing content for specific locales"
tags: ["localization", "i18n", "web", "practice"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Localization Practice

## Summary

Localization practice is the operational side of i18n: managing translation catalogs, quality, and release flow so every locale ships on time and stays correct. It fails on process, not on translation memory.

## Details
- Mechanism: source strings live in catalog files (JSON/PO/XLIFF) keyed by message id; translators edit the catalog; the app loads the right catalog per locale and formats with Intl. Pseudo-locales (e.g. "en-XA") and translation extraction tools (gettext, i18next, FormatJS) keep strings in sync with code.
- Concrete example: a dashboard adding a new metric label extracts the string, sends the catalog for translation, and blocks release until the pseudo-locale check passes; a missed extraction would ship English in 12 locales, so CI fails on untranslated keys.
- Failure modes: untranslated strings silently falling back to English (decide and enforce fallback policy); pluralization and gender handled by concatenation; translators lacking context (screenshots, character limits) producing wrong-length strings; and locale bloat — shipping 50 full catalogs when users need 5.
- Operational tradeoffs: translation is a pipeline with SLA and ownership; in-house vs vendor, per-release vs continuous all trade cost for freshness. Automate extraction and key checks, review translated strings in the real UI (screenshots), and treat missing keys as release blockers.
- RSIS3/mykb relevance: the wiki UI ships its small catalog with a CI check for untranslated keys, documented here so the acquisition loop reuses the practice for new surfaces.
- Fallback policy: define a single fallback locale and a visible marker (e.g. dev-only tooltip) for missing keys; silent English fallback hides gaps until users report them.
- Release cadence: schedule translation slots per release and keep string freeze early; continuous delivery pairs with a translations repository that updates independent of code deploys.
- Pseudo-locale gates: run pseudo-locale builds in CI to catch string-concatenation and layout breaks before real translators spend effort; the pseudo-locale is the cheapest translation test.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/locale-data|Locale Data]]
- [[wiki/web-platforms/message-formatting|Message Formatting]]
- [[wiki/web-platforms/plural-rules|Plural Rules]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
