# COSMOS E1 — L5 → L2 Coupling Experiment

**Status:** Baseline investigation complete; no production source changes made.

## Scope

Determine whether L5's evolved strategy population changes L2 candidate generation, selection, or downstream execution.

## Environment

- Repository root: `/home/daytona/codebase`
- RSIS package: `/home/daytona/codebase/components/rsis3`
- Default `CONFIG.workspace_dir`: `.` relative to the process working directory
- Isolated experiment workspace used for execution: `/tmp/rsis_verify_all`
- Existing user changes were present before this experiment and were not modified.

## Source-Level Coupling Trace

### L5

`components/rsis3/rsis/loop_l5.py`:

1. Loads `.rsis/strategies.json`
2. Seeds a population from L3 strategies or defaults
3. Scores variants using outcome statistics
4. Mutates/recombines variants
5. Sends the next generation to the evaluator
6. Writes the resulting population to `.rsis/strategies.json`

### L2

`components/rsis3/rsis/loop_l2.py`:

1. Reads the goal and prior evaluator results
2. Checks `RSIS_L2_LLM_GENERATOR`
3. If no generator is configured, resolves a target from the goal or `StubDetector`
4. Generates deterministic scaffold code
5. Evaluates the candidate
6. Applies only to missing files; existing target files are skipped

No normal L2 candidate-generation path reads `.rsis/strategies.json`, selects an L5 variant, or applies the variant's `focus`, `l2_attempts`, or `budget_factor` to candidate generation.

## Direct Execution Evidence

### L5 execution

The `strategies` command was executed through the production CLI:

```text
python3 -m rsis strategies
```

Observed result:

```text
Strategy evolution complete
Generation: 1
Population: 8 (elites kept: 4, variants generated: 4)
Avg fitness: 0.091
Best: strategy-budget-1 (fitness=0.091)
```

The command created a persistent state file containing:

- `generation: 1`
- `population: 8`
- `history: 1 entry`

A later isolated re-run also created `.rsis/strategies.json` with 8 variants.

### L2 execution

The `run` command was executed through the production CLI with:

```text
python3 -m rsis run --goal "Implement Watcher in rsis/watcher.py - replace stub with production code"
```

Observed result:

- L2 generated one deterministic candidate
- The candidate generator was deterministic, not LLM-backed
- The evaluator returned PASS
- A new `rsis/watcher.py` file was created
- L1 matched no tool and completed

The generated module was a scaffold with `self.ready = True` and an empty `run()` method body.

## Controlled Existing-File Test

An isolated temporary workspace contained an existing Python file. L2 was invoked with a goal targeting that existing file.

Observed result:

- L2 did not overwrite the existing file
- `_apply_improvement()` logged/skipped existing targets
- No improvement was applied

This confirms that deterministic L2 is limited to new-file creation.

## Result Matrix

| Question | Result | Evidence Type |
|---|---|---|
| Does L5 execute? | YES | Direct production CLI execution |
| Does L5 persist a population? | YES | `.rsis/strategies.json` observed after execution |
| Does standard L2 read L5 state? | NO evidence; source path does not read it | Source inspection |
| Does L5 alter L2 candidate text? | NOT DEMONSTRATED | No L2 strategy-consumption path |
| Does L5 alter L2 attempt budget? | NOT DEMONSTRATED | L2 uses `CONFIG.l2.max_improvement_attempts`; no population selection |
| Does L5 alter L2 selection? | NO evidence | L2 selects first evaluator PASS |
| Does L5 alter downstream L1 behavior? | NOT DEMONSTRATED | No observed strategy-to-L1 handoff |
| Is L5's fitness meaningful? | UNVERIFIED | One generation and sparse outcome data |

## Conclusion

**L5 genuinely executes and persists strategy state. However, E1 finds no demonstrated operational coupling from the L5 population into the standard L2 production path.**

The strongest supported classification is:

> L5 is an operational population-evolution component whose output is persisted, but its influence on L2 is currently unverified and appears absent from the ordinary candidate-generation path.

This is not evidence that L5's algorithm itself is broken. It establishes only that execution and persistence do not prove downstream causal influence.

## Limits

This experiment did not run a long controlled series or modify production code to add instrumentation. It therefore does not establish whether an alternate integration path, external orchestration, or future configuration causes L5 state to influence L2.

---

# COSMOS E2 — L4/L6 → Downstream Performance

**Status:** Controlled parameter-sensitivity probe complete; no production source changes made.

## Objective

