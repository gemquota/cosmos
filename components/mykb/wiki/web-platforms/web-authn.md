---
type: "concept"
title: "Web Authentication (WebAuthn)"
description: "Passwordless and phishing-resistant authentication with public-key credentials"
tags: ["webauthn", "authentication", "security", "passkeys", "fido"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Web_Authentication_API", "https://www.w3.org/TR/webauthn-3/"]
---
# Web Authentication (WebAuthn)

## Summary
WebAuthn authenticates users with public-key cryptography instead of shared secrets. The authenticator (security key, phone, platform TPM) signs challenges; the server stores only public keys. Phishing-resistant by design, it underpins passkeys and passwordless sign-in.

## Details
- **Registration** — the server sends a challenge; the authenticator creates a key pair and returns an attestation/credential with a credential ID.
- **Authentication** — the server challenges the credential; the authenticator signs; the server verifies with the stored public key.
- **Authenticators** — platform (biometrics) and roaming (security keys) types; user verification and resident keys shape the UX.
- **Properties** — scoped by origin and RP ID; resistant to credential phishing because the key never leaves the authenticator.
- **Worked example** — the mykb dashboard offers passkey sign-in alongside password login; the wiki records the ceremony flows.
- **Relevance** — RSIS3's credential layer should adopt WebAuthn where phishing resistance matters.

## Related
- [[wiki/api-protocols/m2m-tokens|Machine-to-Machine Tokens]] — adjacent concept in this wiki
- [[wiki/api-protocols/bearer-tokens|Bearer Tokens]] — adjacent concept in this wiki
- [[wiki/api-protocols/session-invalidation|Session Invalidation]] — adjacent concept in this wiki
- [[wiki/api-protocols/issuer-validation|Issuer Validation]] — adjacent concept in this wiki
- [[wiki/mobile-platform/biometric-authentication|Biometric Authentication]] — existing coverage
- [[wiki/api-protocols/oauth2|OAuth 2.0]] — existing coverage
- [[wiki/api-protocols/openid-connect|OpenID Connect]] — existing coverage
