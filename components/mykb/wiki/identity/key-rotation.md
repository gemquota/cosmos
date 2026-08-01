---
type: "concept"
title: "Key Rotation"
description: "Replacing cryptographic keys on a schedule or on suspicion of compromise"
tags: ["key-rotation", "cryptography", "lifecycle", "secrets"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html"]
---

# Key Rotation

- Key rotation replaces a key with a fresh one so that long-term exposure and cryptanalysis damage stay bounded.
- Rotation applies to signing keys (JWKS), encryption keys (KMS), TLS private keys, API keys, and database secrets.
- Automated, short-lived credentials reduce the value of theft; manual rotation fails when compromise is silent.
- Trade-offs: rotation requires key-versioning, downtime-free cutover, and careful revocation of old keys.
- For mykb: rotation schedules should be part of the key registry, with alerts when rotation is overdue.

## Related

- [[wiki/api-services/api-key-management|API Key Management]] — rotating long-lived API keys
- [[wiki/identity/jwks|JWKS]] — rotating signing keys in the set
- [[wiki/security/secrets-management|Secrets Management]] — storing rotated keys securely
- [[wiki/security/lets-encrypt|Let's Encrypt]] — automated short-lived TLS certificates
