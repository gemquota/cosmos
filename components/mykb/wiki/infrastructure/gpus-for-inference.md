---
type: "concept"
title: "GPUs for Inference"
description: "Serving model inference on GPUs with batching and quantization"
tags: ["gpu", "inference", "ml", "serving"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---

# GPUs for Inference

## Summary
Serving model inference on GPUs is the practice of turning trained models into reliable, cost-effective production services — with batching, quantization, and kernel fusion as the levers that make it affordable. The core difference from training: training maximizes throughput of many concurrent kernels, while inference serves one request at a time with latency budgets, and the GPU is idle most of the time unless the serving stack actively fills it.

## Details
- The fundamental problem is GPU utilization. A single inference request uses a fraction of a GPU's compute (the forward pass is memory-bound for most models), so serving one request at a time wastes the hardware. The answer is continuous batching (also called dynamic batching): the server accumulates concurrent requests into a batch — in flight, not just queued — and the batch's kernels run together, amortizing the memory reads and filling the compute. Because requests arrive and finish at different times, the batch changes continuously; modern inference engines (vLLM, TensorRT-LLM, SGLang) implement this with paged attention (KV-cache pages allocated on demand, like virtual memory for the cache) and prefix caching (shared prompt prefixes computed once). The throughput gains are an order of magnitude or more versus naive static batching.
- The memory bottleneck is the KV cache: for autoregressive decoding, each active request holds the key-value tensors of all its tokens in GPU memory, and cache size — not weights — is what bounds the number of concurrent requests. This is why the serving metrics are tokens/s (throughput), time-to-first-token (TTFT, the prefill phase — prompt processing), and time-per-output-token (TPOT, the decode phase), and why the operational tradeoffs are between batch size (throughput) and latency (each request in the batch adds work to every decode step).
- Quantization is the capacity lever: running weights (and KV cache) at lower precision — FP16 → INT8 → INT4 — roughly halves memory and doubles throughput per step at a modest accuracy cost. The choices (GPTQ, AWQ, bitsandbytes) trade accuracy and ease against the speedup, and the calibration set used for quantization determines the actual quality loss — a poorly calibrated quantized model is a silent quality regression.
- The deployment options: dedicated GPU inference (best latency, highest cost), shared with training on the same pool (utilization peaks but interference and preemption), and the GPU-less alternatives (CPU inference with quantized models for low traffic, or distilled small models that fit anywhere) — the tradeoff is always cost-per-token versus latency and quality.
- Failure modes: OOM from KV-cache growth (requests killed mid-generation), latency tail from batch interference (one long generation delaying others), and silent accuracy loss from aggressive quantization.
- For mykb: the node anchors the inference-serving cluster — it connects accelerator observability, container tooling, and model serving decisions.

## Related
- [[wiki/infrastructure/storage-systems|Storage Systems]]
- [[wiki/infrastructure/ospf-protocols|OSPF Protocols]]
- [[wiki/syntheses/knowledge-acquisition-workflow|Knowledge Acquisition Workflow]] — how stubs grow into full articles in mykb
- [[wiki/syntheses/mykb-acquisition-curation-and-practices|Acquisition, Curation & Practices]] — the curation loop this stub belongs to
