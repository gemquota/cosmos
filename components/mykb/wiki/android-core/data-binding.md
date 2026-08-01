---
type: "concept"
title: "Data Binding"
description: "Declarative binding of layout XML to data with observable expressions"
tags: ["android", "data-binding", "ui", "observables"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Data Binding

Data binding lets layouts bind UI to data directly with expressions like @{viewModel.name}, using observable fields for automatic updates. Android teams now mostly prefer ViewBinding for structure and Compose for reactivity.
- Reduces glue code between XML and Java/Kotlin but adds generated code and build cost.
- Works with LiveData and observable fields to update views when state changes.
- ViewBinding is recommended where only type-safe references are needed.
- Compose data flow replaces most data-binding patterns.

## Related

- [[wiki/android-core/view-binding|View Binding]] — the simpler, type-safe subset that remains recommended
- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]] — binding expressions often target ViewModel state
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — modern declarative replacement
- [[wiki/android-core/livedata|LiveData]] — observable source data binding can consume
