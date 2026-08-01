---
type: "concept"
title: "Server-Sent Events"
description: "SSE: a simple HTTP protocol for servers pushing a stream of events to a browser or client"
tags: ["server-sent-events", "sse", "streaming", "http"]
timestamp: "2026-07-31T00:00:00Z"
status: "stub"
---

# Server-Sent Events

## Summary
Server-Sent Events is a one-way HTTP streaming protocol where the server keeps a connection open and pushes text events. It is the standard transport for token streaming from LLM APIs.

## Details
- Format: lines of 'data: ...' separated by blank lines; clients use EventSource or fetch readers.
- Unlike WebSockets, SSE is one-way and rides plain HTTP, simplifying proxies and retries.
- Handles reconnection with Last-Event-ID automatically.
- RSIS3 relevance: the dashboard consumes RSIS3 streaming telemetry via SSE-style endpoints.

## Related
- [[wiki/ml-frameworks/streaming-responses|Streaming Responses]] — The LLM feature SSE transports
- [[wiki/prompt-engineering/message-format|Message Format]] — The payloads inside events
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — SSE-based streaming endpoint
- [[raw/archive/session-artifacts-2026-07/topics/http-10|http — The underlying protocol
- [[wiki/prompt-engineering/agent-state|Agent State]] — Client-side stream assembly
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool-call events stream over SSE
