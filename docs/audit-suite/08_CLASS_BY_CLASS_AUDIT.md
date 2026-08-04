# 08 — Class-by-Class Audit

**Doc ID:** COSMOS-AUDIT-08 | **Version:** 1.0 | **Generation date:** 2026-08-04
**Coverage:** all 107 Python classes (AST) + 19 TypeScript classes (regex) with dataclass/interface context. High-value classes assessed individually; others listed with docstring-derived purpose. [O] observed; [I] inferred.
**Cross-references:** [07 Function-by-Function](07_FUNCTION_BY_FUNCTION_AUDIT.md) · [17 Concurrency](17_CONCURRENCY_ANALYSIS.md) · [18 Security](18_SECURITY_AUDIT.md)

---

## 1. Registry of Python Classes by Module

### `components/mykb/.wiki-daemon/search_fusion.py` (576 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `SearchHandler` | BaseHTTPRequestHandler | Low |  |

### `components/mykb/server.py` (386 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `Handler` | http.server.SimpleHTTPRequestHandler | Low |  |
| `ReuseAddrTCPServer` | socketserver.TCPServer | Low |  |

### `components/mykb/wiki/server.py` (51 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `Handler` | http.server.SimpleHTTPRequestHandler | Low |  |

### `components/rsis3/rack/rrp_conversation.py` (496 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `RRPConversation333` | (object) | Low | XYZ-Pattern RRP Conversation: X open-ended × Y follow-ups × Z rounds. |

### `components/rsis3/rack/rrp_engine.py` (706 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `AmbiguityVector` | (object) | Low | Four-dimensional ambiguity tracking (0.0 = clear, 1.0 = maximally ambiguous). |
| `TokenBudget` | (object) | Low | Per-round and per-session token budget tracking. |
| `QuestionQualityIndex` | (object) | Low | Rolling average of question quality scores (0.0–1.0). |
| `UserSatisfactionDelta` | (object) | Low | Cumulative satisfaction tracking with trend direction. |
| `TemporalVelocity` | (object) | Low | Round timing and average duration tracking. |
| `TransactionLedgerEntry` | (object) | Low | Single immutable entry in the audit trail. |
| `Checkpoint` | (object) | Low | Fork/rollback support — saves full engine state at a point in time. |
| `RRPEngine` | (object) | Low | Full RRP v2 state machine with telemetry. |

### `components/rsis3/rack/server.py` (29 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `Handler` | http.server.SimpleHTTPRequestHandler | Low |  |

### `components/rsis3/rsis/checkpoint.py` (119 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `CheckpointManager` | (object) | Med | Manages git checkpoints for recovery and rollback. |

### `components/rsis3/rsis/config.py` (388 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L1Config` | (object) | Low | Per-Task Action Loop. |
| `L2Config` | (object) | Low | Per-Session Improvement Loop. |
| `L3Config` | (object) | Low | Cross-Session Evolution Loop. |
| `L4Config` | (object) | Low | Meta-Parameter Optimizer Loop (fast feedback tuning). |
| `L5Config` | (object) | Low | Strategy Evolution Loop (population-based, slow feedback). |
| `L6Config` | (object) | Low | Identity Loop — tunes L3 evolution params (+3 diagonal). |
| `L7Config` | (object) | Low | Meta-Cog Loop — tunes L4 optimizer params (+3 diagonal). |
| `L8Config` | (object) | Low | Meta-Meta Loop — tunes L5 strategy params (+3 diagonal). |
| `L9Config` | (object) | Low | MMM Loop — tunes L6 identity params (+3 diagonal). |
| `ResourceLimits` | (object) | Low | Practical resource bounds to prevent host exhaustion. |
| `MemoryConfig` | (object) | Low | Three-tier memory hierarchy paths. |
| `EvaluatorConfig` | (object) | Low | Immutable evaluator settings. |
| `ToolConfig` | (object) | Low | Sandboxed tool execution for L1 (ported from Agent OS).  `enabled=False` restore |
| `RSISConfig` | (object) | Low |  |

### `components/rsis3/rsis/error_classifier.py` (67 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `ErrorCategory` | Enum | Low | Retry disposition for a failure. |

### `components/rsis3/rsis/evaluator.py` (130 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `EvalResult` | (object) | Low |  |
| `EvaluatorClient` | (object) | Low | Client for the immutable evaluator subprocess. |

