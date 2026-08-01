---
type: "concept"
title: "JNI"
description: "Java Native Interface bridging Kotlin/Java and native C/C++ code"
tags: ["android", "jni", "native", "interop"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# JNI

JNI is the boundary between Kotlin/Java and native code: native functions are declared with external, implemented in C/C++ with names like Java_com_example_MyClass_method, and marshalled through JNIEnv.
- Primitive and object conversions cross the boundary; keep marshalling minimal.
- Global references need explicit management to avoid leaks.
- JNI crashes can take down the process; prefer safe wrappers.
- Kotlin/Native and JNA are alternatives with different trade-offs.

## Related

- [[wiki/android-core/android-ndk|Android NDK]] — the toolchain JNI targets
- [[wiki/android-core/kotlin-language|Kotlin Language]] — Kotlin declares the external functions
- [[wiki/android-core/memory-leak-patterns|Memory Leak Patterns]] — global refs are a classic native leak
- [[wiki/android-core/android-architecture|Android Architecture]] — native layers of the platform
