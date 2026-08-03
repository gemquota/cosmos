---
type: "entity"
title: "LOC"
description: "Localization (l10n)"
tags: ["acronym", "ast", "auth", "aws", "bash", "bootstrap", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
status: "growing"
---

## Loc 2

Localization (l10n) — the adaptation of software for specific languages and cultural contexts.

Localization is the process of adapting a product for a particular locale, while internationalization (i18n) is the engineering that makes adaptation possible. A well-internationalized application keeps every user-facing string in resource files, formats dates, numbers, and currencies through locale-aware APIs, and avoids hard-coded assumptions about text direction or layout.

Translation is only part of the work. Locales differ in date formats, number and decimal separators, currency symbols and positions, plural rules, and sorting order. A translation can be technically accurate but unusable if the UI breaks because strings grew longer, or if plurals are handled with naive concatenation instead of locale-aware plural rules.

Technical infrastructure includes resource files keyed by message IDs, key-value stores per locale, fallback chains when a locale is incomplete, and pseudo-localization to catch layout problems early. Right-to-left languages require mirroring the interface, which is handled with logical properties in CSS rather than hard-coded left and right values.

Tooling keeps localization flowing: extraction of strings from code, translation management systems, and automated checks for missing or unused keys. Localization also affects compliance and trust, since users interact with the product in their own language. The entry sits in the [[wiki/web-platforms/00-index|Security]] and [[wiki/web-platforms/00-index|Authentication]] domains of this knowledge base, where localized messages and error text also carry security meaning.

Localization is never finished: new strings, new locales, and new cultural conventions keep the process alive, and the wiki records it as a practice rather than a one-time task.

Quality gates in CI, such as checking that every locale file parses and that translations do not truncate, keep localization defects out of releases.

**Domain:** Security & Authentication › [[wiki/web-platforms/00-index|Security]] › [[wiki/web-platforms/00-index|Authentication]]

## Related Entities

- [[wiki/security/categories/authentication/audit-hash|Audit Hash]]
- [[wiki/security/categories/authentication/baxdxuoc|Baxdxuoc]]
- [[wiki/security/categories/authentication/blizkl9u|Blizkl9U]]
- [[wiki/security/categories/authentication/bmxbydqu|Bmxbydqu]]
- [[wiki/security/categories/authentication/canvasrenderer-2|Canvasrenderer 2]]
- [[wiki/security/categories/authentication/cbvrzdvz|Cbvrzdvz]]
- [[wiki/security/categories/authentication/ccdy9tdr|Ccdy9Tdr]]
- [[wiki/security/categories/authentication/chlxaaiu|Chlxaaiu]]
