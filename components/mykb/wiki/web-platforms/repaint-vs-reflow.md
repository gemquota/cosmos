---
type: "concept"
title: "Repaint vs Reflow"
description: "Distinguishing pixel repainting from layout reflow work"
tags: ["performance", "rendering", "layout", "browsers"]
timestamp: "2026-08-02T00:00:00Z"
status: "stub"
---
# Repaint vs Reflow

## Summary
Distinguishing pixel repainting from layout reflow work. A stub in the mykb wiki that frames the concept and the questions to expand into a full article.

## Details
- Reflow recomputes geometry; repaint redraws pixels
- Batch DOM writes to minimize reflow cascades
- Open question — how do engines coalesce style and layout work?

## Related
- [[wiki/web-platforms/error-monitoring-web|Error Monitoring for the Web]] — related coverage in the same cluster
- [[wiki/web-platforms/frame-budget|Frame Budget]] — related coverage in the same cluster
- [[wiki/web-platforms/input-latency|Input Latency]] — related coverage in the same cluster
- [[wiki/web-platforms/interaction-to-next-paint|Interaction to Next Paint]] — related coverage in the same cluster
- [[wiki/web-platforms/web-performance-optimization|Web Performance Optimization]] — related coverage in the same cluster
- [[wiki/web-platforms/progressive-web-apps|Progressive Web Apps]] — related coverage in the same cluster
- [[wiki/web-platforms/browser-engines|Browser Engines]] — related coverage in the same cluster
