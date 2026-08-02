---
type: "concept"
title: "WebGPU Compute"
description: "General-purpose GPU programming in the browser: shaders, buffers, and dispatch"
tags: ["webgpu", "gpu", "compute", "web", "performance"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API", "https://www.w3.org/TR/webgpu/"]
---
# WebGPU Compute

## Summary
WebGPU exposes modern GPU capabilities to the web, including general compute: pipelines, storage buffers, and compute dispatch. It supersedes WebGL for compute-heavy work like ML inference, physics, image processing, and data transforms, with explicit resource management and validation.

## Details
- **Model** — adapters (hardware), devices (logical GPU), queues (work submission); pipelines bind shaders to layouts.
- **Compute pass** — dispatch workgroups over a grid; storage buffers pass data in and out; barriers order dependencies.
- **WGSL** — the shader language compiles to backend shaders (Metal, D3D12, Vulkan).
- **Practice** — check support and fall back to WebGL/CPU; keep transfers off the hot path; reuse buffers.
- **Worked example** — the mykb corpus's TF-IDF matrix updates run as a WebGPU compute pass, processing large vocabularies off the main thread.
- **Relevance** — RSIS3's on-device analytics can use WebGPU where available, with graceful fallback.
- **Workgroup limits** — maxComputeWorkgroupSizeInvocations caps threads per workgroup; grid sizes must divide work into bounded workgroups, and buffer alignment rules shape struct layouts.

## Related
- [[wiki/web-platforms/will-change|will-change CSS]] — adjacent concept in this wiki
- [[wiki/web-platforms/compositing-triggers|Compositing Triggers]] — adjacent concept in this wiki
- [[wiki/web-platforms/device-pixel-ratio|Device Pixel Ratio]] — adjacent concept in this wiki
- [[wiki/web-platforms/color-spaces|CSS Color Spaces]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — existing coverage
