---
type: "entity"
title: "Adb 2"
status: "growing"
---

## Adb 2

Android Debug Bridge — command-line tool for interacting with Android devices. Sessions show ADB commands for device management, debugging, and app installation.

**Related technologies:** android, api, auth

**Domain:** Mobile Platform › [[wiki/web-platforms/00-index|Android Core]] › [[wiki/web-platforms/00-index|Api Clients › Adb 2

## Overview

Android Debug Bridge (ADB) is the client-server tool that connects a development machine to an Android device or emulator over USB or TCP. It exposes a device daemon (adbd) on the device, a server on the host, and a client binary the developer invokes. This split lets a single host manage multiple devices and lets commands run either interactively or from scripts, which is why ADB shows up in automation pipelines as well as in manual debugging.

## Common Commands

Device management starts with `adb devices` to list connected devices and `adb shell` to open an interactive shell on the target. File transfer uses `adb push` and `adb pull`, while `adb install` installs an APK and `adb uninstall` removes one. Logs are collected with `adb logcat`, which filters by tag and priority, making it the first stop when diagnosing crashes or network failures. Pairing over wireless uses a QR code or pairing code and then connects over TCP, which keeps the same command set available without a cable.

## Debugging and App Installation

Sessions emphasize ADB as a debugging instrument: inspecting activities with `adb shell dumpsys activity`, checking package details with `dumpsys package`, and pulling crash buffers with `logcat -b crash`. App installation covers both release and debug builds, including the `-r` flag to reinstall while keeping data and `-g` to grant all runtime permissions at install time. The [[wiki/android-core/android-manifest|Android manifest]] declares the components and permissions an app needs, and [[wiki/android-core/android-permissions|permissions]] are often granted or revoked through ADB during development to test authorization flows without touching the UI.

## Automation and Scripting

Because ADB is scriptable, it fits into CI and shell tooling: boot emulators, install builds, run instrumentation, and collect results without manual interaction. [[wiki/android-core/android-services|services]] and background tasks can be started and stopped directly, and `am start` launches activities with explicit intents for integration tests. For Android-specific workflows, the surrounding [[wiki/android-core/00-index|Android Core]] cluster records the platform concepts that ADB manipulates, making the bridge the practical surface for most device automation.

## Related Entities

- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aap-2|Aap 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aar|Aar
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/aarrr|Aarrr
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/abi|Abi
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/accr-2|Accr 2
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/ace-core|Ace Core
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acid|Acid
- [[wiki/web-platforms/supercategories/api-services/categories/api-rest/subcategories/rest-api/acli|Acli
