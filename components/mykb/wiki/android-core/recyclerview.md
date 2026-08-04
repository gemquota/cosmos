---
type: "entity"
title: "RecyclerView"
description: "Efficient list rendering with view recycling and ViewHolder pattern"
tags: ["android", "lists", "ui", "recyclerview"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/develop/ui/views/layout/recyclerview", "https://developer.android.com/reference/androidx/recyclerview/widget/RecyclerView"]
---

# RecyclerView

## Summary


## Details
- RecyclerView renders large lists by recycling item views: a fixed pool of ViewHolders is reused as items scroll, so memory stays flat regardless of list length.
- LayoutManagers (Linear, Grid, StaggeredGrid) arrange items; adapters map data positions to ViewHolders; DiffUtil computes minimal update operations.
- Item decorations, click handling, and nested scrolling are separate concerns, which keeps the core component focused and testable.
- Paging libraries pair with RecyclerView to bound the data set itself, not just the views, for very large collections.
- **Worked example / comparison** — Worked example — a chat history screen recycles message rows; as rows scroll off, their ViewHolders are rebound with the next messages, and DiffUtil dispatches only the changed rows on update.
- For mykb, RecyclerView is the classic imperative answer to Android list performance; its article is evergreen except for API drift.

## Related
- [[wiki/android-core/jetpack-compose|Jetpack Compose]]
- [[wiki/android-core/android-activities|Android Activities]]
- [[wiki/android-core/view-binding|View Binding]]
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/software-engineering/performance-engineering|Performance Engineering]]
