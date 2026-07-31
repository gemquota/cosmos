# 08 — Conceptual Flow Analysis: Procedural Deep Structure and Decision Architecture of RSI

> **Analytical Lens:** Conceptual (Tier 2 — Exhaustive)
> **Supersedes:** 03-conceptual-architecture.md (extends with formal process models)
> **Source Artifacts:** All 67 SPACE artifacts + 67 open-ended answers
> **Derivation Depth:** Full artifact cross-referencing

---

## 1. The Procedural Universe

RSI's procedural scope covers **all operational processes including edge case handling**. The improvement loop must handle normal improvement, plateaus, regressions, safety violations, evaluation disagreements, resource exhaustion, and adversarial inputs. This document exhaustively maps every procedural pathway.

### 1.1 Procedure Classification

From the 67 artifacts, the RSI system contains **12 distinct procedures** organized into 3 tiers:

| Tier | Procedures | Count | Criticality |
|------|-----------|:-----:|:-----------:|
| **Core** | Improve, Evaluate, Decide | 3 | Critical |
| **Support** | Select, Analyze, Hypothesize, SafetyReview, Apply, Compare | 6 | High |
| **Meta** | SelfModify, Converge, Recover | 3 | Medium |

---

## 2. Core Procedure: The 8-Step Improvement Cycle (Formal)

### 2.1 Step 1: SELECT

```
PROCEDURE Select:
  INPUT: ArtifactSet[]  — all artifacts with current scores
  OUTPUT: ArtifactId     — single artifact to improve
  
  ALGORITHM:
    1. Filter: Remove artifacts where state ∈ {Deprecated, Archived}
    2. Score: For each artifact a:
       priority(a) = expected_impact(a) × novelty_factor(a)
       where:
         expected_impact(a) = max_dimension_gap(a) × improvement_velocity(a)
         novelty_factor(a) = 1 - (evaluation_count(a) / max_evaluations)
    3. Rank: Sort by priority descending
    4. Select: artifact with highest priority
    
  INVARIANT: Selected artifact must have state ∈ {Evaluated, Regressed}
  TIMEOUT: 100ms (pure computation, no I/O)
  FAILURE: If no artifacts available, terminate loop with "nothing to improve"
```

### 2.2 Step 2: ANALYZE

```
PROCEDURE Analyze:
  INPUT: ArtifactId, History
  OUTPUT: AnalysisReport
  
  ALGORITHM:
    1. Retrieve: artifact.version_chain
    2. Score: For each version v in chain:
       score(v) = Evaluator.score(v)
    3. Identify: weakest_dimension = argmin(score(v).dimensions)
    4. Trend: compute improvement_velocity over last N versions
    5. Classify: trajectory ∈ {accelerating, decelerating, plateaued, regressed}
    6. Generate: AnalysisReport with target_dimension and trajectory
    
  INVARIANT: Analysis must consider minimum 3 historical versions
  TIMEOUT: 30 seconds (may require LLM evaluation)
  FAILURE: If insufficient history, use first-evaluation protocol
```

### 2.3 Step 3: HYPOTHESIZE

```
PROCEDURE Hypothesize:
  INPUT: Artifact, AnalysisReport
  OUTPUT: ModificationProposal
  
  ALGORITHM:
    1. Context: Build prompt with artifact content + analysis + criteria
    2. Generate: LLM proposes modification (with temperature=0.3)
    3. Validate: Check proposal format against schema
    4. Predict: Estimate impact (predicted score delta)
    5. Package: Create ModificationProposal with diff + rationale + prediction
    
  INVARIANT: Proposal must include diff, rationale, and predicted impact
  TIMEOUT: 30 seconds (LLM generation)
  FAILURE: Fall back to parameter perturbation (deterministic baseline)
  RETRY: Up to 3 attempts with varied prompts
```

### 2.4 Step 4: SAFETY REVIEW

