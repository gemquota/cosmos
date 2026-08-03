---
type: "concept"
title: "DP vs PX"
description: "Density-independent pixels and scale-independent pixels for text"
tags: ["android", "density", "units", "layout"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# DP vs PX

dp (density-independent pixels) normalizes sizes across screen densities: 1dp is 1px on mdpi and 4px on xxxhdpi. sp scales text with the user font-size setting, so text uses sp and geometry uses dp.
- Converting: px = dp * density, where density is the bucket factor.
- Use sp for text so accessibility font scaling works.
- Never mix: fixed px layouts break on high-density screens.
- Compose uses dp by default; sp maps to text units.

## Details

- **Density model** — Android groups screens into density buckets (mdpi = 1x, hdpi = 1.5x, xhdpi = 2x, xxhdpi = 3x, xxxhdpi = 4x); `px = dp * density` is the conversion, and the resource system (dimens.xml, drawable buckets, `sw<N>dp` qualifiers) picks the right variant for the device's bucket, so one layout scales across a 4-inch phone and a 12-inch tablet.
- **Why dp exists** — a fixed 100px button is physically tiny on a high-density phone and huge on a low-density one; dp normalizes to physical size, so a 100dp button occupies roughly the same physical footprint everywhere; the cost is that dp does not adapt to screen size, only density — a 400dp layout is fine on a phone but cramped on a tablet unless width qualifiers or Compose adaptive layouts handle the difference.
- **sp for text** — sp (scale-independent pixels) is dp plus the user's font-size preference: text at 14sp grows when the user picks 'large font', which is an accessibility requirement, not a nice-to-have; the platform applies the scale factor automatically, but only when the unit is sp — hardcoded px or dp text silently ignores the user's setting and fails accessibility audits.
- **Conversion pitfalls** — do not hardcode px, and do not round-trip dp to px at runtime when a resource or Compose API exists for it; the classic bugs are converting with the wrong density (using a fixed 2x factor for all devices), truncating to int too early (1.5dp rounding errors accumulate), and mixing sp and dp for the same text, which breaks layout when the user changes font size.
- **Failure modes** — layouts built in px look correct only on the design device; text in dp overflows or clips on devices with large font settings; and `density` is not a constant — it reflects the display, so anything computed from it must be recomputed on configuration change (screen size, display cutout, multi-window).
- **Compose** — Jetpack Compose uses dp by default for layout and sp for text units; the same density rules apply, with `LocalDensity` providing the current conversion factors; tests should run at multiple densities (mdpi, xxhdpi) and at maximum font scale to catch unit mistakes early.
- **mykb relevance** — the same lesson generalizes: any UI artifact the wiki documents (dashboard embeds, web views) should specify units that adapt to the viewing context rather than fixed pixels, keeping accessibility and density variation first-class.


## Related
- [[wiki/android-core/density-buckets|Density Buckets]] — dp values select bucket resources
- [[wiki/frontend-frameworks/responsive-design|Responsive Design]] — density independence is foundational
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — sp text honors user font settings
- [[wiki/frontend-frameworks/material-design|Material Design]] — the spec is written in dp and sp
