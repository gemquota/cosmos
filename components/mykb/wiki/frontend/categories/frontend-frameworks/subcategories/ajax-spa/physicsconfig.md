---
type: "entity"
title: "PhysicsConfig"
description: "PhysicsConfig: configuring timestep, forces, and collision behavior in physics engines"
tags: ["entity", "ajax", "android", "api", "ast", "auth", "physics"]
timestamp: "2026-07-19T22:41:41Z"
resource: ""
---

# PhysicsConfig

## Summary

PhysicsConfig is the ajax-spa entity for physics-engine configuration: the settings that define a simulation's behavior, from timestep to gravity to collision tolerances. Configuration is where simulation stability and realism are won or lost. It matters because physics engines are only as good as their tuning. Configuration-first simulation design keeps physics tunable without code changes.

## Details

- **Definition** — Physics configuration bundles the numeric and behavioral settings that control a physics simulation.
- **Timestep** — A fixed timestep keeps simulations stable and deterministic; variable steps introduce jitter and tunneling.
- **Forces** — Gravity, friction, and restitution values shape how objects move and bounce.
- **Collision settings** — Tolerances, margins, and contact limits trade accuracy for stability and speed.
- **Determinism** — Identical configuration and inputs should reproduce identical results; float ordering breaks determinism. For replays and multiplayer, determinism is a requirement; the config is part of what must be pinned to preserve it.
- **Worked example** — A game sets a 60 hertz fixed timestep, tunes gravity to feel snappy, and adjusts collision margins to stop jitter.
- **Failure modes** — Instability explosions, objects tunneling through walls, and non-deterministic replays are the classic failures.
- **Practical relevance** — Configuration as data, not code, lets designers and agents tune simulations without recompiling.
- **Validation** — Config values should be validated for range; invalid timesteps and negative masses produce nonsense.
- **Perf tradeoffs** — Collision margins and substep counts trade accuracy for stability and frame budget.
- **Serialization** — Storing physics config with scenes lets designers tweak and ship without developer involvement.
- **Tuning workflow** — Starting from engine defaults, changing one parameter at a time, and recording results yields stable tuning instead of guesswork.

## Related

- [[wiki/frontend/categories/frontend-frameworks/subcategories/angular/aabb-2|AABB]] — collision primitives in simulation
- [[wiki/frontend/categories/frontend-frameworks/subcategories/bootstrap/webglrenderer-2|WebGLRenderer]] — rendering simulated scenes
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/request-2|Request]] — synchronizing simulation state
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/00-index|AJAX SPA Index]] — cluster index page
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/interaction-locks|Interaction Locks]] — locking during simulation
- [[wiki/frontend/categories/frontend-frameworks/subcategories/ajax-spa/canvastexture|CanvasTexture]] — textures in simulation
