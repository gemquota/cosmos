---
type: "concept"
title: "Declarative UI"
description: "Describing UI as a function of state instead of mutating views"
tags: ["ui", "declarative", "state", "framework"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Declarative UI

Declarative UI frameworks render a view tree from state and update it automatically when state changes. Compose, SwiftUI, Flutter, and React all follow this model, replacing imperative findViewById-style code.
- State changes trigger recomputation of the affected UI.
- The framework diffs and updates minimal parts of the tree.
- Fewer state-sync bugs than imperative mutation.
- Performance requires discipline: hoisting and stability.

## Related

- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Android declarative toolkit
- [[wiki/mobile-platform/swiftui|SwiftUI]] — Apple declarative toolkit
- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — Dart declarative toolkit
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — the state half of the model
