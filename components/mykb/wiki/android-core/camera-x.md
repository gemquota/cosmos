---
type: "concept"
title: "Camera X"
description: "Jetpack camera library with use-case based API"
tags: ["android", "camera", "camerax", "media"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Camera X

CameraX is the Jetpack camera library built on Camera2 but hiding its complexity: apps declare use cases (preview, image capture, video, analysis) and the library handles lifecycle and device quirks.
- ProcessCameraProvider binds use cases to a LifecycleOwner.
- ImageAnalysis yields frames to ML pipelines at a configurable rate.
- Extensions (HDR, night, bokeh) apply vendor features when available.
- Lifecycle-aware binding means no manual open/close.

## Related

- [[wiki/android-core/camera2|Camera2]] — the low-level API CameraX wraps
- [[wiki/android-core/android-lifecycle|Android Lifecycle]] — CameraX binds to lifecycle owners
- [[wiki/android-core/android-permissions|Android Permissions]] — camera permission requirements apply
- [[wiki/ai-ml/quantisation|Quantisation]] — analysis frames feed on-device models
