---
type: "concept"
title: "Declarative UI"
description: "Describing UI as a function of state instead of mutating views"
tags: ["ui", "declarative", "state", "framework"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Declarative UI

Declarative UI frameworks render a view tree from state and update it automatically when state changes. Compose, SwiftUI, Flutter, and React all follow this model, replacing imperative findViewById-style code in which the developer manually locates a view and mutates its properties. Instead of describing how to change the screen, the developer describes what the screen should look like for any given state.

- State changes trigger recomputation of the affected UI. The framework reruns the component or composable that depends on the changed state, producing a new description of the view tree.
- The framework diffs and updates minimal parts of the tree. A reconciliation pass compares the new description with the previous one and applies only the differences, which keeps updates cheap even when the whole tree is recomputed.
- Fewer state-sync bugs than imperative mutation. Because the view is derived from state, there is no separate list of UI properties to keep in sync, and the framework guarantees that the screen matches the model.
- Performance requires discipline: hoisting and stability. State should be hoisted to the level where it is shared, expensive computations should be memoized, and stable keys help the diffing algorithm reuse nodes instead of rebuilding them.

The model changes how developers think about UI: the view becomes a pure function of state, and interactivity becomes state updates. Event handlers set new state, and the framework does the rest. Side effects are handled explicitly, through effects that run after rendering rather than through inline mutation.

This approach has become the default for new UI work across platforms, and the related notes below connect it to the specific toolkits: Jetpack Compose on Android, SwiftUI on Apple platforms, Flutter for Dart, and the state-management patterns that supply the state half of the model.



Adoption is driven by the same problems imperative UI made painful: state that is updated in several places, views that silently disagree with the model, and tests that must drive a complex widget tree to verify simple behavior. Declarative frameworks replace those with a single source of truth and render logic that can be unit-tested directly. The trade-off is a new mental model and a learning curve, but for new projects the model has become the default choice.
## Related

- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — Android declarative toolkit
- [[wiki/mobile-platform/swiftui|SwiftUI]] — Apple declarative toolkit
- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — Dart declarative toolkit
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — the state half of the model
