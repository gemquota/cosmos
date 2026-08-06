---
type: "entity"
title: "DPI"
description: "DPI"
tags: ["entity", "acronym", "ajax", "android", "api", "ast"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
status: "growing"
---


## Dpi

DPI appears in 1 session(s) categorized as API, Mobile. Related topics: acronym, ajax, android, api.

DPI stands for dots per inch, a measure of resolution describing how many individual dots or pixels fit into one inch. It is used both for print output and for display density, where it determines how large a given number of pixels appears to the eye.

On Android, density groups such as mdpi, hdpi, xhdpi, and xxhdpi correspond to different DPIs, and the platform scales layout units (dp) and text units (sp) so that interfaces appear physically similar across devices. Assets are provided in multiple density buckets, and the system picks the best-matching resource and scales it, so missing buckets cause blurry or memory-heavy rendering.

Web interfaces face the same problem through the device pixel ratio: a CSS pixel is not the same as a physical pixel on high-density screens, and canvas or image rendering must multiply by the ratio to stay sharp. Responsive images choose different resolutions based on the display, and CSS media queries can vary layout by density as well as by viewport size.

For print and scanning, DPI describes the fidelity of the output or capture, with 300 DPI a common standard for text and 150 DPI for photos. Misunderstanding DPI causes common bugs: oversized downloads, blurry icons, or scaled canvases. The concept connects to the [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/canvastexture|Canvastexture]] entry and the [[wiki/android-core/00-index|Android Core]] domain in this knowledge base.

Testing on a range of densities, from low-end to high-end devices, catches scaling bugs that are invisible on the developer's own monitor.

Asset pipelines generate density variants from a single source image, and tools that automate this reduce the chance of shipping a single-resolution icon to a high-density device.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Frontend Frameworks]] › Dpi

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
