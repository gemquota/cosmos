---
type: "concept"
title: "Deadband Control"
description: "Hysteresis thresholds that keep a controller silent inside a target band and reactive outside it"
tags: [deadband, hysteresis, control, thresholds, rsis3]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: []
---

# Deadband Control

## Summary
Deadband control is the practice of defining a band of acceptable values inside which a controller does nothing, and reacting only when the signal leaves the band. The hysteresis prevents chattering — the loop equivalent of a thermostat switching on and off every second. RSIS3 uses deadbands pervasively: L4's `[target_success_low, target_success_high]`, L6's `[shrink_below, grow_above]`, L7's widening/narrowing of the L4 band, and L9's tuning of the L6 band.

## Details
- **Why a band instead of a setpoint**: a single target invites oscillation around it; a band gives the system permission to do nothing.
- **Narrowing**: when the controller stalls (silent while the signal is bad), the meta-tuner narrows the band so it reacts sooner.
- **Widening**: when the controller oscillates (thrashing across the band edge), the meta-tuner widens it so it stops reacting to noise.
- **Minimum gap**: bands never collapse below a floor (e.g. 0.05), so narrowing can't create a degenerate inverted controller.
- Worked example: success-rate 0.7 inside `[0.5, 0.85]` → L4 proposes nothing; success-rate 0.4 → L4 raises retries.

## Related
- [[wiki/concepts/tuning-oscillation|Tuning Oscillation]] — the failure mode deadbands prevent
- [[wiki/concepts/meta-parameter-tuning|Meta-Parameter Tuning]] — the thresholds it adjusts
- [[wiki/concepts/satisficing|Satisficing]] — the decision-theoretic cousin of band acceptance
- [[wiki/concepts/nine-loop-hierarchy|Nine-Loop Hierarchy]] — L7/L9 adjust the bands