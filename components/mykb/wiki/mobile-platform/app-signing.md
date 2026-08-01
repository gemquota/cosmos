---
type: "concept"
title: "App Signing"
description: "Cryptographic signatures proving app authorship and enabling trusted updates"
tags: ["mobile", "signing", "security", "release", "keystore"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/studio/publish/app-signing"]
---

# App Signing

## Summary

App signing proves authorship and integrity: installers and OS updates verify the signature before accepting an app. Android supports upload keys plus Google Play App Signing, while iOS uses distribution certificates and provisioning profiles. Losing or expiring signing keys is catastrophic because updates require the same identity.

## Details

- A keystore holds the private key; apksigner applies signature schemes v1 (JAR), v2 (APK Signature Scheme), and v3 (key rotation).
- Play App Signing stores the app signing key with Google while you keep an upload key, enabling recovery and key rotation without user data loss.
- Certificate expiry and key loss break update paths; keystore backups belong in a secrets manager with access controls.
- iOS analog: distribution certificates pair with provisioning profiles; both are managed in the developer portal.
- Signing feeds the whole trust chain: CI build artifacts and SBOMs should be signed too, and signing secrets must never enter source control.
- RSIS3 relevance: any APK installed via ADB must be signed; a debug keystore is fine for internal tools but never for distribution.

## Related

- [[wiki/mobile-platform/code-signing-mobile|Code Signing Mobile]] — cross-platform signing landscape for mobile
- [[wiki/mobile-platform/provisioning-profiles|Provisioning Profiles]] — iOS pairing of certificates and device entitlements
- [[wiki/shell-environment/apk-analysis|APK Analysis]] — verifying signatures is part of inspecting a build
- [[wiki/security/secrets-management|Secrets Management]] — keystore private keys are secrets to protect
- [[wiki/security/tls|TLS]] — public-key trust models parallel app signing
- [[wiki/security/supply-chain-security|Software Supply Chain Security]] — signed artifacts anchor the supply chain
