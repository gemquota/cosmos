---
status: "growing"
type: "entity"
title: "BufferSourceNode"
description: "BufferSourceNode"
tags: ["entity", "api", "ast", "aws", "bash", "bug"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---


## Buffersourcenode

BufferSourceNode appears in 1 session(s) categorized as API, Cloud, Debugging, Shell. Related topics: api, aws, bash.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Api Services]] › [[wiki/web-platforms/00-index|Api Rest]] › Buffersourcenode

## Overview

BufferSourceNode is a Web Audio API node that plays back audio samples stored in an AudioBuffer. The buffer holds decoded PCM data, and the node streams it into the connected audio graph on demand. It is the standard building block for sample playback, sound effects, and browser-based audio experiments.

## Core Behavior

- `buffer` holds the decoded audio; `loop`, `loopStart`, and `loopEnd` control repetition.
- `playbackRate` and `detune` shift speed and pitch without changing the source data.
- `start(when, offset, duration)` schedules playback precisely; `stop(when)` halts it.
- The `onended` handler fires when playback finishes or is stopped.

## Scheduling and Lifecycle

Web Audio runs on an internal clock, so start times are passed as absolute context times rather than delayed calls. A source node is one-shot by default: after it stops, the same node cannot be restarted, and a fresh node must be created. That makes buffer management a real concern — long samples should be trimmed or chunked rather than held fully in memory.

## In the Audio Graph

The node sits at the source end of the graph: it produces samples that flow through processing nodes such as filters, gains, and analysers before reaching the destination. Because the graph is pull-based, the source only produces samples while connected and running. Browsers resample internally, but a buffer rate that matches the context rate avoids avoidable CPU cost.

## Practical Patterns

- Preload and decode buffers once, then reuse them across new nodes for responsive playback.
- Connect through a GainNode to control volume and avoid clipping.
- For long audio, stream or decode in chunks instead of loading one large buffer.

## Troubleshooting

- No sound usually means the node is not connected to the destination or the context is suspended.
- Clicking or popping at loop boundaries points to misaligned loop points or missing fade edges.
- `onended` not firing suggests the node was garbage-collected while scheduled; keep a reference until playback completes.

## Related Entities

- [[wiki/api-services/categories/api-rest/subcategories/rest-http/aborted|Aborted]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/aegis|Aegis]]
- [[wiki/agent-systems/categories/agents/subcategories/agent-core/agent-active|Agent Active]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ambiguity-projection-2|Ambiguity Projection 2]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ambiguity-system|Ambiguity System]]
- [[wiki/api-services/categories/api-rest/subcategories/rest-http/ambiguity|Ambiguity]]
- Ap
