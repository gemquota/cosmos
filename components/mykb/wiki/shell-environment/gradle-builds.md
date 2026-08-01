---
type: "concept"
title: "Gradle Builds"
description: "Gradle as the Android build system, invoked from CLI and CI"
tags: ["gradle", "android", "build", "ci"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Gradle Builds

Gradle is the Android build system: it compiles, links, packages, signs, and tests apps, driven by Kotlin DSL scripts and the Android Gradle Plugin. It runs from terminals and CI with caching for speed.
- Tasks like assembleDebug, test, and bundleRelease produce artifacts.
- Configuration cache and build cache speed repeated builds.
- Variants (debug/release, flavors) generate build matrices.
- CI signing keeps keystore secrets out of the build log.

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — Gradle assembles the platform app
- [[wiki/android-core/kotlin-language|Kotlin Language]] — the Gradle Kotlin DSL is the standard
- [[wiki/android-core/proguard-rules|Proguard Rules]] — build-time shrinking configuration
- [[wiki/devops-infra/github-actions|GitHub Actions]] — CI runs Gradle on every push
