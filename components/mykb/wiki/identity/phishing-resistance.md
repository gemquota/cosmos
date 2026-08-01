---
type: "concept"
title: "Phishing Resistance"
description: "Authentication designs that remain secure even when users are tricked into visiting fake sites"
tags: ["phishing", "mfa", "passkeys", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.cisa.gov/secure-our-world/recognize-and-report-phishing"]
---

# Phishing Resistance

- Phishing resistance means the authentication ceremony itself cannot be replayed on an attacker-controlled origin.
- WebAuthn/passkeys achieve this by binding assertions to the origin; legacy MFA (SMS, TOTP, push) can be relayed in real time by AiTM proxies.
- CISA guidance pairs phishing-resistant authentication with recognition and reporting training for humans.
- For RSIS3: classify every authentication method by its phishing resistance and reserve the strongest for privileged actions.

## Related

- [[wiki/identity/passkey-ecosystem|Passkey Ecosystem]] — passkeys are the phishing-resistant default
- [[wiki/identity/web-authn-api|WebAuthn API]] — origin binding is the technical mechanism
- [[wiki/identity/mfa-patterns|MFA Patterns]] — not all MFA is phishing-resistant
- [[wiki/security/passkeys|Passkeys]] — existing article on phishing-resistant credentials
