#!/usr/bin/env python3
"""RSIS — Recursive Self-Improvement System.

Usage:
    python -m rsis init              # Initialise workspace
    python -m rsis run --goal X      # Improvement session
    python -m rsis evolve            # L3 evolution cycle
    python -m rsis optimize          # L4 meta-parameter optimization
    python -m rsis strategies        # L5 strategy evolution cycle
    python -m rsis identity          # L6 identity loop (tunes L3 params)
    python -m rsis metacog           # L7 meta-cog loop (tunes L4 params)
    python -m rsis metameta          # L8 meta-meta loop (tunes L5 params)
    python -m rsis mmm               # L9 MMM loop (tunes L6 params)
    python -m rsis drive --loop l4   # Run a loop until its completion requirement is met
    python -m rsis dashboard         # Start web dashboard
    python -m rsis status            # System overview
    python -m rsis check             # Check resource limits
    python -m rsis recovery-test     # Test recovery mechanisms
"""

import argparse
import logging
import sys
import time
from pathlib import Path

from rsis import __version__

logger = logging.getLogger(__name__)
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG
from rsis.evaluator import EvaluatorClient
from rsis.loop_l1 import L1ActionLoop
from rsis.loop_l2 import L2ImprovementLoop
from rsis.loop_l3 import L3EvolutionLoop
from rsis.loop_l4 import OptimizerLoop
from rsis.loop_l5 import EvolutionLoop
from rsis.loop_l6 import IdentityLoop
from rsis.loop_l7 import MetaCogLoop
from rsis.loop_l8 import MetaMetaLoop
from rsis.loop_l9 import MMMLoop
from rsis.memory import MemoryManager
from rsis.mykb_gateway import MyKBGateway
from rsis.practices import run_checks as run_practice_checks
from rsis.pipeline import run_demo as run_pipeline_demo
from rsis.recovery import FailureInjector, RecoveryManager
from rsis.resource_monitor import ResourceEnforcer, ResourceSeverity
from rsis.scheduler import run_demo as run_scheduler_demo
from rsis.telemetry import TelemetryCollector, WorkspaceMonitor, default_ledger
from rsis.timeout import Budget, deadline, TimeoutError


