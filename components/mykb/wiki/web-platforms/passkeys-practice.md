---
type: "concept"
title: "Passkeys in Practice"
description: "Phishing-resistant, synced credentials that replace passwords across devices"
tags: ["passkeys", "webauthn", "authentication", "security", "fido"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://passkeys.dev/", "https://www.w3.org/TR/webauthn-3/"]
---
# Passkeys in Practice

## Summary
Passkeys are discoverable WebAuthn credentials synced across devices by platform providers (Apple, Google, Microsoft). The user authenticates with biometrics or PIN, and the passkey signs for the origin. They replace passwords with something both easier and more phishing-resistant.

## Details
- **Synced discoverability** — resident keys sync via the account; the phone or security key can authenticate on other devices.
- **Flow** — registration creates a discoverable credential; sign-in shows a passkey sheet; no password database exists server-side.
- **Conditional UI** — `autocomplete="webauthn"` blends passkeys into login forms for smooth migration.
- **Recovery** — account recovery still needs a backup path (recovery codes, email); passkeys are the primary, not the only, factor.
- **Worked example** — the mykb dashboard registers passkeys and keeps a recovery-code fallback in its vault.
- **Relevance** — RSIS3's identity layer should treat passkeys as the recommended primary factor.
- **Cross-device flows** — phone-as-authenticator uses QR pairing to sign on a nearby computer; the same ceremony flows through the platform broker without shared secrets.

## Related
- [[wiki/api-protocols/device-flow|Device Authorization Flow]] — adjacent concept in this wiki
- [[wiki/api-protocols/authorization-code-flow|Authorization Code Flow]] — adjacent concept in this wiki
- [[wiki/api-protocols/refresh-token-rotation|Refresh Token Rotation]] — adjacent concept in this wiki
- [[wiki/api-protocols/audience-claims|Audience Claims]] — adjacent concept in this wiki
- [[wiki/mobile-platform/biometric-authentication|Biometric Authentication]] — existing coverage
- [[wiki/api-protocols/oauth2-pkce|PKCE]] — existing coverage
- [[wiki/identity/passkey-ecosystem|Passkey Ecosystem]] — existing coverage
