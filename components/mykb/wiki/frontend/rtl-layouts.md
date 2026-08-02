---
type: "concept"
title: "RTL Layouts"
description: "dir handling and logical properties for right-to-left"
tags: [rtl", "css", "logical-properties", "i18n", "layout"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_logical_properties_and_values", "https://www.w3.org/TR/css-logical-1/"]
---

# RTL Layouts

## Summary
Right-to-left layouts mirror the page for languages like Arabic and Hebrew: text, alignment, and reading order flow right to left. The dir attribute switches document direction, and logical properties (margin-inline-start, text-align: start) adapt automatically where physical left/right values would break. Building with logical values makes RTL support nearly free.

## Details
- Direction model: dir="rtl" on html flips text direction, alignment defaults, and flex/grid main-axis flow.
- Logical properties: inline-start and block-start map to left/right depending on direction, replacing physical padding, margin, and inset.
- Text alignment: text-align: start and end follow direction; physical left/right must be avoided in mirrored UIs.
- Flexbox and grid: row direction reverses automatically; row-reverse and order tricks are usually wrong fixes.
- Mixed content: bidi text (Latin inside Arabic) needs the Unicode Bidirectional Algorithm and dir on isolated spans.
- Icons and arrows: direction-aware icons should mirror; unicode arrows often need swapping.

## Related
- [[wiki/frontend/internationalization|Internationalization]] — locales that require RTL
- [[wiki/frontend/localization|Localization]] — RTL as part of locale delivery
- [[wiki/frontend/box-model|CSS Box Model]] — logical property variants
- [[wiki/frontend/flexbox|Flexbox]] — direction-aware flow
- [[wiki/frontend/responsive-design|Responsive Design]] — RTL across breakpoints
- [[wiki/web-platforms/css-layout|CSS Layout]] — logical values in the platform