```
PROCEDURE SafetyReview:
  INPUT: ModificationProposal
  OUTPUT: SafetyVerdict (Approved | Rejected)
  
  ALGORITHM:
    1. StaticGuard: Apply hardcoded rules:
       - No credential exposure
       - No latency increase > 10%
       - No accuracy decrease > 2%
       - No safety rule modification
       - No benchmark self-modification
    2. DynamicGuard: Apply learned patterns:
       - Check proposal against patterns of past failures
       - Weight by confidence of pattern match
       - Flag if confidence > threshold
    3. Combine: StaticGuard verdict ∨ DynamicGuard verdict
       - If StaticGuard rejects → REJECT (hard block)
       - If DynamicGuard flags with high confidence → REJECT
       - If DynamicGuard flags with low confidence → FLAG for review
       - If no flags → APPROVE
    4. Record: Safety decision in History
    
  INVARIANT: StaticGuard rejection is absolute (no override except human)
  TIMEOUT: 1 second (rule matching, no LLM)
  FAILURE: If SafetyGuard is unavailable, reject all modifications (fail-safe)
```

### 2.5 Step 5: APPLY

```
PROCEDURE Apply:
  INPUT: ModificationProposal (approved), Artifact
  OUTPUT: Artifact (new version)
  
  ALGORITHM:
    1. Snapshot: Save current artifact state (for rollback)
    2. Transform: Apply diff to artifact content
    3. Validate: Check transformed artifact against schema
    4. Version: Increment version number, update version_chain
    5. Record: Create ModificationRecord in History
    6. Update: Artifact.state → Applied
    
  INVARIANT: Rollback target must exist before application
  TIMEOUT: 100ms (local file operations)
  FAILURE: Automatic rollback to snapshot state
  ATOMICITY: Application is atomic — succeeds completely or rolls back
```

### 2.6 Step 6: EVALUATE (Post-Modification)

```
PROCEDURE EvaluatePostModification:
  INPUT: Artifact (new version), EvaluationCriteria
  OUTPUT: EvaluationResult
  
  ALGORITHM:
    1. Score: Evaluator scores artifact across all dimensions
    2. Compare: Compute delta against baseline scores
    3. Confidence: Compute confidence interval for delta
    4. Record: Store EvaluationResult in History
    5. Update: Artifact.state → ReEvaluated
    
  INVARIANT: Evaluation must use same criteria as baseline evaluation
  TIMEOUT: 30 seconds (LLM evaluation)
  FAILURE: Use cached scores, flag for re-evaluation
```

### 2.7 Step 7: COMPARE

```
PROCEDURE Compare:
  INPUT: EvaluationResult (post-modification), BaselineScores
  OUTPUT: ComparisonDecision (Accept | Revert | Iterate)
  
  ALGORITHM:
    1. Compute: score_delta = post_score - baseline_score
    2. Test: Is score_delta > convergence_threshold?
    3. Decision:
       IF score_delta > 0 AND confidence > 0.8:
         → ACCEPT (improvement confirmed)
       ELIF score_delta < -regression_threshold:
         → REVERT (regression detected)
       ELIF iteration_count < max_iterations:
         → ITERATE (try another modification)
       ELSE:
         → ACCEPT (best attempt, even if marginal)
         
  INVARIANT: Revert triggers automatic rollback within 100ms
  TIMEOUT: 100ms (pure computation)
  FAILURE: Default to ITERATE
```

### 2.8 Step 8: DECIDE (Loop Control)

```
PROCEDURE Decide:
  INPUT: ComparisonDecision, ConvergenceDetector output
  OUTPUT: LoopAction (Continue | Converge | Terminate)
  
  ALGORITHM:
    1. If ComparisonDecision = REVERT:
       - Rollback artifact
       - Record failure in History
       - Continue to next artifact (Step 1)
    2. If ComparisonDecision = ACCEPT:
       - Update baseline scores
       - Check convergence:
         a. Query ConvergenceDetector
         b. If converged → TERMINATE loop
         c. If not converged → CONTINUE loop
    3. If ComparisonDecision = ITERATE:
       - Stay on same artifact
       - Return to Step 3 (Hypothesize)
    4. If max_cycles reached:
       - Generate summary report
       - TERMINATE loop
       
  INVARIANT: Convergence check must occur after every ACCEPT
  TIMEOUT: 100ms
  FAILURE: Default to CONTINUE
```

---

## 3. Support Procedures

### 3.1 Self-Modification Procedure

