---
type: "concept"
title: "Cross-Platform Frameworks"
description: "Sharing one codebase across Android and iOS with Flutter, React Native, and Kotlin Multiplatform"
tags: ["cross-platform", "flutter", "react-native", "kmp", "mobile"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://reactnative.dev/", "https://docs.flutter.dev/"]
---

# Cross-Platform Frameworks

## Summary

Cross-platform frameworks let teams ship Android and iOS from one codebase, cutting duplicated UI and logic work. Flutter and React Native are the main contenders, with Kotlin Multiplatform sharing logic while keeping native UI. The right choice depends on team skills, app type, and how much native behavior you need.

## Details

- Flutter compiles Dart and renders its own pixels via Skia/Impeller, giving consistent UI and strong performance at a larger binary size.
- React Native uses JavaScript/TypeScript with native views, close platform fidelity, and the JS ecosystem.
- Kotlin Multiplatform shares business logic and models while leaving UI native per platform.
- Native modules bridge to device APIs - NDK, JNI, and platform channels are the escape hatches when a framework falls short.
- Hot reload makes iteration fast in both Flutter and React Native.
- Decision factors: team language skills, offline-first data needs, performance ceilings, and long-term maintenance.
- RSIS3 relevance: a mykb companion app could share parsing and sync logic through KMP or Flutter while agents stay platform-native.

## Related

- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — Google render-everything toolkit
- [[wiki/frontend-frameworks/react-native-vs-flutter|React Native vs Flutter]] — the head-to-head comparison
- [[wiki/frontend-frameworks/declarative-ui|Declarative UI]] — both major frameworks are declarative
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]] — iteration speed is a selling point
- [[wiki/android-core/android-ndk|Android NDK]] — native escape hatch for framework gaps
- [[wiki/compositions/language-patterns|Programming Languages Reference]] — framework languages span Dart, JS, Kotlin
- [[wiki/web-platforms/entities/web-stack|Web Technology Stack]] — the web is another cross-platform target
