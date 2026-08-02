---
status: "growing"
type: "entity"
title: "Intent Distribution"
description: "Intent"
tags: ["entity", "ast", "bug", "cli", "edge", "ide"]
timestamp: "2026-07-19T22:41:43Z"
resource: ""
---

## Intent Distribution

Intent — an Android messaging object for communicating between components. Sessions show implicit/explicit intents for starting activities and services.

**Related topics:** bug, cli, edge, ide

**Domain:** Development Tools › [[wiki/dev-tools/supercategories/development/index|Development]] › [[wiki/dev-tools/supercategories/development/categories/cli-tools/index|Cli Tools]]

## Overview

Intents are the asynchronous message objects Android uses to request an action from another component. They carry an action, data URI, type, and extras, and they are delivered by the system to activities, services, or broadcast receivers. The distribution model decouples the sender from the receiver: the sender declares what it wants, and the system (or the app) decides which component handles it.

## Explicit vs Implicit

- **Explicit intents** name the target component class, so delivery is deterministic; they are used for in-app navigation.
- **Implicit intents** declare an action and data but no component; the system resolves them against intent filters in the manifest.

## Delivery Patterns

- `startActivity` launches a UI component; `startService` and `bindService` reach background work.
- `sendBroadcast` fans an event out to multiple receivers.
- Extras carry typed payloads, and a PendingIntent wraps an intent so other apps can invoke it later.

## Intent Filters and Resolution

For implicit intents, the system compares the action, data URI, and MIME type against the intent filters declared in each app's manifest. Categories such as `CATEGORY_DEFAULT` and `CATEGORY_BROWSABLE` narrow the candidate set, and the system prompts the user when several components match. The resolved target can be inspected with `resolveActivity`, which is also how launchers decide which apps handle a share or open action.

## Data and Security Notes

Extras are not encrypted, so sensitive values should travel in explicit intents to a trusted target or be replaced by a reference such as a content URI with scoped permissions. A PendingIntent grants another app the right to execute the wrapped intent with your app's identity, so its flags and target must be chosen carefully. Broadcast receivers should validate the sender and the data they receive, since implicit broadcasts can arrive from any app.

## Related Concepts

- [[wiki/android-core/android-intents|Android Intents]] — the core messaging mechanism
- [[wiki/android-core/android-activities|Activities]] — primary intent targets
- [[wiki/android-core/android-services|Services]] — background intent recipients
- [[wiki/android-core/android-broadcast-receivers|Broadcast Receivers]] — fan-out intent targets

## Related Entities

- [[wiki/dev-tools/supercategories/development/categories/cli-tools/agentic-context-engineering|Agentic Context Engineering]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/cognitive|Cognitive]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/dev|Dev]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/intent|Intent]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/performance|Performance]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/reality|Reality]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/senior-dev|Senior Dev]]
- [[wiki/dev-tools/supercategories/development/categories/cli-tools/sovereign-orchestrator|Sovereign Orchestrator]]
