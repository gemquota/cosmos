---
type: "concept"
title: "Hardware Security Keys"
description: "Physical devices that sign WebAuthn challenges, keeping private keys offline"
tags: ["security-keys", "fido", "webauthn", "hardware"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://fidoalliance.org/fido2/"]
---

# Hardware Security Keys

## Summary
Hardware security keys (FIDO2/CTAP2 devices such as YubiKeys) hold private keys in tamper-resistant hardware and sign authentication challenges only after user presence or PIN. Because the private key never leaves the device and assertions are bound to the origin that registered them, they are the gold-standard phishing-resistant factor — the credential an attacker cannot steal remotely and cannot replay against a fake site.

## Details
- Hardware security keys (FIDO2/CTAP2 devices like YubiKey) hold private keys in tamper-resistant hardware and sign challenges after user presence or PIN. The key material is generated inside the device and never exported; the host receives only signed assertions, so even a fully compromised laptop cannot extract the secret.
- Because the private key never leaves the device and assertions are origin-bound, they are the gold-standard phishing-resistant factor. The origin binding is the crucial property: an assertion signed for `bank.example` is cryptographically invalid for `bank.example.attacker.net`, which is why WebAuthn defeats phishing sites that a code-stealing MFA cannot.
- They serve both passwordless login and the strongest MFA tier (NIST AAL3). In passwordless mode the key is the primary factor (possession plus user verification); in MFA mode it is the possession factor layered on a password; AAL3 maps to hardware-backed authenticators with user verification.
- Concrete example: an administrator's account is protected by a hardware key; a phishing page collects the admin's password but the key refuses to sign for the attacker's origin, the login fails, and the attempted sign-in is logged as a phishing signal — the account is never compromised.
- Operational concerns: key loss requires backup keys or recovery codes, and USB/NFC transport requires OS and browser support. A single key is a single point of failure, so enrollment should always offer a second key or recovery codes; support matrix issues (no NFC on some laptops, no WebAuthn in some browsers) create enrollment friction that must be planned for.
- Failure modes: users who leave the key in the reader (compromising presence verification), lost keys without backups, and policies that allow fallback to weaker factors, which quietly downgrade the protection the key was supposed to provide.
- Operational practice: enforce keys for privileged roles, require a PIN or biometric user verification for the key itself, enroll backup keys at setup, and monitor for sign-in attempts that bypass the key.
- For mykb: hardware keys should be mandatory for admin and agent-owner identities — the identities whose takeover would compromise the whole system.

## Related
- [[wiki/identity/web-authn-api|WebAuthn API]] — the API hardware keys speak
- [[wiki/identity/passkey-ecosystem|Passkey Ecosystem]] — device-bound alternative to synced passkeys
- [[wiki/identity/mfa-patterns|MFA Patterns]] — keys are the strongest MFA pattern
- [[wiki/security/webauthn|WebAuthn]] — existing article on the standard
