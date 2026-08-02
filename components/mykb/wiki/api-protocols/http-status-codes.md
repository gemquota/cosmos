---
type: "concept"
title: "HTTP Status Codes"
description: "1xx-5xx classes and commonly used response codes"
tags: ["http", "status-codes", "error-handling", "web-platforms"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-status-codes", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Status"]
---

# HTTP Status Codes

## Summary
HTTP status codes are three-digit results divided into five classes that tell a client whether the request succeeded, was redirected, or failed. The class digit — 1xx informational, 2xx success, 3xx redirection, 4xx client error, 5xx server error — is the contract clients can depend on even when they do not know the specific code.

## Details
- 1xx is informational: 100 Continue invites the client to send the body; 101 Switching Protocols confirms a protocol upgrade such as WebSocket or h2c.
- 2xx success: 200 OK, 201 Created (with a Location header), 202 Accepted (async processing), 204 No Content for successful writes with no body, 206 Partial Content for range requests.
- 3xx redirection: 301 Moved Permanently and 308 Permanent Redirect (method-preserving), 302 Found and 303 See Other (usually converted to GET), 304 Not Modified for cache revalidation, 307 Temporary Redirect.
- 4xx client errors: 400 Bad Request, 401 Unauthorized (missing or invalid credentials), 403 Forbidden (authenticated but not allowed), 404 Not Found, 405 Method Not Allowed, 409 Conflict, 422 Unprocessable Content, 429 Too Many Requests.
- 5xx server errors: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable (with Retry-After), 504 Gateway Timeout.
- Choosing the wrong class breaks clients: returning 200 with an error body defeats error middleware, while returning 403 instead of 401 breaks login flows and security tooling.

## Related
- [[wiki/api-protocols/http-methods|HTTP Methods]] — methods determine which status codes are legal
- [[wiki/api-protocols/problem-details|Problem Details]] — structured bodies carry error details beyond the code
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — consistent code usage is part of the contract
- [[wiki/api-protocols/http-caching|HTTP Caching]] — 304 revalidation keeps caches fresh
- [[wiki/api-protocols/load-shedding|Load Shedding]] — 503 is the canonical overload response
- [[wiki/api-protocols/rest-apis|REST APIs]] — status codes complete the REST contract
