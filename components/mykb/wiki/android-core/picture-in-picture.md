---
type: "concept"
title: "Picture-in-Picture"
description: "Floating video window that persists while the user does other things"
tags: ["android", "pip", "video", "multitasking"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Picture-in-Picture

Picture-in-picture (PiP) keeps a small floating window of your app visible during playback or navigation. Entering PiP is a lifecycle-aware transition requiring the activity to handle resize.
- Declare supportsPictureInPicture and enter via enterPictureInPictureMode.
- Media playback should continue while in PiP; controls shrink.
- PiP windows respect system gestures and can be dismissed.
- Test timing: entering too early or late breaks the UX.

## Related

- [[wiki/android-core/multi-window|Multi-Window]] — PiP is a constrained multi-window mode
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — PiP transitions are lifecycle events
- [[wiki/android-core/android-activities|Android Activities]] — activities host the PiP window
- [[wiki/mobile-platform/background-execution|Background Execution]] — PiP media work has background rules
