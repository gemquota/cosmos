---
type: "concept"
title: "Data Binding"
description: "Declarative binding of layout XML to data with observable expressions"
tags: ["android", "data-binding", "ui", "observables"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/libraries/data-binding", "https://developer.android.com/reference/androidx/databinding/package-summary"]
---

# Data Binding

## Summary


## Details
- Data binding links UI elements to data sources declaratively in the layout, using expressions like @{user.name}, and updates the UI when the underlying data changes.
- It reduces glue code between view and logic but adds build-time code generation, so compile errors surface as generated-source problems.
- Observable fields, LiveData, and two-way binding keep views in sync; the expression language supports a useful subset of Java/Kotlin.
- Teams often use view binding instead when they only need type-safe view access and not the full expression machinery.
- **Worked example / comparison** — Worked example — a layout binds a user object's name into a TextView via @{user.name}; when the user field updates, the binding refreshes the view automatically.
- For mykb, data-binding is documented alongside view-binding so readers can choose the right mechanism for their screen.

## Related
- [[wiki/android-core/view-binding|View Binding]]
- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]]
- [[wiki/android-core/jetpack-compose|Jetpack Compose]]
- [[wiki/android-core/livedata|LiveData]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/concepts/decision-guides|Decision Guides]]
