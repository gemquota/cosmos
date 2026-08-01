---
type: "concept"
title: "View Binding"
description: "Type-safe generated references to Views, replacing findViewById"
tags: ["android", "view", "binding", "ui"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# View Binding

View binding generates a Binding class for each XML layout whose fields reference every view with an ID, eliminating findViewById casts and null checks. It is null-safe and faster than data binding expressions.
- Enabled per module with buildFeatures { viewBinding true }.
- Preferred over findViewById for type safety and less boilerplate.
- Use activity.setContentView(binding.root) and inflate lists with binding in adapters.
- For declarative UIs, Jetpack Compose largely removes the need for it.

## Related

- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — declarative replacement for view-based binding
- [[wiki/android-core/android-activities|Android Activities]] — binding connects activity code to layout XML
- [[wiki/android-core/data-binding|Data Binding]] — expression-based alternative now superseded
- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — viewBinding is enabled through build configuration
