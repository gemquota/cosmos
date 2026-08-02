---
type: "concept"
title: "Streaming Responses with SSE"
description: "Delivering LLM tokens and events to clients incrementally over HTTP"
tags: ["streaming", "sse", "llm", "transport"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events", "https://docs.anthropic.com/en/docs/build-with-claude/streaming"]
---

# Streaming Responses with SSE

## Summary
Streaming responses send model output as it is generated — token by token over Server-Sent Events — so clients render text, tool calls, and progress in real time. Streaming cuts perceived latency from seconds to milliseconds. It also changes how agents consume LLMs: events arrive incrementally and must be buffered and parsed.

## Details
- **Transport** — SSE keeps one HTTP connection open and pushes `data:` frames; fetch streams and WebSockets are alternatives with different tradeoffs.
- **Event kinds** — text deltas, tool call fragments, citations, and finish reasons; many APIs emit structured event objects.
- **Client handling** — buffers must assemble deltas into complete tool calls before execution; cancellation works by aborting the connection.
- **Worked example** — an agent UI streams the reasoning text, then a tool_call event triggers execution, then the final answer streams.
- **Operational concerns** — proxy timeouts, backpressure, and partial-failure handling around dropped connections.
- **mykb relevance** — streaming responses and server-sent events are existing mykb topics; RSIS3 dashboards use them for live telemetry.

## Related
- [[wiki/ml-frameworks/server-sent-events|Server-Sent Events]] — the SSE protocol
- [[wiki/ml-frameworks/streaming-responses|Streaming Responses]] — existing streaming concept
- [[wiki/llm-agents/realtime-api-latency|Realtime API Latency]] — latency goals streaming serves
- [[wiki/testing/token-usage-tracking|Token Usage Tracking]] — counting streamed tokens
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — latency budgets
- [[wiki/agent-systems/endpoint-health-checks|Endpoint Health Checks]] — monitoring streaming endpoints
- [[wiki/agent-systems/partial-failure-handling|Partial Failure Handling]] — mid-stream failures
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — the API being streamed
