"""Configuration and resource limits for RSIS."""

import json
import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

logger = logging.getLogger(__name__)


# ── Tunable Parameter Registry (+3 diagonal ownership) ────────────────────
# Entries: name -> (min, max, CONFIG attr path, kind)
# Loop k+3 tunes loop k: L4 (Optimizer) owns L1 execution params; L5
# (Evolution) owns L2 params; L6 (Identity) owns L3 params; L7 (Meta-Cog)
# owns L4 params; L8 (Meta-Meta) owns L5 params; L9 (MMM) owns L6 params.
L1_TUNABLES = {
    "l1.max_retries": (1, 8, ("l1", "max_retries"), "int"),
    "l1.max_tool_calls": (5, 25, ("l1", "max_tool_calls_per_step"), "int"),
}

L2_TUNABLES = {
    "l2.max_attempts": (2, 10, ("l2", "max_improvement_attempts"), "int"),
}

L3_TUNABLES = {
    "l3.plateau_timeout_s": (3600, 172800, ("l3", "plateau_timeout_s"), "int"),
}

L4_TUNABLES = {
    "l4.outcome_window": (5, 50, ("l4", "outcome_window"), "int"),
    "l4.min_outcomes": (2, 20, ("l4", "min_outcomes"), "int"),
    "l4.target_success_low": (0.3, 0.7, ("l4", "target_success_low"), "float"),
    "l4.target_success_high": (0.7, 0.95, ("l4", "target_success_high"), "float"),
}

L5_TUNABLES = {
    "l5.mutation_rate": (0.05, 0.6, ("l5", "mutation_rate"), "float"),
    "l5.population_size": (4, 16, ("l5", "population_size"), "int"),
}

L6_TUNABLES = {
    "l6.shrink_below": (0.2, 0.6, ("l6", "shrink_below"), "float"),
    "l6.grow_above": (0.6, 0.95, ("l6", "grow_above"), "float"),
}


# ── Loop Termination Budgets ──────────────────────────────────────────────

@dataclass
class L1Config:
    """Per-Task Action Loop."""
    max_tool_calls_per_step: int = 10
    step_timeout_s: int = 120
    max_retries: int = 3


@dataclass
class L2Config:
    """Per-Session Improvement Loop."""
    max_improvement_attempts: int = 5
    session_timeout_s: int = 1800  # 30 min
    parallel_candidates: int = 0   # 0 = sequential; N = DAG fan-out (multi-agent)
    parallel_retries: int = 0      # per-candidate retry budget (0 = fail fast)
    priority_aging: float = 0.2    # effective-priority boost per wait-second (D2)
    preemption_threshold: float = 5.0  # priority margin to cooperatively preempt (D2)
    shared_memory: bool = True     # per-session SharedMemoryManager for candidates (D2)


@dataclass
class L3Config:
    """Cross-Session Evolution Loop."""
    plateau_sessions: int = 20
    plateau_timeout_s: int = 86400  # 24 h


@dataclass
class L4Config:
    """Meta-Parameter Optimizer Loop (fast feedback tuning)."""
    outcome_window: int = 20
    min_outcomes: int = 5
    target_success_low: float = 0.5
    target_success_high: float = 0.85
    cycle_timeout_s: int = 300  # 5 min
    state_path: str = ".rsis/optimizer_state.json"


@dataclass
class L5Config:
    """Strategy Evolution Loop (population-based, slow feedback)."""
    population_size: int = 8
    elite_fraction: float = 0.5
    mutation_rate: float = 0.2
    seed: int = 42
    generations_per_cycle: int = 1
    cycle_timeout_s: int = 600  # 10 min
    state_path: str = ".rsis/strategies.json"


@dataclass
class L6Config:
    """Identity Loop — tunes L3 evolution params (+3 diagonal)."""
    shrink_below: float = 0.5
    grow_above: float = 0.8
    timeout_step_s: int = 3600  # 1 h
    cycle_timeout_s: int = 600  # 10 min
    state_path: str = ".rsis/identity_state.json"


