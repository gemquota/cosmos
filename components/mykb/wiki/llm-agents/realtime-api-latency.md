---
type: "concept"
title: "Realtime API Latency"
description: "End-to-end latency engineering for realtime speech and agent APIs"
tags: ["realtime-latency", "realtime", "latency", "speech"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Realtime API Latency

## Summary
End-to-end latency engineering for realtime speech and agent APIs

## Details
- Budgets span audio capture, ASR, model inference, and TTS.
- Streaming and chunking hide portions of the pipeline.
- Perceived latency differs from technical latency.
- Measured with latency-budgets-throughput-calibration.

## Related
- [[wiki/llm-agents/voice-agents|Voice Agents]] — primary consumer
- [[wiki/ai-ml/llm-latency-optimization|LLM Latency Optimization]] — model latency
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses with SSE]] — streaming transport
- [[wiki/llm-agents/speech-recognition-systems|Speech Recognition Systems]] — ASR latency
- [[wiki/llm-agents/text-to-speech-llm|Text-to-Speech for LLMs]] — TTS latency
