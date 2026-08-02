---
type: "concept"
title: "JSON-RPC"
description: "JSON-RPC 2.0 requests, responses, and notifications"
tags: ["json-rpc", "rpc", "json", "protocols", "api-design"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://www.jsonrpc.org/specification", "https://www.jsonrpc.org/specification#request_object"]
---

# JSON-RPC

## Summary
JSON-RPC 2.0 is a minimal remote procedure call protocol: requests and responses are JSON objects with a version field, a method name, params, and an id. Notifications omit the id, requests without ids expect no response, and errors carry numeric codes — enough structure to build RPC APIs without a framework.

## Details
- Request: {"jsonrpc": "2.0", "method": "subtract", "params": [42, 23], "id": 1}; params may be positional or named.
- Notification: same without id — the server must not reply; used for events and fire-and-forget commands.
- Response: {"jsonrpc": "2.0", "result": 19, "id": 1} or {"error": {"code": -32601, "message": "Method not found"}, "id": 1}.
- Error codes: -32700 parse error, -32600 invalid request, -32601 method not found, -32602 invalid params, -32603 internal error; application errors use -32000 to -32099.
- Batching: an array of requests is processed and answered with an array of responses; a batch with all notifications gets no response at all.
- Transport: JSON-RPC is transport-agnostic — HTTP POST, WebSocket, TCP, and stdio (LSP uses it over pipes) are all common.
- Famous users: the Language Server Protocol, Ethereum JSON-RPC, and MQTT-over-websocket tooling.

## Related
- [[wiki/api-protocols/rpc-styles|RPC Styles]] — JSON-RPC sits on the RPC spectrum
- [[wiki/api-protocols/json-schema|JSON Schema]] — validating request and response shapes
- [[wiki/api-protocols/websocket-frames|WebSocket Frames]] — JSON-RPC frequently rides WebSockets
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — numeric codes and messages as the contract
- [[wiki/api-protocols/streaming-apis|Streaming APIs]] — notifications as one-way streaming events
