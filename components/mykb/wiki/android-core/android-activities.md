---
type: "concept"
title: "Android Activities"
description: "A single focused screen in an Android app, managed in a back stack and driven by the lifecycle"
tags: ["android", "activities", "ui", "lifecycle", "navigation"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.android.com/guide/components/activities/intro-activities"]
---

# Android Activities

## Summary

An activity is one focused screen in an Android app, backed by the Activity class and organized into tasks with a back stack. Activities are launched through intents, declared in the manifest, and follow a lifecycle that survives configuration changes. Modern apps increasingly use a single-activity architecture where Jetpack Compose or fragments drive the screens inside it.

## Details

- Activities are declared in AndroidManifest.xml and launched with intents; explicit intents name the class, implicit intents describe an action for the system to resolve.
- The task and back stack manage navigation history; launchMode flags such as singleTop, singleTask, and singleInstance change how activities are reused.
- State must survive rotation and process death: onSaveInstanceState covers transient UI state, while ViewModels hold configuration-stable state and repositories own durable data.
- The Activity Result API (registerForActivityResult) replaced startActivityForResult for returning data between activities.
- Activities can participate in multi-window and picture-in-picture modes, which means layouts must handle resizing and insets.
- RSIS3 relevance: Android automation often targets activities by package and intent - for example launching the Termux activity - so knowing their launch rules helps avoid unpredictable task stacks.

## Related

- [[wiki/android-core/viewmodel-pattern|ViewModel Pattern]] — configuration-stable state holder that survives activity recreation
- [[wiki/android-core/android-manifest|Android Manifest]] — declares activities and the intent filters that expose them
- [[wiki/android-core/multi-window|Multi-Window]] — resizable activities in split-screen and freeform modes
- [[wiki/android-core/picture-in-picture|Picture-in-Picture]] — activity as a small floating window for continuous content
- [[wiki/software-engineering/entities/design-patterns|Design Patterns in the Ecosystem]] — component patterns generalize the activity/fragment split
- [[wiki/agent-systems/session-state-machine|Session State Machine]] — activity states mirror the state machines agents use
