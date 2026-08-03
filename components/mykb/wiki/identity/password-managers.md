---
type: "concept"
title: "Password Managers"
description: "Applications that generate, store, and autofill strong unique passwords"
tags: ["passwords", "password-managers", "credentials", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Password_manager"]
---

# Password Managers

## Summary
Password managers centralize credential generation, encrypted storage, and autofill so users can have a unique, high-entropy password per site without memorizing any of them. They are the practical answer to password reuse, which credential-stuffing attacks exploit: one unique password per site means one breach cannot cascade into every account.

## Details
- Password managers centralize credential generation, encrypted storage, and autofill so users can have a unique, high-entropy password per site without memorizing them. The vault encrypts credentials with a key derived from a master password; the client decrypts locally, so the vault provider — even a cloud one — cannot read the stored secrets.
- They are the practical answer to password reuse, which credential-stuffing attacks exploit. Reuse is the vulnerability that turns a breach at one site into takeover at many; a manager removes the incentive to reuse by making each password a random 20-character string the user never needs to remember.
- Concrete example: a user with 200 accounts generates a unique password for each and stores them in the vault; a breach at a forum exposes one of those passwords, but no other account accepts it, so the breach stops at the forum — the exact property credential stuffing depends on is gone.
- The vault should be protected by a strong master password plus multi-factor authentication, and ideally a hardware security key. The master password is now the single most valuable secret the user holds, so it should be high-entropy and backed by MFA; a hardware key bound to the vault raises the cost of vault theft substantially.
- Failure modes: the master password itself being reused or weak; autofill filling credentials on phishing pages (mitigated by origin-bound filling); vault theft combined with a weak master password enabling offline cracking; and lockout — losing the master password can mean losing every account, so recovery options must exist without weakening the vault.
- Tradeoffs: a manager concentrates risk in one vault instead of spreading it across sites — a fair trade when the vault is well protected, but a disaster when it is not; browser-only managers are convenient but expose credentials to browser extensions and sync services, while dedicated apps keep the vault more isolated.
- Open questions for mykb: how RSIS3 should store service credentials without a human vault, and where the master-password risk migrates to — for agent credentials, a machine secret manager with short-lived leases is the vault analogue, and the same single-point-of-failure caution applies.
- RSIS3/mykb relevance: the password-manager pattern is the human mirror of the secrets-management layer; the wiki keeps the comparison explicit so credential-storage decisions for agents borrow the right lessons.

## Related
- [[wiki/identity/credential-stuffing|Credential Stuffing]] — the attack password managers mitigate
- [[wiki/identity/authentication-factors|Authentication Factors]] — master password is a knowledge factor
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — second factor for vault access
- [[wiki/security/secrets-management|Secrets Management]] — machine equivalent of the vault
