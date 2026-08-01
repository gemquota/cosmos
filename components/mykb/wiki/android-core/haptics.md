---
type: "concept"
title: "Haptics"
description: "Vibratory feedback for touch events and notifications"
tags: ["android", "haptics", "vibration", "ux"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Haptics

Haptics give physical feedback through vibration motors: performHapticFeedback on views, HapticFeedbackConstants for standard effects, and the Vibrator service for custom patterns.
- View.performHapticFeedback is the simple, system-consistent path.
- Custom patterns use Vibrator with VibrationEffect; check hasVibrator first.
- Respect system settings for vibration intensity.
- Haptics reinforce gestures and confirmations without sound.

## Related

- [[wiki/android-core/gesture-input|Gesture Input]] — haptics confirm gesture recognition
- [[wiki/android-core/sensors-api|Sensors API]] — vibration sits beside sensor hardware
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — haptics are a non-visual channel
- [[wiki/android-core/android-architecture|Android Architecture]] — hardware abstraction covers the motor
