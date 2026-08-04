---
type: "entity"
title: "AudioContextManager"
description: "AudioContextManager: lifecycle and state management for Web Audio contexts"
tags: ["entity", "api", "ast", "aws", "bash", "bootstrap", "audio"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---

# AudioContextManager

## Summary

AudioContextManager is the bootstrap-cluster entity for managing the Web Audio API's AudioContext: its lifecycle, state, and resource limits. Centralized management keeps audio deterministic and recoverable. It matters because a misused context is the most common cause of silent or broken web audio. Centralized context ownership also makes audio behavior testable and recoverable.

## Details

- **Definition** — An AudioContext manager owns context creation, state transitions, and cleanup so the rest of the app never touches the raw context.
- **Context lifecycle** — Contexts move through suspended, running, and closed states; browsers start them suspended until user interaction.
- **Resume handling** — Managers resume the context from a user gesture, because autoplay policies block sound before interaction.
- **Resource limits** — Browsers cap the number of active contexts; pooling or closing unused contexts prevents quota failures.
- **Latency control** — Latency hints and sample-rate selection trade responsiveness against CPU cost.
- **Worked example** — A game creates one shared context, resumes it on first tap, and routes all sound through a master gain node.
- **Failure modes** — Unresumed contexts, leaked contexts per UI visit, and state changes racing audio rendering cause dead sound.
- **Practical relevance** — A single manager makes audio behavior testable and keeps the rest of the codebase simple.
- **Failure recovery** — Detecting suspended or lost contexts and re-initializing keeps audio alive across interruptions.
- **Test hooks** — A manager exposes state transitions for tests, so audio logic is testable without real hardware.
- **Feature gates** — Muting and volume policies live in the manager, applying globally instead of per-node.
- **Lifecycle events** — Reacting to visibility and power events, such as pausing on tab hide, keeps audio polite and battery-friendly.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/audiocontex|AudioContext]] — the underlying API
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/retroaudio|RetroAudio]] — synthesis using the context
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/canvas-non|Canvas Non]] — media rendering sibling
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/00-index|Bootstrap Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — media pipelines
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/noderenderer|NodeRenderer]] — audio-reactive rendering