### `components/rsis3/rsis/event_bus.py` (89 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `EventBus` | (object) | Low | Topic-based publish/subscribe with replayable history. |

### `components/rsis3/rsis/extrapolation.py` (245 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `TelemetryExtrapolator` | (object) | Low | Analyses historical telemetry to derive insights and predictions. |

### `components/rsis3/rsis/loop_l1.py` (253 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `ToolCall` | (object) | Low | A single tool invocation within an L1 step. |
| `L1Result` | (object) | Low | Outcome of an L1 loop execution. |
| `L1ActionLoop` | (object) | Med | Per-task action loop with checkpointing and telemetry. |

### `components/rsis3/rsis/loop_l2.py` (407 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `ImprovementCandidate` | (object) | Low | A candidate improvement generated by L2. |
| `L2Result` | (object) | Low | Outcome of an L2 improvement session. |
| `L2ImprovementLoop` | (object) | Med | Per-session improvement loop with evaluator gate. |

### `components/rsis3/rsis/loop_l3.py` (256 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L3Result` | (object) | Low | Outcome of an L3 evolution cycle. |
| `L3EvolutionLoop` | (object) | Med | Cross-session evolution loop with full memory consolidation. |

### `components/rsis3/rsis/loop_l4.py` (237 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L4Result` | (object) | Low | Outcome of an L4 optimizer cycle. |
| `OptimizerLoop` | (object) | Low | Tune bounded meta-parameters from outcome telemetry. |

### `components/rsis3/rsis/loop_l5.py` (297 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L5Result` | (object) | Low | Outcome of an L5 evolution cycle. |
| `EvolutionLoop` | (object) | Low | Evolve a persistent population of strategy variants. |

### `components/rsis3/rsis/loop_l6.py` (205 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L6Result` | (object) | Low | Outcome of an L6 identity cycle. |
| `IdentityLoop` | (object) | Low | Tune the L3 plateau timeout from evolution signals. |

### `components/rsis3/rsis/loop_l7.py` (227 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L7Result` | (object) | Low | Outcome of an L7 meta-cog cycle. |
| `MetaCogLoop` | (object) | Low | Meta-tune the L4 optimizer's success deadband. |

### `components/rsis3/rsis/loop_l8.py` (242 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L8Result` | (object) | Low | Outcome of an L8 meta-meta cycle. |
| `MetaMetaLoop` | (object) | Low | Meta-tune the L5 strategy loop's exploration profile. |

### `components/rsis3/rsis/loop_l9.py` (233 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `L9Result` | (object) | Low | Outcome of an L9 MMM cycle. |
| `MMMLoop` | (object) | Low | Meta-tune the L6 identity loop's sensitivity band. |

### `components/rsis3/rsis/memory.py` (346 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `NGramVectorizer` | (object) | Low | Character n-gram based text vectorizer using numpy.  Produces fixed-dimension em |
| `VectorStore` | (object) | Low | Persistent vector store with numpy-based similarity search.  Documents are store |
| `KnowledgeGraph` | (object) | Low | Knowledge graph using NetworkX for insights and relationships.  Nodes represent  |
| `MemoryManager` | (object) | Med | Coordinates the three-tier memory hierarchy. |

### `components/rsis3/rsis/pipeline.py` (319 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `TaskStatus` | str, Enum | Low |  |
| `TaskNode` | (object) | Low | One node of the execution DAG. |
| `DAGWorkerPool` | (object) | Low | Concurrent DAG dispatcher: N worker threads + dynamic routing. |

### `components/rsis3/rsis/practices.py` (234 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `CheckRow` | (object) | Low | One practice check result. |

### `components/rsis3/rsis/priority_pool.py` (567 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `TaskPreemptedError` | Exception | Low | Raised when a RUNNING task yields to a higher-priority task. |
| `TaskCheckpoint` | (object) | Low | Saved progress for a multi-step task (resume point). |
| `PriorityTaskNode` | (object) | Low | One node of a priority-scheduled execution graph. |
| `PriorityWorkerPool` | (object) | Low | Bounded-concurrency executor dispatching ready tasks by priority.  Tasks are reg |
| `AdvancedPriorityWorkerPool` | PriorityWorkerPool | Low | Priority pool with aging ordering + cooperative preemption safeguards.  Extends  |
| `CheckpointRunner` | (object) | Low | Step-pipeline helper with auto-checkpointing + cooperative preemption.  ``run_st |
| `CheckpointWorkerPool` | AdvancedPriorityWorkerPool | Low | Advanced pool that broadcasts aging telemetry as ``worker.priority_tick``.  One  |

