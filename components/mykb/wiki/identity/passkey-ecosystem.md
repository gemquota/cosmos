---
type: "concept"
title: "Passkey Ecosystem"
description: "FIDO2 credentials synced across devices and platforms, positioned to replace passwords at scale"
tags: ["passkeys", "fido2", "webauthn", "identity", "passwordless"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://fidoalliance.org/passkeys/"]
---

# Passkey Ecosystem

## Summary

A passkey is a discoverable WebAuthn credential — a public/private key pair bound to a relying party — that a platform authenticator creates, stores, and syncs across the user's devices. The private key lives in secure hardware-backed storage and signs a challenge only after local user verification (biometric or PIN). The ecosystem is the full stack that makes passkeys usable at scale: relying parties, platform authenticators, sync providers, and the attestation and recovery flows around them. Passkeys matter to mykb because they give RSIS3 a realistic path to phishing-resistant authentication for user-facing interfaces without standing up password infrastructure.

## Details

- Credential model: each passkey is scoped to an origin (RP ID); servers store only the public key, so a server breach does not leak usable authentication material.
- Sync vs device-bound: platform providers (Apple, Google, Microsoft) synchronize passkeys through encrypted recovery keys; security-conscious deployments can prefer device-bound keys via hardware authenticators.
- User verification: the platform enforces local biometric/PIN check before releasing a signature, satisfying the possession-plus-inherence combination NIST wants for AAL2+.
- Ceremonies: registration issues the credential (attestation), login produces an assertion; both are origin-bound, which kills classic phishing.
- Recovery is the open problem: losing access to the sync account means losing credentials, so fallback flows (recovery codes, security keys) remain part of the ecosystem.
- For RSIS3, passkeys fit the triad architecture as the human-facing authn layer, while agents use short-lived service credentials.

## Related

- [[wiki/identity/web-authn-api|WebAuthn API]] — the W3C API passkeys are built on
- [[wiki/identity/passwordless-authentication|Passwordless Authentication]] — passkeys are the flagship passwordless implementation
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — device-bound alternative to synced passkeys
- [[wiki/security/passkeys|Passkeys]] — existing article covering the credential itself
- [[wiki/identity/authentication-factors|Authentication Factors]] — passkeys combine possession and inherence factors
- [[wiki/identity/account-recovery|Account Recovery]] — recovery flows are the ecosystem's weak point
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — identity system that could adopt passkey authn
