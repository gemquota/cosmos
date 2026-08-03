---
type: "concept"
title: "Metacognition"
description: "Thinking about and regulating one's own cognitive processes"
tags: ["metacognition", "self-monitoring", "cognition", "reflection"]
timestamp: "2026-07-31T00:00:00Z"
status: "growing"
---

# Metacognition

## Summary
Metacognition is the agent's ability to monitor, evaluate, and regulate its own thinking — knowing when it is uncertain, stuck, or wrong. It matters because it is the substrate for reflection, calibration, and self-improvement. RSIS3's L2/L3 loops are metacognitive machinery.

## Details
- Sub-skills: monitoring confidence, detecting errors, choosing strategies. Monitoring confidence is the moment-to-moment sense of how sure the current answer is; detecting errors is the ability to catch mistakes before they propagate (checking work, noticing contradiction); choosing strategies is the regulatory layer that switches approach when the current one is not working — try a different decomposition, look up a fact, ask for help. In humans these develop late and unevenly; in AI systems they are engineered, which means they can also be absent.
- In agents: self-critique, confidence checks, and reflection passes. Self-critique asks the model to evaluate its own output against criteria; confidence checks compare stated confidence against actual correctness (the measurable face of metacognition); reflection passes replay a session afterward to extract lessons — what worked, what failed, what to do differently. Each is a metacognitive loop, and each is only as good as its honesty: a model that rates its own errors as successes has metacognitive machinery that is actively harmful.
- Poor metacognition produces confident failure; good metacognition catches it. The failure mode is a system that is wrong with high confidence — which is worse than being wrong with uncertainty, because nothing downstream compensates for it. Calibration is the measurable output: an agent with good metacognition says "I don't know" when it doesn't, and its confidence numbers match its hit rates. The entire field of LLM self-correction is, in essence, an attempt to buy metacognition by construction.
- The known limitations: self-evaluation shares the model's blind spots (a model cannot reliably critique errors it would make again), and metacognitive prompts can produce the appearance of reflection without the substance — "I reflected and the answer is the same" is not reflection. The robust design is external verification: metacognition that is checked against ground truth rather than trusted on self-report.
- Open question: measuring metacognitive accuracy in agents — separating genuine monitoring from learned self-report patterns, and quantifying when a system "knows what it knows".
- RSIS3 relevance: L2/L3 loops are metacognition scaled to the system — the L2 loop monitors L1 outcomes and corrects, L3 monitors L2's corrections across sessions, and the whole stack is the system thinking about its own thinking.

## Related
- [[wiki/llm-agents/self-reflection-agents|Self-Reflection Agents]] — metacognition in action
- [[wiki/agent-systems/recursive-self-improvement|Recursive Self-Improvement]] — metacognition scaled to the system
- [[wiki/concepts/calibration|Calibration]] — the measurable output of metacognition
- [[wiki/concepts/cognitive-load|Cognitive Load]] — monitoring resource usage
- [[wiki/concepts/executive-function|Executive Function]] — the controller metacognition reports to
