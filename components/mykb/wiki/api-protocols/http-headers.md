---
type: "concept"
title: "HTTP Headers"
description: "Standard request and response headers and their conventions"
tags: ["http", "headers", "web-platforms", "protocols"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-fields", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers"]
---

# HTTP Headers

## Summary
HTTP headers are name-value pairs sent with requests and responses that carry metadata: authentication, caching, content description, and connection control. RFC 9110 defines the field syntax and the registry of standard fields, while custom fields use an X- prefix sparingly and ideally follow registered conventions.

## Details
- Request headers: Host (mandatory in HTTP/1.1), Accept, Accept-Encoding, Authorization, User-Agent, Referer, Content-Type, Content-Length, and cache-control directives.
- Response headers: Content-Type with charset, Content-Length, Cache-Control, ETag, Last-Modified, Location, Set-Cookie, Retry-After, and CORS fields like Access-Control-Allow-Origin.
- Field names are case-insensitive but conventionally written in Title-Case; values are structured per field and parsed by recipients, not treated as opaque strings.
- Content headers describe the representation: Content-Type, Content-Length, Content-Encoding, Content-Language, and Content-Disposition govern how the body is interpreted.
- Connection-related fields (Connection, Keep-Alive, Transfer-Encoding) are hop-by-hop and are removed by proxies, unlike end-to-end fields that travel the whole path.
- Security-sensitive fields such as Authorization and Set-Cookie must never be logged or cached in plaintext; proxies and CDNs need explicit configuration to forward them.

## Related
- [[wiki/api-protocols/http-methods|HTTP Methods]] — headers like Content-Type shape method semantics
- [[wiki/api-protocols/http-cookies|HTTP Cookies]] — Set-Cookie and Cookie are specialized header pairs
- [[wiki/api-protocols/content-negotiation|Content Negotiation]] — Accept-family headers drive representation choice
- [[wiki/api-protocols/http-compression|HTTP Compression]] — Content-Encoding and Accept-Encoding negotiate compression
- [[wiki/api-protocols/cors|CORS]] — CORS fields are response headers that relax same-origin rules
- [[wiki/security-auth/security-headers|Security Headers]] — headers like CSP and HSTS harden responses
