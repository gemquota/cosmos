---
type: "concept"
title: "Jetpack Compose"
description: "Declarative Kotlin UI toolkit for Android with automatic recomposition and Material 3"
tags: ["android", "compose", "ui", "declarative", "kotlin"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/develop/ui/compose/documentation"]
---

# Jetpack Compose

## Summary

Jetpack Compose is Android modern UI toolkit: composable functions describe the UI as a pure function of state, and the framework recomposes only what changed. It ships with Material 3 components, tooling previews, and interop with the legacy View system. Compose shifts Android UI work from imperative view mutation to declarative state handling.

## Details

- Composables are Kotlin functions annotated @Composable; state is hoisted via remember and mutableStateOf, and recomposition tracks reads.
- Material 3 integration provides theming, dynamic color, and adaptive components out of the box.
- Navigation Compose, previews, and Compose testing APIs are first-class; baseline profiles and lazy layouts handle performance.
- Interoperability: ComposeView embeds composables in XML layouts and AndroidView embeds classic views, enabling incremental migration.
- Adaptive layouts use window size classes so one codebase covers phones, tablets, and foldables.
- State management patterns (state hoisting, ViewModels, collectAsStateWithLifecycle) replace findViewById-driven imperative code.
- RSIS3 relevance: a dashboard client could be a Compose app consuming mykb over REST or WebSocket, sharing ViewModels with any KMP UI.

## Related

- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — Compose is Android implementation of the declarative model
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — hoisting and ViewModels generalize across toolkits
- [[wiki/mobile-platform/dark-mode-support|Dark Mode Support]] — dynamic color and theme tokens in Compose
- [[wiki/android-core/density-buckets|Density Buckets]] — dp units keep Compose layouts consistent across screens
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — declarative React model parallels Compose
- [[wiki/compositions/dev-workflow|Development Workflow Pattern]] — Compose tooling shapes modern Android workflow
