---
type: "concept"
title: "Credential Stuffing"
description: "Automated attacks replaying breached username/password pairs across many services"
tags: ["credential-stuffing", "attacks", "breaches", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://owasp.org/www-community/attacks/Credential_stuffing"]
---

# Credential Stuffing

- Credential stuffing uses username/password pairs leaked in one breach and replays them at scale against other services, relying on password reuse.
- Because credentials are already valid, it defeats naive rate limits at any single site; botnets distribute the attempts.
- Defenses: unique passwords, breach monitoring, MFA, device reputation, and blocking known-compromised credentials at login.
- Relevant to mykb: RSIS3's login policy should check credentials against breach lists and treat stuffing as a distinct detection signal.

## Related

- [[wiki/identity/password-managers|Password Managers]] — the primary mitigation for reuse
- [[wiki/identity/brute-force-protection|Brute-Force Protection]] — adjacent automated guessing attack
- [[wiki/identity/mfa-patterns|MFA Patterns]] — second factors stop replayed passwords
- [[wiki/identity/account-takeover|Account Takeover]] — the goal of credential stuffing
