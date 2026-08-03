---
type: "concept"
title: "Key Rotation"
description: "Replacing cryptographic keys on a schedule or on suspicion of compromise"
tags: ["key-rotation", "cryptography", "lifecycle", "secrets"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html"]
---

# Key Rotation

## Summary
Key rotation replaces a cryptographic key with a fresh one so that long-term exposure and cryptanalysis damage stay bounded. It applies to signing keys (JWKS), encryption keys (KMS), TLS private keys, API keys, and database secrets — and its core challenge is not generating the new key, but cutover: old and new material must coexist safely while consumers migrate, and old material must be revoked without breaking valid data.

## Details
- Key rotation replaces a key with a fresh one so that long-term exposure and cryptanalysis damage stay bounded. Every signature, ciphertext, and credential has a validity window; rotation caps that window, so a key stolen today becomes useless within the rotation period.
- Rotation applies to signing keys (JWKS), encryption keys (KMS), TLS private keys, API keys, and database secrets. Each has different mechanics: signing keys need both keys in the JWKS during overlap; encryption keys need old keys retained for decrypting existing ciphertext (KMS key versions do this natively); TLS keys rotate via certificate renewal; API keys and database secrets rotate with dual-lifetime schemes.
- Concrete example: a signing key used to mint JWTs is suspected of exposure. The provider generates a new key, adds it to the JWKS alongside the old one, re-signs new tokens with the new key, waits out the maximum token lifetime, then removes the old key — tokens minted before the cutover still verify, and after the window the exposed key is worthless.
- Automated, short-lived credentials reduce the value of theft; manual rotation fails when compromise is silent. If rotation is a manual quarterly ritual, an exposed key lives for months; if credentials are short-lived and auto-renewed (Let's Encrypt certificates, vault leases, rotated refresh tokens), the exposure window shrinks to hours and the process cannot be forgotten.
- Trade-offs: rotation requires key-versioning, downtime-free cutover, and careful revocation of old keys. Versioning lets old ciphertext decrypt; cutover requires consumers to tolerate both keys; revocation must be coordinated so that a revoke-too-early incident does not lock out production.
- Failure modes: rotating on a calendar rather than on exposure risk; breaking consumers that hardcode the key or the JWKS; deleting the old key while ciphertext still depends on it; and rotation storms, where automation rotates so aggressively that the fleet is perpetually mid-cutover.
- For mykb: rotation schedules should be part of the key registry, with alerts when rotation is overdue — the registry is the single source of truth for which keys exist, when they rotate, and what still depends on them.

## Related
- [[wiki/api-services/api-key-management|API Key Management]] — rotating long-lived API keys
- [[wiki/identity/jwks|JWKS]] — rotating signing keys in the set
- [[wiki/security/secrets-management|Secrets Management]] — storing rotated keys securely
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automated short-lived TLS certificates
