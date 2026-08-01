---
type: "concept"
title: "Sensors API"
description: "Accelerometer, gyroscope, and other hardware sensors via SensorManager"
tags: ["android", "sensors", "hardware", "battery"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Sensors API

The Sensors API exposes device hardware sensors - accelerometer, gyroscope, magnetometer, light, proximity - through SensorManager and SensorEventListener. Raw and fused virtual sensors (rotation vector, step counter) simplify app logic.
- Register with a delay (SENSOR_DELAY_NORMAL, GAME, UI, FASTEST) that trades battery for rate.
- Sensor batching lets the hardware buffer readings and wake the app less often.
- Rotation vector and step counter are fused, low-power choices.
- Always unregister in onPause to avoid drain.

## Related

- [[wiki/android-core/android-architecture|Android Architecture]] — sensors sit behind the HAL
- [[wiki/mobile-platform/battery-aware-development|Battery-Aware Development]] — sampling rates are battery trade-offs
- [[wiki/android-core/wear-os|Wear OS]] — wearables live on sensors
- [[wiki/android-core/haptics|Haptics]] — vibration is a sibling actuator
