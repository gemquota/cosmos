---
type: "concept"
title: "Hot Reload"
description: "Instantly applying code changes to a running app during development"
tags: ["hot-reload", "developer-experience", "flutter", "react-native"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Hot Reload

Hot reload pushes code changes into a running app in under a second, preserving state, which collapses the edit-run-test loop. Flutter and React Native made it a competitive differentiator.
- Preserves runtime state across most edits.
- Full restart is needed for structural or native changes.
- Compose previews and SwiftUI previews offer similar loops.
- Requires a running debug session, so CI stays cold.

## Related

- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — hot reload is a Flutter headline feature
- [[wiki/frontend-frameworks/react-native-vs-flutter|React Native vs Flutter]] — both toolkits compete on iteration
- [[wiki/android-core/jetpack-compose|Jetpack Compose]] — previews approximate the loop
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — iteration speed is a framework factor
