---
type: "concept"
title: "Chunked Transfer Encoding"
description: "HTTP/1.1 chunked coding for streamed bodies"
tags: ["http", "chunked", "transfer-encoding", "streaming", "http1"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.rfc-editor.org/rfc/rfc9112#name-chunked-transfer-coding", "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Transfer-Encoding"]
---

# Chunked Transfer Encoding

## Summary
Chunked transfer encoding lets an HTTP/1.1 response (or request) send a body whose total size is unknown in advance: the body is split into size-prefixed chunks followed by a zero-length terminator. It is the mechanism behind streaming responses on HTTP/1.1 before HTTP/2's native streaming.

## Details
- Format: each chunk is <hex-size>\r\n<data>\r\n, ending with 0\r\n\r\n; trailers may follow the terminator for extra metadata such as checksums.
- Purpose: without Content-Length the client cannot know where the body ends; chunking delimits the body so keep-alive connections stay reusable.
- Relationship to Content-Length: they are mutually exclusive; Content-Length wins when both appear (a smuggling hazard), which is why intermediaries strip conflicting fields.
- HTTP/2 and HTTP/3 do not use chunked coding — DATA frames delimit bodies — so chunking is effectively an HTTP/1.x concept.
- Security: request smuggling attacks exploit inconsistent chunk parsing between proxies and origins; strict parsers reject malformed chunk sizes and duplicate framing fields.
- Streaming use: SSE, long polls, and server-sent binary streams rely on chunking to flush data before the full response is ready.

## Related
- [[wiki/api-protocols/http-keep-alive|HTTP Keep-Alive]] — chunking keeps persistent connections usable
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — SSE streams rely on chunked responses
- [[wiki/api-protocols/http2|HTTP/2]] — DATA frames replace chunked coding
- [[wiki/api-protocols/http-headers|HTTP Headers]] — Transfer-Encoding is a hop-by-hop field
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — chunking is the HTTP/1.1 streaming primitive
