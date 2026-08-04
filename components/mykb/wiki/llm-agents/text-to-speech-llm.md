---
type: "concept"
title: "Text-to-Speech for LLMs"
description: "Synthesizing natural speech from model text output"
tags: ["tts", "speech", "tts", "audio"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Text-to-Speech for LLMs

## Summary

Text-to-speech (TTS) for LLMs synthesizes natural speech from model output, closing the loop from generated text to spoken voice. Modern TTS produces expressive, near-human voices with low latency. It matters because voice is the most natural output channel for many agent applications. TTS turns text into presence; its quality is measured by comprehension, naturalness, and latency.

## Details

- **Definition** — TTS converts text into audio, using neural models to generate prosody, rhythm, and timbre that sound natural.
- **Architectures** — Autoregressive and diffusion-based models generate waveforms or intermediate representations that are converted to audio.
- **Voice control** — Speaker embeddings select identity; style and emotion controls shape delivery.
- **Streaming** — Chunked synthesis lets agents start speaking before the full response is generated, cutting perceived latency.
- **Latency budget** — Voice agents budget TTS time alongside recognition and model inference to stay conversational.
- **Failure modes** — Mispronunciations, robotic prosody on complex text, and clicks from poor chunk boundaries degrade trust.
- **Worked example** — A chatbot's answer is split into sentences, synthesized incrementally, and spoken as the next sentences are still being generated.
- **Practical relevance** — TTS quality directly affects user experience in voice agents, assistants, and accessibility features.
- **Pronunciation control** — Lexicons and phoneme overrides fix proper nouns and technical terms that neural models misread.
- **Voice consistency** — Long sessions need stable voice identity across many synthesized chunks.
- **Emotion and emphasis** — Expressive synthesis marks emphasis and sentiment, making output feel intentional rather than flat.
- **Evaluation** — Naturalness ratings, comprehension tests, and latency measurements together capture what users experience.

## Related

- [[wiki/llm-agents/voice-agents|Voice Agents]] — the systems TTS powers
- [[wiki/llm-agents/speech-recognition-systems|Speech Recognition Systems]] — the input-side counterpart
- [[wiki/llm-agents/realtime-api-latency|Realtime API Latency]] — synthesis latency budgets
- [[wiki/llm-agents/audio-models-multimodal-models|Audio and Multimodal Models]] — the model family
- [[wiki/prompt-engineering/tone-control|Tone Control]] — controlling output style
- [[wiki/llm-agents/streaming-responses-sse|Streaming Responses (SSE)]] — streaming synthesis
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — spoken dialog state
