---
status: "growing"
type: "entity"
title: "BufferAttribute"
description: "BufferAttribute"
tags: ["entity", "ajax", "api", "ast", "aws", "bash"]
timestamp: "2026-07-19T22:41:42Z"
resource: ""
---


## Bufferattribute

BufferAttribute appears in 1 session(s) categorized as API, Cloud, Shell. Related topics: ajax, api, aws, bash.

**Domain:** Web Platforms › [[wiki/web-platforms/00-index|Frontend]] › [[wiki/web-platforms/00-index|Frontend Frameworks]] › Bufferattribute

## Overview

BufferAttribute is a Three.js class that stores geometry data — positions, normals, UVs, colors — in flat typed arrays. Each attribute describes one property of every vertex, and the geometry binds them together by index. Keeping data in typed arrays lets the renderer upload it to GPU vertex buffers with minimal conversion.

## Key Properties

- `array` holds the raw numbers; `itemSize` is the number of components per vertex (3 for positions, 2 for UVs).
- `count` is derived from `array.length / itemSize`.
- Updates are signaled with `needsUpdate = true` so the GPU re-uploads only when data changes.
- Interleaved buffers pack several attributes into one array to reduce uploads and cache misses.

## Typical Usage

Attributes are attached to a `BufferGeometry` with `setAttribute('position', new Float32BufferAttribute(vertices, 3))`; the name must match the shader's attribute location. For skinned or animated meshes, per-frame updates mutate the typed array in place and set `needsUpdate` — allocating a fresh array every frame defeats the purpose of GPU buffers. Memory planning matters: a 1M-vertex mesh with three attributes uses tens of megabytes of client memory before any GPU upload, so streaming and LOD strategies keep scenes bounded.

## GPU Notes

- Attributes are uploaded as vertex buffer objects (VBOs) and consumed by shader attribute locations.
- Static geometry uses a one-time upload; dynamic geometry expects frequent `needsUpdate` flushes.
- Index buffers use 16- or 32-bit indices depending on vertex count.
- Usage hints (`StaticDrawUsage`, `DynamicDrawUsage`) tell the driver how to place buffers.

## Related Concepts

- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — the renderer that consumes geometry buffers
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/webg|WebGL]] — the API that transfers buffers to the GPU
- [[wiki/js-ts-ecosystem/entities/typescript-patterns|TypeScript Patterns]] — typed-array idioms in Three.js code

## Related Entities

- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/ac|Ace 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/aa|Aa]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/insecurerequestwarning-2|Insecurerequestwarning 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/jetbrain|Jetbrains 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/cs|Csv 10]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/dataframe-2|Dataframe 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/invalid-login-2|Invalid Login 2]]
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/langchain-2|Langchain 2]]
