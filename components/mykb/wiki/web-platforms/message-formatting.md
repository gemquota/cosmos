---
type: "concept"
title: "Message Formatting"
description: "ICU message syntax for interpolating translated strings with placeholders"
tags: ["i18n", "strings", "formatting", "localization"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Message Formatting

## Summary

Message formatting turns translated templates with placeholders into final strings using ICU MessageFormat syntax — handling plurals, gender, and embedded values without concatenation. It is the correct successor to string interpolation in i18n'd apps.

## Details
- Mechanism: ICU MessageFormat templates like "{count, plural, one {# item} other {# items}}" compile into formatter functions; intl-messageformat and FormatJS implement it in JS. Values are injected as data, and plural/select rules come from CLDR for the target locale.
- Concrete example: "You have {count, plural, =0 {no messages} one {1 message} other {# messages}}" renders correctly in Russian (three plural forms), Arabic (six), and English (two) from the same template — a concatenation approach fails all but English.
- Failure modes: writing plurals by hand per locale; injecting HTML into messages (escape at the boundary or use rich-text syntax); nesting plural inside select incorrectly; forgetting that ordinals and currency have their own CLDR rules; and translator tools mangling the ICU syntax if the catalog is not validated.
- Operational tradeoffs: MessageFormat is more complex than interpolation but is the only maintainable route to correct plurals; keep templates validated (lint in CI), extract them to catalogs, and render at the boundary — never store formatted strings.
- RSIS3/mykb relevance: the wiki UI formats counts and dates through a shared message pipeline; this node pins the ICU syntax subset the loop is allowed to use in generated UI.
- Rich text: use ICU's rich-text tags or placeholders for links inside messages, and escape at render; never interpolate raw HTML into a formatted message.
- Validation: add a CI lint that compiles every catalog entry with intl-messageformat so a translator's syntax slip fails the build.
- Context metadata: give translators character limits and UI context per message; the formatted result is only as good as the constraints the translator knew about.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/plural-rules|Plural Rules]]
- [[wiki/web-platforms/number-formatting|Number Formatting]]
- [[wiki/web-platforms/date-formatting|Date Formatting]]
- [[wiki/mobile-platform/internationalization|Internationalization]]
- [[wiki/mobile-platform/localization|Localization]]
- [[wiki/web-platforms/web-standards|Web Standards]]
