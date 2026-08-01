---
type: "concept"
title: "Crash Reporting"
description: "Collecting, symbolizing, and triaging app crashes in production"
tags: ["android", "crash", "reporting", "observability"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Crash Reporting

Crash reporting captures stack traces from production, symbolizes obfuscated builds, and groups issues by signature. Firebase Crashlytics is the standard choice; native crashes need NDK symbol uploads.
- Upload mapping files so R8-obfuscated stacks are readable.
- Add custom keys and logs to reproduce the failing path.
- Fatal and non-fatal (caught) exceptions both feed trends.
- Rate and severity routing decide what an on-call sees.

## Related

- [[wiki/android-core/anr-diagnostics|ANR Diagnostics]] — sibling runtime-failure channel
- [[wiki/mobile-platform/app-analytics|App Analytics]] — crashes contextualize usage analytics
- [[wiki/android-core/r8-obfuscation|R8 Obfuscation]] — obfuscation must be reversible via maps
- [[wiki/devops-infra/observability|Observability]] — crash data belongs in observability
- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — production monitoring ships with distribution
