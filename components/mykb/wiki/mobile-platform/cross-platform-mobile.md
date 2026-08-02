---
type: "concept"
title: "Cross-Platform Mobile"
description: "Sharing code across iOS and Android: React Native, Flutter, KMP, and the trade-offs"
tags: ["mobile", "cross-platform", "react-native", "flutter", "kotlin"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://reactnative.dev/", "https://flutter.dev/"]
---
# Cross-Platform Mobile

## Summary
Cross-platform frameworks let one codebase target iOS and Android: React Native renders native views from JavaScript, Flutter draws everything with its own engine, and Kotlin Multiplatform shares logic while keeping native UIs. The choice trades team skills, UI fidelity, and platform access.

## Details
- **React Native** — JavaScript/TypeScript with native rendering; a huge ecosystem and native modules bridge platform APIs; the New Architecture improves interop and performance.
- **Flutter** — Dart with its own rendering engine (Impeller/Skia); pixel-identical UI on both platforms and excellent design-token support.
- **Kotlin Multiplatform** — shares business logic and networking across platforms while each platform keeps native UI (Compose/SwiftUI).
- **Trade-offs** — shared code cuts cost but adds abstraction layers; platform features (widgets, accessibility, OS integrations) arrive later.
- **Worked example** — the mykb mobile companion could share the data layer across platforms while rendering native lists per platform.
- **Relevance** — RSIS3's mobile presence should weigh a shared data layer (KMP) against fully shared UI (Flutter/RN).

## Related
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]] — adjacent concept in this wiki
- [[wiki/web-platforms/dvh-svh|Dynamic and Small Viewport Units]] — adjacent concept in this wiki
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — existing coverage
- [[wiki/frontend-frameworks/react-native-vs-flutter|React Native vs Flutter]] — existing coverage
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — existing coverage
