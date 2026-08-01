---
type: "concept"
title: "NFC"
description: "Near-field communication for tags, payments, and host card emulation"
tags: ["android", "nfc", "rfid", "tags"]
timestamp: "2026-08-01T00:00:00Z"
status: "stub"
source: []
---

# NFC

NFC lets Android read tags and act as a contactless card. Apps use NFC adapter APIs with NDEF message parsing, and Host Card Emulation (HCE) serves virtual cards without a secure element.
- Manifest declares NFC feature and NDEF intent filters for tag dispatch.
- HCE implements APDU-based services for payments and access.
- Works at centimeters; expect intermittent reads on first tap.
- Privacy: readers can be passive, so gate actions behind user intent.

## Related

- [[wiki/android-core/bluetooth-le|Bluetooth LE]] — sibling proximity radio
- [[wiki/android-core/android-permissions|Android Permissions]] — NFC access needs declared permissions
- [[wiki/mobile-platform/mobile-security-hardening|Mobile Security Hardening]] — HCE and payments raise the bar
- [[wiki/android-core/android-ndk|Android NDK]] — native stacks sometimes handle NFC
