---
type: "entity"
title: "Google Fonts"
resource: ""
---
description: "Serving web fonts from Google's hosted font platform with performance trade-offs"
tags: ["entity", "android", "api", "ast", "auth", "authentication", "fonts", "web-performance"]
timestamp: "2026-07-19T22:41:42Z"

# Google Fonts

## Summary
Google Fonts is a hosted library of open-licensed web fonts, delivered through stylesheets that reference font files on Google's CDN. It matters because typography shapes readability and brand feel, but every font request costs performance and privacy. Teams must weigh the convenience of hosted fonts against self-hosting and careful delivery optimization. Getting the delivery right is as important as choosing the typeface.

## Details
- **Definition** — the service serves font families plus generated CSS that lists formats and unicode ranges for the requesting browser.
- **Delivery** — hosted fonts benefit from global CDN caching, but the browser makes a third-party request that reveals the visitor's origin.
- **Performance** — font files are large; loading strategy, display behavior, and subsetting determine how much layout shift and delay users experience.
- **Font display** — the display parameter controls the swap, block, or fallback behavior while a font loads, trading flash of invisible text against layout stability.
- **Subsetting** — serving only the glyph ranges a page needs cuts payload size dramatically, especially for Latin text.
- **Self-hosting** — downloading the files and serving them from the application's own origin removes third-party requests at the cost of caching and updates.
- **Preconnect** — hinting the browser to connect to the font origin early shaves critical time from the loading path.
- **Licensing** — the library is open-licensed, but teams should confirm the terms fit their product before relying on it.
- **Common failure modes** — loading many weights and styles, missing preconnect hints, and fonts that block rendering.
- **Worked example** — a marketing site preconnects to the font origin, requests two weights with swap display, and subsets to latin to keep the page fast.
- **Practical relevance** — font delivery choices are a visible, measurable part of web performance and privacy.

## Related
- [[wiki/web-platforms/web-fonts|Web Fonts]] — how web fonts work
- [[wiki/web-platforms/font-loading-strategy|Font Loading Strategy]] — load behavior
- [[wiki/web-platforms/font-display-swap|Font Display Swap]] — swap semantics
- [[wiki/web-platforms/variable-fonts|Variable Fonts]] — flexible typefaces
- [[wiki/web-platforms/font-shift|Font Shift]] — layout impact
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — delivery trade-offs
