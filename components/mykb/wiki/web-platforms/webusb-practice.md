---
type: "concept"
title: "WebUSB in Practice"
description: "Connecting web apps to USB devices: device selection, claim, and control transfers"
tags: ["webusb", "usb", "hardware", "web", "api"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/WebUSB_API", "https://wicg.github.io/webusb/"]
---
# WebUSB in Practice

## Summary
WebUSB lets web pages communicate with USB devices after explicit user selection: list devices, claim interfaces, and perform control/bulk/interrupt transfers. It enables firmware flashers, printer tools, and hardware labs without native drivers. Secure contexts and user gestures are mandatory.

## Details
- **Selection and permissions** — `navigator.usb.requestDevice()` shows a chooser; granted origins persist for that device.
- **Transfers** — control transfers configure; bulk and interrupt transfers move data; `transferOut`/`transferIn` manage streams.
- **Interface claims** — devices must be claimed per interface; drivers may block claiming on some platforms.
- **Constraints** — HTTPS only, Chrome-first support, and OS driver conflicts.
- **Worked example** — a mykb tool flasher updates an embedded device's firmware through WebUSB after the user picks the device from the chooser.
- **Relevance** — RSIS3's device tooling could offer browser-based hardware access where native drivers are unavailable.
- **Session lifecycle** — permissions persist per origin and device; devices disconnect without notice, so apps must handle disconnect, re-request, and re-claim flows gracefully.

## Related
- [[wiki/api-protocols/file-upload-security|File Upload Security]] — adjacent concept in this wiki
- [[wiki/api-protocols/zip-slip|Zip Slip]] — adjacent concept in this wiki
- [[wiki/web-platforms/path-normalization|Path Normalization]] — adjacent concept in this wiki
- [[wiki/web-platforms/allowlist-validation|Allowlist Validation]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/web-components|Web Components]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
