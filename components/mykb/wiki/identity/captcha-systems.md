---
type: "concept"
title: "CAPTCHA Systems"
description: "Challenges that distinguish humans from bots to protect login and registration flows"
tags: ["captcha", "bots", "abuse", "detection"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://developers.google.com/recaptcha/docs/v3"]
---

# CAPTCHA Systems

- CAPTCHAs present puzzles (distorted text, image selection) or invisible risk scores to separate humans from automated clients.
- Modern versions (reCAPTCHA v3, hCaptcha) score interactions in the background instead of interrupting users.
- They defend against credential stuffing, spam, and scraping, but add friction, have accessibility costs, and are defeated by human farms.
- For mykb: CAPTCHAs belong on registration and high-volume public endpoints, not on authenticated internal APIs.

## Related

- [[wiki/identity/credential-stuffing|Credential Stuffing]] — CAPTCHAs blunt automated stuffing
- [[wiki/identity/brute-force-protection|Brute-Force Protection]] — bot defense family
- [[wiki/api-protocols/rate-limiting|Rate Limiting]] — complementary abuse control
- [[wiki/identity/device-fingerprinting|Device Fingerprinting]] — invisible scoring signals
- [[wiki/identity/authentication-factors|Authentication Factors]] — CAPTCHAs defend the authentication entry point
