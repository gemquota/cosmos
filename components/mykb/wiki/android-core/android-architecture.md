---
type: "concept"
title: "Android Architecture"
description: "Layered platform stack from Linux kernel and HAL to framework APIs and app sandbox"
tags: ["android", "architecture", "platform", "kernel", "sandbox"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/platform"]
---

# Android Architecture

## Summary

Android is a mobile operating system built on a Linux kernel, organized as a layered stack: the kernel and hardware abstraction layer (HAL), native libraries and the Android Runtime (ART), the Java/Kotlin application framework, and system apps on top. Every app runs in its own sandbox with a unique Linux UID and its own process, which is the root of Android permission and isolation model. Understanding the stack matters for RSIS3 because its device-access layer runs on Android through Termux, Shizuku, and ADB.

## Details

- The Linux kernel provides drivers, memory and process management, and Binder IPC, the kernel-level mechanism that moves data between processes and components.
- The HAL exposes device hardware (camera, sensors, audio) to the framework through stable interfaces, so vendors can ship drivers without forking the upper layers.
- ART compiles app bytecode: DEX files are translated with a mix of ahead-of-time and just-in-time compilation plus profile-guided optimization.
- The application framework layers system services on top: Activity Manager, Package Manager, Window Manager, Location, Notifications, and Connectivity all talk to apps through Binder.
- Apps are composed of four component types - activities, services, content providers, and broadcast receivers - wired together by intents and declared in the manifest.
- SELinux enforces mandatory access control between apps and system services; runtime permissions gate access to sensitive APIs on top of that.
- Relevance: RSIS3 automation on Android (adb shell, Shizuku, app intents) exercises exactly these layers, so failures usually trace to a sandbox, permission, or Binder boundary.

## Related

- [[wiki/android-core/android-manifest|Android Manifest]] — declares the components and permissions that the framework uses to launch and isolate apps
- [[wiki/android-core/android-ndk|Android NDK]] — native code that compiles against the same kernel and Binder interfaces
- [[wiki/shell-environment/dex-files|DEX Files]] — ART executes DEX bytecode produced from Java and Kotlin sources
- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]] — RSIS3 reaches this stack through Termux, Shizuku, and ADB
- [[wiki/os-shell/entities/bash-patterns|Bash Scripting Patterns]] — shell automation that drives ADB against this platform
- [[wiki/concepts/triad-architecture|Triad Architecture]] — mobile clients are one leg of the RSIS3 triad
