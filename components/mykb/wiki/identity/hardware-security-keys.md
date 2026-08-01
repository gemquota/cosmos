---
type: "concept"
title: "Hardware Security Keys"
description: "Physical devices that sign WebAuthn challenges, keeping private keys offline"
tags: ["security-keys", "fido", "webauthn", "hardware"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://fidoalliance.org/fido2/"]
---

# Hardware Security Keys

- Hardware security keys (FIDO2/CTAP2 devices like YubiKey) hold private keys in tamper-resistant hardware and sign challenges after user presence or PIN.
- Because the private key never leaves the device and assertions are origin-bound, they are the gold-standard phishing-resistant factor.
- They serve both passwordless login and the strongest MFA tier (NIST AAL3).
- Operational concerns: key loss requires backup keys or recovery codes, and USB/NFC transport requires OS and browser support.
- For mykb: hardware keys should be mandatory for admin and agent-owner identities.

## Related

- [[wiki/identity/web-authn-api|WebAuthn API]] — the API hardware keys speak
- [[wiki/identity/passkey-ecosystem|Passkey Ecosystem]] — device-bound alternative to synced passkeys
- [[wiki/identity/mfa-patterns|MFA Patterns]] — keys are the strongest MFA pattern
- [[wiki/security/webauthn|WebAuthn]] — existing article on the standard
