---
type: "concept"
title: "Web Notifications"
description: "The Notifications API: requesting permission and displaying system-level notifications"
tags: ["notifications", "web", "api", "permissions", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Notifications_API", "https://www.w3.org/TR/notifications/"]
---
# Web Notifications

## Summary
The Notifications API shows system-level notifications from web pages: title, body, icon, and actions. Permission is user-granted and can be revoked; notifications can wake the service worker for click handling. Combined with Push, they deliver updates even when the page is closed.

## Details
- **Permission flow** — `Notification.requestPermission()` prompts once; respect the choice and explain the value before asking.
- **Lifecycle** — notifications persist until dismissed or closed; `onclick` focuses the app; actions offer quick choices.
- **Service worker integration** — notificationclick events route through the service worker even if the page is closed.
- **Anti-patterns** — nagging permission prompts, notification spam, and notifications without a click destination.
- **Worked example** — the mykb wiki sends a notification when a long-running acquisition pass completes, linking back to the log.
- **Relevance** — RSIS3's background tasks can surface completion without keeping a UI open.
- **Quiet hours** — respect system Do Not Disturb; browsers may suppress notifications; scheduling and frequency caps prevent the permission from being revoked.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-events|Webhook Events]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-topics|Webhook Topics]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-subscriptions|Webhook Subscriptions]] — adjacent concept in this wiki
- [[wiki/mobile-platform/push-notifications|Push Notifications]] — existing coverage
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — existing coverage
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
