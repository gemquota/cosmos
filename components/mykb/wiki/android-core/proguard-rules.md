---
type: "concept"
title: "Proguard Rules"
description: "Keep and shrink rules for ProGuard and R8"
tags: ["android", "proguard", "r8", "optimization"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Proguard Rules

ProGuard rules tell the shrinker what to keep: reflection targets, annotations, serialized classes, and JNI-bound symbols. R8 applies them during release builds; wrong rules crash apps at runtime.
- -keep rules protect entry points the compiler cannot see.
- Reflection, Gson, Retrofit models, and JNI need explicit rules.
- Read mapping files to decode obfuscated crash stacks.
- Enable shrinking only with full rule coverage and testing.

## Related

- [[wiki/android-core/r8-obfuscation|R8 Obfuscation]] — R8 consumes these rules
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — shrinking is a hardening layer
- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — rules live in Gradle config
- [[wiki/shell-environment/apk-analysis|APK Analysis]] — inspect what survived shrinking
