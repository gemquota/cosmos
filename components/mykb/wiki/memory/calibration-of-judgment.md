---
type: "concept"
title: "Calibration of Judgment"
description: "The match between subjective confidence and actual accuracy"
tags: ["calibration", "confidence", "judgment"]
timestamp: "2026-08-02T00:00:00Z"
status: "growing"
source: ["https://en.wikipedia.org/wiki/Calibration_(statistics)", "https://dictionary.apa.org/calibration"]
---

# Calibration of Judgment

## Summary

Calibration of Judgment — The match between subjective confidence and actual accuracy.

## Details

- Calibration is the correspondence between stated confidence and objective accuracy: perfectly calibrated judgments are right 80% of the time when confidence is 80%. People are systematically overconfident on hard questions and underconfident on easy ones, with large individual and domain differences.
- Measurement: collect many confidence-outcome pairs, bin by confidence, and compare to accuracy — the calibration curve. Calibration is trainable with feedback, especially when forecasts are frequent and outcomes are quickly knowable.
- Worked example: a developer who answers '90% sure' correctly only 65% of the time is overconfident; a calibration log with outcomes, reviewed monthly, typically narrows the gap.
- Calibration matters wherever confidence informs decisions: medical judgment, financial forecasts, code review, and self-assessment. Overconfidence causes both missed risk and wasted caution.
- mykb relevance: calibration-training and confidence-ratings entries give the wiki a practical toolkit for judgment hygiene.

## Related

- [[wiki/meta-learning/calibration-training|Calibration Training]] — the remedy
- [[wiki/meta-learning/confidence-ratings|Confidence Ratings]] — the measure
- [[wiki/concepts/calibration-curves|Calibration Curves]] — the diagnostic plot
- [[wiki/concepts/overconfidence-mitigation|Overconfidence Mitigation]] — targeted techniques
- [[wiki/concepts/calibration|Calibration]] — existing wiki article
- [[wiki/syntheses/evidence-and-provenance|Evidence and Provenance: Open Threads]] — existing wiki article
