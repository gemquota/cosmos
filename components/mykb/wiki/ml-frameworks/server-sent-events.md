---
type: "concept"
title: "Server-Sent Events"
description: "HTTP streaming transport that pushes model tokens to clients as they are generated"
tags: ["sse", "streaming", "http", "real-time"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events", "https://developer.mozilla.org/en-US/docs/Web/API/EventSource"]
---

# Server-Sent Events

## Summary
Server-Sent Events (SSE) is a one-way HTTP streaming protocol used to deliver LLM tokens as they are generated. It matters because users perceive streaming as responsiveness, and agents need incremental output. SSE is simpler than WebSockets for one-way model-to-client flow.

## Details
- **Mechanism** — the server keeps a response open and writes text/event-stream messages per token or chunk.
- **Benefits** — lower time-to-first-token perception, cancellation support, and simple reconnection.
- **Worked example** — a chat UI renders tokens via SSE events, showing a typing effect and enabling stop-mid-generation.
- **Alternatives** — WebSockets for bidirectional flows; both feed streaming-responses-sse patterns.
- **mykb relevance** — RSIS3 chat loops should stream to feel instant.
- **Worked example** — a chat UI renders tokens via SSE events, showing a typing effect and enabling stop-mid-generation.
- **Reliability** — reconnection with last-event-id and heartbeat comments keeps long generations robust.
- **Alternatives** — WebSockets for bidirectional flows; SSE suits one-way model-to-client streaming with simpler semantics.
- **mykb relevance** — streaming responses make RSIS3 knowledge loops feel immediate and responsive.

## Related
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses with SSE]] — streaming pattern
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — perceived latency
- [[wiki/llm-agents/realtime-api-latency|Realtime API Latency]] — realtime budgets
- [[wiki/llm-agents/llm-gateway-and-routing|LLM Gateway and Routing]] — streaming gateways
- [[wiki/agent-systems/agent-observability|Agent Observability]] — streamed telemetry
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — the API surface it uses
- [[wiki/syntheses/knowledge-system|Knowledge System Overview]] — the KB loop this work feeds
- [[wiki/agent-systems/retry-jitter|Retry Jitter]] — related concept in this cluster