### `components/rsis3/rsis/recovery.py` (198 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `RecoveryTestResult` | (object) | Low | Result of a recovery mechanism test. |
| `RecoveryManager` | (object) | Med | Manages the triple recovery system. |
| `FailureInjector` | (object) | Low | Injects controlled failures to test recovery mechanisms.  Used in automated reco |

### `components/rsis3/rsis/resource_monitor.py` (204 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `ResourceSeverity` | Enum | Low |  |
| `ResourceAlert` | (object) | Low | An alert triggered when a resource limit is exceeded. |
| `ResourceEnforcer` | (object) | Low | Active resource monitor and enforcement.  Runs a background thread that periodic |

### `components/rsis3/rsis/scheduler.py` (213 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `Priority` | IntEnum | Low | Scheduling priorities — lower numbers run first. |
| `Task` | (object) | Low | One schedulable unit of work. |
| `AgentScheduler` | (object) | Low | Priority-queue scheduler with depth + cycle guards. |

### `components/rsis3/rsis/shared_memory.py` (143 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `MemoryConflictError` | Exception | Low | Raised when an optimistic update fails due to a version mismatch. |
| `MemoryRegister` | (object) | Low | One versioned register in shared working memory. |
| `SharedMemoryManager` | (object) | Med | Thread-safe working memory with fine-grained locking + OCC. |

### `components/rsis3/rsis/telemetry.py` (390 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `TelemetryEvent` | (object) | Low | A single telemetry event. |
| `TelemetryCollector` | (object) | Med | Collects and flushes workspace telemetry. |
| `WorkspaceMonitor` | (object) | Low | Lightweight workspace resource monitor using psutil when available. |
| `CostLedger` | (object) | Low | Thread-safe, persistent LLM cost ledger with a hard budget cap.  Every LLM call  |

### `components/rsis3/rsis/timeout.py` (105 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `TimeoutError` | Exception | Low | Raised when a loop exceeds its budgeted time. |
| `Budget` | (object) | Low | Track and enforce a budget of iterations or time.  Used by L1, L2, and L3 to enf |

### `components/rsis3/rsis/tools/base.py` (46 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `ToolStatus` | str, Enum | Low |  |
| `ToolResult` | (object) | Low |  |
| `Tool` | abc.ABC | Low | Base class for all tools. |

### `components/rsis3/rsis/tools/hitl.py` (279 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `RiskLevel` | IntEnum | Low | Five-step risk ladder; higher = more operator oversight needed. |
| `ApprovalMode` | (object) | Low | Approval behavior for requests at/above the risk threshold. |
| `HITLSafetyGate` | (object) | Low | Intercepts tool calls, evaluates risk, and routes to the operator. |

### `components/rsis3/rsis/tools/manager.py` (202 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `SecretVault` | (object) | Low | Holds credentials out of band (env vars or OS keyring). |
| `ToolManager` | (object) | Med | Registry + authorization + audit for all tool execution. |

### `components/rsis3/rsis/tools/sandbox.py` (351 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `SandboxResult` | (object) | Low | Result of one sandboxed operation. |
| `Sandbox` | (object) | High |  |

### `components/rsis3/rsis/tools/workspace_tools.py` (115 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `ListFilesTool` | Tool | Low |  |
| `ReadFileTool` | Tool | Low |  |
| `WriteFileTool` | Tool | Low |  |
| `RunCodeTool` | Tool | Low |  |

### `components/rsis3/tests/test_error_classifier.py` (58 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `TestClassifyText` | (object) | Low |  |
| `TestClassifyError` | (object) | Low |  |
| `TestIsRetryable` | (object) | Low |  |

### `components/rsis3/tests/test_loop_l1_retry.py` (102 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `StubTelemetry` | (object) | Low |  |
| `StubCheckpoint` | (object) | Low |  |

### `components/space/docs-server.py` (51 LOC)

| Class | Bases | Risk | Purpose (docstring) |
|-------|-------|------|---------------------|
| `Handler` | http.server.SimpleHTTPRequestHandler | Low |  |