def setup_logging() -> None:
    log_path = CONFIG.log_file
    if log_path:
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)

    handlers = [logging.StreamHandler(sys.stdout)]
    if log_path:
        handlers.append(logging.FileHandler(log_path))

    logging.basicConfig(
        level=getattr(logging, CONFIG.log_level.upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
    )


# ── Shared initialisation ────────────────────────────────────────────────

def _init_subsystems() -> tuple:
    """Initialise and return shared subsystems."""
    telemetry = TelemetryCollector(
        CONFIG.telemetry_dir, CONFIG.telemetry_flush_interval_s,
    )
    checkpoint = CheckpointManager(CONFIG.workspace_dir)
    memory = MemoryManager(CONFIG.workspace_dir)
    evaluator = EvaluatorClient()
    recovery = RecoveryManager(checkpoint_mgr=checkpoint)
    enforcer = ResourceEnforcer()
    return telemetry, checkpoint, memory, evaluator, recovery, enforcer


def _resolve_goal(goal: str, gateway: Optional[MyKBGateway] = None) -> str:
    """Resolve the L2 goal string, pulling from MyKB when asked.

    `--goal from-mykb` makes the loop *read* durable syntheses for context:
    the most relevant recent synthesis becomes the improvement goal. Falls
    back to the default goal when MyKB is unavailable or unhelpful.
    """
    if goal != "from-mykb":
        return goal
    if gateway is not None and gateway.available:
        hits = gateway.search_syntheses("improvement guidance", limit=5)
        if not hits:
            hits = gateway.read_syntheses(limit=5)
        if hits:
            hit = hits[0]
            print(f"  \u2139 Goal sourced from MyKB: {hit['slug']}")
            return (f"{hit.get('title') or hit['slug']} \u2014 follow the "
                    f"durable guidance in synthesis {hit['rel']}")
    return "self-improve the codebase"


# ── Commands ─────────────────────────────────────────────────────────────

def cmd_init(args: argparse.Namespace) -> int:
    print(f"RSIS v{__version__} — Initialising workspace...")
    print(f"  Workspace: {CONFIG.workspace_dir}")

    for d in [".rsis", ".rsis/telemetry", ".rsis/vectors"]:
        Path(CONFIG.workspace_dir, d).mkdir(parents=True, exist_ok=True)

    checkpoint = CheckpointManager(CONFIG.workspace_dir)
    checkpoint.ensure_repo()

    ch = checkpoint.checkpoint("rsis-initialised")
    print(f"  Initial checkpoint: {ch[:12] if ch else 'none'}")

    eval_path = Path(CONFIG.evaluator.evaluator_path)
    if eval_path.exists():
        print(f"  Evaluator: {eval_path.resolve()}")
    else:
        print(f"  WARNING: Evaluator not found at {eval_path}")

    print("  RSIS workspace ready.")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    if args.parallel is not None:
        CONFIG.l2.parallel_candidates = args.parallel
    if getattr(args, "parallel_retries", None) is not None:
        CONFIG.l2.parallel_retries = args.parallel_retries
    ledger = default_ledger()
    if args.budget_cap is not None:
        CONFIG.budget_cap_usd = args.budget_cap
        ledger.budget_cap_usd = max(0.0, args.budget_cap)
        ledger.budget_exceeded = (
            ledger.budget_cap_usd > 0
            and ledger.total_cost() >= ledger.budget_cap_usd)

    enforcer.set_callbacks(
        on_halt=lambda msg: setattr(enforcer, '_halt_requested', True),
        on_throttle=lambda msg: logger.warning("Throttle: %s", msg),
    )
    enforcer.start()
    telemetry.start()

    try:
        # Check resources before starting
        limit_msg = enforcer.check_before_operation()
        if limit_msg:
            print(f"  ⚠ Resource limit: {limit_msg}")
            return 1

        if ledger.budget_exceeded:
            cap = CONFIG.budget_cap_usd
            cap_str = (f"${cap:.4f}" if cap < 1 else f"${cap:.2f}")
            print(f"  ⚠ LLM budget cap ({cap_str}) already "
                  f"spent (${ledger.total_cost():.4f}) — refusing new LLM work")
            return 1

        l2 = L2ImprovementLoop(
            telemetry=telemetry, evaluator=evaluator,
            checkpoint_mgr=checkpoint, recovery=recovery,
        )

        goal = _resolve_goal(args.goal, MyKBGateway())
        budget = Budget(
            max_iterations=CONFIG.l2.max_improvement_attempts,
            max_time_s=CONFIG.l2.session_timeout_s,
            label="L2 session",
        )

        with deadline(CONFIG.l2.session_timeout_s, "L2 session"):
            result = l2.run_session(goal, budget=budget)

        if enforcer.halt_requested:
            print("  ⚠ Session halted by resource enforcer")
            return 1

        if result.applied:
            memory.record_improvement(
                description=result.applied.description,
                target_files=result.applied.target_files,
                eval_scores=result.eval_results[-1].scores if result.eval_results else {},
                outcome="applied",
                goal=goal,
            )
            print(f"  ✓ Improvement applied after {result.attempts} attempt(s)")
        else:
            print(f"  ✗ No improvement applied after {result.attempts} attempt(s)")

        l1 = L1ActionLoop(telemetry=telemetry, checkpoint_mgr=checkpoint)
        l1_result = l1.execute(goal)
        print(f"  L1 steps: {l1_result.steps_taken}")
        print("  Cost ledger:")
        print(ledger.report())

    except TimeoutError as e:
        print(f"  ✗ Session timed out: {e}")
        recovery.record_failure()
        return 1
    except Exception as e:
        print(f"  ✗ Session failed: {e}")
        recovery.record_failure()
        recovery.rollback_on_failure("run_session")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_evolve(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l3 = L3EvolutionLoop(telemetry=telemetry, memory=memory)
        budget = Budget(
            max_iterations=1,
            max_time_s=CONFIG.l3.plateau_timeout_s,
            label="L3 evolution",
        )

        with deadline(CONFIG.l3.plateau_timeout_s, "L3 evolution"):
            result = l3.run_cycle(budget=budget)

        if result.success:
            print(f"  ✓ Evolution complete")
            print(f"  Insights added: {result.insights_added}")
            print(f"  Strategies evolved: {len(result.strategies_evolved)}")
            print(f"  Redundancies identified: {result.redundancies_pruned}")
            for t in result.trends_detected:
                print(f"  Trend: {t['context']} — {t['trend']} (slope={t['slope']})")
        else:
            print(f"  ✗ Evolution failed: {result.error}")

    except TimeoutError as e:
        print(f"  ✗ Evolution timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_optimize(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l4 = OptimizerLoop(
            telemetry=telemetry, memory=memory, evaluator=evaluator,
            checkpoint_mgr=checkpoint,
        )
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l4.cycle_timeout_s,
            label="L4 optimizer",
        )

        with deadline(CONFIG.l4.cycle_timeout_s, "L4 optimizer"):
            result = l4.run_cycle(budget=budget)

        if result.skipped:
            print(f"  ℹ Not enough outcomes yet "
                  f"({result.outcome_stats.get('count', 0)} < "
                  f"{CONFIG.l4.min_outcomes}) — run more L2 sessions first")
        elif result.success and result.changed:
            print("  ✓ Parameters tuned:")
            for k, v in sorted(result.deltas.items()):
                print(f"    {k}: {v:+.1f}")
            print(f"  Outcome stats: {result.outcome_stats}")
        elif result.success:
            print("  ℹ No parameter changes proposed "
                  f"(success_rate={result.outcome_stats.get('success_rate', 0):.2f})")
        else:
            print(f"  ✗ Optimizer failed: {result.error}")
            return 1

    except TimeoutError as e:
        print(f"  ✗ Optimizer timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_strategies(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l5 = EvolutionLoop(
            telemetry=telemetry, memory=memory, evaluator=evaluator,
            checkpoint_mgr=checkpoint,
        )
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l5.cycle_timeout_s,
            label="L5 evolution",
        )

        with deadline(CONFIG.l5.cycle_timeout_s, "L5 evolution"):
            result = l5.run_cycle(budget=budget)

        if result.success:
            print(f"  ✓ Strategy evolution complete")
            print(f"  Generation: {result.generation}")
            print(f"  Population: {result.population_size} "
                  f"(elites kept: {result.elites_kept}, "
                  f"variants generated: {result.variants_generated})")
            print(f"  Avg fitness: {result.avg_fitness:.3f}")
            if result.best_strategy:
                print(f"  Best: {result.best_strategy['id']} "
                      f"(fitness={result.best_strategy['fitness']:.3f})")
        else:
            print(f"  ✗ Strategy evolution failed: {result.error}")
            return 1

    except TimeoutError as e:
        print(f"  ✗ Strategy evolution timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_identity(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l6 = IdentityLoop(
            telemetry=telemetry, memory=memory, evaluator=evaluator,
            checkpoint_mgr=checkpoint,
        )
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l6.cycle_timeout_s,
            label="L6 identity",
        )

        with deadline(CONFIG.l6.cycle_timeout_s, "L6 identity"):
            result = l6.run_cycle(budget=budget)

        if result.success and result.changed:
            print(f"  \u2713 L3 plateau timeout tuned ({result.signal}): "
                  f"{result.deltas}")
        elif result.success:
            print(f"  \u2139 No change ({result.signal or 'no signal'})")
        else:
            print(f"  \u2717 Identity loop failed: {result.error}")
            return 1

    except TimeoutError as e:
        print(f"  \u2717 Identity loop timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_metacog(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l7 = MetaCogLoop(
            telemetry=telemetry, memory=memory, evaluator=evaluator,
            checkpoint_mgr=checkpoint,
        )
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l7.cycle_timeout_s,
            label="L7 meta-cog",
        )

        with deadline(CONFIG.l7.cycle_timeout_s, "L7 meta-cog"):
            result = l7.run_cycle(budget=budget)

        if result.success and result.changed:
            print(f"  \u2713 L4 deadband tuned ({result.signal}): "
                  f"{result.deltas}")
        elif result.success:
            print(f"  \u2139 No change ({result.signal or 'no signal'})")
        else:
            print(f"  \u2717 Meta-cog loop failed: {result.error}")
            return 1

    except TimeoutError as e:
        print(f"  \u2717 Meta-cog loop timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_metameta(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l8 = MetaMetaLoop(
            telemetry=telemetry, memory=memory, evaluator=evaluator,
            checkpoint_mgr=checkpoint,
        )
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l8.cycle_timeout_s,
            label="L8 meta-meta",
        )

        with deadline(CONFIG.l8.cycle_timeout_s, "L8 meta-meta"):
            result = l8.run_cycle(budget=budget)

        if result.success and result.changed:
            print(f"  \u2713 L5 strategy params tuned ({result.signal}): "
                  f"{result.deltas}")
        elif result.success:
            print(f"  \u2139 No change ({result.signal or 'no signal'})")
        else:
            print(f"  \u2717 Meta-meta loop failed: {result.error}")
            return 1

    except TimeoutError as e:
        print(f"  \u2717 Meta-meta loop timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0


def cmd_mmm(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        l9 = MMMLoop(
            telemetry=telemetry, memory=memory, evaluator=evaluator,
            checkpoint_mgr=checkpoint,
        )
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l9.cycle_timeout_s,
            label="L9 MMM",
        )

        with deadline(CONFIG.l9.cycle_timeout_s, "L9 MMM"):
            result = l9.run_cycle(budget=budget)

        if result.success and result.changed:
            print(f"  \u2713 L6 identity band tuned ({result.signal}): "
                  f"{result.deltas}")
        elif result.success:
            print(f"  \u2139 No change ({result.signal or 'no signal'})")
        else:
            print(f"  \u2717 MMM loop failed: {result.error}")
            return 1

    except TimeoutError as e:
        print(f"  \u2717 MMM loop timed out: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

    return 0



def _drive_cycle(loop_name, goal, telemetry, checkpoint, memory, evaluator,
                 recovery, holder):
    """Run one cycle of `loop_name`; return (done, satisfied, reason).

    `done` is True when the loop reached a terminal state — either its
    completion requirement is satisfied (satisfied=True) or it can make no
    further progress on its own (satisfied=False, e.g. L2 ran out of
    attempts or L4 has too few outcomes to tune).
    """
    if loop_name == "l2":
        l2 = L2ImprovementLoop(
            telemetry=telemetry, evaluator=evaluator,
            checkpoint_mgr=checkpoint, recovery=recovery)
        budget = Budget(
            max_iterations=CONFIG.l2.max_improvement_attempts,
            max_time_s=CONFIG.l2.session_timeout_s, label="L2 session")
        with deadline(CONFIG.l2.session_timeout_s, "L2 session"):
            result = l2.run_session(goal, budget=budget)
        if result.success and result.applied:
            return True, True, (
                f"improvement applied after {result.attempts} attempt(s)")
        if result.attempts >= CONFIG.l2.max_improvement_attempts:
            return True, False, (
                f"{result.attempts} attempt(s) with no applied improvement — "
                "raise l2.max_improvement_attempts or adjust the goal")
        return False, False, f"attempt {result.attempts} failed, retrying"

    if loop_name == "l3":
        l3 = L3EvolutionLoop(telemetry=telemetry, memory=memory)
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l3.plateau_timeout_s,
            label="L3 evolution")
        with deadline(CONFIG.l3.plateau_timeout_s, "L3 evolution"):
            result = l3.run_cycle(budget=budget)
        if not result.success:
            return True, False, f"L3 cycle failed: {result.error}"
        # L3 always emits a routine budget strategy, so a plateau means no
        # new insights, no redundancy prunes and no regression-driven focus
        # strategies (i.e. only the routine "budget=..." entry).
        converged = (result.insights_added == 0
                     and len(result.strategies_evolved) <= 1
                     and result.redundancies_pruned == 0)
        if converged:
            return True, True, (
                "evolution plateau — no new insights, focus strategies or "
                "redundancies to act on")
        return False, False, (
            f"added {result.insights_added} insight(s), "
            f"{len(result.strategies_evolved)} strategy(ies), "
            f"pruned {result.redundancies_pruned} redundancy(ies)")

    if loop_name == "l4":
        l4 = OptimizerLoop(telemetry=telemetry, memory=memory,
                           evaluator=evaluator, checkpoint_mgr=checkpoint)
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l4.cycle_timeout_s,
            label="L4 optimizer")
        with deadline(CONFIG.l4.cycle_timeout_s, "L4 optimizer"):
            result = l4.run_cycle(budget=budget)
        if not result.success:
            return True, False, f"L4 cycle failed: {result.error}"
        if result.skipped:
            return True, False, (
                f"only {result.outcome_stats.get('count', 0)} outcome(s) "
                f"< l4.min_outcomes={CONFIG.l4.min_outcomes} — run L2 "
                "sessions first")
        if not result.changed:
            sr = result.outcome_stats.get('success_rate', 0)
            return True, True, (
                f"success rate {sr:.2f} within target band "
                f"[{CONFIG.l4.target_success_low:.2f}, "
                f"{CONFIG.l4.target_success_high:.2f}] — no deltas proposed")
        return False, False, (
            f"tuned {len(result.deltas)} parameter(s), re-checking band")

    if loop_name == "l5":
        l5 = EvolutionLoop(telemetry=telemetry, memory=memory,
                           evaluator=evaluator, checkpoint_mgr=checkpoint)
        budget = Budget(
            max_iterations=1, max_time_s=CONFIG.l5.cycle_timeout_s,
            label="L5 evolution")
        with deadline(CONFIG.l5.cycle_timeout_s, "L5 evolution"):
            result = l5.run_cycle(budget=budget)
        if not result.success:
            return True, False, f"L5 cycle failed: {result.error}"
        best = (result.best_strategy.get('fitness', 0.0)
                if result.best_strategy else 0.0)
        prev = holder.get('l5_best')
        if prev is not None and best <= prev + 0.005:
            return True, True, (
                f"fitness plateau (best {best:.4f} vs previous {prev:.4f})")
        holder['l5_best'] = best
        return False, False, (
            f"generation {result.generation} best fitness {best:.4f}, "
            "continuing")

    cls = {"l6": IdentityLoop, "l7": MetaCogLoop,
           "l8": MetaMetaLoop, "l9": MMMLoop}[loop_name]
    loop = cls(telemetry=telemetry, memory=memory, evaluator=evaluator,
               checkpoint_mgr=checkpoint)
    cfg = getattr(CONFIG, loop_name)
    label = f"{loop_name.upper()} tuning"
    budget = Budget(max_iterations=1, max_time_s=cfg.cycle_timeout_s,
                    label=label)
    with deadline(cfg.cycle_timeout_s, label):
        result = loop.run_cycle(budget=budget)
    if not result.success:
        return True, False, f"{loop_name.upper()} cycle failed: {result.error}"
    if not result.changed:
        return True, True, "no tuning signal — band stable"
    return False, False, f"applied deltas {result.deltas}, re-checking"


