---
type: "entity"
title: "AABB"
description: "AABB: axis-aligned bounding boxes for collision, picking, and spatial queries"
tags: ["acronym", "ajax", "android", "angular", "api", "ast", "bash", "entity", "geometry"]
timestamp: "2026-07-19T22:41:40Z"
resource: ""
---

# AABB

## Summary

AABB (axis-aligned bounding box) is the frontend entity for the rectangular bounds used to approximate shapes in collision detection, picking, and spatial queries. AABBs trade precision for speed and simplicity. They matter because they are the workhorse of interactive geometry. AABBs are the cost model that makes interactive geometry affordable on modest hardware.

## Details

- **Definition** — An axis-aligned bounding box is the smallest rectangle, aligned to the coordinate axes, that contains a shape.
- **Construction** — AABB bounds are computed from min and max coordinates across all points of the object.
- **Intersection tests** — Two AABBs overlap if their extents overlap on every axis; the test is a few comparisons, making it very fast.
- **Broad phase** — Collision systems first filter with AABBs, then run precise tests only on candidates that overlap.
- **Spatial queries** — AABBs accelerate picking, view culling, and neighbor searches by cheaply excluding most objects.
- **Worked example** — A canvas app tests pointer hits against each element's AABB first, then checks exact pixel shapes for the winners.
- **Failure modes** — Tight bounds that rotate with objects require recomputation; stale bounds cause missed or phantom hits.
- **Practical relevance** — Every interactive editor, from node canvases to games, leans on AABB tests for responsiveness.
- **Updating bounds** — Moving objects require bounds recomputation; caching them per object amortizes the cost.
- **Hierarchies** — Bounding volume hierarchies partition space so queries skip entire subtrees.
- **Precision** — Bounds that are too tight miss overlaps; expanding by a margin trades precision for reliability.
- **Precision tuning** — A small expansion margin absorbs floating-point error, trading a tiny false-positive rate for reliability.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/area|AREA]] — layout regions as rectangles
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/above-2|ABOVE]] — stacking order of bounds
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/canvaspool-2|CanvasPool]] — canvas rendering of bounds
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/build|BUILD]] — cluster sibling page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/00-index|Angular Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — rendering bounds
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/physicsconfig|PhysicsConfig]] — collision geometry
