---
type: "concept"
title: "Speech Recognition Systems"
description: "Systems converting audio speech into text with low latency and high accuracy"
tags: ["asr", "speech", "recognition", "audio"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# Speech Recognition Systems

## Summary

Speech recognition systems convert spoken audio into text with low latency and high accuracy. They are the input side of voice interfaces and a preprocessing step for many multimodal pipelines. They matter because transcription quality sets the ceiling for everything downstream in a voice agent. ASR quality is measured in context: a transcript is only as useful as the actions taken on it.

## Details

- **Definition** — Automatic speech recognition (ASR) maps an audio signal to a sequence of words, typically with a language model over acoustic features.
- **Acoustic modeling** — Models learn the mapping from sound to phonemes or subword units, handling accents, noise, and speaking rate.
- **Streaming vs batch** — Streaming ASR emits words as they are spoken; batch ASR processes full recordings with higher accuracy.
- **Latency** — End-to-end latency includes audio capture, model inference, and endpointing; voice agents budget each stage.
- **Robustness** — Background noise, overlapping speech, and domain vocabulary are the main accuracy challenges.
- **Punctuation and casing** — Readable transcripts require restoring punctuation and capitalization, which raw words do not carry.
- **Failure modes** — Mis-heard commands, silent truncation, and confident errors on rare words are the practical failure modes.
- **Practical relevance** — ASR errors propagate into dialog state, so recognition quality must be measured in the full pipeline.
- **Vocabulary adaptation** — Domain terms and names need custom lexicons; generic models stumble on them.
- **Speaker handling** — Diarization separates who said what, which matters for meetings and multi-speaker audio.
- **Quality metrics** — Word error rate is the headline metric, but task success is the one that counts in agents.

## Related

- [[wiki/llm-agents/voice-agents|Voice Agents]] — the systems ASR feeds
- [[wiki/llm-agents/audio-models-multimodal-models|Audio and Multimodal Models]] — the model family
- [[wiki/llm-agents/realtime-api-latency|Realtime API Latency]] — transcription latency budgets
- [[wiki/llm-agents/dialog-state-tracking|Dialog State Tracking]] — consuming transcripts
- [[wiki/llm-agents/text-to-speech-llm|Text-to-Speech for LLMs]] — the output side of voice
