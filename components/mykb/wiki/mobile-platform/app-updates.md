---
type: "concept"
title: "App Updates"
description: "Delivering new versions via stores, in-app updates, and staged rollouts"
tags: ["mobile", "updates", "distribution", "release"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# App Updates

App updates move users to new versions through store mechanisms: Android in-app updates API, iOS forced updates, and staged rollouts. Update UX affects adoption of fixes and features.
- Android in-app updates: immediate or flexible flows.
- iOS has no in-app update API; prompt-and-redirect patterns apply.
- Version skew breaks APIs - gate server endpoints by min version.
- Staged rollout catches regressions before full reach.

## Related

- [[wiki/mobile-platform/staged-rollouts|Staged Rollouts]] — percentaged release of updates
- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — updates flow through distribution channels
- [[wiki/mobile-platform/app-store-review|App Store Review]] — updates re-enter review
- [[wiki/android-core/dynamic-features|Dynamic Features]] — bundles and updates interact
