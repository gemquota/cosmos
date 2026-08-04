---
type: "entity"
title: "Request"
description: "Request: HTTP request lifecycle and handling in SPAs"
tags: ["ajax", "api", "ast", "auth", "authentication", "bootstrap", "bug", "cli", "cloud", "dom", "entity", "spa", "http"]
timestamp: "2026-07-19T22:41:39Z"
resource: ""
---

# Request

## Summary

Request is the ajax-spa entity for HTTP requests in single-page applications: how clients construct, send, and handle them. Request handling spans methods, headers, bodies, caching, and errors. It matters because every SPA feature ultimately depends on reliable request behavior. Requests are the contract between the SPA and its backend; both sides must honor it.

## Details

- **Definition** — An HTTP request carries a method, target, headers, and optional body from client to server, and receives a response.
- **Methods** — GET, POST, PUT, PATCH, and DELETE map to read, create, replace, update, and remove semantics.
- **Headers** — Content types, auth tokens, and cache directives shape how both sides interpret the exchange.
- **Bodies** — Serialization formats and size limits govern the payload; validation catches malformed data early.
- **Errors** — Status codes signal outcomes; clients must distinguish retryable from permanent failures. Clients should also surface the failed request context, such as URL and status, so users and logs can trace the failure.
- **Worked example** — A login form POSTs credentials, stores the returned token, and retries once on a network failure.
- **Failure modes** — Missing credentials, unhandled timeouts, and responses whose shape drifts from the client model break SPAs.
- **Practical relevance** — Request abstractions, like serialized queues, exist to make these interactions predictable.
- **Abort handling** — Cancelled requests must not update state after unmount, preventing race conditions in the UI.
- **Retry policy** — Retries belong on idempotent requests, with backoff, and must not duplicate side effects.
- **Security headers** — Consistent headers for auth, content type, and cross-origin settings keep requests valid and safe.
- **Interceptors** — Centralizing headers, logging, and error handling in interceptors keeps individual call sites simple.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/serialized-request-queue|Serialized Request Queue]] — ordering request execution
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecure Request Warning]] — mixed-content request hazards
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/interaction-locks|Interaction Locks]] — guarding UI during requests
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/00-index|AJAX SPA Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/captcha-detected|Captcha Detected]] — blocked request handling
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/context-updates|Context Updates]] — state after responses
