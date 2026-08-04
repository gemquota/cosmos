---
type: "entity"
title: "BRO"
description: "BroadcastReceiver"
tags: ["entity", "acronym", "api", "ast", "auth", "authentication"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
status: "growing"
---

## Bro

BroadcastReceiver — an Android component for listening to system-wide broadcast messages.

**Related topics:** api, auth, authentication

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Security Auth]] › [[wiki/web-platforms/00-index|Auth Security]] › Bro

## Overview

BroadcastReceiver is one of the four core Android components, along with activities, services, and content providers. It is a message listener: the system delivers intents — both system broadcasts like connectivity changes and app-defined broadcasts — to registered receivers, which then respond. Receivers are designed to be short-lived: the platform expects the onReceive callback to finish quickly, so long work is delegated to a service. The BRO acronym on this page abbreviates the component name as it appeared in session material.

## Registration and Delivery

A receiver can be declared statically in the manifest, which lets the system launch it even when the app is not running, or registered dynamically at runtime, which ties its lifetime to the registering context. [[wiki/android-core/android-broadcast-receivers|android broadcast receivers]] documents the full lifecycle, including the ordering and priority rules that govern delivery. Static registration is convenient but drains battery, so modern Android restricts many implicit broadcasts and pushes developers toward dynamic registration or job scheduling instead.

## Security Considerations

Broadcasts carry data across app boundaries, which makes them a security surface. A malicious app can spoof broadcasts, and a receiver can leak sensitive data in its response. The guidance is to use explicit intents with package targeting for sensitive messages, export receivers only when necessary, and validate the sender where trust matters. [[wiki/android-core/android-intents|android intents]] explains the delivery mechanism, and [[wiki/android-core/android-manifest|the manifest]] controls which receivers are exposed. When a receiver handles authentication results — the auth tag on this page — extra care applies, since credentials or tokens may ride inside the intent extras.

## Session Context

The entity surfaced in a session tagged API, auth, and authentication, matching an app where broadcast delivery (login result, token refresh, session expiry) feeds the authentication flow. [[wiki/android-core/00-index|Android Core]] groups the platform material, and [[wiki/security/00-index|Security]] holds the surrounding identity guidance.

## Related Entities

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ab|Ab]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/automatic|Automatic 10]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/fov-2|Fov 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/selective-chaos|Selective Chaos]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/rubenverborgh|Rubenverborgh]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/sim-speed|Sim Speed]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/missing-content|Missing Content]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/searchtext|Searchtext]]