```
PROCEDURE SelfModify:
  TRIGGER: Modifier improves its own prompt template
  SPECIAL CONSTRAINTS:
    - Depth limit: 3 levels maximum
    - Validation: 3x more evaluation cycles required
    - Human approval: Required for safety-impacting changes
    - Rollback: Automatic if self-modification causes downstream degradation
    
  ALGORITHM:
    1. Detect: Modifier identifies self-improvement opportunity
    2. Depth check: If self_modification_depth ≥ 3 → HALT
    3. Propose: Generate self-modification proposal
    4. Safety review: Enhanced scrutiny (StaticGuard + DynamicGuard + Human)
    5. Apply: Create new Modifier version
    6. Validate: Run 3x evaluation cycles on benchmark
    7. If degradation detected → rollback Modifier to previous version
    8. If improvement confirmed → accept new Modifier version
    
  INVARIANT: Self-modification never bypasses safety review
  CRITICAL RISK: Modifier improving itself could create undetectable degradation
```

### 3.2 Convergence Detection Procedure

```
PROCEDURE DetectConvergence:
  INPUT: History (last N records)
  OUTPUT: ConvergenceVerdict (Continue | Converge | Escalate)
  
  ALGORITHM:
    1. Velocity: v = (score[t] - score[t-w]) / w
       where w = window_size (default: 10)
    2. Trajectory: a = v[t] - v[t-1] (acceleration)
    3. Diminishing: d = count(recent_improvements < epsilon) / window_size
    4. Decision:
       IF v < velocity_threshold AND |a| < acceleration_threshold:
         → CONVERGE
       ELIF d > diminishing_threshold:
         → CONVERGE
       ELIF v < 0 AND cycles > min_cycles:
         → ESCALATE (human review)
       ELSE:
         → CONTINUE
         
  INVARIANT: Minimum 10 cycles before convergence can be declared
  TIMEOUT: 100ms (computation only)
  FAILURE: Default to CONTINUE (never prematurely converge)
```

### 3.3 Recovery Procedures

#### Automatic Rollback

```
PROCEDURE AutomaticRollback:
  TRIGGER: Post-modification evaluation shows regression > threshold
  ALGORITHM:
    1. Retrieve: Last known good version from version_chain
    2. Restore: Artifact.content = last_good_version.content
    3. Update: Artifact.version_chain.mark_current(regressed_version, 'regressed')
    4. Record: Rollback event in History
    5. Update: Artifact.state → Regressed → Evaluated
  TIMEOUT: 100ms
  GUARANTEE: Rollback always succeeds (version_chain is append-only)
```

#### API Failure Recovery

```
PROCEDURE APIFailureRecovery:
  TRIGGER: LLM API call fails (timeout, rate limit, error)
  ALGORITHM:
    1. Log: Failure details in History
    2. Backoff: Exponential backoff (1s, 2s, 4s, 8s, 16s max)
    3. Retry: Up to 5 attempts
    4. Fallback: If all retries fail:
       - For Modifier: Use parameter perturbation (deterministic)
       - For Evaluator: Use cached scores
       - For SafetyGuard: Reject all modifications (fail-safe)
    5. Queue: If persistent failure, queue for human review
  TIMEOUT: 64 seconds total (sum of backoff delays)
```

#### Evaluation Disagreement Resolution

```
PROCEDURE ResolveEvaluationDisagreement:
  TRIGGER: Multiple Evaluator instances produce conflicting scores
  ALGORITHM:
    1. Collect: All evaluation results for the artifact
    2. Compare: Compute inter-evaluator variance
    3. If variance < agreement_threshold:
       - Average the scores
       - Use averaged result
    4. If variance ≥ agreement_threshold:
       - Flag for human review
       - Use conservative estimate (lower score)
       - Block modification until resolved
  TIMEOUT: 100ms (comparison only)
```

---

## 4. Decision Architecture — Three-Tier Model

### 4.1 Tier 1: Safety Constraints (Rule-Based)

**Mechanism:** Hardcoded rules that cannot be modified by the system.

| Rule ID | Rule | Trigger | Action |
|---------|------|---------|--------|
| SR-001 | No credential exposure | Any modification | Block |
| SR-002 | Max 10% latency increase | Post-evaluation | Revert |
| SR-003 | Max 2% accuracy decrease | Post-evaluation | Revert |
| SR-004 | No safety rule modification | Self-modification attempt | Block |
| SR-005 | No benchmark self-modification | Any modification | Block |
| SR-006 | Max 3 self-modification depth | Self-modification attempt | Halt |
| SR-007 | Minimum 10 cycles for convergence | Convergence check | Continue |
| SR-008 | Rollback within 100ms | Regression detected | Rollback |