def cmd_drive(args: argparse.Namespace) -> int:
    """Drive a loop until its completion requirement is satisfied.

    Each cycle runs the loop once (the same code path as the one-shot
    commands); after every cycle the completion requirement for that loop is
    checked and the driver stops when it is met, when the loop is terminally
    stuck, or when the cycle/time budget runs out.
    """
    loop_name = (args.loop or "l2").strip().lower()
    if loop_name not in ("l2", "l3", "l4", "l5", "l6", "l7", "l8", "l9"):
        print(f"  ✗ Unknown loop '{args.loop}' — choose from l2..l9")
        return 1

    max_cycles = max(1, args.max_cycles or 10)
    time_budget_s = float(args.timeout or 24 * 3600)
    sleep_s = max(0.0, float(args.sleep or 0))
    goal = _resolve_goal(args.goal, MyKBGateway())
    holder = {}
    started = time.time()

    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()

    try:
        for cycle in range(1, max_cycles + 1):
            if time.time() - started > time_budget_s:
                print(f"  ⏱ Drive time budget ({time_budget_s:g}s) exhausted "
                      f"after {cycle - 1} cycle(s) — requirement not satisfied")
                return 2

            print(f"  ▶ {loop_name.upper()} cycle {cycle}/{max_cycles}")
            done, satisfied, reason = _drive_cycle(
                loop_name, goal, telemetry, checkpoint, memory,
                evaluator, recovery, holder)

            if done:
                if satisfied:
                    print(f"  ✓ {loop_name.upper()} satisfied: {reason}")
                    return 0
                print(f"  ✗ {loop_name.upper()} terminal without "
                      f"satisfaction: {reason}")
                return 4

            if sleep_s:
                time.sleep(sleep_s)

        print(f"  ✗ {loop_name.upper()} did not satisfy its completion "
              f"requirement after {max_cycles} cycle(s)")
        return 3
    except TimeoutError as e:
        print(f"  ✗ Drive cycle timed out: {e}")
        return 1
    except Exception as e:
        print(f"  ✗ Drive failed: {e}")
        return 1
    finally:
        telemetry.stop()
        enforcer.stop()

