---
type: "concept"
title: "Jailbreak Detection"
description: "Detecting jailbroken iOS devices at runtime"
tags: ["ios", "jailbreak", "security", "detection"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Jailbreak Detection

Jailbreak detection checks for iOS device compromises: Cydia presence, unusual file paths, or code-injection hooks. It feeds risk decisions but is bypassable, so treat it as one signal in a hardening stack.
- Checks: file existence, fork/exec behavior, dylib injection, entitlements.
- Response options: warn, degrade features, or block sensitive flows.
- App Store review limits what evasion tricks are acceptable.
- Combine with integrity checks, not as the only defense.

## Related

- [[wiki/mobile-platform/rooted-device-detection|Rooted Device Detection]] — the Android counterpart
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — detection is one layer
- [[wiki/mobile-platform/biometric-authentication|Biometric Authentication]] — compromised devices change biometric trust
- [[wiki/shell-environment/apk-analysis|APK Analysis]] — analysis reveals detection weaknesses