@dataclass
class L7Config:
    """Meta-Cog Loop — tunes L4 optimizer params (+3 diagonal)."""
    oscillation_window: int = 4
    stall_window: int = 3
    deadband_step: float = 0.05
    cycle_timeout_s: int = 600  # 10 min
    state_path: str = ".rsis/metacog_state.json"


@dataclass
class L8Config:
    """Meta-Meta Loop — tunes L5 strategy params (+3 diagonal)."""
    stagnation_window: int = 3
    volatility_window: int = 4
    fitness_epsilon: float = 0.005
    mutation_step: float = 0.05
    population_step: int = 2
    cycle_timeout_s: int = 600  # 10 min
    state_path: str = ".rsis/metameta_state.json"


@dataclass
class L9Config:
    """MMM Loop — tunes L6 identity params (+3 diagonal)."""
    oscillation_window: int = 4
    stall_window: int = 3
    band_step: float = 0.05
    cycle_timeout_s: int = 600  # 10 min
    state_path: str = ".rsis/mmm_state.json"


# ── Resource Limits ───────────────────────────────────────────────────────

@dataclass
class ResourceLimits:
    """Practical resource bounds to prevent host exhaustion."""
    disk_usage_pct: float = 80.0
    max_memory_rss_mb: int = 4096
    max_cpu_cores: int = max(1, os.cpu_count() or 4) - 1
    evaluator_api_calls_per_min: int = 100


# ── Memory Configuration ─────────────────────────────────────────────────

@dataclass
class MemoryConfig:
    """Three-tier memory hierarchy paths."""
    repo_root: str = "."
    git_branch: str = "rsis-evolution"
    knowledge_graph_path: str = ".rsis/knowledge_graph.json"
    vector_store_path: str = ".rsis/vectors"
    vector_store_dimension: int = 384  # e.g. all-MiniLM-L6-v2


# ── Evaluator Configuration ──────────────────────────────────────────────

@dataclass
class EvaluatorConfig:
    """Immutable evaluator settings."""
    evaluator_path: str = "evaluator/evaluator.py"
    evaluator_prompt_path: str = "evaluator/prompt.txt"
    model: str = "gpt-4o-mini"
    startup_digest_verify: bool = True
    read_only_mount: bool = True


# ── Tool Layer (sandbox + allowlists + HITL) ─────────────────────────────

@dataclass
class ToolConfig:
    """Sandboxed tool execution for L1 (ported from Agent OS).

    `enabled=False` restores the pre-port behaviour (no tools, no sandbox).
    HITL is off by default so unattended runs never prompt; set
    `hitl_enabled` + `approval_mode` for operator-gated runs.
    """
    enabled: bool = True

    # Sandbox
    sandbox_backend: str = "auto"            # auto | restricted | subprocess | docker
    sandbox_timeout: int = 30
    sandbox_allow_network: bool = False
    sandbox_mem_limit: str = "data"          # data | as | off
    sandbox_max_memory_mb: int = 512
    sandbox_docker_image: str = "python:3.11-slim"
    sandbox_docker_mem_limit: str = "256m"
    sandbox_docker_nano_cpus: int = 1_000_000_000

    # HITL approvals
    hitl_enabled: bool = False
    approval_mode: str = "interactive"       # auto | interactive | api | deny
    approval_threshold: str = "high"         # SAFE..CRITICAL (name or 1-5)
    approval_timeout: float = 60.0           # api-mode fail-closed timeout (s)
    auto_approve_tools: list = field(default_factory=list)

    # Secrets + audit
    secret_backend: str = "env"              # env | keyring
    audit_log: str = ".rsis/audit.jsonl"
    hitl_log: str = ".rsis/hitl.jsonl"


# ── Main Configuration ───────────────────────────────────────────────────

