---
type: "concept"
title: "TensorFlow"
description: "Google's ML framework with production serving focus, used across Google's model stack"
tags: ["tensorflow", "deep-learning", "framework"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---
# TensorFlow

## Summary

TensorFlow is Google's ML framework: graph-based execution, Keras as the high-level API, TF Serving for production, and TPU support. Its role is now legacy-adjacent for new research — but large deployed stacks still run on it, and migration decisions need real data.

## Details
- Mechanism: TF 2.x executes eagerly by default with tf.function for graph compilation; Keras layers/models provide the standard authoring API; TF Serving exposes models via gRPC/REST with versioning and batching; TF Lite and TF.js target mobile/edge/web; TPUs are first-class (via XLA) though JAX now gets equal treatment.
- Concrete example: a legacy recommendation model trains in Keras on TPU, serves via TF Serving with a versioned endpoint; a mobile app runs a TF Lite quantized model; a team evaluating modernization benchmarks TF against PyTorch on its actual workload before committing to a migration.
- Failure modes: API churn across TF 1.x/2.x (old codebases resist upgrades); graph/eager inconsistencies (tf.function tracing surprises); serving version and signature drift; and ecosystem momentum — new models and libraries increasingly target PyTorch/JAX first.
- Operational tradeoffs: TF's production story (serving, TPU, Lite) is mature, but its ecosystem advantage has shifted; the pragmatic path is maintaining working TF stacks in place, benchmarking alternatives before migration, and avoiding new greenfield investment without a specific TF advantage.
- RSIS3/mykb relevance: the wiki records the legacy TF stack's serving contract and its benchmark data, so the loop's modernization proposals start from measurement, not fashion.
- Signature hygiene: TF Serving endpoints bind to signatures (inputs/outputs); version and document them, since a changed signature breaks clients silently.
- TPU vs GPU: TPU economics only pay off at scale and with XLA-friendly models; benchmark the actual workload before assuming TPU superiority.

## Related
- [[wiki/ml-frameworks/pytorch|PyTorch]] — The dominant competitor
- [[wiki/ml-frameworks/jax|JAX]] — Google's research successor
- [[wiki/ml-frameworks/google-gemini|Google Gemini]] — Google's model family built on its stack
- [[wiki/ai-ml/transformer-architecture|Transformer Architecture]] — Implemented across frameworks
- [[wiki/ml-frameworks/onnx|ONNX]] — Interop format spanning frameworks
- [[wiki/ai-ml/fine-tuning|Fine-Tuning]] — TF checkpoints still fine-tuned in production
