---
type: "concept"
title: "Deep Linking"
description: "URLs that open specific content inside an app via verified App Links and Universal Links"
tags: ["mobile", "deep-linking", "urls", "navigation", "app-links"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/training/app-links"]
---

# Deep Linking

## Summary

Deep links are URLs that open specific content inside an app instead of a browser. Android App Links and iOS Universal Links bind a domain to an app through verified association files, so links open the app without a confirmation prompt. Deep linking connects web, email, notifications, and QR codes to in-app destinations.

## Details

- Android intent filters with http(s) data URIs plus autoVerify trigger verification against assetlinks.json on the domain.
- iOS uses the Associated Domains entitlement and an apple-app-site-association file for the same trust model.
- Fallbacks matter: when the app is absent, the link should open the web page or a store listing.
- Handlers should validate hosts and URIs to prevent open redirects and intent injection attacks.
- Campaign analytics on link opens measure acquisition; each destination should log its source.
- RSIS3 relevance: notifications from a companion app can deep-link into the exact mykb note or dashboard view.

## Related

- [[wiki/android-core/android-manifest|Android Manifest]] — intent filters and verification declarations live here
- [[wiki/mobile-platform/ios-platform|iOS Platform]] — Universal Links are the iOS half of deep linking
- [[wiki/android-core/instant-apps|Instant Apps]] — instant experiences rely on the same URL model
- [[wiki/mobile-platform/app-analytics|App Analytics]] — link opens feed acquisition metrics
- [[wiki/api-protocols/rest-apis|REST APIs]] — URLs are the shared web-to-app vocabulary
- [[wiki/security/oauth2|OAuth 2.0]] — redirect URIs and deep links share validation concerns
