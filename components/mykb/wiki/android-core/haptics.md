---
type: "concept"
title: "Haptics"
description: "Vibratory feedback for touch events and notifications"
tags: ["android", "haptics", "vibration", "ux"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Haptics

Haptics give physical feedback through the vibration motor of a device, turning touch into a felt response. They are one of the main non-visual, non-auditory channels in mobile UX: a confirmation tap, a scroll tick, or an error buzz tells the user something happened without any change on screen.

- View.performHapticFeedback is the simple, system-consistent path. It plays a standard effect tied to a view, such as confirming a long press or rejecting an action, and respects the user's system-level haptic settings automatically.
- HapticFeedbackConstants lists the standard effects, including KEYBOARD_TAP, LONG_PRESS, CONFIRM, and REJECT. Choosing a system constant keeps behavior consistent with the rest of the operating system.
- Custom patterns use the Vibrator service with VibrationEffect. createOneShot produces a single pulse of a given duration and amplitude, while createWaveform sequences pulses with timing, optional repetition, and per-segment amplitudes.
- Check hasVibrator (and, on some devices, hasAmplitudeControl) before calling the vibrator, because hardware support varies across devices and emulators.
- Respect system settings for vibration intensity. Apps should check the haptic feedback enabled setting and avoid overriding it; accessibility users often reduce or disable vibration.
- Keep effects short and meaningful. Long or repeated vibration is unpleasant, drains battery, and can trigger motion-sensitive conditions.
- Haptics reinforce gestures and confirmations without sound. A drag snap, a completed download, or a failed login all benefit from a quick, distinct pulse.

Because vibration sits close to the hardware, it is managed through the platform's hardware abstraction layer rather than through direct motor control. The related notes below connect haptics to gesture input, sensor hardware, accessibility, and Android architecture, showing where the haptic channel fits in the wider system.



Design guidance keeps haptics effective: one effect per event, consistent mapping between event type and pattern, and preview support during development. Platforms increasingly expose tuning options so that a subtle tick can be distinguished from a strong alert. Testing on real hardware matters, because emulators rarely reproduce motor characteristics, and the same code can feel different across devices.
## Related

- [[wiki/android-core/gesture-input|Gesture Input]] — haptics confirm gesture recognition
- [[wiki/android-core/sensors-api|Sensors API]] — vibration sits beside sensor hardware
- [[wiki/mobile-platform/mobile-accessibility|Mobile Accessibility]] — haptics are a non-visual channel
- [[wiki/android-core/android-architecture|Android Architecture]] — hardware abstraction covers the motor
