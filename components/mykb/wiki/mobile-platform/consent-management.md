---
type: "concept"
title: "Consent Management"
description: "User consent for tracking, notifications, and data collection"
tags: ["mobile", "consent", "privacy", "gdpr"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Consent Management

Consent management captures explicit user choices about tracking, notifications, and data collection, required by GDPR, CCPA, and store policies. It includes SDK consent flows, ATT (iOS), and notification opt-ins.
- Map every data collection purpose to a consent requirement.
- iOS ATT prompts app tracking transparency; Android has no direct analog.
- Store consent records with timestamps and versions for audit.
- Never collect before consent; make withdrawal easy.

## Related

- [[wiki/mobile-platform/app-analytics|App Analytics]] — analytics are the main consent consumer
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — notification opt-in is a consent flow
- [[wiki/android-core/android-permissions|Android Permissions]] — OS permissions complement consent
- [[wiki/mobile-platform/app-store-review|App Store Review]] — stores enforce privacy declarations
