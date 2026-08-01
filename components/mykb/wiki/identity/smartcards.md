---
type: "concept"
title: "Smartcards"
description: "Credit-card-sized tokens with embedded chips that hold certificates and private keys"
tags: ["smartcards", "pki", "tokens", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: ["https://en.wikipedia.org/wiki/Smart_card"]
---

# Smartcards

- Smartcards embed a secure chip holding private keys and X.509 certificates, used for login, signing, and physical access (PIV/CAC in government).
- Authentication happens via PIN plus on-card key operations, making them two-factor and phishing-resistant in principle.
- They predate FIDO keys and remain dominant in regulated and government environments; readers are a deployment cost.
- For mykb: smartcard support is relevant when federating with government or enterprise PKI systems.

## Related

- [[wiki/security-auth/digital-certificates|Digital Certificates]] — cards store certificates and keys
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — the modern consumer alternative
- [[wiki/identity/identity-providers|Identity Providers]] — cards integrate with enterprise IdPs
- [[wiki/security-auth/public-key-infrastructure|Public Key Infrastructure]] — the PKI that issues card credentials
