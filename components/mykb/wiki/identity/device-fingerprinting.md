---
type: "concept"
title: "Device Fingerprinting"
description: "Identifying devices from browser and hardware signals for risk scoring and fraud detection"
tags: ["fingerprinting", "device", "risk", "detection"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Device_fingerprint"]
---

# Device Fingerprinting

- Device fingerprinting assembles browser, OS, screen, font, and network signals into a stable device identifier without cookies.
- Uses: risk-based authentication, fraud detection, session binding, and bot detection; it is also a privacy concern because it is hard for users to reset.
- Fingerprints are probabilistic — they work as a signal, not proof — and degrade across updates and privacy browsers.
- For mykb: fingerprints belong in the risk engine as one environment attribute, never as a standalone authentication factor.

## Related

- [[wiki/identity/mfa-patterns|MFA Patterns]] — risk-based MFA consumes device signals
- [[wiki/identity/captcha-systems|CAPTCHA Systems]] — bot detection relative to fingerprinting
- [[wiki/security-auth/attribute-based-access-control|Attribute-Based Access Control]] — device as an environment attribute
- [[wiki/security/zero-trust|Zero Trust Architecture]] — device posture as a verification signal
