---
type: "concept"
title: "Android NDK"
description: "Native Development Kit for C/C++ code compiled per Android ABI"
tags: ["android", "ndk", "native", "c++"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Android NDK

The NDK compiles C and C++ into native libraries packaged per ABI (arm64-v8a, armeabi-v7a, x86_64), called from Kotlin/Java through JNI. Use it for performance-critical or reused C/C++ code, not general app logic.
- CMake builds native libs; Gradle wires them into APKs and app bundles.
- ABIs inflate size - ship only what devices need.
- JNI bridges the type systems; keep boundaries small.
- Crash symbolization needs native debug info (NDK stack, symbol files).

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — native libs sit below the framework
- [[wiki/android-core/jni|JNI]] — the Kotlin-to-native bridge
- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — CMake and Gradle coordinate native builds
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — native escape hatch for framework apps
