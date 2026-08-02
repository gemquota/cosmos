---
type: "concept"
title: "View Binding"
description: "Type-safe generated references to Views, replacing findViewById"
tags: ["android", "view", "binding", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/topic/libraries/view-binding", "https://www.geeksforgeeks.org/view-binding-in-android-jetpack/"]
---

# View Binding

## Summary


## Details
- View binding generates a Binding class for each layout, exposing typed references to every view that has an ID, so findViewById and manual casting disappear.
- It is null-safe by construction: only views with IDs are referenced, and the generated class matches the layout exactly at build time.
- Binding instances should be created and released with the screen lifecycle (for example, set to null in onDestroyView) to avoid leaks.
- It differs from data binding: view binding is a lightweight, type-safe alternative to findViewById and does not evaluate binding expressions.
- **Worked example / comparison** — Worked example — activity_main.xml generates ActivityMainBinding; inflate once, then access binding.buttonSave and binding.editTextName without casts.
- For mykb, view-binding is documented as the modern replacement for findViewById and as the simpler sibling of data-binding.

## Related
- [[wiki/android-core/jetpack-compose|Jetpack Compose]]
- [[wiki/android-core/android-activities|Android Activities]]
- [[wiki/android-core/data-binding|Data Binding]]
- [[wiki/shell-environment/gradle-builds|Gradle Builds]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/ai-ml/article-health-scores|Article Health Scores]]
- [[wiki/data-storage/code-in-wiki|Code in the Wiki]]
