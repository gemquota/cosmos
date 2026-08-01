---
type: "concept"
title: "Biometric Authentication"
description: "Face or fingerprint verification with BiometricPrompt, Face ID, and Touch ID"
tags: ["mobile", "biometrics", "authentication", "security", "privacy"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/training/sign-in/biometric-auth"]
---

# Biometric Authentication

## Summary

Biometric authentication verifies a person with a face or fingerprint through BiometricPrompt on Android and Face ID or Touch ID on iOS, with fallback to device credentials. It improves UX for unlocking local secrets and satisfies stronger security policies when paired with server-side authentication. Biometric data stays on device - it never leaves the secure enclave.

## Details

- BiometricPrompt supports BIOMETRIC_STRONG, BIOMETRIC_WEAK, and DEVICE_CREDENTIAL authenticators, letting you choose strength.
- Android classes biometric strength as Class 3 (strong), Class 2 (weak), and Class 1 (convenience); Class 3 enables cryptographic operations.
- Keystore/KeyChain keys with setUserAuthenticationRequired unlock only after biometric success, protecting local secrets.
- Handle cancellation, lockout, and not-enrolled states with graceful fallbacks to PIN or password.
- Biometrics complement, not replace, server auth: pair with OAuth, passkeys, or MFA flows.
- Privacy and consent: enrollment prompts and permission UX should be explicit, and biometric data must not be logged.
- RSIS3 relevance: local API keys and session unlock could use biometrics instead of a plaintext master password.

## Related

- [[wiki/mobile-platform/rooted-device-detection|Rooted Device Detection]] — biometric trust drops on compromised devices
- [[wiki/mobile-platform/jailbreak-detection|Jailbreak Detection]] — the iOS counterpart of root detection
- [[wiki/mobile-platform/consent-management|Consent Management]] — enrollment and usage sit inside consent flows
- [[wiki/security/webauthn|WebAuthn]] — platform authenticators standardize biometric use
- [[wiki/security/passkeys|Passkeys]] — passkeys build on platform biometrics
- [[wiki/security/mfa|Multi-Factor Authentication]] — biometrics as one factor in MFA
