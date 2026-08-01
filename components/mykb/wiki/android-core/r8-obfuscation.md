---
type: "concept"
title: "R8 Obfuscation"
description: "The default Android shrinker and obfuscator"
tags: ["android", "r8", "obfuscation", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# R8 Obfuscation

R8 is the default Android release optimizer: it shrinks unused code, optimizes bytecode, and obfuscates names to slow reverse engineering. It replaced ProGuard as the default while keeping rule compatibility.
- Runs automatically in release builds; rules come from ProGuard files.
- Obfuscation renames classes and members; mapping files restore them.
- Keep rules protect reflection and framework entry points.
- Obfuscation deters casual analysis, not determined attackers.

## Related

- [[wiki/android-core/proguard-rules|Proguard Rules]] — the rules R8 applies
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — one layer of defense
- [[wiki/android-core/crash-reporting|Crash Reporting]] — mapping files symbolize stacks
- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — R8 runs inside the build
