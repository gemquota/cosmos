---
type: "entity"
title: "Kotlin Multiplatform"
description: "Sharing Kotlin logic across platforms with expect/actual, KMP tooling, and native UIs"
tags: ["kotlin", "multiplatform", "mobile", "shared-logic", "android"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://kotlinlang.org/docs/multiplatform.html", "https://kotlinlang.org/docs/multiplatform-expect-actual.html"]
---
# Kotlin Multiplatform

## Summary
Kotlin Multiplatform (KMP) shares business logic — networking, storage, validation — across Android, iOS, desktop, and web while each platform keeps its native UI. `expect`/`actual` declarations map platform-specific APIs, and the Gradle toolchain builds per-target artifacts.

## Details
- **Shared module** — common code compiles to JVM, native (iOS), and JS/Wasm targets; platform libraries plug in via expect/actual.
- **Ecosystem** — Ktor for networking, kotlinx.serialization, coroutines, and SQLDelight/Realm share data layers.
- **iOS interop** — Kotlin/Native emits Objective-C frameworks consumed by SwiftUI; concurrency rules (new memory model) matter.
- **Compose Multiplatform** — shares UI too, competing with SwiftUI for the presentation layer.
- **Worked example** — the mykb client shares its sync and wiki API client in a KMP module with native UIs per platform.
- **Relevance** — KMP fits RSIS3's logic-heavy, UI-varied architecture.
- **Gradle targets** — the shared module configures jvm(), iosArm64(), iosSimulatorArm64(), and js() targets; the `androidTarget` and cocoapods plugins wire native integration into the build.

## Related
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/i18n-web|Web Internationalization]] — adjacent concept in this wiki
- [[wiki/web-platforms/locale-data|Locale Data]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — existing coverage
- [[wiki/android-core/kotlin-language|Kotlin Language]] — existing coverage
- [[wiki/frontend-frameworks/state-management-mobile|State Management Mobile]] — existing coverage
