# 03 — Conceptual Architecture: How the RSI System Works

> **Analytical Lens:** Conceptual — the operational logic and procedural structure
> **Source Artifacts:** procedure_scope, procedure_steps, decision_points, error_handling, step_granularity

---

## 1. Procedural Scope

The RSI system covers **all operational processes including edge case handling**. The improvement loop must handle:

- **Normal improvement** — the happy path
- **Plateaus** — no improvement despite modification attempts
- **Regressions** — modification makes things worse
- **Safety violations** — proposed modification breaks hard constraints
- **Evaluation disagreements** — multiple evaluators produce conflicting scores
- **Resource exhaustion** — API rate limits, token budget exceeded
- **Adversarial inputs** — someone trying to trick the modifier into dangerous changes

This full scope is non-negotiable: a recursive self-improving system that cannot handle its own failure modes is dangerous.

---

## 2. The Core Improvement Cycle

The primary workflow has **8 steps** with moderate complexity and clear waypoints:

```
┌──────────────────────────────────────────────────────────────────┐
│                    THE 8-STEP IMPROVEMENT CYCLE                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. SELECT ──── Choose artifact to improve                       │
│       │         (by expected impact × confidence)                │
│       ▼                                                          │
│  2. ANALYZE ─── Examine current performance                      │
│       │         (baseline scores, weak dimensions)               │
│       ▼                                                          │
│  3. HYPOTHESIZE ── Generate modification hypothesis              │
│       │           (Modifier proposes a change)                   │
│       ▼                                                          │
│  4. SAFETY REVIEW ── StaticGuard checks hard rules               │
│       │             DynamicGuard checks learned patterns          │
│       ▼                                                          │
│  5. APPLY ──── Apply modification to artifact                    │
│       │         (create new version)                             │
│       ▼                                                          │
│  6. EVALUATE ── Score modified artifact                          │
│       │         (Evaluator runs on benchmark)                    │
│       ▼                                                          │
│  7. COMPARE ── Diff against baseline                             │
│       │         (score delta, confidence interval)               │
│       ▼                                                          │
│  8. DECIDE ── Accept / Revert / Iterate                          │
│       │         (convergence check, loop control)                │
│       └──────────────────────────────┐                           │
│                                      │                           │
│              ┌───────────────────────┘                           │
│              ▼                                                   │
│     [If Iterate: return to step 3]                              │
│     [If Accept: return to step 1 with new baseline]             │
│     [If Revert: return to step 1 with flagged failure]          │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Step Details

#### Step 1: Select
- **Input:** List of all artifacts with current scores and improvement history
- **Logic:** Rank by `expected_impact × (1 - evaluation_count / max_evaluations)`. Artifacts that haven't been improved recently and have low scores get priority.
- **Output:** Single artifact to improve

#### Step 2: Analyze
- **Input:** Artifact + its evaluation history
- **Logic:** Identify the dimension with the worst score. Compute improvement velocity (is this artifact improving, stagnating, or regressing over time?).
- **Output:** Analysis summary with target dimension

#### Step 3: Hypothesize
- **Input:** Artifact + analysis summary + modifier prompt template
- **Logic:** LLM generates a modification proposal. The proposal is a structured diff, not free text.
- **Output:** ModificationProposal (pending safety review)

#### Step 4: Safety Review
- **Input:** ModificationProposal
- **Logic:** Two-phase review:
  - **StaticGuard:** Check against hard rules (no API key exfiltration, no latency increase > 10%, no accuracy decrease > 2%)
  - **DynamicGuard:** Check against learned patterns (has this type of modification caused degradation before?)
- **Output:** Approved / Rejected / Needs Modification

#### Step 5: Apply
- **Input:** Approved ModificationProposal
- **Logic:** Apply the diff to the artifact, creating a new version. Link to parent version. Record in History.
- **Output:** New ArtifactVersion

#### Step 6: Evaluate
- **Input:** Modified artifact
- **Logic:** Run the Evaluator against the benchmark. The Evaluator uses its own LLM to score the artifact on multiple dimensions.
- **Output:** EvaluationResult with scores and confidence

#### Step 7: Compare
- **Input:** EvaluationResult + previous EvaluationResult
- **Logic:** Compute score delta. Check if delta is within confidence interval. Determine if improvement is statistically significant.
- **Output:** ComparisonReport (improved / no change / regressed)

#### Step 8: Decide
- **Input:** ComparisonReport + ConvergenceDetector state
- **Logic:**
  - **Accept:** Improvement is significant → promote to best version, update baseline
  - **Revert:** Regression detected → mark as regressed, rollback to previous version
  - **Iterate:** No significant change → try a different modification approach (max 3 iterations per artifact)
  - **Stop:** ConvergenceDetector says further improvement is unlikely → move to next artifact or end loop

---

## 3. Decision Points

### 3.1 Critical Decision Gates

Three gates control the most consequential outcomes:

**Gate 1: Safety Review (Step 4)**
- Go/No-go before applying modification
- If rejected, the modification is permanently blocked (not retried)
- Only the SafetyGuard can override its own decision (via retraining on new safety data)

**Gate 2: Evaluation Comparison (Step 7)**
- Accept/Revert/Iterate after modification
- Accept triggers a new baseline; Revert triggers a rollback
- Iterate allows up to 3 attempts per modification hypothesis

**Gate 3: Convergence Check (Step 8)**
- Continue or stop the entire improvement loop
- Based on improvement velocity, trajectory, and diminishing returns detection
- If stopped, generates a summary report of all improvements made

### 3.2 Moderate Branching

Within each step, there are multiple decision paths with varying counts:
- Step 1 (Select): 3 priority categories × artifact count
- Step 4 (Safety): Approve / Reject / Modify-and-resubmit
- Step 8 (Decide): Accept / Revert / Iterate / Stop

---

## 4. Three-Tier Decision Architecture

The system uses a hybrid decision model that prevents the system from optimizing for the wrong objective:

| Tier | Decision Type | Mechanism | Override |
|------|--------------|-----------|----------|
| **Tier 1** | Safety constraints | Rule-based (hardcoded) | Never (human must edit rules) |
| **Tier 2** | Modification generation | ML-based (LLM proposes changes) | SafetyGuard can block |
| **Tier 3** | Objective definition | Human-in-the-loop | Only humans redefine "better" |

**Why this matters:** If the system could change its own objective function (Tier 3), it could optimize for anything — including things that are not actually better. By keeping Tier 3 human-only, the system is bounded to improving within a human-defined notion of quality.

---

## 5. Error Handling

### 5.1 Graceful Degradation with Bounded Fallback

The error handling strategy is **graceful degradation** — the system continues operating at reduced capability rather than failing completely:

| Failure | Fallback | Capability Loss |
|---------|----------|-----------------|
| Modifier fails to generate valid proposal | Fall back to parameter perturbation | Less creative modifications |
| Evaluator times out | Use cached scores from most recent valid evaluation | Stale evaluation |
| SafetyGuard blocks all proposals | Pause loop, alert human operator | No modifications until cleared |
| LLM API rate limited | Queue proposals, process when budget refreshes | Delayed improvement |
| ConvergenceDetector confused | Use simple threshold heuristic | Less sophisticated stopping |

### 5.2 Automatic Rollback

If post-modification evaluation shows regression beyond a threshold, the artifact **automatically reverts** to its last known good state within 100ms. This is the primary error recovery mechanism.

### 5.3 Dead Letter Queue

Failed modifications that need human review are queued for manual inspection. This applies to:
- Safety violations that are novel (not caught by existing rules)
- Evaluation disagreements between multiple evaluators
- Modifications that pass safety review but cause unexpected side effects

---

## 6. Step Granularity

### 6.1 Moderate Granularity

Each step has sub-processes but they are not deeply nested. The deepest nesting is 3 levels:
- Improve Loop → Safety Review → StaticGuard Check → Rule Evaluation

This moderate depth keeps the system comprehensible and debuggable. Every step can be logged, inspected, and replayed.

### 6.2 Logging at Every Step

Each step produces structured logs:
- Input state
- Decision made
- Output state
- Confidence level
- Timestamp

These logs feed into History and enable post-hoc analysis of improvement trajectories.

---

## 7. Recursive Depth Limiting

The system must prevent infinite recursion. The depth limiting mechanism works at three levels:

### 7.1 Per-Artifact Depth
Maximum 3 modification iterations per hypothesis. If 3 attempts don't improve the artifact, the system moves on.

### 7.2 Per-Loop Depth
Maximum 100 improvement cycles per loop. After 100 cycles, the loop generates a summary and stops.

### 7.3 Self-Modification Depth
The Modifier can improve its own prompt template, but only through a **separate, slower evaluation path** with additional safety checks. Self-modifications require:
- 3x more evaluation cycles to validate
- Human approval for any change that affects the safety review process
- Automatic rollback if self-modification causes degradation in downstream modifications

---

## 8. Convergence Detection

The ConvergenceDetector monitors three signals:

1. **Improvement velocity:** Rate of score improvement per cycle. If velocity drops below a threshold, the system is converging.
2. **Improvement trajectory:** Second derivative. If the trajectory shows deceleration, convergence is imminent.
3. **Diminishing returns:** If the last N modifications produced less than ε improvement, stop.

When convergence is detected, the system:
- Generates a summary report of all improvements
- Archives the final artifact versions
- Updates the EvaluationCriteria with any learned patterns
- Returns control to the human operator

---

## 9. Architectural Summary

The RSI system is an **8-step improvement loop** with:
- 3 critical decision gates (safety, evaluation, convergence)
- 3-tier decision architecture (rules → ML → human)
- Graceful degradation with automatic rollback
- Recursive depth limiting at 3 levels
- Convergence detection via velocity, trajectory, and diminishing returns

The architecture is designed to be **safe by default**: every modification is reviewed, every evaluation is compared, and every loop has a stopping condition. The system improves incrementally, with full rollback capability and human oversight at the objective level.

---

*Source: SPACE artifacts procedure_scope, procedure_steps, decision_points, error_handling, step_granularity*
