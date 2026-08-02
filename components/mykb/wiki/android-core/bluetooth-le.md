---
type: "concept"
title: "Bluetooth LE"
description: "Low-energy Bluetooth for peripherals, beacons, and wearables"
tags: ["android", "bluetooth", "ble", "gatt"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Bluetooth LE

Bluetooth LE connects Android to low-power peripherals through scanning, GATT services, and characteristics. It powers wearables, beacons, and IoT accessories with minimal battery cost.
- Scan with BluetoothLeScanner; connect over GATT with a BluetoothGattCallback.
- Permissions: BLUETOOTH_SCAN and BLUETOOTH_CONNECT on Android 12+.
- Advertise to be discoverable by other devices.
- BLE is connection-oriented; design around reconnects.

## Scanning and Advertising

BLE operates on the 2.4 GHz band across 40 channels, with three dedicated advertising channels that let receivers discover nearby devices without establishing a full connection. Android exposes scanning through `BluetoothLeScanner`; a `ScanFilter` narrows results by service UUID, device name, or MAC address, while `ScanSettings` control duty cycle and reporting latency. Advertising is the counterpart: the `BluetoothLeAdvertiser` emits advertisement packets carrying the service UUID, device name, and manufacturer-specific data, so beacons and peripheral-style payloads can be read by nearby scanners. Choosing a sane scan interval and reporting window directly trades discovery latency against battery drain.

## GATT Services and Characteristics

Once a device is discovered, the Generic Attribute Profile (GATT) organizes data into services, characteristics, and descriptors. A `BluetoothGattCallback` receives connection state changes and characteristic read, write, and notification events. Operations such as MTU negotiation, service discovery, and descriptor writes must be sequenced, because the Android GATT stack processes one operation at a time and callbacks arrive asynchronously. Characteristics that change frequently are best consumed via notifications rather than polling; notifications keep the radio idle between events, which is the main reason BLE can sustain long-lived links on coin-cell devices.

## Reconnection and Lifecycle

Because BLE links are connection-oriented and radios sleep aggressively, links drop easily when the peer moves out of range or stops responding. Robust designs track connection state, retry with exponential backoff, and re-discover services after reconnect. On Android 12 and later, apps must declare `BLUETOOTH_SCAN` and `BLUETOOTH_CONNECT` in the manifest and request them at runtime, while older releases use the legacy `BLUETOOTH` and `BLUETOOTH_ADMIN` permissions. Connection intervals, supervision timeouts, and PHY selection (1M, 2M, or coded long-range) are negotiated with the peer, so firmware and app settings must agree for stable throughput.

## Related

- [[wiki/android-core/wear-os|Wear OS]] — watches pair over BLE
- [[wiki/android-core/android-permissions|Android Permissions]] — BLE uses dedicated runtime permissions
- [[wiki/android-core/nfc|NFC]] — the sibling short-range radio
- [[wiki/mobile-platform/mobile-network-optimization|Mobile Network Optimization]] — BLE sidesteps cellular data
