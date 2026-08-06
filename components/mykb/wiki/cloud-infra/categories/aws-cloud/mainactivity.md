---
type: "entity"
title: "MainActivity"
description: "Activity"
tags: ["entity", "android", "angular", "ast", "aws", "bash"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
status: "growing"
---

## Mainactivity

Activity — an Android component representing a single screen with a user interface. Sessions show lifecycle management and navigation patterns.

Each Activity is a window into the app's user interface and is declared in the manifest, where launch modes, permissions, and intent filters are configured. An Activity is started by an Intent and is responsible for inflating its layout, restoring its state, and coordinating with other components on the screen.

The Activity lifecycle consists of onCreate(), onStart(), onResume(), onPause(), onStop(), and onDestroy(). The system calls these methods as the Activity moves between the foreground and background, and in response to configuration changes such as rotation. State that must survive recreation is written to the Bundle in onSaveInstanceState() and restored in onCreate() or onRestoreInstanceState(); heavier state belongs in a ViewModel that outlives the Activity.

Activities host Fragments and coordinate navigation between screens. Best practices keep business logic out of the Activity, delegate data loading to ViewModels and repositories, and handle configuration changes without rebuilding unnecessary work. Lifecycle-aware components such as LiveData and coroutine scopes make it easier to start and stop work in sync with the visible state of the screen. Automated tests commonly drive Activities with Espresso to verify navigation and user flows. The patterns recorded in the [[wiki/web-platforms/00-index|Aws Cloud]] domain show these lifecycle and navigation concerns recurring across sessions, especially when apps talk to cloud backends.

The entry is filed under AWS Cloud because the sessions that mention it combine mobile UI work with cloud-backed features, and the same lifecycle discipline applies when Activities fetch data from remote services.

The manifest entry also defines the activity's parent for navigation, and launch modes such as singleTop and singleTask shape how the system reuses existing instances.

**Domain:** Mobile Platform › [[wiki/android-core/00-index|Android Core]] › [[wiki/cloud-infra/categories/aws-cloud/00-index|Aws Cloud]]

## Related Entities

- [[raw/archive/junk-entities-2026-08/cloud-infra/categories/aws-cloud/damp|Damp]]
- [[wiki/cloud-infra/categories/aws-cloud/particle-simulation-2|Particle Simulation 2]]
- [[raw/archive/junk-entities-2026-08/cloud-infra/categories/aws-cloud/sysfont|Sysfont]]
- [[raw/archive/junk-entities-2026-08/cloud-infra/categories/aws-cloud/memorytrace|Memorytrace]]
