---
type: "concept"
title: "WebP vs AVIF"
description: "Comparing modern image codecs for size and quality"
tags: ["images", "formats", "webp", "avif"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# WebP vs AVIF

## Summary

WebP and AVIF are the modern image formats replacing JPEG/PNG: both deliver major byte savings, with AVIF generally winning on compression at the cost of encode time and compatibility. The practical answer is <picture> with both plus JPEG fallback.

## Details
- Mechanism: WebP (VP8/VP9-based) supports lossy/lossless and alpha; AVIF (AV1-based) compresses better, supports HDR/wide-gamut, and higher chroma formats, but encodes several times slower. Both are supported by all evergreen browsers; AVIF's gap is older Safari/iOS versions, making the fallback chain matter.
- Concrete example: a hero JPEG at 300KB becomes ~180KB WebP or ~120KB AVIF at comparable quality; a screenshot-heavy wiki page ships AVIF with WebP and JPEG fallbacks via <picture>, and an encoder pipeline (sharp/cwebp/avifenc) generates all variants at build time.
- Failure modes: choosing format by file size alone — visual quality and artifact types differ (AVIF smoothing vs WebP blocking); transparent and animation cases (WebP anim, AVIF anim) having separate support stories; encode-time costs on large batches delaying CI; and content that must match brand color exactly needing careful profiles.
- Operational tradeoffs: AVIF maximizes savings but complicates the pipeline and fallback markup; WebP is the pragmatic middle. Standard practice: AVIF first, WebP second, JPEG/PNG fallback, with srcset for sizes — and remember quality-per-byte beats format purity: re-encode old JPEGs only where they dominate traffic.
- RSIS3/mykb relevance: the wiki's image pipeline generates AVIF/WebP/JPEG tiers with a quality table documented here, keeping the loop's asset costs bounded.
- Quality calibration: pick quality targets per image type (photos vs screenshots vs graphics) rather than one global setting; screenshots compress differently and the same quality number can look terrible on text-heavy images.
- Pipeline validation: decode-test every encoder output in CI with a real browser to catch corrupt or unsupported files; a format that encodes fine but decodes broken is worse than the size savings.

## Related
- [[wiki/web-platforms/lazy-loading-practice|Lazy Loading in Practice]]
- [[wiki/web-platforms/svg-scaling|SVG Scaling]]
- [[wiki/web-platforms/retina-displays|Retina Displays]]
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]]
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]]
