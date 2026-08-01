---
type: "concept"
title: "Code Signing Mobile"
description: "Signing and identity across iOS and Android releases"
tags: ["mobile", "signing", "security", "release"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Code Signing Mobile

Code signing proves who built an app and keeps updates trusted, on both platforms: iOS certificates and profiles, Android keystores and signature schemes. Mismanaged keys are a release blocker.
- iOS: distribution certificates + provisioning profiles; store and ad-hoc modes.
- Android: upload key + Play App Signing; v1/v2/v3 schemes.
- Store private keys in a secrets manager with rotation and backup.
- CI must sign without exposing keys to logs.

## Related

- [[wiki/mobile-platform/app-signing|App Signing]] — the Android deep-dive
- [[wiki/mobile-platform/provisioning-profiles|Provisioning Profiles]] — the iOS half
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — signing anchors app integrity
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — signatures feed the supply chain
