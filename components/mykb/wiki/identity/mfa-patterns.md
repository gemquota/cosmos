---
type: "concept"
title: "MFA Patterns"
description: "Deployment patterns for multi-factor authentication: push, TOTP, hardware keys, and risk-based step-up"
tags: ["mfa", "2fa", "authentication", "nist", "security"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://pages.nist.gov/800-63-3/sp800-63b.html"]
---

# MFA Patterns

## Summary

Multi-factor authentication (MFA) requires two or more independent authentication factor categories — knowledge, possession, inherence — so that compromising one factor does not grant access. Patterns differ in the second factor's technology and in how phishing-resistant it is. NIST SP 800-63B is explicit that not all MFA is equal: SMS one-time codes are discouraged (the channel is hijackable), while hardware-backed WebAuthn authenticators are the phishing-resistant gold standard. MFA patterns matter to RSIS3 because the assurance level attached to an identity depends on which pattern it uses.

## Details

- Common patterns: TOTP app codes, push notification approval, email/SMS OTP, hardware security keys, and platform biometric passkeys; each trades convenience against resistance to phishing and SIM-swap.
- Phishing resistance: WebAuthn/passkey MFA binds assertions to the origin, so a lookalike login page cannot replay the factor; TOTP and push are vulnerable to real-time relay (AiTM) attacks.
- Step-up authentication: low-risk actions use the base session; admin actions, key changes, or money movement re-require a factor, often a hardware key.
- Enrollment and recovery: backup codes, recovery keys, and device re-enrollment must be designed so that losing the factor does not lock the user out or weaken security.
- Risk-based/adaptive MFA: signals (device, location, behavior) trigger factor challenges only when risk is elevated, balancing friction and protection.
- For mykb, a pattern matrix — risk level x action x factor — gives RSIS3 a single place to enforce assurance on every sensitive operation.

## Related

- [[wiki/identity/authentication-factors|Authentication Factors]] — the factor categories MFA combines
- [[wiki/identity/totp|TOTP]] — time-based one-time codes as a factor
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — phishing-resistant possession factor
- [[wiki/security/mfa|Multi-Factor Authentication]] — existing article on MFA
- [[wiki/security/zero-trust|Zero Trust Architecture]] — MFA as a per-request verification signal
- [[wiki/identity/account-recovery|Account Recovery]] — recovery must not bypass MFA
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — assurance levels assigned per pattern
