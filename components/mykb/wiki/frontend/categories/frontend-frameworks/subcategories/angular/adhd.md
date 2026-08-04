---
type: "entity"
title: "ADHD"
description: "ADHD: attention-aware interface design and focus management"
tags: ["entity", "acronym", "angular", "api", "ast", "auth", "attention", "ux"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# ADHD

## Summary

ADHD is the frontend entity for attention in interface design: how layouts, motion, and notifications compete for user focus. Attention-aware design reduces distraction and supports users with varying attentional capacity. It matters because attention is the scarcest resource any interface spends. Attention-aware design is a measurable craft: fewer interruptions, fewer errors, better completion.

## Details

- **Definition** — Attention-aware design acknowledges that users have limited, interruptible focus and shapes the interface around that constraint.
- **Distraction budget** — Every notification, animation, and autoplay element spends attention; interfaces should ration it deliberately.
- **Focus management** — Keyboard focus order, skip links, and stable focus after updates keep navigation predictable.
- **Visual noise** — Density, contrast, and motion all contribute to cognitive load; calming defaults help users sustain attention.
- **Task continuity** — Preserving context across navigation, such as scroll position and in-progress state, reduces reorientation cost.
- **Failure modes** — Interrupt-driven designs, autoplaying media, and cluttered dashboards erode focus and increase error rates.
- **Worked example** — A form disables irrelevant controls, groups related fields, and reports progress so users can complete it in one sitting.
- **Practical relevance** — Accessibility guidelines increasingly encode attention support, making it a compliance issue as well as a UX one.
- **Progressive loading** — Revealing content as it is needed keeps initial views focused instead of overwhelming.
- **Reduced motion** — Respecting motion preferences removes distracting animation for users who request calm.
- **Session continuity** — Remembering in-progress work across sessions reduces the cost of returning.
- **Measurement** — Session-completion and error-rate metrics make attention-aware design a testable outcome, and user control over density and motion respects different attentional needs.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/alert|ALERT]] — notifications competing for attention
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/area|AREA]] — layout that guides attention
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — performance keeps attention uninterrupted
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/global-config|Global Config]] — attention preferences
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/automationmanager|AutomationManager]] — automating focus work
