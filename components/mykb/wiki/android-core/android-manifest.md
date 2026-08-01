---
type: "concept"
title: "Android Manifest"
description: "XML contract declaring components, permissions, and intent filters to the OS"
tags: ["android", "manifest", "configuration", "permissions"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Android Manifest

The AndroidManifest.xml is the app contract with the OS: it declares every component, the permissions the app requires, hardware features, and intent filters. It is merged from library manifests during Gradle builds.
- Declares activities, services, content providers, and receivers so the system can launch them.
- Lists uses-permission entries and feature requirements such as camera or NFC.
- Holds intent filters that advertise capabilities, including deep-link patterns.
- Inspect merged output with aapt or Android Studio to debug manifest conflicts.

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — the manifest wires components into the platform stack
- [[wiki/android-core/android-intents|Android Intents]] — intent filters in the manifest resolve implicit intents
- [[wiki/android-core/android-permissions|Android Permissions]] — manifest declarations feed the permission model
- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — manifest merging happens during the build
- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]] — ADB and tooling read manifest metadata