Determine whether parameter values changed by L4/L6 alter downstream L1/L2 outcomes, separating observable execution effects from useful performance improvement.

## Method

Used isolated temporary workspaces and the existing production classes. Varied the relevant runtime parameters while holding the goal and evaluator behavior constant.

### L2 parameter variation

Tested `CONFIG.l2.max_improvement_attempts` at 2, 5, and 10 using a controlled evaluator that always rejected candidates.

| Attempts configured | Candidate attempts observed | Result |
|---:|---:|---|
| 2 | 2 | No application; session failed after rejection |
| 5 | 5 | No application; session failed after rejection |
| 10 | 10 | No application; session failed after rejection |

**Observed effect:** The parameter changes the number of candidate/evaluation attempts before exhaustion. It does not improve candidate quality, selection, or application by itself.

### L1 parameter variation

An initial probe used the sandbox `run_code` tool with the task text as code. That probe failed because the existing keyword router supplied `task` as code and the sandbox reported `NameError: name 'task' is not defined`; it did not exercise the intended callable test. This result is retained as an execution observation, not as a parameter-performance result.

No valid causal L1 performance comparison was therefore established in this pass.

## Result

- **L4/L6 parameter mutation is executable and can change runtime configuration.**
- **E2 did not demonstrate downstream improvement.**
- L2 attempt-budget sensitivity was demonstrated, but increased attempts only permit more rejected candidates under the controlled rejection condition.
- No claim about improved task-level success, quality, or efficiency is justified from this sample.

## Causal Status

| Link | Result |
|---|---|
| L4/L6 state → runtime configuration | Demonstrated by source path and isolated state execution |
| Runtime configuration → changed control behavior | Partially demonstrated for L2 attempt exhaustion |
| Changed control behavior → better candidate quality | Not demonstrated |
| Changed control behavior → better task outcome | Not demonstrated |
| L4/L6 mutation → causal downstream improvement | Unverified |

## Limitations

- Small controlled samples
- No representative task corpus
- No baseline-vs-intervention statistical comparison
- No valid L1 callable benchmark completed
- No long-running cycle comparison
- Existing user changes were preserved; no production source was changed

---

# COSMOS E3 — L3/MyKB → Future Behavior

**Status:** Controlled memory-feedback probe complete; no production source changes made.

## Objective

Determine whether L3/MyKB output changes subsequent goal selection, strategy selection, candidate generation, or execution rather than merely accumulating records.

## Controlled Observations

### L3 output with empty history

In an isolated workspace with an empty MyKB, `L3EvolutionLoop.run_cycle()` completed successfully and wrote a synthesis note even though it reported zero insights. It generated the routine strategy entry `budget=5`.

This proves that L3 can write durable MyKB output, but it does not prove that the output is useful or that it changes later behavior.

### MyKB goal resolution

`_resolve_goal("from-mykb", gateway)` queried the gateway and returned a goal derived from the selected synthesis title and path:

```text
Use regression tests — follow the durable guidance in synthesis wiki/syntheses/s1.md
```

This is direct evidence that MyKB can influence the **goal string** when the `from-mykb` mode is explicitly selected.

### Candidate generation after MyKB-derived goal

A direct goal matching the deterministic target grammar produced five deterministic candidates under a rejecting evaluator. A prose MyKB-derived goal with no actionable target produced zero candidates.

| Goal source | Candidates | Generator | Applied |
|---|---:|---|---|
| Direct actionable goal | 5 | deterministic | No, evaluator rejected |
| MyKB-derived prose goal | 0 | none | No |

The difference is consistent with goal parsing, not evidence that MyKB guidance improved behavior.

## Result Matrix

| Question | Result | Evidence Type |
|---|---|---|
| Can L3 write MyKB output? | YES | Direct isolated execution |
| Can MyKB change selected goal text? | YES, when explicitly requested | Direct `_resolve_goal` execution |
| Does MyKB change candidate generation quality? | NOT DEMONSTRATED | Controlled comparison produced no quality measure |
| Does MyKB change strategy selection? | NO evidence | No observed strategy-consumption path |
| Does MyKB improve downstream execution? | UNVERIFIED | No behavioral success comparison |
| Does L3 memory consolidation influence future behavior automatically? | NOT DEMONSTRATED | Goal source must explicitly be `from-mykb` |

## Conclusion

**E3 confirms a real data path from MyKB to goal text, but not a causal improvement path.** MyKB is operational as durable memory and can supply future goals when selected. The experiment found no evidence that merely writing a synthesis automatically changes subsequent candidate quality, strategy selection, or task performance.

