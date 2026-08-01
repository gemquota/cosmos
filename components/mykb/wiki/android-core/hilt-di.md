---
type: "concept"
title: "Hilt DI"
description: "Dagger-based dependency injection tuned for Android"
tags: ["android", "di", "dagger", "hilt"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Hilt DI

Hilt is Google dependency-injection library built on Dagger, generating wiring for Android components at compile time. It provides standard scopes, automatic injection into components, and integration with ViewModels and WorkManager.
- @HiltAndroidApp application and @AndroidEntryPoint components bootstrap the graph.
- Modules provide bindings; qualifiers disambiguate same-typed dependencies.
- KSP-based Dagger is faster than the old annotation-processing path.
- DI keeps networking, repositories, and agents testable.

## Related

- [[wiki/android-core/kotlin-language|Kotlin Language]] — Hilt is Kotlin-first
- [[wiki/android-core/room-database|Room Database]] — repositories get database access via DI
- [[wiki/android-core/android-architecture|Android Architecture]] — DI wires the layered architecture
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — injection is a structural pattern