## 2. Key Class Deep-Dives (observed)

#### 2.1 `Sandbox` — HIGH (by design)
- Backends: `auto`, `restricted`, `subprocess`, `docker`; lazy docker client; `SandboxResult` dataclass.
- `_child_limits` uses `preexec_fn` for rlimits + privilege drop (documented: keep minimal, prefer docker when threaded).
- Tier-2 `_run_restricted` executes `exec(bytecode, restricted_globals)` in-process. [O]
#### 2.2 `PriorityPool` — MED
- Effective-priority aging (`priority_aging` per wait-second) + cooperative preemption (`preemption_threshold`); 307-LOC test suite. [O]
- Dense scheduler logic; the giant-killer for the "heaviest module" label.
#### 2.3 `TelemetryCollector` / `WorkspaceMonitor`
- Telemetry + workspace monitoring + cost ledger (budget_cap_usd) — three responsibilities in one module [I, Med].
#### 2.4 Config dataclasses (`rsis/config.py`)
- `RSISConfig`, `L1Config`…`L9Config`, `ResourceLimits` — one dataclass per loop tier, clean. Import-time singleton `CONFIG = load_config()`. [O]
- Tuning state fields are plain `dataclasses.field`; ownership registry lives in module constants.
#### 2.5 `SpaceInstance` / `createSpace` (`space/src/engine/core.ts`)
- Engine as a closure over `Map<string,SessionState>` + typed event handlers — idiomatic TS module pattern. [O]
- Value/query types in `space/src/types/index.ts` (54 interfaces). [O]

## 3. TypeScript Classes & Interfaces Summary

| Class | LOC(file) | File |
|-------|-----------|------|
| `NullProvider` | 19 | `components/space/src/llm/providers/null-provider.ts` |
| `SpecificationGenerator` | 37 | `components/space/src/llm/spec-generator.ts` |
| `ArtifactSynthesizer` | 43 | `components/space/src/llm/artifact-synthesizer.ts` |
| `GeminiProvider` | 49 | `components/space/src/llm/providers/gemini-provider.ts` |
| `QuestionRefiner` | 49 | `components/space/src/llm/question-refiner.ts` |
| `AnthropicProvider` | 50 | `components/space/src/llm/providers/anthropic-provider.ts` |
| `MistralProvider` | 51 | `components/space/src/llm/providers/mistral-provider.ts` |
| `OpenAIProvider` | 52 | `components/space/src/llm/providers/openai-provider.ts` |
| `OllamaProvider` | 56 | `components/space/src/llm/providers/ollama-provider.ts` |
| `QualityScorer` | 65 | `components/space/src/llm/quality-scorer.ts` |
| `TemplateProvider` | 74 | `components/space/src/llm/providers/template-provider.ts` |
| `SnapshotManager` | 80 | `components/space/src/engine/snapshot-manager.ts` |
| `ArtifactTracker` | 130 | `components/space/src/data/artifact-tracker.ts` |
| `GitIntegration` | 204 | `components/space/src/integration/git.ts` |
| `AutoSaveManager` | 222 | `components/space/src/storage/filesystem.ts` |
| `FileSystemStorage` | 222 | `components/space/src/storage/filesystem.ts` |
| `SQLiteStorage` | 270 | `components/space/src/storage/sqlite.ts` |
| `entities` | 305 | `components/space/scripts/run-rsi.ts` |
| `ArtifactExtractor` | 659 | `components/space/src/data/artifact-extractor.ts` |
Interfaces (54) live mostly in `components/space/src/types/index.ts` and `storage/types.ts` — the clean provider seams. [O]

## 4. Design-Quality Findings

- **dataclass usage is idiomatic** (19 files import `dataclasses`); state is mostly immutable value objects. [O]
- **Inheritance is shallow** — classes are concrete with 0–1 bases; composition over inheritance. [O]
- **No ABC/Protocol interfaces for RSIS3 subsystems** (MemoryManager/Telemetry are concrete) — reduces substitutability; mitigated by direct unit tests. [I, Med]
- **Python `enum`** in 6 files (ToolStatus, ResourceSeverity, …) — typed-constant discipline. [O]

---
*End of document 08. Next: [09 Control Flow Analysis](09_CONTROL_FLOW_ANALYSIS.md).*