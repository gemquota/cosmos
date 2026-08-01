---
type: "concept"
title: "RecyclerView"
description: "Efficient list rendering with view recycling and ViewHolder pattern"
tags: ["android", "lists", "ui", "recyclerview"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# RecyclerView

RecyclerView renders large lists efficiently by recycling item views and pairing them with ViewHolders, driven by adapters and layout managers. It is the classic imperative answer to list performance on Android.
- LayoutManagers (Linear, Grid, StaggeredGrid) control arrangement; DiffUtil computes minimal updates.
- Item decoration, click handling, and nested scrolling are separate concerns.
- LazyColumn in Compose is the declarative successor with the same recycling ideas.
- Large datasets should pair with paging libraries to bound memory.

## Related

- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — LazyColumn is the modern list primitive
- [[wiki/android-core/android-activities|Android Activities]] — lists live inside activity or fragment screens
- [[wiki/android-core/view-binding|View Binding]] — bind item layouts without findViewById
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — list semantics matter to TalkBack
