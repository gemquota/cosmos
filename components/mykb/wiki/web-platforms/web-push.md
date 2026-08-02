---
type: "concept"
title: "Web Push"
description: "Sending notifications to users from servers via push services and service workers"
tags: ["push", "notifications", "service-workers", "web", "realtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Push_API", "https://web.dev/articles/push-notifications-overview"]
---
# Web Push

## Summary
Web Push lets servers deliver messages to browsers through push services, waking a service worker even when the site is closed. The flow: subscribe with VAPID keys, send the subscription to the server, and have the server POST encrypted payloads to the push service. It is the mobile-app-like channel of the web.

## Details
- **Subscription flow** — `pushManager.subscribe()` with a VAPID public key returns a subscription endpoint; store it server-side per user.
- **Delivery** — the server sends encrypted payloads (E2E via applicationServerKey) to the push service, which queues and delivers; payloads may be dropped.
- **Display** — the service worker's `push` event shows a notification or triggers a background sync.
- **Lifecycle** — unsubscribe and prune stale endpoints (410s); keep payloads small; 4KB limit on most browsers.
- **Worked example** — the mykb daemon pushes completion notifications with VAPID keys stored in its secrets manager.
- **Relevance** — RSIS3's long-running agents can alert users without a foreground UI.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-topics|Webhook Topics]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]] — adjacent concept in this wiki
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
