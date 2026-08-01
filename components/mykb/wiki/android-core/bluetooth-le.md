---
type: "concept"
title: "Bluetooth LE"
description: "Low-energy Bluetooth for peripherals, beacons, and wearables"
tags: ["android", "bluetooth", "ble", "gatt"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# Bluetooth LE

Bluetooth LE connects Android to low-power peripherals through scanning, GATT services, and characteristics. It powers wearables, beacons, and IoT accessories with minimal battery cost.
- Scan with BluetoothLeScanner; connect over GATT with a BluetoothGattCallback.
- Permissions: BLUETOOTH_SCAN and BLUETOOTH_CONNECT on Android 12+.
- Advertise to be discoverable by other devices.
- BLE is connection-oriented; design around reconnects.

## Related

- [[wiki/android-core/wear-os|Wear OS]] — watches pair over BLE
- [[wiki/android-core/android-permissions|Android Permissions]] — BLE uses dedicated runtime permissions
- [[wiki/android-core/nfc|NFC]] — the sibling short-range radio
- [[wiki/mobile-platform/mobile-network-optimization|Mobile Network Optimization]] — BLE sidesteps cellular data
