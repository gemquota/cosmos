---
type: "concept"
title: "Voice Agents"
description: "Agents that converse through speech recognition and synthesis in real time"
tags: ["voice-agents", "voice", "agents", "realtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Voice Agents

## Summary
Agents that converse through speech recognition and synthesis in real time

## Details
- Pipeline: ASR, language model, TTS, with barge-in handling.
- Low latency is critical for natural conversation.
- Realtime APIs bundle the audio loop.
- Evaluate with realtime-api-latency budgets.

## Related
- [[wiki/llm-agents/speech-recognition-systems|Speech Recognition Systems]] — hearing
- [[wiki/llm-agents/text-to-speech-llm|Text-to-Speech for LLMs]] — speaking
- [[wiki/llm-agents/realtime-api-latency|Realtime API Latency]] — performance target
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — conversation state
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses with SSE]] — streaming patterns