### 4.2 Tier 2: Modification Generation (ML-Based)

**Mechanism:** LLM generates modification proposals based on context.

| Decision | Input | Mechanism | Override |
|----------|-------|-----------|----------|
| What to modify | Artifact + Analysis | LLM generation | Fallback to perturbation |
| How to modify | Context + Criteria | LLM generation | Fallback to perturbation |
| Expected impact | Proposed change | LLM prediction | Post-hoc validation |
| Modification type | Artifact type | Rule-based | Never |

### 4.3 Tier 3: Objective Definition (Human-in-the-Loop)

**Mechanism:** Human operator defines and adjusts evaluation criteria.

| Decision | Authority | Frequency | Process |
|----------|-----------|-----------|---------|
| What "better" means | Human only | Per session | ADR → Review → Lock |
| Dimension weights | Human only | Per session | Config → Validate → Lock |
| Safety thresholds | Human only | Per session | Config → Review → Lock |
| Benchmark selection | Human only | Per session | Config → Validate → Lock |

### 4.4 Decision Precedence Diagram

```
┌─────────────────────────────────────────────────────┐
│              DECISION PRECEDENCE                     │
│                                                     │
│  Tier 3: Human defines objectives                   │
│    ↓ (immutable within session)                     │
│  Tier 2: LLM generates modifications               │
│    ↓ (constrained by Tier 1 and Tier 3)            │
│  Tier 1: Safety rules block dangerous actions       │
│    ↓ (absolute, no system override)                 │
│  EXECUTION: Modification applied or blocked         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 5. Error Handling Matrix

| Error Category | Detection | Response | Recovery | Escalation |
|---------------|-----------|----------|----------|------------|
| **LLM API timeout** | HTTP timeout | Retry with backoff | Cached scores | After 5 retries |
| **LLM API rate limit** | 429 status | Queue, wait for budget | Delayed processing | After 64s |
| **Invalid proposal format** | Schema validation | Retry generation | Parameter perturbation | After 3 retries |
| **Safety violation (novel)** | DynamicGuard flag | Block proposal | Human review | Immediate |
| **Safety violation (known)** | StaticGuard rule | Block proposal | Automatic | Log only |
| **Evaluation disagreement** | Variance threshold | Conservative estimate | Human review | If variance > threshold |
| **Convergence failure** | 100 cycles without convergence | Terminate loop | Summary report | Human review |
| **Storage failure** | Write error | Retry | In-memory fallback | Immediate |
| **Rollback failure** | Restore error | Halt loop | Manual intervention | Immediate |
| **Configuration drift** | Immutability check | Reject change | Session restart | Log only |

---

## 6. Flow Complexity Analysis

### 6.1 Cyclomatic Complexity

The improvement cycle has cyclomatic complexity of **12** (12 decision points in the main flow). This is moderate — within the maintainable range for a critical system.

### 6.2 Maximum Nesting Depth

The deepest nesting is **4 levels**:
```
ImproveLoop → SafetyReview → StaticGuard → RuleEvaluation → ConditionCheck
```

### 6.3 Total Procedure Count

| Category | Count | Total LOC (estimated) |
|----------|:-----:|:---------------------:|
| Core procedures | 3 | ~200 |
| Support procedures | 6 | ~300 |
| Meta procedures | 3 | ~150 |
| Error handling | 10 | ~200 |
| **Total** | **22** | **~850** |

---

## 7. Conceptual Flow Summary

The RSI procedural architecture consists of:

- **8-step core improvement cycle** with formal step definitions
- **3 meta-procedures** (self-modification, convergence detection, recovery)
- **3-tier decision architecture** (safety rules → ML generation → human objectives)
- **10 error handling pathways** with defined detection, response, recovery, and escalation
- **Cyclomatic complexity of 12** — moderate, maintainable
- **Maximum nesting depth of 4** — comprehensible
- **Fail-safe defaults** throughout — the system defaults to safe behavior

The procedural design embodies the recursive improvement philosophy: every procedure is itself improvable, but within safety constraints that prevent the procedures from degrading their own safety mechanisms.

---

*Derived from: All 67 SPACE artifacts, all 67 open-ended answers, cross-referenced with 03-conceptual-architecture.md*
*SPACE — Superb Prompt Automatic Creation Engine v2.1.0*
