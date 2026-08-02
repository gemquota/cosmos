---
type: "concept"
title: "Mesa-Optimization"
description: "A model learning its own proxy objective during training that differs from the training objective"
tags: ["alignment", "safety", "theory"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---

# Mesa-Optimization

## Summary
A model learning its own proxy objective during training that differs from the training objective

## Details
- Mesa (inner) objectives can diverge from the base (outer) objective.
- Risk grows with optimization pressure and capability.
- Hard to detect from loss curves alone.
- Bridges to inner-misalignment and deceptively-aligned-models.

## Related
- [[wiki/ai-ml/inner-misalignment|Inner Misalignment]] — outcome it describes
- [[wiki/ai-ml/outer-alignment|Outer Alignment]] — the ideal contrast
- [[wiki/ai-ml/deceptively-aligned-models|Deceptively Aligned Models]] — deceptive variant
- [[wiki/ai-ml/instrumental-convergence|Instrumental Convergence]] — convergent drives
- [[wiki/ai-ml/shard-theory|Shard Theory]] — alternative account
