---
type: "concept"
title: "CSS Animations"
description: "Keyframe-driven property animation with iteration control"
tags: ["css", "animation", "keyframes", "ux"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
---
# CSS Animations

## Summary

CSS animations move elements between keyframes declaratively, running on the compositor when possible. They are the preferred tool for state-driven motion that must survive page reloads and stay in sync with CSS.

## Details
- Mechanism: @keyframes defines named steps; animation properties set duration, easing, delay, iteration, direction, fill mode, and play state. Unlike transitions, animations do not need a state change to start — they run on load or when a class is added, and can pause/resume.
- Concrete example: a skeleton loader pulses opacity 0.4→1 on a pseudo-element; a toast slides in with translateY and fades via opacity, both compositor-only. Fill modes (forwards) hold the end state, preventing the element from snapping back when the animation ends.
- Failure modes: animating layout properties (top, height) causes per-frame layout and jank; infinite animations ignore prefers-reduced-motion unless explicitly gated; forgetting fill-mode makes animated elements jump at the end; and delays with negative values cause first-paint glitches when used carelessly.
- Operational tradeoffs: CSS animations are simpler and more robust than JS rAF loops for fixed motion, but complex choreography (stagger, timeline control) needs the Web Animations API or a library. Keep animation counts low and motion subtle to avoid battery and distraction costs.
- RSIS3/mykb relevance: dashboard pulse indicators and chart transitions use short compositor-friendly CSS animations, and the wiki documents a motion budget so new animations do not degrade interaction-to-next-paint.
- Keyframe specificity: later keyframes override earlier ones and the top-level animation properties; animation shorthand resets all animation-* values, so set the shorthand last or use longhands deliberately.
- Debugging: DevTools animations panel shows timelines, easing curves, and playback controls, which beats guessing at timing bugs.
- Reduced motion: gate decorative animation behind prefers-reduced-motion at the token level (a motion-off class or media query), not per-animation, so new animations inherit the policy.

## Related
- [[wiki/web-platforms/web-animations|Web Animations API]]
- [[wiki/web-platforms/css-transforms|CSS Transforms]]
- [[wiki/web-platforms/css-transitions|CSS Transitions]]
- [[wiki/web-platforms/css-layout|CSS Layout]]
- [[wiki/web-platforms/component-architecture|Component Architecture]]
- [[wiki/web-platforms/web-apis|Web APIs]]