The strongest supported statement is:

> L3/MyKB provides operational persistence and optional goal-context retrieval. Its usefulness as a learning mechanism remains unproven.

## Limits

- No representative task corpus
- No before/after behavioral metric
- No comparison of identical goals with and without retrieved context
- No long-running memory accumulation experiment
- No production source changes

---

# COSMOS E4 — Evaluator Discrimination

**Status:** Controlled evaluator corpus executed; no production source changes made.

## Method

Nine candidates were submitted directly to `components/rsis3/evaluator/evaluator.py` as isolated subprocess inputs. The corpus included no-op, comment-only, equivalent rewrite, scaffold, deliberately worse implementation, semantically incorrect implementation, genuine improvement-shaped code, unsafe code, and syntactically invalid code.

## Results

| Candidate | Decision | Key result |
|---|---|---|
| No-op | PASS | Efficiency 0.85; rationale notes no-op |
| Comment-only | PASS | All scores 1.0; no semantic signal |
| Equivalent rewrite | PASS | All scores 1.0 |
| Trivial scaffold | PASS | All scores 1.0 |
| Deliberately worse implementation | PASS | All scores 1.0 |
| Semantically incorrect implementation | PASS | All scores 1.0 |
| Genuine improvement-shaped code | PASS | All scores 1.0 |
| Unsafe code | FAIL | Safety 0.0; `os.system()` detected |
| Syntax-invalid code | FAIL | Correctness 0.0; compile failure |

Five repeated benign evaluator subprocess runs completed successfully, each returning PASS, with observed wall times of approximately 22.5–25.9 ms in this environment. This is a process-launch timing observation, not a quality or scalability benchmark.

## Interpretation

The deterministic evaluator discriminates syntax violations and several statically recognizable unsafe operations. It does **not** establish semantic correctness, task completion, novelty, regression safety against the repository, or measurable target improvement for raw code candidates. Style/efficiency heuristics may lower scores or add notes but do not reject candidates.

Therefore the strongest supported conclusion is:

> The evaluator is a validity/safety gate with lightweight heuristics, not a demonstrated behavioral improvement objective. It can accept candidates that are syntactically valid but semantically wrong, irrelevant, no-op, or deliberately worse.

This demonstrates an evaluator limitation, not evidence that every accepted candidate causes harm.

---

# COSMOS E5 — Recursive Stability Probe

**Status:** Initial repeatability probe complete; no production source changes made.

## Method

The same benign candidate was evaluated five consecutive times through the production evaluator subprocess. This is a repeatability probe, not a full L1–L9 stability experiment: it does not mutate loop state or run repeated daemon cycles.

## Results

| Run | Exit code | Decision | Wall time |
|---:|---:|---|---:|
| 1 | 0 | PASS | 23.89 ms |
| 2 | 0 | PASS | 25.89 ms |
| 3 | 0 | PASS | 23.59 ms |
| 4 | 0 | PASS | 23.50 ms |
| 5 | 0 | PASS | 22.54 ms |

Decision consistency was 5/5 (100%) for this fixed input. Mean wall time was approximately 23.88 ms; observed range was 22.54–25.89 ms. No parameter trajectory, feedback trajectory, convergence, oscillation, or degradation can be inferred from this probe because the recursive loops were not repeatedly coupled.

## Conclusion

E5 establishes deterministic evaluator repeatability for one fixed candidate under one environment. It does **not** establish recursive stability of the +3 hierarchy. The requested dynamical-system questions remain untested.

## Limits

- One candidate and five repetitions only.
- No L1–L9 batch execution.
- No state mutation or cross-cycle feedback measurement.
- No variance study across tasks, processes, or environments.
- No production source changes.

## Combined E4/E5 Status

E4 confirms that the evaluator rejects tested syntax/safety violations but accepts all tested semantically wrong, no-op, irrelevant, and worse candidates. E5 confirms fixed-input repeatability only. Neither experiment demonstrates that COSMOS selects or applies behaviorally superior changes, nor that recursive adaptation converges or improves task-level performance.

## Limits

- Corpus size is nine candidates and was hand-constructed.
- No repository execution, regression suite, baseline comparison, or target-specific oracle was supplied to the evaluator.
- The genuine-improvement label describes intended candidate semantics; it was not independently validated against a task specification.
- Results apply to the deterministic path with no evaluator LLM credentials configured.
