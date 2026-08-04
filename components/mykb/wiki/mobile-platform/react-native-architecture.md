---
type: "entity"
title: "React Native Architecture"
description: "How React Native works: JS thread, native modules, bridge, and the New Architecture"
tags: ["react-native", "architecture", "mobile", "javascript", "bridges"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://reactnative.dev/docs/new-architecture-intro", "https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here"]
---
# React Native Architecture

## Summary
React Native runs JavaScript on a separate thread and renders native views via a bridge (legacy) or JSI (new). The New Architecture — Fabric renderer, TurboModules, and Codegen — replaces the async bridge with synchronous, typed interop. Understanding the threading model explains performance and platform behavior.

## Details
- **Threads** — JS thread runs the app; native UI thread renders; native modules thread handles work; a dedicated shadow thread computes layout (Yoga).
- **Bridge (legacy)** — batched JSON serialization between JS and native; async and expensive, causing jank under load.
- **New Architecture** — JSI allows direct native method calls; Fabric supports synchronous updates and concurrent rendering; TurboModules lazily load modules.
- **Codegen** — generates typed interfaces from specs, removing manual glue.
- **Worked example** — a mykb reader scrolling long logs benefits from Fabric's synchronous layout and memoized components.
- **Relevance** — RN's threading model informs how RSIS3's mobile clients should structure expensive work.

## Related
- [[wiki/web-platforms/device-detection|Device Detection]] — adjacent concept in this wiki
- [[wiki/web-platforms/user-agent-parsing|User-Agent Parsing]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/microtasks|Microtasks]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/task-queues|Task Queues]] — adjacent concept in this wiki
- [[wiki/frontend-frameworks/react-native-vs-flutter|React Native vs Flutter]] — existing coverage
- [[wiki/frontend-frameworks/cross-platform-frameworks|Cross-Platform Frameworks]] — existing coverage
- [[wiki/frontend-frameworks/hot-reload|Hot Reload]] — existing coverage
