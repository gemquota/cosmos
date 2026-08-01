---
type: "concept"
title: "Rooted Device Detection"
description: "Detecting rooted Android devices and adjusting trust"
tags: ["android", "root", "detection", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Rooted Device Detection

Root detection looks for su binaries, Magisk, or superuser packages to decide how much to trust a device. Rooted devices can bypass sandboxing, so sensitive flows may need to degrade.
- Checks: su presence, package manager for root apps, test-keys builds.
- Magisk is harder to detect than legacy su; expect arms races.
- Users may legitimately root; weigh blocking against UX.
- Treat as risk scoring, not a hard guarantee.

## Related

- [[wiki/mobile-platform/jailbreak-detection|Jailbreak Detection]] — the iOS counterpart
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — one input to risk decisions
- [[wiki/mobile-platform/biometric-authentication|Biometric Authentication]] — strong biometrics on rooted devices
- [[wiki/shell-environment/adb-tooling|ADB Tooling]] — adb root exposes device state
