---
type: "concept"
title: "Password Managers"
description: "Applications that generate, store, and autofill strong unique passwords"
tags: ["passwords", "password-managers", "credentials", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Password_manager"]
---

# Password Managers

- Password managers centralize credential generation, encrypted storage, and autofill so users can have a unique, high-entropy password per site without memorizing them.
- They are the practical answer to password reuse, which credential-stuffing attacks exploit.
- The vault should be protected by a strong master password plus multi-factor authentication, and ideally a hardware security key.
- Open questions for mykb: how RSIS3 should store service credentials without a human vault, and where the master-password risk migrates to.

## Related

- [[wiki/identity/credential-stuffing|Credential Stuffing]] — the attack password managers mitigate
- [[wiki/identity/authentication-factors|Authentication Factors]] — master password is a knowledge factor
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — second factor for vault access
- [[wiki/security/secrets-management|Secrets Management]] — machine equivalent of the vault
