---
type: "concept"
title: "Email Verification"
description: "Proving control of an email address, typically via a one-time link or code"
tags: ["email", "verification", "identity", "otp"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc5321"]
---

# Email Verification

## Summary
Email verification proves a user controls a mailbox by sending a one-time link or code that they must present back. It is the lowest common denominator of identity proofing and the default recovery channel for most services — ubiquitous, cheap, and asynchronous, but also the weakest commonly used factor, because mailbox compromise and phishing make it unsuitable as a sole factor for anything sensitive.

## Details
- Email verification proves a user controls a mailbox by sending a one-time link or code that they must present back. The flow is: collect the address, send a secret (link token or code) to it, require the user to return the secret within a validity window, and only then mark the address verified.
- It is the lowest common denominator of identity proofing and the default recovery channel for most services. Because virtually everyone has email and the flow needs no specialized hardware, it is the baseline every service supports; it is also the channel attackers first target, since a compromised mailbox grants access to any identity that trusts it.
- Weaknesses: mailbox compromise, domain takeover, and phishing of the verification link make it unsuitable as a sole factor. A mailbox that is hijacked (weak password, no MFA on the mail provider) hands over every verification link; a lapsed domain can be re-registered by an attacker to capture its mail; and phishing can steal the verification link before the user uses it, completing the proof as the attacker.
- Concrete example: a service sends a six-digit code to the user's inbox. The user's mail provider is itself protected only by a password that appeared in a breach; an attacker logs in, reads the code, and completes verification as the user — the service never learns it verified the wrong person.
- Failure modes: verification links that never expire; codes with unlimited retry counts, enabling brute force; addresses that are verified but never re-checked (a mailbox can be abandoned and recycled); and the assumption that "verified" means "owned by a human" — throwaway and catch-all addresses defeat it trivially.
- RFC 5321 (SMTP) defines the transport; the verification logic is application-level — token generation, expiry, retry limits, and binding to the account are all the application's responsibility.
- For mykb: email verification should bootstrap low-assurance identities only, with higher assurance reserved for stronger factors — treat a verified mailbox as a contact and recovery channel, not as proof of identity.

## Related
- [[wiki/identity/otp-codes|OTP Codes]] — email codes are a one-time-code pattern
- [[wiki/identity/authentication-factors|Authentication Factors]] — mailbox control is a possession proxy
- [[wiki/identity/account-recovery|Account Recovery]] — email is the default recovery channel
- [[wiki/security/ldap|LDAP]] — directory identities often key on email
