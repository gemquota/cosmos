---
type: "concept"
title: "HTTP Compression"
description: "Content-Encoding negotiation with gzip, br, and deflate"
tags: ["http", "compression", "performance", "content-encoding", "web-platforms"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9110#name-content-encoding", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Compression"]
---

# HTTP Compression

## Summary
HTTP compression reduces payload size by encoding the representation before transfer. The client advertises acceptable codings with Accept-Encoding, the server applies one and labels it with Content-Encoding, and the recipient decodes before use. gzip, deflate, and brotli dominate, with brotli typically winning on text.

## Details
- Negotiation: Accept-Encoding: gzip, deflate, br with q-values; identity means no encoding, and * is a wildcard fallback.
- Content-Encoding records what was applied — the reverse of Content-Type, which describes the decoded data; Transfer-Encoding, by contrast, is a hop-by-hop wire format.
- gzip (RFC 1952) is the near-universal baseline; deflate (zlib) is widely supported but historically buggy in servers; brotli (br) gives the best ratios for HTML, CSS, and JSON at higher CPU cost.
- Compression is a security trade-off: highly compressible secrets amplify BREACH-style side channels, so CSRF tokens and secrets should not sit in compressed responses.
- Only compress above a size threshold — small payloads expand or waste CPU, and media that is already compressed (images, video) should be sent as-is.
- CDNs and gateways commonly add compression centrally, letting origin servers omit it, which is why both Accept-Encoding handling and Vary headers matter for caches.

## Related
- [[wiki/api-protocols/content-negotiation|Content Negotiation]] — Accept-Encoding is one axis of representation negotiation
- [[wiki/api-protocols/http-headers|HTTP Headers]] — Content-Encoding and Vary are response fields
- [[wiki/api-protocols/http-caching|HTTP Caching]] — Vary: Accept-Encoding keeps compressed variants distinct
- [[wiki/api-protocols/http2|HTTP/2]] — stream compression complements header compression
- [[wiki/cloud-infra/content-delivery-networks|CDNs]] — edge compression centralizes encoding work