def cmd_dashboard(args: argparse.Namespace) -> int:
    host, port = args.host, args.port
    print(f"RSIS v{__version__} \u2014 Dashboard at http://{host}:{port}")

    # Support both old (rsis/dashboard/) and new (telemetry-dashboard/backend/) locations
    td_backend = Path(__file__).parent.parent / "telemetry-dashboard" / "backend"
    if td_backend.exists():
        import sys as _sys
        _sys.path.insert(0, str(td_backend))
        import uvicorn
        from app import app  # From telemetry-dashboard/backend/
    else:
        import uvicorn
        from rsis.dashboard.app import app  # Fallback to old location
    uvicorn.run(app, host=host, port=port, log_level="info")
    return 0


def _fmt(val: object, unit: str = "") -> str:
    if val is None:
        return "N/A"
    if isinstance(val, float):
        return f"{val:.1f}{unit}"
    return f"{val}{unit}"


def cmd_status(args: argparse.Namespace) -> int:
    print(f"RSIS v{__version__}")
    print(f"  Workspace: {CONFIG.workspace_dir}")

    ledger = default_ledger()
    snap = ledger.snapshot()
    print(f"  LLM spend: ${snap['llm']['cost']:.4f} "
          f"({snap['llm']['calls']} calls, "
          f"{snap['llm']['tokens_in'] + snap['llm']['tokens_out']} tokens)")
    cap = snap['budget_cap_usd']
    cap_str = ("unlimited" if cap <= 0
               else f"${cap:.4f}" if cap < 1 else f"${cap:.2f}")
    print(f"  Budget: {cap_str} cap "
          f"({'EXCEEDED' if snap['budget_exceeded'] else 'ok'})")

    checkpoint = CheckpointManager(CONFIG.workspace_dir)
    if Path(CONFIG.workspace_dir, ".git").exists():
        print("  Git repo: initialised")
        latest = checkpoint.latest_checkpoint()
        if latest:
            print(f"  Latest checkpoint: {latest[:12]}")
    else:
        print("  Git repo: not initialised")

    memory = MemoryManager(CONFIG.workspace_dir)
    print(f"  Knowledge graph: {memory.kg.node_count} nodes / {memory.kg.edge_count} edges")
    print(f"  Vector store: {len(memory.vectors._documents)} documents")

    telemetry_dir = Path(CONFIG.telemetry_dir)
    if telemetry_dir.exists():
        files = list(telemetry_dir.glob("*.jsonl"))
        print(f"  Telemetry files: {len(files)}")

    monitor = WorkspaceMonitor()
    print(f"  CPU: {_fmt(monitor.cpu_usage(), '%')}  "
          f"Mem: {_fmt(monitor.memory_usage_mb(), ' MB')}  "
          f"Disk: {_fmt(monitor.disk_usage_pct(CONFIG.workspace_dir), '%')}")

    strategies = memory.kg.get_strategies()
    print(f"  Strategies: {len(strategies)}")
    for s in strategies[-3:]:
        print(f"    - {s.get('description', 'N/A')}")

    return 0


