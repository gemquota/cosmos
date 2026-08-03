---
type: "concept"
title: "Streaming Responses"
description: "Incrementally delivering LLM output as tokens are generated, reducing perceived latency"
tags: ["streaming", "apis", "latency", "llm"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# Streaming Responses

## Summary

Streaming responses deliver model output incrementally — token deltas over SSE — so users see progress and first tokens arrive in hundreds of ms instead of seconds. It changes perceived latency, UX, and the engineering of the serving path.

## Details
- Mechanism: the server streams server-sent events (SSE) with delta chunks (content, tool calls, reasoning); clients accumulate deltas until the final chunk signals completion (with usage); HTTP/2 and connection reuse matter for many parallel streams; proxies must not buffer the response or streaming is defeated.
- Concrete example: a chat UI renders tokens as they arrive — the first token in ~300ms, full answer later; a RAG agent streams its reasoning then its answer; a dashboard streams chart annotations live. The failure pattern: a proxy or framework buffering the whole response, turning a stream into a long wait.
- Failure modes: buffering intermediaries (CDN/proxy buffering kills TTFT — configure no-buffer); client accumulation bugs (re-encoding partial deltas as full messages); reconnection semantics — streams break on network blips and clients must resume or restart; and cost/telemetry gaps when usage arrives only in the final chunk.
- Operational tradeoffs: streaming trades server simplicity for UX and perceived latency; the discipline is end-to-end streaming (server → proxy → client), no-buffer configuration, and client logic that treats the stream as append-only with a terminal event.
- RSIS3/mykb relevance: the wiki's agent console would stream loop progress and answers, so long passes feel responsive and cancelable instead of opaque.
- Backpressure: producers can outpace slow clients; streaming frameworks need flow control (or the connection buffers grow) — test under slow-client conditions.
- Error mid-stream: define how partial content and errors are signaled (final error event, status) so clients can render what arrived and retry cleanly.

## Related
- [[wiki/ml-frameworks/server-sent-events|Server-Sent Events]] — The transport used for streaming
- [[wiki/ml-frameworks/chat-completions|Chat Completions]] — The endpoint that supports streaming
- [[wiki/prompt-engineering/tool-calling|Tool Calling]] — Tool-call fragments in streams
- [[wiki/prompt-engineering/agent-state|Agent State]] — Consuming partial outputs safely
- [[wiki/ml-frameworks/openai-api|OpenAI API]] — Reference streaming support
