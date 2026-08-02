---
type: "concept"
title: "APK Analysis"
description: "Inspecting APKs: manifests, resources, bytecode, and signatures"
tags: ["apk", "reverse-engineering", "analysis", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# APK Analysis

APK analysis inspects what is inside an installable: manifest, resources, DEX bytecode, native libs, and signatures, using tools like aapt, apktool, jadx, and apksigner. It serves security review and learning.

## Anatomy of an APK

An APK is a ZIP archive containing the pieces Android needs to install and run an app:

- `AndroidManifest.xml` — package name, permissions, components, and intent filters, compiled to binary XML.
- `classes.dex` — the Dalvik bytecode implementing the app logic, often split across multiple DEX files.
- `resources.arsc` — the compiled resource table mapping IDs to values.
- `res/` — raw resources such as layouts, drawables, and strings.
- `lib/` — native libraries per ABI.
- `META-INF/` — the signature files used by the system to verify the publisher.

## Static Analysis Workflow

- `aapt dump badging` shows package, permissions, and activities.
- `apktool` decodes resources and smali for patching.
- `jadx` decompiles DEX to Java for reading.
- `apksigner verify` checks signature validity.

Beyond these basics, a thorough review checks exported components, over-permissive permissions, hardcoded secrets, weak crypto, cleartext traffic, and R8/ProGuard obfuscation coverage. Analysis supports malware triage, privacy audits, security review of third-party SDKs, and learning how real apps are structured.

## Dynamic Analysis

Static review is complemented by dynamic analysis: running the app in an emulator or device under a debugger, instrumentation framework, or proxy captures runtime behavior, network traffic, certificate-pinning bypasses, and file-system writes that inspection of the archive alone cannot see.

## Limitations

No single tool sees the whole picture: aapt omits runtime behavior, apktool output hides obfuscated control flow, and jadx can misread aggressive optimizations — so findings should be cross-checked across tools before drawing conclusions.

## Related

- [[wiki/shell-environment/adb-tooling|ADB Tooling]] — pull APKs from devices
- [[wiki/shell-environment/dex-files|DEX Files]] — the bytecode inside
- [[wiki/mobile-platform/app-signing|App Signing]] — signatures verified during analysis
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — analysis reveals hardening gaps
- [[wiki/android-core/r8-obfuscation|R8 Obfuscation]] — what obfuscated bytecode looks like
- [[wiki/android-core/proguard-rules|ProGuard Rules]] — the rules that shape it

