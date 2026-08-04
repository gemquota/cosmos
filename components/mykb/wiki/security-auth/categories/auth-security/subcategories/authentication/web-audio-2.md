---
type: "entity"
title: "Web Audio"
resource: ""
---
description: "The browser audio API for synthesis, processing, and playback graphs"
tags: ["android", "api", "ast", "auth", "authentication", "aws", "bash", "bootstrap", "bug", "entity", "audio"]
timestamp: "2026-07-19T22:41:41Z"

# Web Audio

## Summary
Web Audio is the browser API for generating, processing, and routing audio through a graph of nodes. It matters because it enables everything from simple beeps to full synthesizers and audio visualizers without plugins. Its node-graph model differs from the HTML audio element and rewards a deliberate, testable structure, especially as graphs grow.

## Details
- **Definition** — the API centers on an AudioContext, with source nodes, processing nodes, and a destination connected into a routing graph.
- **AudioContext** — the context owns the audio clock and output; it starts suspended in some browsers until a user gesture resumes it.
- **Node graph** — sources such as oscillators, buffers, and streams feed filters, gains, and analyzers before reaching the destination.
- **Scheduling** — precise timing is handled by scheduling events on the context clock rather than by timing callbacks manually.
- **Analyzers** — analyser nodes expose frequency and time-domain data, powering visualizers and level meters.
- **Worklets** — AudioWorklet runs custom DSP in a dedicated thread, avoiding main-thread jank for heavy processing.
- **Autoplay policy** — browsers restrict audio before user interaction, so applications must design the gesture flow explicitly.
- **Common failure modes** — leaking contexts and nodes, unconnected graphs that silently produce silence, and timing drift from sloppy scheduling.
- **Worked example** — a game plays a synthesized hit sound by connecting an oscillator through a gain envelope to the destination, then stopping the node after the envelope ends.
- **Practical relevance** — Web Audio turns the browser into an audio platform with predictable, controllable output.

- **Spatial audio** — panner and listener nodes place sounds in 3D space, which games and VR rely on for immersion.
- **Gain control** — master gain nodes provide a single place to mute or duck all output, essential for UI polish.
## Related
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audio|Audio]] — audio concepts
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audionode|AudioNode]] — node model
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/audioworklet|AudioWorklet]] — custom DSP
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — keeping audio smooth
- [[wiki/web-platforms/browser-engines|Browser Engines]] — API support
- [[wiki/testing/performance-testing|Performance Testing]] — audio latency checks
