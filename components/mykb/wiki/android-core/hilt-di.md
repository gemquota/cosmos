---
type: "entity"
title: "Hilt DI"
description: "Dagger-based dependency injection tuned for Android"
tags: ["android", "di", "dagger", "hilt"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://dagger.dev/hilt/", "https://developer.android.com/training/dependency-injection/hilt-android"]
---

# Hilt DI

## Summary


## Details
- Hilt is the dependency-injection framework for Android built on Dagger, generating the graph at compile time so missing dependencies fail the build, not the runtime.
- Modules declare providers, components scope objects (singleton, activity, fragment, view model), and qualifiers disambiguate bindings.
- Hilt integrates with Android's lifecycle: it can inject into activities, fragments, services, ViewModels, and even WorkManager workers.
- The cost is build-time code generation and a learning curve around scoping rules; the payoff is explicit, testable wiring.
- **Worked example / comparison** — Worked example — a repository annotated @Singleton is provided by a module; an activity and a ViewModel both request it and receive the same instance, with no manual wiring.
- For mykb, Hilt is documented as the dependency-injection standard in the android-core cluster, with links to the DI concepts it implements.

## Related
- [[wiki/android-core/kotlin-language|Kotlin Language]]
- [[wiki/android-core/room-database|Room Database]]
- [[wiki/android-core/android-architecture|Android Architecture]]
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/concepts/decision-guides|Decision Guides]]
