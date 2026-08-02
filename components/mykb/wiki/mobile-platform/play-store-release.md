---
type: "concept"
title: "Play Store Release"
description: "Shipping Android apps: signing, internal testing, staged rollouts, and Play Console"
tags: ["android", "play-store", "release", "signing", "distribution"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/studio/publish", "https://support.google.com/googleplay/android-developer/answer/9859348"]
---
# Play Store Release

## Summary
Play Store release runs through the Play Console: app signing (Play App Signing), internal/closed/open testing tracks, and staged rollouts. Releases are immutable once published, so version codes must increment, and each track has its own rollout percentage and review.

## Details
- **Signing** — an upload key signs the AAB; Google manages the app signing key; key security determines long-term control.
- **App bundles (AAB)** — Play generates per-device APKs, shrinking downloads; delivery types (install-time, on-demand) shape size.
- **Testing tracks** — internal testing for quick iteration, closed testing for beta groups, open testing for public beta.
- **Staged rollout** — release to a percentage, monitor crash-free sessions and ratings, then ramp.
- **Worked example** — the mykb Android app ships an AAB to internal testing, then ramps staged rollouts by 10%.
- **Relevance** — RSIS3's release playbook mirrors these tracks for its Android-first deployment.

## Related
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/web-platforms/l10n-practice|Localization Practice]] — adjacent concept in this wiki
- [[wiki/web-platforms/i18n-web|Web Internationalization]] — adjacent concept in this wiki
- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — existing coverage
- [[wiki/mobile-platform/staged-rollouts|Staged Rollouts]] — existing coverage
- [[wiki/mobile-platform/app-updates|App Updates]] — existing coverage
