---
type: "concept"
title: "Offline Testing"
description: "Verifying behavior without network and on reconnect"
tags: ["offline-testing", "testing", "pwa", "sync"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://developer.chrome.com/docs/workbox/", "https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps"]
---

# Offline Testing

## Summary
Offline testing verifies behavior without network and on reconnect: queued actions, cached reads, sync conflict handling, and graceful degraded modes. Offline-first apps live or die by these paths.

## Details
- Simulate with airplane mode, network throttling, and proxy blackholing such as netem.
- Verify reads from cache, queued writes, optimistic UI, sync on reconnect, and conflict resolution.
- PWA scope: service worker caching strategies like cache-first and stale-while-revalidate.
- Test reconnect storms: many queued writes flushing at once.
- Timeouts and partial network, flaky signal, matter as much as total loss.
- Conflicts need deterministic policies: last-write-wins, version vectors, or user prompts.
- Track offline metrics, queue depth and sync success, in production telemetry.

## Related
- [[wiki/testing/mobile-testing|Mobile Testing]] — mobile network conditions
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — service worker offline behavior
- [[wiki/mobile-platform/offline-first-apps|Offline-First Apps]] — architecture offline tests validate
- [[wiki/mobile-platform/mobile-data-sync|Mobile Data Sync]] — reconnect synchronization
- [[wiki/testing/compatibility-testing|Compatibility Testing]] — offline behavior across clients
- [[wiki/testing/recovery-testing|Recovery Testing]] — recovery after network loss
