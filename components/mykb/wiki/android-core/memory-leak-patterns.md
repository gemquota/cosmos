---
type: "concept"
title: "Memory Leak Patterns"
description: "Common Android leak causes: static references, listeners, and handler callbacks"
tags: ["android", "memory", "leaks", "performance"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Memory Leak Patterns

Android leaks usually come from objects outliving their components: static references to activities, unregistered listeners, and anonymous handlers holding the outer class. LeakCanary surfaces them in development.
- Static singletons holding Context or Activity are the classic leak.
- Unregister broadcast receivers and observers in onPause or onDestroy.
- Handlers and coroutines capture scopes; cancel them on teardown.
- Lint and LeakCanary catch most leaks before release.

## Related

- [[wiki/android-core/app-threading|App Threading]] — threads outliving components leak
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — lifecycle callbacks are the cleanup points
- [[wiki/android-core/anr-diagnostics|ANR Diagnostics]] — leaks often accompany ANRs
- [[wiki/android-core/crash-reporting|Crash Reporting]] — OOM crashes trace back to leaks
