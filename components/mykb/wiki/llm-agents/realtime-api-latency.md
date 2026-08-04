---
type: "concept"
title: "Realtime API Latency"
description: "End-to-end latency engineering for realtime speech and agent APIs"
tags: ["realtime-latency", "realtime", "latency", "speech"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Realtime API Latency

## Summary

Realtime API latency is the engineering discipline of keeping end-to-end delay low for speech and agent APIs: capture, recognition, inference, synthesis, and delivery. Latency targets are what make conversation feel natural instead of robotic. It matters because every millisecond in the pipeline compounds into perceived lag. Latency is a feature: it decides whether the system feels like a conversation or a tool.

## Details

- **Definition** — End-to-end latency is the time from the user speaking to the agent's response being heard, measured across the whole pipeline.
- **Budgeting** — Each stage, from audio capture to TTS playback, gets a budget; budgets make latency a design constraint, not an accident.
- **Streaming** — Partial results and incremental audio hide latency by starting output before input completes.
- **Infrastructure** — Network hops, cold starts, and queueing add fixed costs that must be engineered down.
- **Perception** — Humans notice pauses above roughly a few hundred milliseconds; variance is as damaging as average delay.
- **Failure modes** — Optimizing one stage while ignoring jitter, or measuring latency without the full user path, misses the real experience.
- **Worked example** — A voice agent targets two hundred milliseconds to first audio by streaming recognition and synthesizing sentence chunks.
- **Practical relevance** — Latency engineering separates usable voice interfaces from demos.
- **Warm start** — Pre-warmed sessions and connection reuse eliminate cold-start spikes from the user path.
- **Backpressure** — Client and server must negotiate load so latency does not degrade into buffering and gaps.
- **Measurement** — Percentile tracking, not averages, reveals the tail latencies users actually feel.
- **Headroom** — Latency budgets must reserve headroom for load spikes so the experience degrades gradually instead of collapsing.

## Related

- [[wiki/llm-agents/voice-agents|Voice Agents]] — the systems with latency targets
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — model-side latency work
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses (SSE)]] — streaming transport
- [[wiki/llm-agents/speech-recognition-systems|Speech Recognition Systems]] — input-stage latency
- [[wiki/llm-agents/text-to-speech-llm|Text-to-Speech for LLMs]] — output-stage latency