@dataclass
class RSISConfig:
    l1: L1Config = field(default_factory=L1Config)
    l2: L2Config = field(default_factory=L2Config)
    l3: L3Config = field(default_factory=L3Config)
    l4: L4Config = field(default_factory=L4Config)
    l5: L5Config = field(default_factory=L5Config)
    l6: L6Config = field(default_factory=L6Config)
    l7: L7Config = field(default_factory=L7Config)
    l8: L8Config = field(default_factory=L8Config)
    l9: L9Config = field(default_factory=L9Config)
    resources: ResourceLimits = field(default_factory=ResourceLimits)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    evaluator: EvaluatorConfig = field(default_factory=EvaluatorConfig)
    tools: ToolConfig = field(default_factory=ToolConfig)

    # Workspace
    workspace_dir: str = "."

    # Telemetry
    telemetry_dir: str = ".rsis/telemetry"
    telemetry_flush_interval_s: int = 5

    # LLM cost accounting (persistent ledger + hard budget cap)
    cost_log: str = ".rsis/costs.jsonl"
    budget_cap_usd: float = 0.0           # 0 = unlimited

    # Logging
    log_level: str = "INFO"
    log_file: Optional[str] = ".rsis/rsis.log"

    # Checkpoint
    checkpoint_before_mutation: bool = True


def _clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, float(value)))


def _apply_tuned_state(cfg: RSISConfig) -> RSISConfig:
    """Override config defaults with persisted L4–L7 state at startup.

    Single injection point: the tuned values reach every loop because they
    read CONFIG at construction time. Corrupt/missing state files fall back
    to defaults.
    """
    cfg_lookup = {}
    for reg in (L1_TUNABLES, L2_TUNABLES, L3_TUNABLES, L4_TUNABLES,
                L5_TUNABLES, L6_TUNABLES):
        for name, (lo, hi, attr_path, kind) in reg.items():
            cfg_lookup[name] = (lo, hi, attr_path, kind)

    def _apply(name, value):
        lo, hi, attr_path, kind = cfg_lookup[name]
        obj = cfg
        for part in attr_path[:-1]:
            obj = getattr(obj, part)
        v = _clamp(value, lo, hi)
        setattr(obj, attr_path[-1], int(round(v)) if kind == "int" else float(v))

    # L4 optimizer state (owns l1.*)
    l4_path = Path(cfg.workspace_dir) / cfg.l4.state_path
    if l4_path.exists():
        try:
            state = json.loads(l4_path.read_text())
            for name, value in state.get("params", {}).items():
                if name in cfg_lookup:
                    _apply(name, value)
        except Exception as e:
            logger.warning("Ignoring L4 state %s: %s", l4_path, e)

    # L5 best strategy (owns l2.*)
    l5_path = Path(cfg.workspace_dir) / cfg.l5.state_path
    if l5_path.exists():
        try:
            data = json.loads(l5_path.read_text())
            population = data.get("population", [])
            if population:
                best = max(population, key=lambda s: s.get("fitness", 0.0))
                attempts = best.get("params", {}).get("l2_attempts", 5)
                _apply("l2.max_attempts", attempts)
        except Exception as e:
            logger.warning("Ignoring L5 state %s: %s", l5_path, e)

    # L6 identity state (owns l3.*)
    l6_path = Path(cfg.workspace_dir) / cfg.l6.state_path
    if l6_path.exists():
        try:
            state = json.loads(l6_path.read_text())
            for name, value in state.get("params", {}).items():
                if name in cfg_lookup:
                    _apply(name, value)
        except Exception as e:
            logger.warning("Ignoring L6 state %s: %s", l6_path, e)

    # L7 meta-cog state (owns l4.*)
    l7_path = Path(cfg.workspace_dir) / cfg.l7.state_path
    if l7_path.exists():
        try:
            state = json.loads(l7_path.read_text())
            for name, value in state.get("params", {}).items():
                if name in cfg_lookup:
                    _apply(name, value)
        except Exception as e:
            logger.warning("Ignoring L7 state %s: %s", l7_path, e)

    # L8 meta-meta state (owns l5.*)
    l8_path = Path(cfg.workspace_dir) / cfg.l8.state_path
    if l8_path.exists():
        try:
            state = json.loads(l8_path.read_text())
            for name, value in state.get("params", {}).items():
                if name in cfg_lookup:
                    _apply(name, value)
        except Exception as e:
            logger.warning("Ignoring L8 state %s: %s", l8_path, e)

    # L9 MMM state (owns l6.*)
    l9_path = Path(cfg.workspace_dir) / cfg.l9.state_path
    if l9_path.exists():
        try:
            state = json.loads(l9_path.read_text())
            for name, value in state.get("params", {}).items():
                if name in cfg_lookup:
                    _apply(name, value)
        except Exception as e:
            logger.warning("Ignoring L9 state %s: %s", l9_path, e)

    return cfg


