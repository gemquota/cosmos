---
type: "concept"
title: "gRPC-Web"
description: "Browser gRPC over HTTP/1.1 via a proxy"
tags: ["grpc", "grpc-web", "browsers", "http1", "protobuf"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/grpc/grpc-web", "https://grpc.io/blog/state-of-grpc-web/"]
---

# gRPC-Web

## Summary
gRPC-Web lets browsers call gRPC services without WebSocket transport or HTTP/2 trailers: a proxy translates the gRPC protocol into an HTTP/1.1-compatible form that fetch and XHR can use. It brings typed protobuf contracts to browser clients while keeping the server implementation unchanged.

## Details
- Why a proxy: browsers cannot send HTTP/2 trailers, which gRPC uses for status, so grpc-web (the gateway) converts trailer data into headers or a base64 status blob.
- Deployment: the grpc-web proxy (Envoy with grpc-web filter, grpc-web Node proxy, or grpc-gateway) sits in front of the gRPC server.
- Request encoding: messages are sent as protobuf (or JSON with the JSON codec) over POST; the Content-Type is application/grpc-web+proto.
- Streaming support: server-streaming works via chunked responses; client-streaming and bidi-streaming are not supported — a significant limitation.
- Client libraries: @grpc/grpc-js-web, grpc-web (JavaScript), and wrappers for React; generated clients use the same .proto contracts.
- Trade-offs: no bidi means realtime chat needs WebSockets or SSE alongside; browsers impose CORS, so gateways must set Access-Control-Allow-* headers.
- Modern alternative: connect-es (Connect protocol) offers native browser streaming over HTTP/1.1 without a proxy, and speaks gRPC interop.

## Related
- [[wiki/api-protocols/grpc|gRPC]] — the server protocol grpc-web adapts for browsers
- [[wiki/api-protocols/cors|CORS]] — browser calls require CORS configuration
- [[wiki/api-protocols/grpc-gateway|gRPC Gateway]] — an alternative proxy exposing JSON REST
- [[wiki/api-protocols/server-sent-events|Server-Sent Events]] — one-way browser streaming without gRPC
- [[wiki/api-protocols/protobuf|Protobuf]] — the wire format browsers must decode
