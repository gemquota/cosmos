---
type: "entity"
title: "AEC"
description: "Acronym referenced in session adc6df02"
tags: ["acronym", "android", "api", "ast", "auth", "authentication", "entity"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
status: "growing"
---

## Aec 2

AEC — Architecture, Engineering, and Construction. An industry sector referenced in sessions.

**Related topics:** android, api, auth, authentication

**Domain:** Mobile Platform › [[wiki/android-core/00-index|Android Core]] › [[wiki/web-platforms/00-index|Auth Security › Aec 2]]

## Overview

AEC stands for Architecture, Engineering, and Construction — the industry sector that designs and builds the built environment. Software in this space covers CAD and BIM tools, project management platforms, structural analysis, and field applications used on construction sites. The sector is notable for long project lifecycles, strict regulatory requirements, and a mix of desktop, web, and mobile tooling, which is why an acronym entity for it can surface in sessions that also touch mobile platforms and authentication.

## Industry Context

AEC software deals with large, versioned artifacts: building models, blueprints, specifications, and change orders. Teams collaborate across firms, so document exchange and access control are central concerns — login, roles, and audit trails appear wherever drawings are shared. Mobile apps are common for on-site work, giving the Android tag on this page its context: field workers need authenticated, offline-capable clients that sync drawings and status back to the office. The API tag reflects the service layer that connects those clients to the project database.

## Software Concerns

Because a single project can involve dozens of organizations, authentication and authorization are not optional: every user must be mapped to a project role, and changes must be attributable. Sessions touching AEC therefore tend to discuss identity flows alongside the domain logic. [[wiki/android-core/00-index|Android Core]] documents the mobile platform where field apps run, [[wiki/api-services/00-index|API Services]] covers the interfaces those apps consume, and [[wiki/security/00-index|Security]] groups the authentication material that governs access. The broader [[wiki/web-platforms/00-index|Web Platforms]] tree holds the browser-based project portals common in the sector.

## Session Context

The acronym was captured in a single session with android, api, auth, and authentication tags, so this page anchors the industry-sector thread for future work. It deliberately keeps the expansion general — AEC also collides with other expansions in other contexts, so the tags and related entities matter more than the exact product involved.

## Related Entities

- [[wiki/security-auth/categories/auth-security/subcategories/authentication/abuseipdb-2|Abuseipdb 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/ac-2|Ac 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/access-denied|Access Denied]]
- [[raw/archive/junk-entities-2026-08c/security-auth/categories/auth-security/subcategories/authentication/ach-2|Ach 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/actionnode-2|Actionnode 2]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/addressfamily|Addressfamily]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/agentconfig|Agentconfig]]
- [[wiki/security-auth/categories/auth-security/subcategories/authentication/agentswitchrecord|Agentswitchrecord]]
