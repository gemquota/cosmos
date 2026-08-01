---
type: "concept"
title: "In-App Billing"
description: "Google Play Billing for digital purchases inside apps"
tags: ["android", "billing", "monetization", "play"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# In-App Billing

In-app billing sells digital goods through Google Play Billing: one-time products, subscriptions, and consumables, with Play handling payment and receipts. The Play Billing Library replaces the old v3 API.
- Query product details, launch the purchase flow, and confirm acknowledgements.
- Verify purchase tokens server-side before granting entitlement.
- Consumables allow repeat purchase; subscriptions track renewals.
- Test with license testers and the billing emulator.

## Related

- [[wiki/android-core/subscription-management|Subscription Management]] — recurring billing lifecycle
- [[wiki/mobile-platform/mobile-app-distribution|Mobile App Distribution]] — billing is tied to Play distribution
- [[wiki/mobile-platform/consent-management|Consent Management]] — purchases need explicit user intent
- [[wiki/mobile-platform/app-analytics|App Analytics]] — conversion tracking around purchases
