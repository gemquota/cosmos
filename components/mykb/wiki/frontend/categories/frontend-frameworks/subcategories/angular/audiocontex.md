---
type: "entity"
title: "AudioContext"
description: "AudioContext: the Web Audio API's audio graph, clock, and state"
tags: ["ajax", "android", "angular", "api", "ast", "auth", "authentication", "aws", "bash", "bootstrap", "bug", "css", "documentation", "entity", "audio"]
timestamp: "2026-07-19T22:41:38Z"
resource: ""
---

# AudioContext

## Summary

AudioContext is the angular-cluster entity for the Web Audio API's central object: the graph that routes audio sources through processing nodes to output. It defines the clock, sample rate, and state of all audio in a page. It matters because nearly every web audio feature hangs off this one object. Treating the context as a managed resource prevents the most common audio failures.

## Details

- **Definition** — An AudioContext represents a complete audio processing graph, including the master output and the hardware connection.
- **Audio graph** — Source nodes, processing nodes, and destination nodes connect into a graph that the browser renders continuously.
- **State machine** — Contexts are suspended, running, or closed; browsers start them suspended and require a user gesture to resume.
- **Clock and timing** — The context's sample-accurate clock schedules events precisely, unlike setTimeout-based timing.
- **Sample rate** — The context's sample rate defines the graph's fidelity and CPU cost; resampling happens automatically.
- **Worked example** — An oscillator connects to a gain node and the destination; scheduling starts and stops the tone on the audio clock.
- **Failure modes** — Forgetting to resume, creating many contexts, and leaking nodes that are never disconnected exhaust resources.
- **Practical relevance** — Central managers wrap the context's quirks so application code stays portable across browsers.
- **Node cleanup** — Disconnecting nodes and stopping sources prevents silent background processing and leaks.
- **Context loss** — Hardware changes can close contexts; apps should detect and rebuild the graph.
- **Autoplay policy** — User-gesture resume is a browser requirement; the manager encapsulates it once.
- **Offline contexts** — Rendering to an offline context produces audio without a live device, which is ideal for tests and pre-rendered effects.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/audiocontextmanager|AudioContextManager]] — managing context lifecycle
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/retroaudio|RetroAudio]] — synthesis built on the context
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — cluster sibling page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
