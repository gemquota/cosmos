---
type: "concept"
title: "Android Manifest"
description: "XML contract declaring components, permissions, and intent filters to the OS"
tags: ["android", "manifest", "configuration", "permissions"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/topics/manifest/manifest-intro", "https://developer.android.com/guide/topics/manifest/application-element"]
---

# Android Manifest

## Summary


## Details
- The manifest declares app identity, components, permissions, and hardware/software features; the package manager reads it before any component runs.
- Component declarations are the core: each activity, service, receiver, and provider must be listed or the system cannot launch it.
- Permissions are requested here at install time (or runtime for dangerous groups), and the manifest is also where the app declares its minimum and target SDK.
- Manifest errors are a classic first-run failure: a missing intent-filter or undeclared component produces silent crashes or invisible launcher icons.
- **Worked example / comparison** — Worked example — declaring a service requires its class, exported flag, and any intent-filter; forgetting the declaration means Context.startService throws, while forgetting the filter means other apps cannot find it.
- For mykb, android-manifest sits in the android-core cluster; freshness review is important here because manifest rules change with each Android release.

## Related
- [[wiki/android-core/android-architecture|Android Architecture]]
- [[wiki/android-core/android-intents|Android Intents]]
- [[wiki/android-core/android-permissions|Android Permissions]]
- [[wiki/shell-environment/gradle-builds|Gradle Builds]]
- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]]
- [[wiki/concepts/promotion-readiness|Promotion Readiness]]
- [[wiki/dev-tools/markdown-linting|Markdown Linting]]
- [[wiki/concepts/content-freshness-review|Content Freshness Review]]
