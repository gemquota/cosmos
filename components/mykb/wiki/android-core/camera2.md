---
type: "concept"
title: "Camera2"
description: "Low-level Android camera API for manual control"
tags: ["android", "camera", "camera2", "media"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Camera2

Camera2 gives direct control over the camera pipeline: camera devices, capture sessions, and per-frame capture requests with manual focus, exposure, and RAW output. It is powerful but verbose compared with CameraX.
- CameraManager opens CameraDevice; CameraCaptureSession issues CaptureRequests.
- Support for manual ISO, shutter, focus, and burst capture.
- Hardware level (LEGACY, LIMITED, FULL) determines available capabilities.
- Use CameraX unless you need frame-level control.

## Related

- [[wiki/android-core/camera-x|Camera X]] — the recommended high-level alternative
- [[wiki/android-core/android-permissions|Android Permissions]] — camera permission gates access
- [[wiki/android-core/android-ndk|Android NDK]] — native pipelines consume camera frames
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — camera privacy and foreground rules
