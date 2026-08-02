---
type: "concept"
title: "Deep Linking on Mobile"
description: "Opening apps directly from URLs: URI schemes, universal links, and app links"
tags: ["deep-linking", "mobile", "urls", "ios", "android"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/training/app-links/deep-linking", "https://developer.apple.com/ios/universal-links/"]
---
# Deep Linking on Mobile

## Summary
Deep links route URLs into apps: custom schemes (myapp://) and verified HTTPS links — Universal Links on iOS, App Links on Android. Verified links win trust and survive permission prompts. Deep links power notifications, QR codes, and cross-app journeys.

## Details
- **Custom schemes** — simple but unverified: any app can claim a scheme, so treat them as untrusted.
- **Universal/App Links** — HTTPS URLs with an association file (apple-app-site-association, assetlinks.json) prove ownership.
- **Handling** — the app parses the URL into navigation state; fallback to the website when the app is absent.
- **Deferred linking** — after install, attributes which link caused the install.
- **Worked example** — the mykb wiki article URLs open the app directly via verified app links, with web fallback.
- **Relevance** — RSIS3's mobile client should route all external entry points through verified links.
- **Link verification** — the applinks association file must be served at the well-known path over HTTPS, and Android verifies assetlinks.json against the package name and signing certificate before honoring links.

## Related
- [[wiki/api-protocols/url-structure|URL Structure]] — adjacent concept in this wiki
- [[wiki/api-protocols/uri-vs-url|URI vs URL]] — adjacent concept in this wiki
- [[wiki/api-protocols/percent-encoding|Percent-Encoding]] — adjacent concept in this wiki
- [[wiki/api-protocols/punycode-domains|Punycode Domains]] — adjacent concept in this wiki
- [[wiki/mobile-platform/deep-linking|Deep Linking]] — existing coverage
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — existing coverage
- [[wiki/mobile-platform/app-updates|App Updates]] — existing coverage
