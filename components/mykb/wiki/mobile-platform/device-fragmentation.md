---
type: "concept"
title: "Device Fragmentation"
description: "The diversity of devices, OS versions, screens, and OEMs that mobile teams must support"
tags: ["mobile", "fragmentation", "devices", "testing", "android"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/studio/publish/versioning", "https://developer.android.com/guide/topics/resources/providing-resources"]
---
# Device Fragmentation

## Summary
Device fragmentation is the diversity of hardware and software in the wild: OS versions, screen sizes, densities, foldables, and OEM behaviors. Android is the extreme case; iOS still has a version and size spread. Strategies include adaptive layouts, resource qualifiers, and analytics-driven support tiers.

## Details
- **Screen and density** — dp/dip units, density buckets, and resource qualifiers (small/large, sw600dp) adapt layouts.
- **OS version spread** — set minimum SDKs by usage analytics; feature-detect platform APIs rather than assuming versions.
- **OEM behavior** — battery savers, aggressive background killing, and UI skins break assumptions; test on real hardware.
- **Foldables and large screens** — adaptive layouts and multi-window support extend the matrix.
- **Worked example** — the mykb app targets Android 8+ (95% of users), uses adaptive layouts, and tests on a representative device farm.
- **Relevance** — RSIS3's Android-first deployment must embrace the same fragmentation discipline.

## Related
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/web-platforms/responsive-breakpoints|Responsive Breakpoints]] — adjacent concept in this wiki
- [[wiki/web-platforms/vw-vh|vw and vh Units]] — adjacent concept in this wiki
- [[wiki/mobile-platform/adaptive-layouts|Adaptive Layouts]] — existing coverage
- [[wiki/mobile-platform/tablet-support|Tablet Support]] — existing coverage
- [[wiki/android-core/density-buckets|Density Buckets]] — existing coverage