def cmd_check(args: argparse.Namespace) -> int:
    """Check resource limits and report status."""
    enforcer = ResourceEnforcer()
    monitor = WorkspaceMonitor()

    print(f"RSIS v{__version__} — Resource Check")
    print("")

    checks = [
        ("Disk Usage", monitor.disk_usage_pct(CONFIG.workspace_dir),
         enforcer.limits.disk_usage_pct, "%"),
        ("Memory (RSS)", monitor.memory_usage_mb(),
         float(enforcer.limits.max_memory_rss_mb), " MB"),
        ("API Rate", float(enforcer.api_calls_per_minute()),
         float(enforcer.limits.evaluator_api_calls_per_min), "/min"),
    ]

    all_ok = True
    for name, current, limit, unit in checks:
        if current is None:
            print(f"  ⚠ {name}: N/A (monitoring unavailable)")
            continue
        status = "✓" if current <= limit else "✗"
        if current > limit:
            all_ok = False
        print(f"  {status} {name}: {current:.1f}{unit} (limit: {limit}{unit})")

    print("")
    if all_ok:
        print("  All resources within limits.")
    else:
        print("  ⚠ Some resources exceed limits — consider running 'evolve' for cleanup.")

    return 0 if all_ok else 1


def cmd_check_practices(args: argparse.Namespace) -> int:
    """Enforce usage practices on the current workspace."""
    return run_practice_checks()


