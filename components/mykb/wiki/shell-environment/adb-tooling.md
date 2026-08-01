---
type: "concept"
title: "ADB Tooling"
description: "Android Debug Bridge: shell access, installs, and logs from a host"
tags: ["adb", "android", "shell", "debugging"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# ADB Tooling

ADB (Android Debug Bridge) connects a host to Android devices over USB or Wi-Fi: shell, install, logcat, port forwarding, and input simulation. It is the backbone of RSIS3 device automation and debugging.
- adb shell opens a device shell; adb install pushes APKs.
- logcat streams system and app logs with filters.
- am start fires intents; input taps and types coordinates.
- Wireless debugging (Android 11+) removes the cable.

## Related

- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]] — RSIS3 uses ADB for device access
- [[wiki/android-core/android-architecture|Android Architecture]] — ADB talks to the platform services
- [[wiki/shell-environment/apk-analysis|APK Analysis]] — pull and inspect APKs from devices
- [[wiki/os-shell/entities/bash-patterns|Bash Scripting Patterns]] — ADB fits shell automation loops
