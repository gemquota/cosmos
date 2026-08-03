---
type: "concept"
title: "Device Detection"
description: "Classifying devices via UA, Client Hints, and feature probing"
tags: ["device", "responsive", "web", "detection"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# Device Detection

## Summary

Device detection infers hardware and capabilities from user-agent strings or client hints. It is unreliable as a primary signal for layout — responsive design should react to features, not device names — but remains useful for downloads, billing, and analytics.

## Details
- Mechanism: user-agent parsing extracts OS, browser, and device tokens; the modern alternative is Client Hints (Sec-CH-UA, Sec-CH-UA-Mobile, Sec-CH-UA-Platform) which are structured and opt-in. UA strings are free-form, change per vendor, and can be spoofed.
- Concrete example: a music site serves high-bitrate downloads on desktop and warns mobile users about data costs — a legitimate use. Rendering a "mobile menu" based on UA while a tablet with a desktop viewport gets the wrong layout is the classic misuse.
- Failure modes: UA strings lying (desktop browsers claiming mobile to get m-sites, bots faking); Client Hints missing when the server does not opt in or the user disables them; device classes changing (foldables, hybrid laptops) breaking fixed assumptions; and using detection where feature detection or viewport size would work.
- Operational tradeoffs: detection is cheap and synchronous, while feature/Client-Hint approaches need revalidation and can be async. Use it only for decisions features cannot express — app-store deep links, peripheral capabilities, analytics cohorts. Cache and version your parser's dataset, since device lists rot.
- RSIS3/mykb relevance: dashboard telemetry tags sessions with coarse device class (from hints, not UA parsing) to segment Core Web Vitals by hardware tier.
- Progressive disclosure: even for legitimate detection use cases, always provide a manual override ("view desktop site") because detection errors are inevitable.
- Privacy: Client Hints are sent per-request and can be fingerprinting signals; minimize which hints you request and retain them only as long as needed.
- Feature-first: reach for viewport, pointer, and capability detection before device names; detection should answer what the device can do, not what it is called.

## Related
- [[wiki/web-platforms/responsive-design-systems|Responsive Design Systems]]
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]]
- [[wiki/web-platforms/device-detection|Device Detection]]
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]]
- [[wiki/web-platforms/web-apis|Web APIs]]
- [[wiki/web-platforms/browser-engines|Browser Engines]]
- [[wiki/web-platforms/web-standards|Web Standards]]
