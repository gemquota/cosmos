---
type: "concept"
title: "Payment Request API"
description: "Standardized browser checkout: payment methods, shipping, and the user approval sheet"
tags: ["payments", "web", "api", "checkout", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API", "https://www.w3.org/TR/payment-request/"]
---
# Payment Request API

## Summary
The Payment Request API standardizes checkout: the browser shows a native payment sheet, the user picks a method and confirms, and the app receives a payment response. It supports cards, wallets, and third-party methods, plus shipping and contact details. The app still handles the actual authorization server-side.

## Details
- **Flow** — construct a PaymentRequest with methods, details, and options; `show()` opens the sheet; `canMakePayment()` checks support.
- **Security model** — only the final authorized payment token matters; never trust client-side success alone.
- **Shipping and contact** — `shippingoptionchange` events update totals; contact info arrives with user consent.
- **Adoption** — browser support varies; the API is best layered behind feature detection with a checkout fallback.
- **Worked example** — the mykb storefront offers the payment sheet for subscriptions while the server confirms webhook-verified payments.
- **Relevance** — RSIS3's commerce features should follow the same server-confirmed pattern.

## Related
- [[wiki/api-protocols/webhook-delivery|Webhook Delivery]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-signatures|Webhook Signatures]] — adjacent concept in this wiki
- [[wiki/api-protocols/webhook-retries|Webhook Retries]] — adjacent concept in this wiki
- [[wiki/api-protocols/secure-flag|Secure Cookie Flag]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/api-protocols/api-keys|API Keys]] — existing coverage
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — existing coverage
