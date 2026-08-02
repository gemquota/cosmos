---
type: "concept"
title: "gRPC Gateway"
description: "gRPC-to-REST JSON transcoding"
tags: ["grpc", "gateway", "rest", "transcoding", "protobuf"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://github.com/grpc-ecosystem/grpc-gateway", "https://grpc-ecosystem.github.io/grpc-gateway/"]
---

# gRPC Gateway

## Summary
grpc-gateway generates a reverse proxy that exposes gRPC services as RESTful JSON APIs: HTTP requests are transcoded to protobuf RPCs using annotations in the .proto files. Teams get one service definition and two client surfaces — typed gRPC internally, JSON over HTTP for browsers and third parties.

## Details
- Mechanism: google.api.http annotations on RPC methods declare the HTTP mapping (get: /v1/users/{name}); the gateway generates a Go reverse proxy.
- Transcoding: URL path and query parameters map to protobuf fields; JSON bodies convert to messages; gRPC responses serialize back to JSON.
- Status mapping: gRPC status codes translate to HTTP status codes (NotFound -> 404, InvalidArgument -> 400, Unauthenticated -> 401) via a well-known mapping.
- Streaming: server-streaming RPCs can stream JSON chunks or use chunked encoding; bidi and client-streaming are not supported the same way.
- OpenAPI output: the gateway can emit OpenAPI v2/v3 specs from the proto annotations, giving REST tooling for free.
- Alternatives: Google Cloud Endpoints and Envoy gRPC-JSON transcoders provide the same idea at the proxy level without codegen.
- Fit: perfect when the service layer already owns the domain model; avoid when REST semantics need to diverge from the RPC shape.

## Related
- [[wiki/api-protocols/grpc|gRPC]] — the RPC framework being exposed as REST
- [[wiki/api-protocols/openapi|OpenAPI]] — gateway-generated specs document the REST surface
- [[wiki/api-protocols/grpc-status-codes|gRPC Status Codes]] — code-to-HTTP mapping is core to transcoding
- [[wiki/api-protocols/api-gateway|API Gateway]] — the gateway pattern generalizes this proxy
- [[wiki/api-protocols/protobuf|Protobuf]] — annotations live in the proto definitions
