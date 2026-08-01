---
type: "concept"
title: "Provisioning Profiles"
description: "iOS entitlements pairing certificates, App IDs, and devices"
tags: ["ios", "signing", "provisioning", "entitlements"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Provisioning Profiles

Provisioning profiles bind an iOS app identity to certificates, App ID, and (for development) devices, enabling installation and capability entitlements like push and keychain sharing. They are the iOS analog of Android signing plus permissions.
- Development vs distribution profiles; managed in the Apple developer portal.
- Xcode auto-manages signing; CI needs exported profiles and certificates.
- Expired profiles break installs and updates.
- Entitlements inside profiles gate capabilities.

## Related

- [[wiki/mobile-platform/code-signing-mobile|Code Signing Mobile]] — the broader signing landscape
- [[wiki/mobile-platform/app-signing|App Signing]] — Android signing comparison
- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — profiles gate store and device delivery
- [[wiki/mobile-platform/ios-platform|iOS Platform]] — profiles are iOS-specific
