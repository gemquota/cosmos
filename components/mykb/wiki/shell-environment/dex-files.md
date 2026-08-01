---
type: "concept"
title: "DEX Files"
description: "Dalvik Executable bytecode format executed by ART"
tags: ["dex", "android", "bytecode", "reverse-engineering"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# DEX Files

DEX files hold compiled Java/Kotlin bytecode that ART executes; an APK contains one or more classes.dex. Tools like dexdump, baksmali, and jadx turn DEX into readable forms.
- The multidex format splits large apps into several classes.dex files.
- Android 5.0+ ART compiles DEX ahead of time for performance.
- Smali is the assembly-level representation for patching.
- Obfuscation and reflection make DEX analysis harder.

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — ART executes DEX at runtime
- [[wiki/shell-environment/apk-analysis|APK Analysis]] — DEX lives inside the APK
- [[wiki/android-core/android-ndk|Android NDK]] — native libs sit beside DEX
- [[wiki/android-core/kotlin-language|Kotlin Language]] — Kotlin compiles to DEX
