---
type: "entity"
title: "OscillatorNode"
description: "OscillatorNode is an entity from the wiki's session index whose name refers to the audio node that generates a periodic waveform, a core building block of web a"
tags: ["entity", "android", "api", "ast", "aws", "bash"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# OscillatorNode

## Summary
OscillatorNode is an entity from the wiki's session index whose name refers to the audio node that generates a periodic waveform, a core building block of web audio synthesis. Oscillators produce the tones that instruments, alarms, and test signals are built from. This page documents the concept behind the entity. Oscillators are the simplest sound source and the foundation of synthesis.

## Details
- **Definition** — an oscillator is a signal source that generates a repeating waveform, typically sine, square, triangle, or sawtooth, at a controllable frequency.
- **Web Audio role** — in web audio graphs, oscillator nodes feed into gain, filter, and destination nodes to produce sound.
- **Parameters** — frequency and waveform type are the primary controls; modulation can vary them over time for richer sound.
- **Use cases** — oscillators build tones, test signals, simple instruments, and alarm sounds in applications.
- **Worked example** — an app creates a sine oscillator, connects it through a gain node to the destination, and ramps the frequency to play a rising alarm.
- **Failure modes** — unconnected graphs produce silence, unbounded gain causes clipping, and missing user-gesture context blocks playback.
- **Relation to audio entities** — the entity belongs to the family of audio nodes recorded in the REST cluster.
- **Practical relevance** — oscillator nodes are a standard part of audio programming, and this entity anchors notes about audio synthesis.
- **Modulation** — frequency and gain modulation create movement that static tones lack.
- **Graph discipline** — every oscillator needs a path to the destination or it silently contributes nothing.
- **Failure example** — an oscillator left running after its sound should stop leaks audio and battery.

## Related
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audioctx|AudioCtx]] — the audio context entity
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audionode|AudioNode]] — the node family
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audioworklet|AudioWorklet]] — advanced audio processing
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audio|Audio]] — the audio concept entity
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/00-index|API REST HTTP Index]] — the cluster this entity belongs to
