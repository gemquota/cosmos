---
type: "concept"
title: "Geolocation API"
description: "Accessing device location with permission, accuracy options, and privacy constraints"
tags: ["geolocation", "location", "web", "api", "privacy"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API", "https://www.w3.org/TR/geolocation/"]
---
# Geolocation API

## Summary
The Geolocation API gives web pages the device's position with user permission: latitude, longitude, accuracy, and optional altitude/speed. It powers maps, delivery tracking, and local recommendations. Permission prompts, accuracy trade-offs, and secure contexts constrain its use.

## Details
- **Permission model** — the browser prompts per origin; users can deny or revoke; secure contexts are required.
- **Accuracy options** — `enableHighAccuracy` trades battery and latency for precision; watchPosition streams updates.
- **Privacy** — location is sensitive: explain why it is needed, offer manual entry fallbacks, and avoid transmitting when not required.
- **Fallbacks** — IP geolocation and manual location entry cover denied or unavailable GPS.
- **Worked example** — a field-notes view in the mykb app attaches coordinates to entries only after explicit consent.
- **Relevance** — RSIS3's context-aware features should treat location as opt-in, ephemeral data.
- **Accuracy patterns** — one-shot getCurrentPosition suits maps; watchPosition suits tracking; falling back to coarse IP location preserves the feature when GPS is denied.

## Related
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/api-protocols/third-party-cookies|Third-Party Cookies]] — adjacent concept in this wiki
- [[wiki/api-protocols/partitioned-cookies|Partitioned Cookies]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/android-core/location-services|Location Services]] — existing coverage
- [[wiki/mobile-platform/mobile-network-optimization|Mobile Network Optimization]] — existing coverage
