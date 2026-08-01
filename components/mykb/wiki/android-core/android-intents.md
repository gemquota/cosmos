---
type: "concept"
title: "Android Intents"
description: "Messaging objects that start activities and services, deliver broadcasts, and carry data between apps"
tags: ["android", "intents", "components", "navigation", "messaging"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/components/intents-filters"]
---

# Android Intents

## Summary

Intents are the message objects that connect Android components: they start activities and services, deliver broadcasts, and shuttle data between apps. Explicit intents name a target component; implicit intents declare an action that the system resolves against intent filters. Intents are also how deep links and notifications reach specific screens.

## Details

- An intent carries action, data URI, category, type, extras (a Bundle), and an optional explicit component.
- Implicit intents resolve against intent filters declared in the manifest; when several apps match, the system shows a chooser.
- PendingIntent wraps an intent with permission so another component (notification, widget, app) can fire it later on your behalf.
- App Links and deep links are intents with http(s) data URIs matched by verified intent filters.
- Extras should stay small - Parcelable payloads cross process boundaries via Binder; large data belongs in storage with a reference passed along.
- RSIS3 relevance: ADB and app automation drive the device by firing intents, and Shizuku-based tools can listen for intents from other apps.

## Related

- [[wiki/android-core/android-manifest|Android Manifest]] — intent filters that advertise capabilities are declared here
- [[wiki/mobile-platform/deep-linking|Deep Linking]] — URLs resolved into intents for in-app navigation
- [[wiki/android-core/picture-in-picture|Picture-in-Picture]] — PiP entries are launched with specialized intents
- [[wiki/shell-environment/adb-tooling|ADB Tooling]] — shell am start fires intents from the command line
- [[wiki/api-protocols/rest-apis|REST APIs]] — intent messaging is Android analog of URL routing
- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]] — device automation layer built on intents
