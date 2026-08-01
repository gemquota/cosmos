---
type: "concept"
title: "Brute-Force Protection"
description: "Controls that slow or stop repeated guessing of credentials and secrets"
tags: ["brute-force", "rate-limiting", "authentication", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"]
---

# Brute-Force Protection

- Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts.
- OWASP's Authentication Cheat Sheet recommends per-account and per-IP limits plus monitoring of distributed attempts.
- Credential stuffing distributes attempts across many IPs, so limits must combine IP reputation, device signals, and breach-list checks.
- Design must avoid easy denial of service: lockouts create an attacker-controlled availability vector.
- For mykb: layered throttling on login, token issuance, and recovery endpoints keeps guessing expensive.

## Related

- [[wiki/identity/credential-stuffing|Credential Stuffing]] — distributed guessing that needs layered defense
- [[wiki/identity/lockout-policies|Lockout Policies]] — the lockout half of throttling
- [[wiki/identity/captcha-systems|CAPTCHA Systems]] — bot deterrence at the entry point
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — API-level throttling primitive
- [[wiki/identity/mfa-patterns|MFA Patterns]] — MFA defeats automated guessing
