---
type: "concept"
title: "Brute-Force Protection"
description: "Controls that slow or stop repeated guessing of credentials and secrets"
tags: ["brute-force", "rate-limiting", "authentication", "defense"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"]
---

# Brute-Force Protection

## Summary
Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts so that guessing a password or secret becomes economically infeasible. It is a layering problem: online guessing, distributed credential stuffing, and offline cracking each need different controls, and a protection scheme that stops one may be useless against the others.

## Details
- Brute-force protection throttles repeated authentication attempts through rate limiting, delays, and lockouts. Per-account limits stop single-target guessing; per-IP limits stop small-scale attackers; delays make bursts costly; lockouts halt repeated failures entirely. OWASP's Authentication Cheat Sheet recommends per-account and per-IP limits plus monitoring of distributed attempts.
- Credential stuffing distributes attempts across many IPs, so limits must combine IP reputation, device signals, and breach-list checks. A per-IP cap alone is defeated by botnets rotating residential proxies; the defense combines global breach-list matching (reject known-stolen passwords), device and behavior signals, and adaptive challenges.
- Concrete example: an attacker runs a password spray — one password against many accounts — which stays under per-account limits by design. Protection detects the pattern across accounts (many logins, one password, one origin), raises a challenge for the affected attempts, and queues the accounts for forced password reset if the password appears in breach data.
- Design must avoid easy denial of service: lockouts create an attacker-controlled availability vector. If five failed attempts lock an account for a day, an attacker can lock out every user trivially; the mitigation is to escalate gradually (delay, then challenge, then limited lockout), tie lockouts to evidence of attack rather than raw failure counts, and exempt or carefully handle accounts with many failed attempts that are actually legitimately locked-out users.
- Failure modes: protection that only applies to the login endpoint while token issuance and recovery endpoints are unprotected; lockout policies that do not distinguish the attacker's target from the attacker's source; and monitoring that logs attempts but never acts on the patterns.
- Operational practice: rate-limit login, token issuance, and recovery separately; combine per-account and per-IP limits; monitor for spray patterns; and make MFA the decisive control — a phishing-resistant factor makes most guessing attacks fail at the second factor.
- For mykb: layered throttling on login, token issuance, and recovery endpoints keeps guessing expensive, and the telemetry should feed the same security monitoring that watches for takeover.

## Related
- [[wiki/identity/credential-stuffing|Credential Stuffing]] — distributed guessing that needs layered defense
- [[wiki/identity/lockout-policies|Lockout Policies]] — the lockout half of throttling
- [[wiki/identity/captcha-systems|CAPTCHA Systems]] — bot deterrence at the entry point
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — API-level throttling primitive
- [[wiki/identity/mfa-patterns|MFA Patterns]] — MFA defeats automated guessing
