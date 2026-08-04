---
type: "concept"
title: "Voice Agents"
description: "Agents that converse through speech recognition and synthesis in real time"
tags: ["voice-agents", "voice", "agents", "realtime"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Voice Agents

## Summary

Voice agents converse through speech recognition and synthesis in real time, letting users interact by talking. They chain ASR, language understanding, action, and TTS into one low-latency loop. They matter because voice is the most accessible interface for many users and contexts. Voice is the most demanding interface because its latencies and errors are immediately audible.

## Details

- **Definition** — A voice agent is an end-to-end conversational system where input is spoken and output is spoken.
- **Pipeline** — Recognition, understanding, response generation, and synthesis run in sequence, with each stage adding latency.
- **Turn-taking** — Detecting when the user stops speaking and when to interrupt requires endpointing and barge-in handling.
- **State** — Dialog state tracking keeps the conversation coherent across spoken turns, including corrections and mid-sentence changes.
- **Latency** — Conversational feel demands tight budgets: recognition and synthesis must stream, not wait for completion.
- **Failure modes** — Misheard inputs, latency that feels like silence, and interruptions handled poorly break the illusion of conversation.
- **Worked example** — A customer-service agent listens, transcribes, answers, and speaks the response, pausing when the user interrupts.
- **Practical relevance** — Voice agents are the proving ground for realtime multimodal systems and streaming APIs.
- **Graceful degradation** — When speech fails, the agent should fall back to text or a clear apology rather than silence.
- **Privacy** — Audio is sensitive data; voice agents need explicit capture consent and minimal retention.
- **Testing** — Voice flows need end-to-end testing with recorded audio, not just text transcripts.
- **Evaluation** — Voice agents need end-to-end metrics, such as task completion per conversation, beyond per-stage accuracy.

## Related

- [[wiki/llm-agents/speech-recognition-systems|Speech Recognition Systems]] — hearing side of the agent
- [[wiki/llm-agents/text-to-speech-llm|Text-to-Speech for LLMs]] — speaking side of the agent
- [[wiki/llm-agents/realtime-api-latency|Realtime API Latency]] — the latency constraints
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — conversation memory
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses (SSE)]] — streaming response patterns
