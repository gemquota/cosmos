---
type: "concept"
title: "Machine Learning on the Web"
description: "Running ML models in the browser: ONNX Runtime, TensorFlow.js, WebNN, and WebGPU"
tags: ["ml", "web", "webnn", "webgpu", "inference"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://webmachinelearning.github.io/webnn/", "https://onnxruntime.ai/docs/"]
---
# Machine Learning on the Web

## Summary
The browser is now a serious ML runtime: TensorFlow.js and ONNX Runtime execute models in JS or Wasm, WebNN exposes hardware accelerators, and WebGPU unlocks GPU compute. Inference stays on-device, which means privacy, offline use, and no server cost — at the price of model size and capability.

## Details
- **Runtimes** — ONNX Runtime Web and TensorFlow.js ship converted models; WebGPU backends accelerate them when available.
- **Hardware abstraction** — WebNN maps operations to CPU, GPU, or NPU with fallbacks; support and opsets vary by browser.
- **Model deployment** — quantize (int8) and shrink models; stream weights; cache them in IndexedDB or Cache Storage.
- **Privacy trade-off** — on-device inference keeps data local but limits model size to what devices can load.
- **Worked example** — a text-classifier tags mykb notes on-device with an int8 ONNX model and WebGPU acceleration when present.
- **Relevance** — RSIS3's local-first design makes on-device inference a natural fit for private knowledge processing.

## Related
- [[wiki/js-ts-ecosystem/dynamic-import|Dynamic Import]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/module-preload|modulepreload]] — adjacent concept in this wiki
- [[wiki/js-ts-ecosystem/import-maps|Import Maps]] — adjacent concept in this wiki
- [[wiki/web-platforms/evergreen-browsers|Evergreen Browsers]] — adjacent concept in this wiki
- [[wiki/web-platforms/web-apis|Web APIs]] — existing coverage
- [[wiki/web-platforms/javascript-runtimes|JavaScript Runtimes]] — existing coverage
- [[wiki/web-platforms/browser-engines|Browser Engines]] — existing coverage
