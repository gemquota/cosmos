---
type: "entity"
title: "WebAuthn API"
description: "W3C standard API for public-key credential registration and assertion in browsers and platforms"
tags: ["webauthn", "w3c", "api", "fido", "authentication"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.w3.org/TR/webauthn-3/"]
---

# WebAuthn API

## Summary

WebAuthn is the W3C Recommendation that exposes FIDO2 public-key credentials to web applications through the Credential Management API (navigator.credentials.create and navigator.credentials.get). It turns authenticators — platform biometrics, OS keychains, or USB/Bluetooth/NFC hardware keys — into first-class authentication devices. It matters because it is the only browser-native mechanism that is both phishing-resistant (credentials are bound to origin) and password-free (the server keeps only a public key). WebAuthn is the substrate under the passkey ecosystem and the interoperable core of modern passwordless login.

## Details

- Registration (attestation): the RP generates a challenge, the authenticator creates a new key pair and returns the public key, credential ID, and attestation statement; the RP stores the public key.
- Authentication (assertion): the RP sends a challenge, the authenticator signs it with the stored private key after local user verification, and the RP verifies the signature over the origin, challenge, and RP ID.
- Credential types: non-discoverable credentials require a credential ID from the server; discoverable (resident) keys can be selected from the authenticator itself — the basis of passkeys.
- Security properties: assertions are scoped to the RP ID and origin, which defeats lookalike-domain phishing; private keys never leave the authenticator.
- Extensions and attestation: transports, large blob, and attestation formats (packed, tpm, android-key) let RPs tune security and device assurance.
- For RSIS3, WebAuthn offers a standards path to authenticate humans to mykb interfaces while keeping agent-to-service authn on separate credentials.

## Related

- [[wiki/identity/passkey-ecosystem|Passkey Ecosystem]] — the deployed product layer over WebAuthn
- [[wiki/identity/passwordless-authentication|Passwordless Authentication]] — WebAuthn is the API behind passwordless
- [[wiki/identity/hardware-security-keys|Hardware Security Keys]] — roaming authenticators speak WebAuthn via CTAP
- [[wiki/identity/phishing-resistance|Phishing Resistance]] — origin-bound assertions are the mechanism
- [[wiki/security/webauthn|WebAuthn]] — existing article on the standard
- [[wiki/security/passkeys|Passkeys]] — discoverable WebAuthn credentials
- [[wiki/api-protocols/rest-apis|REST APIs]] — registration endpoints that drive WebAuthn ceremonies
- [[wiki/concepts/identity-system|RSIS3 Identity System]] — identity system adopting WebAuthn for human access
