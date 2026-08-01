---
type: "concept"
title: "Android Permissions"
description: "Runtime-gated access model protecting sensitive data and system capabilities"
tags: ["android", "permissions", "privacy", "security", "runtime"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/topics/permissions/overview"]
---

# Android Permissions

## Summary

Android permissions protect sensitive data and system capabilities behind declared, user-approved grants. The model distinguishes normal permissions (auto-granted), dangerous permissions (runtime requests), and signature permissions (same-certificate apps). Runtime permission prompts appeared in Android 6.0 and continue to evolve with one-time grants and auto-reset.

## Details

- Apps declare uses-permission entries in the manifest; protection levels determine whether installation or runtime consent is required.
- Dangerous permissions live in groups and are requested at runtime with a rationale, typically via registerForActivityResult.
- Android 11 added one-time grants and permission auto-reset for unused apps; Android 13 introduced granular media permissions and notification permission.
- Signature permissions protect app-to-app APIs and are the basis for plugin ecosystems like Shizuku.
- Scoped storage and background location restrictions constrain what broad permissions actually grant.
- Least privilege is the design goal: request only what a feature needs, and pair OS permissions with product-level consent management.
- RSIS3 relevance: the device-access skill must declare and request exactly the permissions it uses - notifications, SMS, camera - and handle denial gracefully.

## Related

- [[wiki/mobile-platform/consent-management|Consent Management]] — OS permission prompts sit inside product consent flows
- [[wiki/android-core/location-services|Location Services]] — location requires precise runtime permission handling
- [[wiki/security/rbac|RBAC]] — permission grants mirror role-based access control
- [[wiki/security/zero-trust|Zero Trust Architecture]] — least privilege applies to devices as well as services
- [[wiki/llm-agents/permission-model|Permission Model]] — agents need the same least-privilege discipline
- [[wiki/mobile-platform/entities/android-device-access|Android Device Access]] — every device capability RSIS3 uses maps to a permission