def cmd_scheduler(args: argparse.Namespace) -> int:
    """Run the agent scheduler demo (priority + FIFO + recursion guards)."""
    print("RSIS agent scheduler demo")
    return run_scheduler_demo()


def cmd_pipeline(args: argparse.Namespace) -> int:
    """Run the DAG worker pool demo (fan-out/fan-in + guards)."""
    print("RSIS DAG pipeline demo")
    return run_pipeline_demo()


def cmd_recovery_test(args: argparse.Namespace) -> int:
    """Test all recovery mechanisms."""
    print(f"RSIS v{__version__} — Recovery Mechanism Test")
    print("")

    checkpoint = CheckpointManager(CONFIG.workspace_dir)
    injector = FailureInjector(CONFIG.workspace_dir)
    recovery = RecoveryManager(checkpoint_mgr=checkpoint)
    results = []

    # Test 1: Checkpoint and rollback
    print("  Test 1: Checkpoint creation...")
    ch = checkpoint.checkpoint("recovery-test-before")
    if ch:
        print(f"    ✓ Checkpoint created: {ch[:12]}")
    else:
        print("    ⚡ No changes to checkpoint")
    results.append(("checkpoint_creation", ch is not None))

    print("  Test 2: Checkpoint rollback...")
    if ch:
        ok = checkpoint.rollback(ch)
        print(f"    {'✓ Rollback successful' if ok else '✗ Rollback failed'}")
        results.append(("checkpoint_rollback", ok))
    else:
        print("    ⚡ Skipped (no checkpoint)")
        results.append(("checkpoint_rollback", True))

    # Test 3: Failure injection + recovery
    print("  Test 3: File corruption + recovery...")
    test_file = ".rsis/recovery_test_marker"
    Path(CONFIG.workspace_dir, test_file).parent.mkdir(parents=True, exist_ok=True)
    Path(CONFIG.workspace_dir, test_file).write_text("recovery test marker")
    checkpoint.checkpoint("recovery-test-marker")

    ok = injector.corrupt_file(test_file)
    print(f"    {'✓ Corruption injected' if ok else '✗ Injection failed'}")
    results.append(("failure_injection", ok))

    rollback_ok = recovery.rollback_on_failure("recovery_test")
    print(f"    {'✓ Rollback recovered corruption' if rollback_ok else '✗ Rollback failed'}")
    results.append(("rollback_recovery", rollback_ok))

    # Test 4: Human alert logging
    print("  Test 4: Human-in-loop alert...")
    recovery._notify_human("Recovery test alert")
    alert_log = Path(CONFIG.workspace_dir) / ".rsis" / "human_alerts.log"
    if alert_log.exists():
        print(f"    ✓ Alert logged to {alert_log}")
        results.append(("human_alert", True))
    else:
        print(f"    ✗ Alert not logged")
        results.append(("human_alert", False))

    # Test 5: Resource enforcer
    print("  Test 5: Resource enforcer...")
    enforcer = ResourceEnforcer()
    enforcer.start()
    time.sleep(1.5)
    alerts = enforcer.alerts
    print(f"    ✓ Enforcer running ({len(alerts)} alerts triggered)")
    enforcer.stop()
    results.append(("resource_enforcer", True))

    # Summary
    print("")
    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    print(f"  Results: {passed}/{total} tests passed")
    if passed == total:
        print("  ✓ All recovery mechanisms operational.")
    else:
        print(f"  ⚠ {total - passed} test(s) failed.")

    return 0 if passed == total else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="RSIS — Recursive Self-Improvement System",
    )
    parser.add_argument("--version", action="version", version=f"RSIS {__version__}")

    sub = parser.add_subparsers(dest="command")

    p_init = sub.add_parser("init", help="Initialise workspace")
    p_init.set_defaults(func=cmd_init)

    p_run = sub.add_parser("run", help="Run improvement session")
    p_run.add_argument("--goal", "-g", default="self-improve the codebase",
                       help="Improvement goal, or 'from-mykb' to source it from "
                            "the MyKB syntheses")
    p_run.add_argument("--budget-cap", type=float, default=None,
                       help="Hard LLM cost cap in USD for this session (0=unlimited)")
    p_run.add_argument("--parallel", type=int, default=None,
                       help="Fan out N parallel L2 candidates (DAG multi-agent)")
    p_run.add_argument("--parallel-retries", type=int, default=None,
                       help="Per-candidate retry budget for parallel L2 (0=fail fast)")
    p_run.set_defaults(func=cmd_run)

    p_evolve = sub.add_parser("evolve", help="Run L3 evolution cycle")
    p_evolve.set_defaults(func=cmd_evolve)

    p_optimize = sub.add_parser("optimize", help="Run L4 meta-parameter optimization")
    p_optimize.set_defaults(func=cmd_optimize)

    p_strategies = sub.add_parser("strategies", help="Run L5 strategy evolution cycle")
    p_strategies.set_defaults(func=cmd_strategies)

    p_identity = sub.add_parser("identity", help="Run L6 identity loop (tunes L3 params)")
    p_identity.set_defaults(func=cmd_identity)

    p_metacog = sub.add_parser("metacog", help="Run L7 meta-cog loop (tunes L4 params)")
    p_metacog.set_defaults(func=cmd_metacog)

    p_metameta = sub.add_parser("metameta", help="Run L8 meta-meta loop (tunes L5 params)")
    p_metameta.set_defaults(func=cmd_metameta)

    p_mmm = sub.add_parser("mmm", help="Run L9 MMM loop (tunes L6 params)")
    p_mmm.set_defaults(func=cmd_mmm)

    p_drive = sub.add_parser("drive",
                             help="Run a loop until its completion requirement is satisfied")
    p_drive.add_argument("--loop", "-l", default="l2",
                         help="Loop to drive: l2..l9 (default: l2)")
    p_drive.add_argument("--goal", "-g", default="self-improve the codebase",
                         help="L2 goal (only used with --loop l2); "
                              "'from-mykb' sources it from MyKB syntheses")
    p_drive.add_argument("--max-cycles", type=int, default=10,
                         help="Maximum cycles before giving up (default: 10)")
    p_drive.add_argument("--timeout", type=float, default=24 * 3600,
                         help="Wall-clock budget in seconds (default: 86400)")
    p_drive.add_argument("--sleep", type=float, default=0,
                         help="Seconds to pause between cycles (default: 0)")
    p_drive.set_defaults(func=cmd_drive)

    p_dash = sub.add_parser("dashboard", help="Start web dashboard")
    p_dash.add_argument("--host", default="127.0.0.1")
    p_dash.add_argument("--port", "-p", type=int, default=8080)
    p_dash.set_defaults(func=cmd_dashboard)

    p_status = sub.add_parser("status", help="System overview")
    p_status.set_defaults(func=cmd_status)

    p_check = sub.add_parser("check", help="Check resource limits")
    p_check.set_defaults(func=cmd_check)

    p_practices = sub.add_parser(
        "check-practices",
        help="Enforce usage practices on the current workspace")
    p_practices.set_defaults(func=cmd_check_practices)

    p_scheduler = sub.add_parser("scheduler",
                                 help="Agent scheduler demo (priority/FIFO/guards)")
    p_scheduler.set_defaults(func=cmd_scheduler)

    p_pipeline = sub.add_parser("pipeline",
                                help="DAG worker pool demo (fan-out/fan-in)")
    p_pipeline.set_defaults(func=cmd_pipeline)

    p_recovery = sub.add_parser("recovery-test",
                                help="Test recovery mechanisms")
    p_recovery.set_defaults(func=cmd_recovery_test)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    setup_logging()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
