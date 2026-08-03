---
type: "concept"
title: "Native vs Hybrid Apps"
description: "Native, hybrid, and web-wrapped apps: capability, cost, and experience trade-offs"
tags: ["mobile", "hybrid", "native", "architecture", "web"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.apple.com/documentation/technologies", "https://developer.android.com/studio"]
---
# Native vs Hybrid Apps

## Summary
Native apps use platform SDKs (SwiftUI/UIKit, Jetpack Compose); hybrid apps wrap web views (Capacitor, Cordova); cross-platform frameworks sit in between. Native maximizes performance and platform integration; web-wrapped minimizes cost and shares code with the website.

## Details
- **Native** — full API access, best performance and platform feel, but two codebases and two release pipelines.
- **Web-wrapped** — one web codebase packaged in a shell; fast to ship, but OS integration, offline, and performance lag.
- **Hybrid bridges** — Capacitor plugins expose device APIs; push, biometrics, and storage work through bridges.
- **Decision factors** — team skills, offline needs, hardware access, store policies, and update cadence.
- **Worked example** — the mykb wiki is web-first; a Capacitor wrapper gives the mobile app shell with deep links to articles.
- **Relevance** — RSIS3's Termux-first tooling suggests web-first with wrappers where store distribution is required.

## Related
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/vw-vh|vw and vh Units]] — adjacent concept in this wiki
- [[wiki/web-platforms/touch-action-css|touch-action CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/dark-mode-practice|Dark Mode Practice]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — existing coverage
- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — existing coverage
- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — existing coverage
