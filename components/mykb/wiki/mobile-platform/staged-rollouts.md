---
type: "concept"
title: "Staged Rollouts"
description: "Phased release of app versions to a percentage of users"
tags: ["mobile", "release", "rollout", "risk"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Staged Rollouts

Staged rollouts ship a new version to a small user percentage, monitor crashes and feedback, then ramp up. Both Play and App Store support percentage-based release with rollback.
- Start at 1-5% and watch crash-free rate before ramping.
- Pair with feature flags to disable risky paths without a release.
- Have a rollback plan: revert to the previous version.
- Notifications and in-app banners tell early users what changed.

## Related

- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — rollouts are a distribution phase
- [[wiki/mobile-platform/app-updates|App Updates]] — the artifact being rolled out
- [[wiki/devops-infra/feature-flags|Feature Flags]] — flags complement staged release
- [[wiki/mobile-platform/app-analytics|App Analytics]] — metrics gate the ramp
