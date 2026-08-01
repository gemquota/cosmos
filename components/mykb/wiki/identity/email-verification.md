---
type: "concept"
title: "Email Verification"
description: "Proving control of an email address, typically via a one-time link or code"
tags: ["email", "verification", "identity", "otp"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://www.rfc-editor.org/rfc/rfc5321"]
---

# Email Verification

- Email verification proves a user controls a mailbox by sending a one-time link or code that they must present back.
- It is the lowest common denominator of identity proofing and the default recovery channel for most services.
- Weaknesses: mailbox compromise, domain takeover, and phishing of the verification link make it unsuitable as a sole factor.
- RFC 5321 (SMTP) defines the transport; the verification logic is application-level.
- For mykb: email verification should bootstrap low-assurance identities only, with higher assurance reserved for stronger factors.

## Related

- [[wiki/identity/otp-codes|OTP Codes]] — email codes are a one-time-code pattern
- [[wiki/identity/authentication-factors|Authentication Factors]] — mailbox control is a possession proxy
- [[wiki/identity/account-recovery|Account Recovery]] — email is the default recovery channel
- [[wiki/security/ldap|LDAP]] — directory identities often key on email
