---
type: "concept"
title: "Passwordless Authentication"
description: "Authentication that replaces passwords with cryptographic keys, biometrics, or possession-based one-time codes"
tags: ["passwordless", "authentication", "fido", "passkeys", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://fidoalliance.org/passwordless/"]
---

# Passwordless Authentication

## Summary

Passwordless authentication removes the shared-secret password from the login ceremony, replacing it with evidence the user proves possession of: a cryptographic key on a device, a biometric, or a one-time code delivered to a trusted channel. It matters because passwords are the root of most account compromise: they are phishable, reused, and stored in plaintext by too many services. Removing them eliminates an entire class of credential-stuffing and phishing attacks. FIDO Alliance guidance frames passwordless as the convergence of strong authentication and better UX: the user authenticates once to their device, and the device authenticates to services.

## Details

- FIDO2/WebAuthn is the dominant standard: the device generates a public/private key pair per relying party, keeps the private key in a secure enclave, and signs challenges — the server never sees a reusable secret.
- Platform authenticators (phone face/fingerprint, OS keychain) make keys portable across devices via provider sync, which is the passkey model; roaming authenticators like hardware security keys keep the key offline.
- One-time-code passwordless (magic links, email OTPs) is simpler but weaker: the possession channel itself can be phished or hijacked, so NIST treats it as a lower assurance route.
- Passwordless removes the need for password-hashing infrastructure but introduces new problems: device loss, account recovery, and attestation of the authenticator model.
- For RSIS3/mykb, passwordless is the model for agent and user identities that never expose long-lived secrets: sessions are derived from device-held keys rather than stored passwords.

## Related

- [[wiki/identity/passkey-ecosystem|Passkey Ecosystem]] — the deployed, synced form of passwordless credentials
- [[wiki/identity/web-authn-api|WebAuthn API]] — the browser API that implements passwordless ceremonies
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — roaming authenticator option for passwordless
- [[wiki/security/passkeys|Passkeys]] — existing article on the passkey credential model
- [[wiki/identity/authentication-factors|Authentication Factors]] — passwordless shifts from knowledge to possession factors
- [[wiki/identity/phishing-resistance|Phishing Resistance]] — phishing resistance is passwordless's headline property
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — agent identities designed around key-based authentication