def load_config() -> RSISConfig:
    """Load configuration, potentially from environment overrides."""
    cfg = RSISConfig()
    # Environment overrides
    if "RSIS_WORKSPACE" in os.environ:
        cfg.workspace_dir = os.environ["RSIS_WORKSPACE"]
    if "RSIS_DISK_USAGE_PCT" in os.environ:
        cfg.resources.disk_usage_pct = float(os.environ["RSIS_DISK_USAGE_PCT"])
    if "RSIS_LOG_LEVEL" in os.environ:
        cfg.log_level = os.environ["RSIS_LOG_LEVEL"]
    if "RSIS_EVALUATOR_MODEL" in os.environ:
        cfg.evaluator.model = os.environ["RSIS_EVALUATOR_MODEL"]
    if "RSIS_BUDGET_CAP_USD" in os.environ:
        cfg.budget_cap_usd = float(os.environ["RSIS_BUDGET_CAP_USD"])
    if "RSIS_COST_LOG" in os.environ:
        cfg.cost_log = os.environ["RSIS_COST_LOG"]
    if "RSIS_TOOLS_ENABLED" in os.environ:
        cfg.tools.enabled = os.environ["RSIS_TOOLS_ENABLED"].lower() in ("1", "true", "yes")
    if "RSIS_SANDBOX_BACKEND" in os.environ:
        cfg.tools.sandbox_backend = os.environ["RSIS_SANDBOX_BACKEND"]
    if "RSIS_SANDBOX_TIMEOUT" in os.environ:
        cfg.tools.sandbox_timeout = int(os.environ["RSIS_SANDBOX_TIMEOUT"])
    if "RSIS_HITL_ENABLED" in os.environ:
        cfg.tools.hitl_enabled = os.environ["RSIS_HITL_ENABLED"].lower() in ("1", "true", "yes")
    if "RSIS_APPROVAL_MODE" in os.environ:
        cfg.tools.approval_mode = os.environ["RSIS_APPROVAL_MODE"]
    if "RSIS_APPROVAL_THRESHOLD" in os.environ:
        cfg.tools.approval_threshold = os.environ["RSIS_APPROVAL_THRESHOLD"]
    if "RSIS_L2_PARALLEL" in os.environ:
        cfg.l2.parallel_candidates = int(os.environ["RSIS_L2_PARALLEL"])
    if "RSIS_L2_PARALLEL_RETRIES" in os.environ:
        cfg.l2.parallel_retries = int(os.environ["RSIS_L2_PARALLEL_RETRIES"])
    if "RSIS_L2_PRIORITY_AGING" in os.environ:
        cfg.l2.priority_aging = float(os.environ["RSIS_L2_PRIORITY_AGING"])
    if "RSIS_L2_PREEMPTION_THRESHOLD" in os.environ:
        cfg.l2.preemption_threshold = float(
            os.environ["RSIS_L2_PREEMPTION_THRESHOLD"])
    if "RSIS_L2_SHARED_MEMORY" in os.environ:
        cfg.l2.shared_memory = os.environ["RSIS_L2_SHARED_MEMORY"].lower() in (
            "1", "true", "yes")
    return _apply_tuned_state(cfg)


# Convenience singleton
CONFIG = load_config()
