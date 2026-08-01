---
type: "concept"
title: "Kotlin Language"
description: "Statically typed JVM language with null safety and coroutines, the official Android language"
tags: ["kotlin", "language", "android", "jvm", "coroutines"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://kotlinlang.org/docs/home.html"]
---

# Kotlin Language

## Summary

Kotlin is a statically typed language by JetBrains that runs on the JVM and is the official language for Android development. It adds null safety, data classes, extension functions, and structured concurrency while remaining fully interoperable with Java. Kotlin Multiplatform extends the same code to iOS, web, and native targets.

## Details

- Null safety is enforced in the type system: nullable types use ?, with safe calls, the elvis operator, and smart casts eliminating most NPEs.
- Data classes, sealed classes, destructuring, and extension functions cut boilerplate compared with Java.
- Coroutines provide structured concurrency with suspend functions and dispatchers, the foundation of modern Android networking and DB code.
- Interoperability: Kotlin and Java call each other directly; annotation processing runs through kapt or the faster KSP.
- The K2 compiler and Kotlin Multiplatform let business logic compile to JVM, native, and JS targets while keeping platform UIs separate.
- Tooling includes the Gradle Kotlin DSL, detekt/ktlint for style, and Compose compiler integration.
- RSIS3 relevance: a Kotlin companion app could share parsing and sync logic with the JVM-side mykb tooling via shared modules.

## Related

- [[wiki/android-core/kotlin-coroutines|Kotlin Coroutines]] — structured concurrency is Kotlin core for Android
- [[wiki/android-core/kotlin-flows|Kotlin Flows]] — reactive streams built on coroutines
- [[wiki/android-core/hilt-di|Hilt DI]] — Kotlin-first dependency injection for Android
- [[wiki/compositions/language-patterns|Programming Languages Reference]] — Kotlin sits in the language landscape
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Ecosystem]] — both are pragmatic typed languages for app UIs
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — Kotlin idioms reshape classic patterns
