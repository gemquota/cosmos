---
type: "concept"
title: "Dynamic Features"
description: "On-demand app modules delivered via Play Feature Delivery"
tags: ["android", "modules", "delivery", "play"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Dynamic Features

Dynamic feature modules let apps download code and resources on demand, shrinking the initial install. Google Play serves them per feature, so unused features stay uninstalled until needed.
- Modules declare a dependency on the base module in Gradle.
- Install, uninstall, and request status via SplitInstallManager.
- Features can be on-demand, conditional (by country/device), or at install time.
- Works only with app bundles published to Google Play.

## Related

- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — feature delivery is part of Play distribution
- [[wiki/mobile-platform/app-updates|App Updates]] — bundles and updates interact with modules
- [[wiki/android-core/android-architecture|Android Architecture]] — modularity reshapes the app graph
- [[wiki/shell-environment/gradle-builds|Gradle Builds]] — module builds are configured in Gradle
