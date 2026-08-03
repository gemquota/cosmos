---
type: "concept"
title: "Plural Rules"
description: "Locale-dependent plural categories such as one, few, and many"
tags: ["i18n", "plurals", "grammar", "localization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Plural Rules

## Summary

Plural rules select grammatical forms by count — English has one/other, Russian one/few/many/other, Arabic six forms — and only CLDR data can get them right. Intl.PluralRules plus ICU MessageFormat are the standard implementation.

## Details
- Mechanism: Intl.PluralRules(locale).select(n) returns the category for that count (zero, one, two, few, many, other); the categories and thresholds come from CLDR per language. MessageFormat templates use {n, plural, one {...} other {...}} to pick the right string, with =0/=1 exact-value overrides.
- Concrete example: "{n} {n, plural, one {item} other {items}}" works for English but fails Russian, where 1 → one, 2-4 → few, 5-21 → many, and 22-24 → few again; a naive n === 1 ? singular : plural branch renders "5 товар" instead of "5 товаров".
- Failure modes: hand-coding singular/plural branches; using plural rules for languages with no plural distinction (Japanese, Chinese — always other); ordinal rules (1st/2nd) being a separate CLDR dataset; formatting plurals in one locale and reusing the string elsewhere; and counts that are floats or negative needing their own category behavior.
- Operational tradeoffs: correct plurals require translator-authored forms per category — a real process cost, since translators must understand CLDR categories. Tooling (FormatJS, gettext's plural forms) generates the right branch count; validate with a rule table per locale rather than trusting intuition.
- RSIS3/mykb relevance: the wiki UI pluralizes "N notes/syntheses" through Intl.PluralRules; this node pins the supported locales and their category counts for loop-generated copy.
- Zero handling: many languages collapse 0 into other or one; CLDR's =0 override exists exactly for product copy like "no items", so decide per message whether 0 deserves its own form.
- Tooling: gettext uses nplurals/plural forms per language and can precompute branch counts; keep the category table visible in the catalog so translators see which forms are required.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/number-formatting|Number Formatting]]
- [[wiki/web-platforms/date-formatting|Date Formatting]]
- [[wiki/web-platforms/timezone-formatting|Timezone Handling]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
