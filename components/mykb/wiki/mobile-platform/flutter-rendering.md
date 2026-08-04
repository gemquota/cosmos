---
type: "entity"
title: "Flutter Rendering"
description: "How Flutter paints pixels: Dart widgets, RenderObjects, layers, and the engine"
tags: ["flutter", "rendering", "dart", "mobile", "ui"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://docs.flutter.dev/resources/architectural-overview", "https://docs.flutter.dev/resources/rendering"]
---
# Flutter Rendering

## Summary
Flutter renders everything itself rather than using native views. Widgets (immutable descriptions) build Elements, which create RenderObjects that layout and paint into layers; the engine rasterizes with Skia or Impeller. This gives consistent pixels everywhere at the cost of drawing everything.

## Details
- **Widget tree** — configuration-only; rebuilding widgets is cheap because render objects persist.
- **Render pipeline** — build, layout, paint, and composite per frame; constraints flow down, sizes flow up.
- **Impeller** — the modern GPU backend precompiles shaders, eliminating runtime shader jank.
- **Isolates** — Dart runs on a UI isolate; heavy work moves to compute isolates; platform channels call native code.
- **Worked example** — the mykb charts in Flutter re-render only dirty layers, keeping 60fps on mid-range devices.
- **Relevance** — Flutter's uniform rendering simplifies RSIS3's multi-device UI targets.
- **Frame pipeline timing** — each Flutter frame runs animation, build, layout, paint, and rasterization; `WidgetsBinding.addPostFrameCallback` schedules work after the frame settles to avoid jank.

## Related
- [[wiki/web-platforms/frame-budget|Frame Budget]] — adjacent concept in this wiki
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]] — adjacent concept in this wiki
- [[wiki/web-platforms/repaint-vs-reflow|Repaint vs Reflow]] — adjacent concept in this wiki
- [[wiki/web-platforms/will-change|will-change CSS]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/flutter-framework|Flutter Framework]] — existing coverage
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — existing coverage
- [[wiki/frontend-frameworks/react-native-vs-flutter|React Native vs Flutter]] — existing coverage
