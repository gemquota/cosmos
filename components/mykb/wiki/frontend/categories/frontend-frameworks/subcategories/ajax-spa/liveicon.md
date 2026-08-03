---
type: "entity"
title: "LiveIcon"
description: "AJAX — async web data exchange, Android — mobile development platform, API — service communication interface"
tags: ["entity", "ajax", "android", "api", "ast", "auth"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---


## Liveicon

LiveIcon appears in 1 session(s) categorized as API, Mobile, Security. Related topics: ajax, android, api, auth.

A live icon is an application or notification icon that changes over time or in response to state, rather than remaining static. Animated and adaptive icons give an app a sense of life, conveying activity, progress, or status at a glance.

On Android, adaptive icons are defined as foreground and background layers that the launcher crops and scales into a mask, so the same icon adapts to different device shapes. Live updates can animate the foreground layer, for example a clock whose hands move or a badge that counts unread items. Notification icons can likewise change to reflect progress, with small monochrome images that the system tints.

Live icons are constrained by platform policy: launchers control when and how often animations run, battery and performance limits discourage constant redraw, and accessibility guidelines require that motion not interfere with usability. Icon updates should be lightweight, driven by events rather than polling where possible, and should degrade gracefully to a static representation.

Security appears in the same sessions because live icons are sometimes used to draw attention to sensitive notifications, and the underlying capability, updating app identity, must not be spoofable by other apps. The term connects to the [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/canvastexture|Canvastexture]] entry for rendering techniques and the [[wiki/web-platforms/00-index|Android Core]] domain.

Sessions pair live icon work with canvas rendering and notification handling, and the entry records those connections for reuse in future icon and notification features.

The term is recorded as a capability pattern rather than a specific API, since the details differ by platform while the underlying idea, state expressed through the icon, stays the same.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Frontend Frameworks]] › Liveicon

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ace-10|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrains-10|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/csv-10|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
