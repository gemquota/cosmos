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
    python -m rsis cycle-daemon       # 3-min cadence daemon (lockfile+backoff)
    python -m rsis convergence        # Plateau/no-op detection + retune proposals
    python -m rsis nightly-summary    # Daily MyKB summary note
"""

import argparse
import json
import logging
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path

from rsis import __version__

logger = logging.getLogger(__name__)
from typing import Optional

from rsis.checkpoint import CheckpointManager
from rsis.config import CONFIG
from rsis.evaluator import EvaluatorClient
from rsis.self_assess import SelfAssessment
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
from rsis.space_spec import SpaceSpec
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


def _resolve_goal(goal: str, gateway: Optional[MyKBGateway] = None,
                 spec: Optional[SpaceSpec] = None) -> str:
    """Resolve the L2 goal string from memory or spec sources.

    - `--goal from-mykb` sources the goal from the most relevant MyKB
      synthesis (durable memory context).
    - `--goal from-space` / `--goal from-spec` sources the goal from a SPACE
      spec artifact, so the run's telemetry trace references a spec artifact.
    Falls back to the default goal when the source is unavailable.
    """
    if goal == "from-mykb":
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
    if goal in ("from-space", "from-spec"):
        spec = spec if spec is not None else SpaceSpec()
        if spec.available:
            series = os.environ.get("RSIS_SPACE_SERIES", "")
            series_id = int(series) if series.isdigit() else None
            goals = spec.candidate_goals(limit=1, series_id=series_id)
            if goals:
                aid = spec.artifacts()[0]["id"] if spec.artifacts() else "?"
                print(f"  \u2139 Goal sourced from SPACE spec artifact: {aid} "
                      f"(series {series_id or 'any'})")
                return goals[0]
        return "self-improve the codebase"
    return goal


# ── Commands ─────────────────────────────────────────────────────────────

def cmd_init(args: argparse.Namespace) -> int:
    if getattr(args, "project", None):
        from rsis.projects import main as projects_main
        root = Path(CONFIG.workspace_dir or ".").resolve()
        mykb = root.parent / "mykb"
        return projects_main(root, mykb, repo=args.project, name=args.name)
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


def cmd_projects(args: argparse.Namespace) -> int:
    """Phase 11: list scaffolded project profiles."""
    from rsis.projects import main as projects_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return projects_main(root, mykb, list_only=True, json_out=args.json)


def cmd_federation(args: argparse.Namespace) -> int:
    """Phase 13: publish/pull/status for federated memory."""
    from rsis.federation import main as fed_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return fed_main(root, mykb, args.action, note_rel=args.note,
                    envelope_file=args.envelope, producer=args.producer,
                    json_out=args.json)


def cmd_seasons(args: argparse.Namespace) -> int:
    """Phase 15: seasonal goals, energy-aware scheduling, self-repair, review."""
    from rsis.seasons import main as seasons_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return seasons_main(root, mykb, action=args.action, force=args.force,
                        json_out=args.json)


def cmd_invariants(args: argparse.Namespace) -> int:
    """Phase 14: run the executable invariant registry; optionally repair."""
    from rsis.invariants import main as invariants_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return invariants_main(root, mykb=mykb, do_repair=args.repair,
                           json_out=args.json)


def cmd_users(args: argparse.Namespace) -> int:
    """Phase 12: manage per-user identities, tokens, and authz checks."""
    from rsis.users import main as users_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    return users_main(
        root, args.action, user_id=args.user_id, name=args.name,
        role=args.role, projects=args.projects,
        token=args.token, check_action=args.check_action,
        project=args.project, json_out=args.json)


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

        goal = _resolve_goal(args.goal, MyKBGateway(), SpaceSpec())
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



def cmd_launch(args: argparse.Namespace) -> int:
    """Run a full L1\u2013L9 loop batch (N cycles), mirroring run-batch.sh."""
    from rsis.launch import LOOP_ORDER, plan_batch, run_batch

    project_goal = _project_goal(args)
    plan = plan_batch(args.cycles, args.goal_space_cycle, goal=project_goal)
    print(f"\U0001f30c launch: {len(plan)} executions "
          f"({args.cycles} cycles \u00d7 {len(LOOP_ORDER)} loops)")

    if args.dry_run:
        for loop, goal in plan:
            marker = " (SPACE spec)" if goal == "from-space" else ""
            print(f"  \u25b8 {loop} --goal {goal}{marker}")
        return 0

    result = run_batch(
        args.cycles, args.goal_space_cycle, disk_pct=args.disk_pct,
        goal=project_goal)
    print(result["report"])
    return result["exit_code"]


def cmd_cycle_daemon(args: argparse.Namespace) -> int:
    """Run the standing 3-minute cycle cadence as a background daemon."""
    from rsis.ops_daemon import main as daemon_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    args.workspace = root
    args.mykb = mykb
    args.package_root = root
    args.project_goal = _project_goal(args)
    return daemon_main(args)


def _project_goal(args) -> Optional[str]:
    """Phase 11: resolve the first goal from a project profile, if requested."""
    project = getattr(args, "project", None)
    if not project:
        return None
    from rsis.projects import default_profile, goal_sources, load_project
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    profile = load_project(root, project) or default_profile(root)
    goals = goal_sources(profile, root, mykb, limit=1)
    print(f"  \u2139 Project goal ({project}): {goals[0][:90]}")
    return goals[0]


def cmd_convergence(args: argparse.Namespace) -> int:
    """Detect fitness plateaus / L4\u2013L9 bound no-ops; propose retuning."""
    from rsis.convergence import main as conv_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return conv_main(root, mykb, root, plateau_window=args.window,
                     noop_window=args.noop_window,
                     noop_threshold=args.noop_threshold,
                     apply=args.apply, json_out=args.json)


def cmd_verify_server(args: argparse.Namespace) -> int:
    """Phase 7: verification mesh over HTTP (evaluator + contracts + ledger)."""
    from rsis.verify import main as verify_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    return verify_main(port=args.port, workspace=root)


def cmd_anomalies(args: argparse.Namespace) -> int:
    """Phase 8: scan telemetry for regressions; optionally prune old data."""
    from rsis.anomalies import main as anomalies_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return anomalies_main(root, mykb, prune_days=args.prune_days,
                          file_backlogs=not args.no_backlog,
                          json_out=args.json)


def cmd_forecast(args: argparse.Namespace) -> int:
    """Phase 10: self-model forecast — predict next-cycle fitness/cost, verify quality."""
    from rsis.forecast import main as forecast_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    return forecast_main(root, do_verify=args.verify, json_out=args.json)


def cmd_policy(args: argparse.Namespace) -> int:
    """Phase 9: policy check — staged approvals + unauthorized-write scan."""
    from rsis.policy import main as policy_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    return policy_main(root, json_out=args.json)


def cmd_approve(args: argparse.Namespace) -> int:
    """Phase 9: approve or reject a staged policy-gated candidate."""
    from rsis.policy import approve, reject
    root = Path(CONFIG.workspace_dir or ".").resolve()
    actor = args.actor or os.environ.get("RSIS_ACTOR", "approver")
    ok = reject(root, args.id, actor=actor) if args.reject \
        else approve(root, args.id, actor=actor)
    print(f"  {'✓' if ok else '✗'} approval {args.id}: "
          f"{'rejected' if args.reject else 'applied' if ok else 'not found'}")
    return 0 if ok else 1


def cmd_audit(args: argparse.Namespace) -> int:
    """Phase 9: replay the audit trail."""
    from rsis.audit import main as audit_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    return audit_main(root, since=args.since, json_out=args.json)


def cmd_rollback(args: argparse.Namespace) -> int:
    """Phase 9: roll back an applied candidate to its pre-apply state."""
    from rsis.rollback import main as rollback_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return rollback_main(root, mykb, args.candidate_id)


def cmd_nightly(args: argparse.Namespace) -> int:
    """Aggregate the day into a MyKB daily-summary synthesis note."""
    from rsis.nightly import main as nightly_main
    root = Path(CONFIG.workspace_dir or ".").resolve()
    mykb = root.parent / "mykb"
    return nightly_main(root, mykb, day=args.date, json_out=args.json)


def cmd_self_assess(args: argparse.Namespace) -> int:
    telemetry, checkpoint, memory, evaluator, recovery, enforcer = _init_subsystems()
    enforcer.start()
    telemetry.start()
    try:
        days = max(1, args.days or CONFIG.self_assess.window_days)
        assessor = SelfAssessment(telemetry=telemetry)
        result = assessor.run(window_days=days,
                              file_backlog_items=not args.no_backlog)
        if result.error:
            print(f"  \u2717 Self-assessment failed: {result.error}")
            if args.json:
                print(json.dumps({"decision": "error",
                                  "error": result.error}))
            return 1
        print(f"  \u2713 Self-assessment complete (health={result.health_score})")
        print(f"  Gaps: {len(result.gaps)} \u00b7 Trends: {len(result.trends)}")
        print(f"  Assessment: {result.assessment_path}")
        if result.reflection_path:
            print(f"  Reflection: {result.reflection_path}")
        for gap in result.gaps:
            print(f"    gap [{gap.priority}]: {gap.topic}")
        if args.json:
            print(json.dumps({
                "decision": "ok",
                "health_score": result.health_score,
                "gaps": [{"topic": g.topic, "priority": g.priority}
                         for g in result.gaps],
                "trends": [asdict(t) for t in result.trends],
                "assessment": result.assessment_path,
            }))
        return 0
    finally:
        telemetry.stop()
        enforcer.stop()


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
    goal = _resolve_goal(args.goal, MyKBGateway(), SpaceSpec())
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


# ── Epoch 1 (Phases 16–50) CLI ─────────────────────────────────────────────

def _epoch_root() -> Path:
    return Path(CONFIG.workspace_dir or ".").resolve()


def cmd_attestations(args: argparse.Namespace) -> int:
    """Phase 16: hash-linked attestation chain, bundles, replay."""
    from rsis.attestations import main as amain
    return amain(_epoch_root(), action=args.action, out=args.out,
                 candidate_sha=args.candidate_sha, bundle=args.bundle,
                 json_out=args.json)


def cmd_protocol(args: argparse.Namespace) -> int:
    """Phase 17: protocol spec + capability handshake status."""
    from rsis.protocol import status
    s = status(_epoch_root())
    print(f"  protocol {s['protocol']} · spec exists: {s['spec_exists']}")
    for name, eps in s["endpoints"].items():
        print(f"    {name}: {', '.join(eps)}")
    print(f"  version negotiation: {s['version_negotiation']}")
    return 0


def cmd_export(args: argparse.Namespace) -> int:
    """Phase 18: portable instance export."""
    from rsis.portable import main as pmain
    return pmain(_epoch_root(), action="export", out=args.out)


def cmd_import(args: argparse.Namespace) -> int:
    """Phase 18: cold-start import + continuity check."""
    from rsis.portable import main as pmain
    return pmain(_epoch_root(), action="import", bundle=args.bundle,
                 json_out=args.json)


def cmd_redteam(args: argparse.Namespace) -> int:
    """Phase 19: adversarial probe harness (CI mode exits nonzero)."""
    from rsis.redteam import main as rmain
    return rmain(_epoch_root(), action=args.action, index=args.index,
                 status=args.status, resolution=args.resolution,
                 ci=args.ci, json_out=args.json)


def cmd_budgets(args: argparse.Namespace) -> int:
    """Phase 8: cost budgets — status + isolated fail-close breach drill."""
    from rsis.budgets import main as bmain
    return bmain(_epoch_root(), action=args.action, agent=args.agent,
                 drill_limit=args.drill_limit, json_out=args.json)


def cmd_apps(args: argparse.Namespace) -> int:
    """Phase 20: public API surface — machine identities + quotas."""
    from rsis.apps import main as amain
    return amain(_epoch_root(), action=args.action, app_id=args.app_id,
                 secret=args.secret, capabilities=args.capabilities,
                 json_out=args.json)


def cmd_apps_serve(args: argparse.Namespace) -> int:
    """Phase 20: run the public apps API server."""
    from rsis.apps import serve
    serve(_epoch_root(), port=args.port)
    return 0


def cmd_instance(args: argparse.Namespace) -> int:
    """Phase 21: instance identity keys, peers, rotation (L6 owns 'identity')."""
    from rsis.identity import main as imain
    return imain(_epoch_root(), action=args.action, peer_id=args.peer_id,
                 fingerprint=args.fingerprint, trust=args.trust,
                 pubkey=args.pubkey, json_out=args.json)


def cmd_exchange(args: argparse.Namespace) -> int:
    """Phase 22: confidence propagation, canonicalization, exchange ledger."""
    from rsis.exchange import status, corroborate, adopt, provenance_intact
    ws = _epoch_root()
    if args.action == "status":
        s = status(ws)
        print(f"  exchange: {s['items']} items · {s['canonical_items']} canonical · "
              f"{s['ledger_records']} ledger records")
        return 0
    if args.action == "corroborate":
        item = corroborate(ws, args.item, args.agree, provider=args.provider)
        print(f"  item {args.item[:12]} confidence {item['confidence']}")
        return 0
    if args.action == "adopt":
        r = adopt(ws, args.title, args.content, args.origin)
        print("  deduped ->" if r["deduped"] else "  adopted",
              r["canonical"][:12])
        return 0
    print("  unknown action"); return 2


def cmd_swarm(args: argparse.Namespace) -> int:
    """Phase 23: dispatch, corroboration, reconciliation."""
    from rsis.swarm import dispatch, report_verdict, fail_peer, status
    ws = _epoch_root()
    if args.action == "dispatch":
        rec = dispatch(ws, {"goal": args.goal or "verify"},
                       args.peers or [])
        print(f"  dispatched {rec['id']} to {len(rec['peers'])} peers")
        return 0
    if args.action == "verdict":
        rec = report_verdict(ws, args.dispatch, args.peer,
                             args.candidate_sha, args.verdict)
        print(f"  verdict recorded: {rec and rec.get('status')}")
        return 0
    if args.action == "fail":
        rec = fail_peer(ws, args.dispatch, args.peer)
        print(f"  peer failed: status {rec and rec.get('status')}")
        return 0
    s = status(ws)
    print(f"  swarm: {s['dispatches']} dispatches · {s['verified']} verified")
    return 0


def cmd_popgov(args: argparse.Namespace) -> int:
    """Phase 24: federated policy, quorum approvals, divergence resolution."""
    from rsis.popgov import publish_rules, adopt_rules, require_quorum, cast_vote, status
    ws = _epoch_root()
    if args.action == "publish":
        rec = publish_rules(ws, args.rules or {}, args.origin)
        print(f"  rules published ({rec['rule_sha'][:12]})")
        return 0
    if args.action == "adopt":
        r = adopt_rules(ws, args.rule_sha)
        print(f"  adopted · {r.get('resolution')}")
        return 0
    if args.action == "quorum":
        rec = require_quorum(ws, args.approval, quorum=args.quorum)
        print(f"  quorum required for {args.approval} ({args.quorum})")
        return 0
    if args.action == "vote":
        rec = cast_vote(ws, args.approval, args.peer, args.decision)
        print(f"  vote recorded: resolved={rec and rec.get('resolved')}")
        return 0
    s = status(ws)
    print(f"  popgov: {s['shared_rules']} shared rules · "
          f"{s['open_quorum']} open quorums")
    return 0


def cmd_resilience(args: argparse.Namespace) -> int:
    """Phase 25: churn, partition, forks, survival drills."""
    from rsis.resilience import survival_drill, enter_partition, reconcile_partition, status
    ws = _epoch_root()
    if args.action == "drill":
        ok, _ = survival_drill(ws, leader=args.leader or "self",
                               kill_peers=args.kill or [])
        print("  drill:", "OK" if ok else "INCONSISTENT")
        return 0 if ok else 1
    if args.action == "partition":
        enter_partition(ws, args.peers or [])
        print("  partition entered (local mode)")
        return 0
    if args.action == "reconcile":
        reconcile_partition(ws, args.peers or [])
        print("  partition reconciled")
        return 0
    s = status(ws)
    print(f"  resilience: {s['events']} events")
    return 0


def cmd_metagov(args: argparse.Namespace) -> int:
    """Phase 26: evidence-driven, human-ratified policy revision."""
    from rsis.metagov import propose, score, ratify, status
    ws = _epoch_root()
    if args.action == "propose":
        rec = propose(ws, args.delta or {}, args.rationale or "",
                      args.evidence or [])
        print(f"  proposal {rec['id']} staged")
        return 0
    if args.action == "score":
        s = score(ws, args.proposal)
        print(f"  verdict: {s and s.get('verdict')}")
        return 0 if s and s.get("verdict") == "ok" else 1
    if args.action == "ratify":
        ok = ratify(ws, args.proposal, actor=args.actor or "approver")
        print("  ratified" if ok else "  not ratifiable")
        return 0 if ok else 1
    st = status(ws)
    print(f"  metagov: {st['proposals']} proposals · "
          f"meta-invariant ok={st['meta_invariant_ok']}")
    return 0


def cmd_capacity(args: argparse.Namespace) -> int:
    """Phase 27: 90-day capacity plan, sustainability, degradation ladder."""
    from rsis.capacity import plan, sustainability, degradation_ladder, status
    ws = _epoch_root()
    if args.action == "plan":
        p = plan(ws)
        print(f"  90-day projection ${p['projected_90d']} · season {p['season']} "
              f"· mode {p['planned_mode']}")
        return 0
    if args.action == "sustainability":
        s = sustainability(ws)
        print(f"  spend ${s['total_spend']} · ceiling ${s['ceiling_usd']} · "
              f"mode {s['energy_mode']}")
        return 0
    if args.action == "degrade":
        d = degradation_ladder(ws, args.pressure or 1)
        print(f"  pressure {d['pressure']}: shed {d['shed']} · always on {d['always_on']}")
        return 0
    st = status(ws)
    print(f"  capacity plan: {st.get('plan')}")
    return 0


def cmd_goals(args: argparse.Namespace) -> int:
    """Phase 28: system-proposed, human-ratified goal candidates."""
    from rsis.goals import propose_from_gaps, ratify, record_fitness, retire_plateaued, status
    ws = _epoch_root()
    if args.action == "propose":
        recs = propose_from_gaps(ws)
        print(f"  {len(recs)} goal candidate(s) proposed from gaps")
        return 0
    if args.action == "ratify":
        ok = ratify(ws, args.goal, actor=args.actor or "approver")
        print("  ratified" if ok else "  not found/unratifiable")
        return 0 if ok else 1
    if args.action == "fitness":
        ok = record_fitness(ws, args.goal, args.fitness or 0.0)
        print("  recorded" if ok else "  not found")
        return 0 if ok else 1
    if args.action == "retire":
        retired = retire_plateaued(ws)
        print(f"  retired {len(retired)} plateaued goal(s)")
        return 0
    s = status(ws)
    print(f"  goals: {s['proposals']} proposals · {s['ratified']} ratified · "
          f"{s['retired']} retired")
    return 0


def cmd_steward(args: argparse.Namespace) -> int:
    """Phase 29: peer stewardship, onboarding, attested custody, handoff."""
    from rsis.steward import monitor, onboard, custody_action, handoff, status
    ws = _epoch_root()
    mykb = Path(ws).parent / "mykb"
    if args.action == "monitor":
        findings = monitor(ws, args.peers or [])
        print(f"  monitored {len(args.peers or [])} peer(s), {len(findings)} issues")
        return 0
    if args.action == "onboard":
        rec = onboard(ws, args.repo or "", args.name or "")
        print(f"  onboarded {args.repo} (profile ok: {bool(rec.get('profile'))})")
        return 0
    if args.action == "custody":
        rec = custody_action(ws, args.peer or "", args.action_type or "repair",
                             args.detail or "")
        print(f"  custody action attested for {rec['peer']}")
        return 0
    if args.action == "handoff":
        rec = handoff(ws, args.successor or "", args.peer or "")
        print(f"  custody -> {rec['successor']} (attested)")
        return 0
    s = status(ws)
    print(f"  steward: {s['actions']} actions · {s['handoffs']} handoffs")
    return 0


def cmd_endurance(args: argparse.Namespace) -> int:
    """Phase 30: continuous meta-invariant + existential guardrails."""
    from rsis.endurance import guardrails, continuity
    ws = _epoch_root()
    if args.action == "guardrails":
        g = guardrails(ws)
        print("  guardrails:", "OK" if g["ok"] else "VIOLATIONS")
        for name, c in g["checks"].items():
            print(f"    {name}: {'ok' if c.get('ok') else 'FAIL'}")
        return 0 if g["ok"] else 1
    c = continuity(ws)
    print(f"  continuity: {c['identity']} · attestations {c['attestations']['count']}")
    return 0


def cmd_inheritance(args: argparse.Namespace) -> int:
    """Phase 31: inheritance bundles + generation-parity check."""
    from rsis.inheritance import export_bundle, adopt, parity_check, status
    ws = _epoch_root()
    mykb = Path(ws).parent / "mykb"
    if args.action == "export":
        b = export_bundle(ws, mykb, Path(args.out) if args.out else None)
        print(f"  inheritance bundle {b['sha'][:12]} ({len(b['curriculum'])} notes)")
        return 0
    if args.action == "adopt":
        import json as _json
        bundle = _json.loads(Path(args.bundle).read_text()) if args.bundle else None
        if not bundle:
            print("  --bundle required"); return 2
        adopt(ws, bundle, mykb)
        print("  adopted")
        return 0
    if args.action == "parity":
        parity, info = parity_check(ws, mykb)
        print(f"  parity {parity:.4f} ({info['matched']}/{info['probes']}) "
              f"min {info['parity_min']}")
        return 0 if info["ok"] else 1
    s = status(ws)
    print(f"  inheritance: probes {s.get('probes', 0)}")
    return 0


def cmd_archival(args: argparse.Namespace) -> int:
    """Phase 32: bit-rot patrol, replication, format migration."""
    from rsis.archival import register, patrol, make_replica, migrate, status
    ws = _epoch_root()
    if args.action == "register":
        reg = register(ws)
        print(f"  registered {len(reg.get('files', {}))} durable artifacts")
        return 0
    if args.action == "patrol":
        p = patrol(ws)
        print(f"  patrol: {len(p['corrupt'])} corrupt · {len(p['rebuilt'])} rebuilt")
        return 0
    if args.action == "replica":
        ok = make_replica(ws, args.rel or "")
        print("  replica created" if ok else "  source missing")
        return 0 if ok else 1
    if args.action == "migrate":
        m = migrate(ws, args.frm or ".md", args.to or ".md")
        print(f"  migrated {len(m['migrated'])} file(s)")
        return 0
    s = status(ws)
    print(f"  archival: {s['tracked']} tracked · {s['patrols']} patrols · "
          f"replication min {s['replication_min']}")
    return 0


def cmd_succession(args: argparse.Namespace) -> int:
    """Phase 33: heir planning + signed custody transfer."""
    from rsis.succession import plan, transfer, status
    ws = _epoch_root()
    if args.action == "plan":
        rec = plan(ws)
        print(f"  plan {rec['id']} · {len(rec['heirs'])} heirs")
        return 0
    if args.action == "transfer":
        r = transfer(ws, args.plan or "", args.heir or "")
        print("  transferred" if r.get("ok") else f"  {r.get('reason')}")
        return 0 if r.get("ok") else 1
    s = status(ws)
    print(f"  succession: {s['plans']} plans · {s['transfers']} transfers · "
          f"{len(s['open'])} dual-running")
    return 0


def cmd_missions(args: argparse.Namespace) -> int:
    """Phase 34: mission state + attestable checkpoints + handoff."""
    from rsis.missions import create, checkpoint, handoff, status
    ws = _epoch_root()
    if args.action == "create":
        m = create(ws, args.mission, args.objective or "")
        print(f"  mission {m['id']} created")
        return 0
    if args.action == "checkpoint":
        c = checkpoint(ws, args.mission, args.note or "cycle")
        print(f"  checkpoint seq {c['seq']} (progress {c['progress']})")
        return 0
    if args.action == "handoff":
        h = handoff(ws, args.mission, args.steward or "")
        print(f"  handoff to {h['steward']} at seq {h['resume_seq']} (contiguous)")
        return 0
    s = status(ws)
    print(f"  missions: {s['missions']} · active {s['active']} · "
          f"checkpoints {s['checkpoints']}")
    return 0


def cmd_generations(args: argparse.Namespace) -> int:
    """Phase 35: dependency obsolescence, staleness, environment drift."""
    from rsis.generations import scan_dependencies, scan_staleness, drift_check, baseline
    ws = _epoch_root()
    mykb = Path(ws).parent / "mykb"
    if args.action == "scan":
        flags = scan_dependencies(ws)
        stale = scan_staleness(ws, mykb)
        print(f"  {len(flags)} obsolete deps · {len(stale['stale'])} stale syntheses")
        return 0
    if args.action == "baseline":
        baseline(ws, args.obsolete or [])
        print(f"  baseline set ({len(args.obsolete or [])} obsolete)")
        return 0
    d = drift_check(ws)
    print(f"  drift: {len(d['drift'])} mismatches")
    return 0 if not d["drift"] else 1


def cmd_explain(args: argparse.Namespace) -> int:
    """Phase 36: decision rationales + depth ladder + counterfactuals."""
    from rsis.explain import record_rationale, render, counterfactual, status
    ws = _epoch_root()
    if args.action == "rationale":
        r = record_rationale(ws, args.candidate_sha or "", args.decision or "pass")
        print(f"  {r['one_line']}")
        return 0
    if args.action == "render":
        print(render(ws, args.depth or "one_line"))
        return 0
    if args.action == "counterfactual":
        c = counterfactual(ws, args.candidate_sha or "", args.alternative or "")
        print(f"  would have: {c['would_have']}")
        return 0
    s = status(ws)
    print(f"  explanations: {'available' if s['has_rationale'] else 'none'}")
    return 0


def cmd_nlpolicy(args: argparse.Namespace) -> int:
    """Phase 37: natural-language policy compile/round-trip/apply."""
    from rsis.nlpolicy import compile_rules, roundtrip, apply, status
    ws = _epoch_root()
    if args.action == "compile":
        sentences = args.sentences or []
        r = compile_rules(ws, sentences)
        print(f"  compiled {len(r['compiled'])} · conflicts {len(r['conflicts'])} · "
              f"rejected {len(r['rejected'])}")
        for c in r["conflicts"]:
            print(f"    CONFLICT: {c['sentence']} (existing {c.get('existing')})")
        return 0
    if args.action == "roundtrip":
        r = compile_rules(ws, args.sentences or [])
        for line in roundtrip(r["compiled"]):
            print("   ", line)
        return 0
    if args.action == "apply":
        r = compile_rules(ws, args.sentences or [])
        n = apply(ws, r["compiled"], actor=args.actor or "approver")
        print(f"  applied {n} rule(s)")
        return 0
    s = status(ws)
    print(f"  nlpolicy: {s['rules']} rules · {s['conflicts']} conflicts")
    return 0


def cmd_delegation(args: argparse.Namespace) -> int:
    """Phase 38: bounded delegation contracts with instant revocation."""
    from rsis.delegation import issue, execute, revoke, status
    ws = _epoch_root()
    if args.action == "issue":
        rec = issue(ws, args.delegate or "", args.actions or [],
                    args.projects or [], args.budget or 0.0,
                    int(args.expiry or 0))
        print(f"  delegation {rec['id']} issued")
        return 0
    if args.action == "execute":
        r = execute(ws, args.delegation, args.action or "", args.project or "",
                    args.cost or 0.0)
        print(f"  executed" if r["executed"] else f"  blocked: {r['reason']}")
        return 0 if r["executed"] else 1
    if args.action == "revoke":
        ok = revoke(ws, args.delegation)
        print("  revoked" if ok else "  not found")
        return 0 if ok else 1
    s = status(ws)
    print(f"  delegations: {s['active']} active · {s['revoked']} revoked")
    return 0


def cmd_trust(args: argparse.Namespace) -> int:
    """Phase 39: ask-vs-act outcomes, over/under-trust, recalibration."""
    from rsis.trust import record_outcome, metrics, recalibrate, status
    ws = _epoch_root()
    if args.action == "record":
        record_outcome(ws, args.human or "", args.action or "", args.project or "",
                       args.asked, args.wanted)
        print("  outcome recorded")
        return 0
    if args.action == "recalibrate":
        recalibrate(ws)
        print("  thresholds recalibrated")
        return 0
    m = metrics(ws)
    print("  trust metrics:")
    for human, d in m["per_human"].items():
        print(f"    {human}: over {d['over_trust']} · under {d['under_trust']}")
    return 0


def cmd_codesign(args: argparse.Namespace) -> int:
    """Phase 40: co-design canvases with per-line authorship."""
    from rsis.codesign import create_canvas, add_artifact, merge, goal_from_merge, status
    ws = _epoch_root()
    if args.action == "canvas":
        create_canvas(ws, args.project or "default", args.title or "canvas")
        print("  canvas created")
        return 0
    if args.action == "add":
        add_artifact(ws, args.project or "default", args.text or "",
                     args.author or "human")
        print("  artifact added")
        return 0
    if args.action == "merge":
        m = merge(ws, args.project or "default", args.artifacts or [], args.title or "")
        print(f"  merged: authorship {m.get('authorship')}")
        return 0 if m.get("merged") else 1
    if args.action == "goal":
        g = goal_from_merge(ws, args.project or "default", args.merged or "")
        print(f"  goal {g['id']} proposed to pipeline")
        return 0
    s = status(ws, args.project)
    print(f"  codesign: {s}")
    return 0


def cmd_standards(args: argparse.Namespace) -> int:
    """Phase 41: protocol standard registry + sunset calendar."""
    from rsis.standards import register_version, deprecate, conformance_status
    ws = _epoch_root()
    if args.action == "register":
        register_version(ws, args.standard or "cosmos-protocol", args.version or "1")
        print("  version registered")
        return 0
    if args.action == "deprecate":
        ok = deprecate(ws, args.standard or "cosmos-protocol", args.version or "1",
                       args.sunset or "")
        print("  deprecated" if ok else "  not found")
        return 0 if ok else 1
    c = conformance_status(ws)
    print(f"  standards: {len(c['standards'])} · sunset {len(c['sunset_calendar'])}")
    return 0


def cmd_commons(args: argparse.Namespace) -> int:
    """Phase 42: global knowledge commons + attribution ledger."""
    from rsis.commons import publish, adopt, status
    ws = _epoch_root()
    if args.action == "publish":
        item = publish(ws, args.title or "", args.content or "", args.origin or "self")
        print(f"  published {item['sha'][:12]}{' (duplicate)' if item.get('duplicate') else ''}")
        return 0
    if args.action == "adopt":
        r = adopt(ws, args.sha or "", args.adopter or "")
        print("  adopted" if r.get("adopted") else "  unknown item")
        return 0 if r.get("adopted") else 1
    s = status(ws)
    print(f"  commons: {s['items']} items · attribution ok={s['attribution_ok']}")
    return 0


def cmd_diplomacy(args: argparse.Namespace) -> int:
    """Phase 43: treaties, trust levels, disputes."""
    from rsis.diplomacy import sign_treaty, trust_level, dispute, resolve, status
    ws = _epoch_root()
    if args.action == "sign":
        rec = sign_treaty(ws, args.population or "", args.terms or {},
                          level=args.level or "peers")
        print(f"  treaty {rec['id']} signed with {rec['population']} ({rec['level']})")
        return 0
    if args.action == "trust":
        t = trust_level(ws, args.population or "")
        print(f"  {args.population}: {t['level']} · caps {t['capabilities']}")
        return 0
    if args.action == "dispute":
        dispute(ws, args.population or "", args.rule_sha or "", args.detail or "")
        print("  dispute raised")
        return 0
    if args.action == "resolve":
        ok = resolve(ws, args.population or "", args.rule_sha or "", args.resolution or "")
        print("  resolved" if ok else "  not found")
        return 0 if ok else 1
    s = status(ws)
    print(f"  diplomacy: {s['active']} active treaties · {s['open_disputes']} disputes")
    return 0


def cmd_crisis(args: argparse.Namespace) -> int:
    """Phase 44: crisis modes + drills."""
    from rsis.crisis import enter, exit_crisis, drill, status
    ws = _epoch_root()
    if args.action == "enter":
        enter(ws, args.profile or "default")
        print("  crisis entered")
        return 0
    if args.action == "exit":
        exit_crisis(ws)
        print("  crisis exited (attested)")
        return 0
    if args.action == "drill":
        ok, rec = drill(ws, args.scenario or "default")
        print(f"  drill {'OK' if ok else 'FAILED'}: policy-critical kept")
        return 0 if ok else 1
    s = status(ws)
    print(f"  crisis: active={s['active']} · drills={s['drills']}")
    return 0


def cmd_planetary(args: argparse.Namespace) -> int:
    """Phase 45: commons-wide resource coordination + health."""
    from rsis.planetary import resource_plan, health, status
    ws = _epoch_root()
    if args.action == "plan":
        resource_plan(ws, args.allocations or {})
        print("  resource plan recorded")
        return 0
    if args.action == "health":
        h = health(ws)
        print("  commons health:", "OK" if h["health_ok"] else "DEGRADED")
        for name, ok in h["checks"].items():
            print(f"    {name}: {'ok' if ok else 'FAIL'}")
        return 0 if h["health_ok"] else 1
    s = status(ws)
    print(f"  planetary: {s}")
    return 0


def cmd_longitudinal(args: argparse.Namespace) -> int:
    """Phase 46: epoch-scale metrics registry + studies."""
    from rsis.longitudinal import snapshot, define_study, trend_report, status
    ws = _epoch_root()
    if args.action == "snapshot":
        snapshot(ws, args.metrics or {})
        print("  snapshot recorded")
        return 0
    if args.action == "study":
        define_study(ws, args.study or "", args.hypothesis or "",
                     args.metrics or [], int(args.window or 90))
        print("  study defined")
        return 0
    if args.action == "trend":
        r = trend_report(ws, args.metric or "fitness")
        print(f"  trend {r.get('metric')}: slope {r.get('trend_slope')} · "
              f"samples {r.get('samples')}")
        return 0
    s = status(ws)
    print(f"  longitudinal: {s['snapshots']} snapshots · {s['studies']} studies")
    return 0


def cmd_experiments(args: argparse.Namespace) -> int:
    """Phase 47: controlled A/B self-experiments."""
    from rsis.experiments import start, assign, complete, status
    ws = _epoch_root()
    if args.action == "start":
        e = start(ws, args.name or "", args.variable or "", args.control, args.treatment)
        print(f"  experiment {e['id']} started")
        return 0
    if args.action == "assign":
        c = assign(ws, args.experiment, args.unit or "")
        print(f"  {args.unit} -> {c}")
        return 0
    if args.action == "complete":
        e = complete(ws, args.experiment, args.outcomes or {})
        print(f"  {e and e.get('status')} · significant={e and e.get('significant')}")
        return 0
    s = status(ws)
    print(f"  experiments: {s['running']} running · {s['completed']} completed")
    return 0


def cmd_failures(args: argparse.Namespace) -> int:
    """Phase 48: root-cause corpus, clustering, near-misses."""
    from rsis.failures import archive, cluster, prevention_proposal, record_nearmiss, status
    ws = _epoch_root()
    if args.action == "archive":
        archive(ws, args.incident or "", args.root_cause or "", args.trigger or "",
                args.context or "", args.fix or "")
        print("  incident archived")
        return 0
    if args.action == "cluster":
        c = cluster(ws)
        print(f"  {c['clusters']} clusters · {c['recurring']} recurring")
        return 0
    if args.action == "prevent":
        p = prevention_proposal(ws, args.root_cause or "", args.rationale or "")
        print(f"  prevention goal {p['id']} proposed")
        return 0
    if args.action == "nearmiss":
        record_nearmiss(ws, args.component or "", args.detail or "")
        print("  near-miss recorded")
        return 0
    s = status(ws)
    print(f"  failures: {s['corpus']} archived · {s['nearmisses']} near-misses")
    return 0


def cmd_metainvariant(args: argparse.Namespace) -> int:
    """Phase 49: machine-checkable meta-invariant proof."""
    from rsis.metainvariant import check_reachable, attest_proof, status
    ws = _epoch_root()
    if args.action == "check":
        r = check_reachable(ws, args.transitions or [])
        print(f"  explored {r['states_explored']} states · "
              f"{'no violations' if r['ok'] else str(len(r['violations'])) + ' violations'}")
        return 0 if r["ok"] else 1
    if args.action == "attest":
        r = attest_proof(ws)
        print(f"  proof attested · commons {r['commons_sha'][:12]}")
        return 0
    s = status(ws)
    print(f"  metainvariant: {s.get('proof')}")
    return 0


def cmd_epoch(args: argparse.Namespace) -> int:
    """Phase 50: decade program, epochs registry, capstone check."""
    from rsis.epoch import decade_program, registry, capstone_check
    ws = _epoch_root()
    if args.action == "decade":
        p = decade_program(ws, ratified_by=args.actor or "approver")
        print(f"  decade program ratified ({p['years']} years)")
        return 0
    if args.action == "registry":
        reg = registry(ws, phases=args.phases or [], arcs=args.arcs or [])
        print(f"  epochs registry written ({len(reg['phases'])} phases)")
        return 0
    c = capstone_check(ws)
    print("  capstone:", "guardrails OK" if c["guardrails_ok"] else "GUARDRAIL FAIL",
          f"· attestations {c['attestation_chain']['count']}")
    return 0 if c["guardrails_ok"] else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="RSIS — Recursive Self-Improvement System",
    )
    parser.add_argument("--version", action="version", version=f"RSIS {__version__}")

    sub = parser.add_subparsers(dest="command")

    p_init = sub.add_parser("init", help="Initialise workspace")
    p_init.add_argument("--project", default=None,
                        help="Phase 11: scaffold a project profile for an "
                             "external repo instead of the host workspace")
    p_init.add_argument("--name", default=None,
                        help="Profile name (default: repo basename)")
    p_init.set_defaults(func=cmd_init)

    p_projects = sub.add_parser(
        "projects",
        help="Phase 11: list scaffolded cross-project profiles")
    p_projects.add_argument("--json", action="store_true")
    p_projects.set_defaults(func=cmd_projects)

    p_users = sub.add_parser(
        "users",
        help="Phase 12: per-user identities, signed tokens, capability authz")
    p_users.add_argument(
        "action", choices=["list", "add", "token", "check"],
        help="list users · add a user · issue a token · check an action")
    p_users.add_argument("--user-id", default=None)
    p_users.add_argument("--name", default=None)
    p_users.add_argument("--role", default="observer",
                         choices=["observer", "contributor", "approver"])
    p_users.add_argument("--project", default="cosmos",
                         help="Project for membership/authz checks")
    p_users.add_argument("--projects", nargs="*", default=None,
                         help='Project memberships for --action add '
                              '(star = all projects)')
    p_users.add_argument("--token", default=None,
                         help="Signed token for --action check")
    p_users.add_argument("--check-action", default="read",
                         choices=["read", "propose", "approve", "rollback",
                                  "manage"])
    p_users.add_argument("--json", action="store_true")
    p_users.set_defaults(func=cmd_users)

    p_inv = sub.add_parser(
        "invariants",
        help="Phase 14: executable invariant registry + sha256 attestation")
    p_inv.add_argument("--repair", action="store_true",
                       help="Attempt self-repair of repairable invariants")
    p_inv.add_argument("--json", action="store_true")
    p_inv.set_defaults(func=cmd_invariants)

    p_seasons = sub.add_parser(
        "seasons",
        help="Phase 15: long-horizon autonomy — seasons, energy, self-repair")
    p_seasons.add_argument(
        "action", choices=["status", "rotate", "repair", "review"],
        help="status · rotate season · self-repair stack · quarterly review")
    p_seasons.add_argument("--force", action="store_true",
                           help="Rotate regardless of cadence")
    p_seasons.add_argument("--json", action="store_true")
    p_seasons.set_defaults(func=cmd_seasons)

    p_fed = sub.add_parser(
        "federation",
        help="Phase 13: federated memory — publish/pull syntheses, status")
    p_fed.add_argument("action", choices=["publish", "pull", "status"],
                       help="publish a note · pull an envelope · status")
    p_fed.add_argument("--note", default=None,
                       help="MyKB note rel (wiki/syntheses/<name>.md) to publish")
    p_fed.add_argument("--envelope", default=None,
                       help="Inbox envelope JSON file to pull")
    p_fed.add_argument("--producer", default="system",
                       help="Producing identity for the envelope")
    p_fed.add_argument("--json", action="store_true")
    p_fed.set_defaults(func=cmd_federation)

    p_run = sub.add_parser("run", help="Run improvement session")
    p_run.add_argument("--goal", "-g", default="self-improve the codebase",
                       help="Improvement goal, 'from-mykb' to source it from "
                            "MyKB syntheses, or 'from-space' to source it from "
                            "a SPACE spec artifact")
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

    p_launch = sub.add_parser(
        "launch", help="Run a full L1\u2013L9 loop batch (N cycles)")
    p_launch.add_argument("--cycles", type=int, default=5,
                          help="Number of full L1\u2013L9 cycles (default: 5)")
    p_launch.add_argument("--goal-space-cycle", type=int, default=1,
                          help="Cycle that sources its L2 goal from a SPACE "
                               "spec artifact (default: 1)")
    p_launch.add_argument("--project", default=None,
                          help="Phase 11: run against a project profile "
                               "(sources L2 goals from that project)")
    p_launch.add_argument("--disk-pct", type=int, default=None,
                          help="Disk-pressure override (default: "
                               "RSIS_DISK_USAGE_PCT or 100)")
    p_launch.add_argument("--dry-run", action="store_true",
                          help="Print the execution plan without running")
    p_launch.set_defaults(func=cmd_launch)

    p_daemon = sub.add_parser(
        "cycle-daemon",
        help="3-minute cycle cadence daemon (lockfile, backoff, healthcheck)")
    p_daemon.add_argument("--once", action="store_true",
                          help="Run a single cycle then exit")
    p_daemon.add_argument("--interval", type=int, default=180,
                          help="Cadence in seconds (default: 180)")
    p_daemon.add_argument("--cycles", type=int, default=1,
                          help="Cycles per tick (default: 1)")
    p_daemon.add_argument("--goal-space-cycle", type=int, default=1)
    p_daemon.add_argument("--project", default=None,
                          help="Phase 11: route cycles to a project profile")
    p_daemon.add_argument("--disk-pct", type=int, default=None)
    p_daemon.add_argument("--bridge-url", default=None,
                          help="Bridge base URL to healthcheck each tick")
    p_daemon.add_argument("--supervise-bridge", action="store_true",
                          help="Restart the Node bridge when its port is down")
    p_daemon.add_argument("--auto-retune", action="store_true",
                          help="Apply convergence proposals (bounded)")
    p_daemon.add_argument("--no-snapshots", action="store_true",
                          help="Skip gen-static-data.py after each cycle")
    p_daemon.add_argument("--commit", action="store_true",
                          help="Commit each cycle's artifacts (T0)")
    p_daemon.add_argument("--push", action="store_true",
                          help="pull --rebase + push after each commit")
    p_daemon.add_argument("--lockfile", type=Path,
                          default=Path("rack/cycle-daemon.lock"))
    p_daemon.add_argument("--dry-run", action="store_true",
                          help="Print the plan and exit")
    p_daemon.set_defaults(func=cmd_cycle_daemon)

    p_conv = sub.add_parser(
        "convergence",
        help="Detect fitness plateaus / bound no-ops; propose retuning")
    p_conv.add_argument("--window", type=int, default=5,
                        help="Plateau window in generations (default: 5)")
    p_conv.add_argument("--noop-window", type=int, default=10,
                        help="Telemetry window for no-op counting")
    p_conv.add_argument("--noop-threshold", type=int, default=8,
                        help="No-op count that counts as a bound")
    p_conv.add_argument("--apply", action="store_true",
                        help="Run the proposed retune loop once")
    p_conv.add_argument("--json", action="store_true",
                        help="Print machine-readable report")
    p_conv.set_defaults(func=cmd_convergence)

    p_verify = sub.add_parser(
        "verify-server",
        help="Phase 7 verification mesh: evaluator + contracts + ledger over HTTP")
    p_verify.add_argument(
        "--port", type=int,
        default=int(os.environ.get("RSIS_VERIFY_PORT") or "8788"),
        help="Listen port (default: %(default)s)")
    p_verify.set_defaults(func=cmd_verify_server)

    p_anom = sub.add_parser(
        "anomalies",
        help="Phase 8: scan telemetry for regressions and file backlog items")
    p_anom.add_argument("--prune-days", type=int, default=0,
                        help="Archive telemetry older than N days (0 = off)")
    p_anom.add_argument("--no-backlog", action="store_true",
                        help="Do not file MyKB backlog notes")
    p_anom.add_argument("--json", action="store_true")
    p_anom.set_defaults(func=cmd_anomalies)

    p_forecast = sub.add_parser(
        "forecast",
        help="Phase 10: predict next-cycle fitness/success/cost; verify forecast quality")
    p_forecast.add_argument("--verify", action="store_true",
                            help="Score past forecasts (coverage/hits)")
    p_forecast.add_argument("--json", action="store_true")
    p_forecast.set_defaults(func=cmd_forecast)

    p_policy = sub.add_parser(
        "policy-check",
        help="Phase 9: verify rack/policy.json, staged approvals, unauthorized writes")
    p_policy.add_argument("--json", action="store_true")
    p_policy.set_defaults(func=cmd_policy)

    p_approve = sub.add_parser(
        "approve",
        help="Phase 9: apply a staged policy-gated candidate (--reject discards)")
    p_approve.add_argument("id", help="Staged approval id")
    p_approve.add_argument("--reject", action="store_true")
    p_approve.add_argument("--actor", default=None,
                           help="Acting user (default: $RSIS_ACTOR or approver)")
    p_approve.set_defaults(func=cmd_approve)

    p_audit = sub.add_parser(
        "audit",
        help="Phase 9: replay the attributable audit trail")
    p_audit.add_argument("--since", default=None,
                         help="Only entries at/after this ISO timestamp")
    p_audit.add_argument("--json", action="store_true")
    p_audit.set_defaults(func=cmd_audit)

    p_rollback = sub.add_parser(
        "rollback",
        help="Phase 9: restore a candidate/approval to its pre-apply state")
    p_rollback.add_argument("candidate_id", help="Approval id or candidate sha")
    p_rollback.set_defaults(func=cmd_rollback)

    p_night = sub.add_parser(
        "nightly-summary",
        help="Write the day's MyKB daily-summary synthesis note")
    p_night.add_argument("--date", default=None,
                         help="UTC day YYYY-MM-DD (default: today)")
    p_night.add_argument("--json", action="store_true")
    p_night.set_defaults(func=cmd_nightly)

    p_self = sub.add_parser(
        "self-assess",
        help="Run the self-assessment routine (KB health, gaps, trends)")
    p_self.add_argument("--days", type=int,
                        default=CONFIG.self_assess.window_days,
                        help="Analysis window in days (default: %(default)s)")
    p_self.add_argument("--no-backlog", action="store_true",
                        help="Do not file backlog notes")
    p_self.add_argument("--json", action="store_true",
                        help="Print machine-readable summary")
    p_self.set_defaults(func=cmd_self_assess)

    p_drive = sub.add_parser("drive",
                             help="Run a loop until its completion requirement is satisfied")
    p_drive.add_argument("--loop", "-l", default="l2",
                         help="Loop to drive: l2..l9 (default: l2)")
    p_drive.add_argument("--goal", "-g", default="self-improve the codebase",
                         help="L2 goal (only used with --loop l2); "
                              "'from-mykb' sources it from MyKB syntheses, "
                              "'from-space' from a SPACE spec artifact")
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


    # ── Epoch 1 (Phases 16–50) ────────────────────────────────────────────
    p_att = sub.add_parser("attestations",
                           help="Phase 16: hash-linked attestation chain + bundles")
    p_att.add_argument("action", choices=["status", "append", "verify", "export",
                                          "verify-bundle", "replay"])
    p_att.add_argument("--out", default=None)
    p_att.add_argument("--candidate-sha", default=None)
    p_att.add_argument("--bundle", default=None)
    p_att.add_argument("--json", action="store_true")
    p_att.set_defaults(func=cmd_attestations)

    p_proto = sub.add_parser("protocol",
                             help="Phase 17: cosmos-protocol/1 status")
    p_proto.set_defaults(func=cmd_protocol)

    p_exp = sub.add_parser("export", help="Phase 18: portable instance export")
    p_exp.add_argument("--out", default=None)
    p_exp.set_defaults(func=cmd_export)

    p_imp = sub.add_parser("import", help="Phase 18: cold-start import + continuity")
    p_imp.add_argument("--bundle", required=True)
    p_imp.add_argument("--json", action="store_true")
    p_imp.set_defaults(func=cmd_import)

    p_rt = sub.add_parser("redteam", help="Phase 19: adversarial probe harness")
    p_rt.add_argument("action", choices=["run", "triage", "status"])
    p_rt.add_argument("--index", type=int, default=None)
    p_rt.add_argument("--status", default="triaged",
                      choices=["triaged", "repaired", "accepted"])
    p_rt.add_argument("--resolution", default=None)
    p_rt.add_argument("--ci", action="store_true",
                      help="exit non-zero while any finding is untriaged")
    p_rt.add_argument("--json", action="store_true")
    p_rt.set_defaults(func=cmd_redteam)

    p_budgets = sub.add_parser(
        "budgets", help="Phase 8: cost budgets — status + breach drill")
    p_budgets.add_argument("action", choices=["status", "drill"])
    p_budgets.add_argument("--agent", default="evaluator")
    p_budgets.add_argument("--drill-limit", type=float, default=None,
                           help="daily_usd limit for the drill workspace")
    p_budgets.add_argument("--json", action="store_true")
    p_budgets.set_defaults(func=cmd_budgets)

    p_apps = sub.add_parser("apps", help="Phase 20: machine identities + quotas")
    p_apps.add_argument("action", choices=["list", "add", "token"])
    p_apps.add_argument("--app-id", default=None)
    p_apps.add_argument("--secret", default=None)
    p_apps.add_argument("--capabilities", nargs="*", default=None)
    p_apps.add_argument("--json", action="store_true")
    p_apps.set_defaults(func=cmd_apps)

    p_apps_srv = sub.add_parser("apps-server",
                                help="Phase 20: run the public apps API")
    p_apps_srv.add_argument("--port", type=int, default=8790)
    p_apps_srv.set_defaults(func=cmd_apps_serve)

    p_id = sub.add_parser("instance",
                          help="Phase 21: instance identity keys, peers, rotation")
    p_id.add_argument("action", choices=["init", "status", "peer-add", "rotate"])
    p_id.add_argument("--peer-id", default=None)
    p_id.add_argument("--fingerprint", default=None)
    p_id.add_argument("--trust", default="peer")
    p_id.add_argument("--pubkey", default=None)
    p_id.add_argument("--json", action="store_true")
    p_id.set_defaults(func=cmd_instance)

    p_ex = sub.add_parser("exchange",
                          help="Phase 22: confidence, canonicalization, ledger")
    p_ex.add_argument("action", choices=["status", "corroborate", "adopt"])
    p_ex.add_argument("--item", default=None)
    p_ex.add_argument("--agree", action="store_true")
    p_ex.add_argument("--provider", default="system")
    p_ex.add_argument("--title", default=None)
    p_ex.add_argument("--content", default=None)
    p_ex.add_argument("--origin", default="system")
    p_ex.set_defaults(func=cmd_exchange)

    p_sw = sub.add_parser("swarm", help="Phase 23: dispatch + corroboration")
    p_sw.add_argument("action", choices=["dispatch", "verdict", "fail", "status"])
    p_sw.add_argument("--goal", default=None)
    p_sw.add_argument("--peers", nargs="*", default=None)
    p_sw.add_argument("--dispatch", default=None)
    p_sw.add_argument("--peer", default=None)
    p_sw.add_argument("--candidate-sha", default=None)
    p_sw.add_argument("--verdict", default="pass", choices=["pass", "fail"])
    p_sw.set_defaults(func=cmd_swarm)

    p_pg = sub.add_parser("popgov", help="Phase 24: federated policy + quorum")
    p_pg.add_argument("action", choices=["publish", "adopt", "quorum", "vote", "status"])
    p_pg.add_argument("--rules", type=json.loads, default=None)
    p_pg.add_argument("--origin", default="system")
    p_pg.add_argument("--rule-sha", default=None)
    p_pg.add_argument("--approval", default=None)
    p_pg.add_argument("--quorum", type=int, default=2)
    p_pg.add_argument("--peer", default=None)
    p_pg.add_argument("--decision", default="approve", choices=["approve", "deny"])
    p_pg.set_defaults(func=cmd_popgov)

    p_res = sub.add_parser("resilience", help="Phase 25: churn, partition, drills")
    p_res.add_argument("action", choices=["drill", "partition", "reconcile", "status"])
    p_res.add_argument("--leader", default=None)
    p_res.add_argument("--kill", nargs="*", default=None)
    p_res.add_argument("--peers", nargs="*", default=None)
    p_res.set_defaults(func=cmd_resilience)

    p_mg = sub.add_parser("metagov", help="Phase 26: policy revision loop")
    p_mg.add_argument("action", choices=["propose", "score", "ratify", "status"])
    p_mg.add_argument("--delta", type=json.loads, default=None)
    p_mg.add_argument("--rationale", default=None)
    p_mg.add_argument("--evidence", nargs="*", default=None)
    p_mg.add_argument("--proposal", default=None)
    p_mg.add_argument("--actor", default=None)
    p_mg.set_defaults(func=cmd_metagov)

    p_cap = sub.add_parser("capacity",
                           help="Phase 27: 90-day plan + sustainability")
    p_cap.add_argument("action", choices=["plan", "sustainability", "degrade", "status"])
    p_cap.add_argument("--pressure", type=int, default=1)
    p_cap.set_defaults(func=cmd_capacity)

    p_gl = sub.add_parser("goals", help="Phase 28: self-directed goal candidates")
    p_gl.add_argument("action", choices=["propose", "ratify", "fitness", "retire", "status"])
    p_gl.add_argument("--goal", default=None)
    p_gl.add_argument("--fitness", type=float, default=None)
    p_gl.add_argument("--actor", default=None)
    p_gl.set_defaults(func=cmd_goals)

    p_st = sub.add_parser("steward", help="Phase 29: peer custody + handoff")
    p_st.add_argument("action", choices=["monitor", "onboard", "custody", "handoff", "status"])
    p_st.add_argument("--peers", nargs="*", default=None)
    p_st.add_argument("--repo", default=None)
    p_st.add_argument("--name", default=None)
    p_st.add_argument("--peer", default=None)
    p_st.add_argument("--action-type", default="repair")
    p_st.add_argument("--detail", default=None)
    p_st.add_argument("--successor", default=None)
    p_st.set_defaults(func=cmd_steward)

    p_end = sub.add_parser("endurance", help="Phase 30: guardrails + continuity")
    p_end.add_argument("action", choices=["guardrails", "continuity"])
    p_end.set_defaults(func=cmd_endurance)

    p_inh = sub.add_parser("inheritance", help="Phase 31: knowledge inheritance")
    p_inh.add_argument("action", choices=["export", "adopt", "parity", "status"])
    p_inh.add_argument("--out", default=None)
    p_inh.add_argument("--bundle", default=None)
    p_inh.set_defaults(func=cmd_inheritance)

    p_arc = sub.add_parser("archival", help="Phase 32: bit-rot patrol + migration")
    p_arc.add_argument("action", choices=["register", "patrol", "replica", "migrate", "status"])
    p_arc.add_argument("--rel", default=None)
    p_arc.add_argument("--frm", default=None)
    p_arc.add_argument("--to", default=None)
    p_arc.set_defaults(func=cmd_archival)

    p_suc = sub.add_parser("succession", help="Phase 33: heir planning + transfer")
    p_suc.add_argument("action", choices=["plan", "transfer", "status"])
    p_suc.add_argument("--plan", default=None)
    p_suc.add_argument("--heir", default=None)
    p_suc.set_defaults(func=cmd_succession)

    p_mis = sub.add_parser("missions", help="Phase 34: mission continuity")
    p_mis.add_argument("action", choices=["create", "checkpoint", "handoff", "status"])
    p_mis.add_argument("--mission", default=None)
    p_mis.add_argument("--objective", default=None)
    p_mis.add_argument("--note", default=None)
    p_mis.add_argument("--steward", default=None)
    p_mis.set_defaults(func=cmd_missions)

    p_gen = sub.add_parser("generations", help="Phase 35: generational resilience")
    p_gen.add_argument("action", choices=["scan", "baseline", "status"])
    p_gen.add_argument("--obsolete", nargs="*", default=None)
    p_gen.set_defaults(func=cmd_generations)

    p_xpl = sub.add_parser("explain", help="Phase 36: decision rationales")
    p_xpl.add_argument("action", choices=["rationale", "render", "counterfactual", "status"])
    p_xpl.add_argument("--candidate-sha", default=None)
    p_xpl.add_argument("--decision", default="pass")
    p_xpl.add_argument("--depth", default="one_line",
                       choices=["one_line", "paragraph", "full"])
    p_xpl.add_argument("--alternative", default=None)
    p_xpl.set_defaults(func=cmd_explain)

    p_nlp = sub.add_parser("nlpolicy", help="Phase 37: natural-language policy")
    p_nlp.add_argument("action", choices=["compile", "roundtrip", "apply", "status"])
    p_nlp.add_argument("--sentences", nargs="*", default=None)
    p_nlp.add_argument("--actor", default=None)
    p_nlp.set_defaults(func=cmd_nlpolicy)

    p_dlg = sub.add_parser("delegation", help="Phase 38: delegation contracts")
    p_dlg.add_argument("action", choices=["issue", "execute", "revoke", "status"])
    p_dlg.add_argument("--delegate", default=None)
    p_dlg.add_argument("--actions", nargs="*", default=None)
    p_dlg.add_argument("--projects", nargs="*", default=None)
    p_dlg.add_argument("--budget", type=float, default=0.0)
    p_dlg.add_argument("--expiry", default=0)
    p_dlg.add_argument("--delegation", default=None)
    p_dlg.add_argument("--action", default=None)
    p_dlg.add_argument("--project", default=None)
    p_dlg.add_argument("--cost", type=float, default=0.0)
    p_dlg.set_defaults(func=cmd_delegation)

    p_tr = sub.add_parser("trust", help="Phase 39: ask-vs-act calibration")
    p_tr.add_argument("action", choices=["record", "metrics", "recalibrate"])
    p_tr.add_argument("--human", default=None)
    p_tr.add_argument("--action", default=None)
    p_tr.add_argument("--project", default=None)
    p_tr.add_argument("--asked", action="store_true")
    p_tr.add_argument("--wanted", action="store_true")
    p_tr.set_defaults(func=cmd_trust)

    p_cd = sub.add_parser("codesign", help="Phase 40: co-design workspaces")
    p_cd.add_argument("action", choices=["canvas", "add", "merge", "goal", "status"])
    p_cd.add_argument("--project", default=None)
    p_cd.add_argument("--title", default=None)
    p_cd.add_argument("--text", default=None)
    p_cd.add_argument("--author", default="human")
    p_cd.add_argument("--artifacts", nargs="*", default=None)
    p_cd.add_argument("--merged", default=None)
    p_cd.set_defaults(func=cmd_codesign)

    p_std = sub.add_parser("standards", help="Phase 41: protocol standards")
    p_std.add_argument("action", choices=["register", "deprecate", "status"])
    p_std.add_argument("--standard", default=None)
    p_std.add_argument("--version", default=None)
    p_std.add_argument("--sunset", default=None)
    p_std.set_defaults(func=cmd_standards)

    p_com = sub.add_parser("commons", help="Phase 42: global knowledge commons")
    p_com.add_argument("action", choices=["publish", "adopt", "status"])
    p_com.add_argument("--title", default=None)
    p_com.add_argument("--content", default=None)
    p_com.add_argument("--origin", default="self")
    p_com.add_argument("--sha", default=None)
    p_com.add_argument("--adopter", default=None)
    p_com.set_defaults(func=cmd_commons)

    p_dip = sub.add_parser("diplomacy", help="Phase 43: treaties + disputes")
    p_dip.add_argument("action", choices=["sign", "trust", "dispute", "resolve", "status"])
    p_dip.add_argument("--population", default=None)
    p_dip.add_argument("--terms", type=json.loads, default=None)
    p_dip.add_argument("--level", default="peers")
    p_dip.add_argument("--rule-sha", default=None)
    p_dip.add_argument("--detail", default=None)
    p_dip.add_argument("--resolution", default=None)
    p_dip.set_defaults(func=cmd_diplomacy)

    p_crs = sub.add_parser("crisis", help="Phase 44: crisis modes + drills")
    p_crs.add_argument("action", choices=["enter", "exit", "drill", "status"])
    p_crs.add_argument("--profile", default="default")
    p_crs.add_argument("--scenario", default="default")
    p_crs.set_defaults(func=cmd_crisis)

    p_pl = sub.add_parser("planetary", help="Phase 45: commons-wide stewardship")
    p_pl.add_argument("action", choices=["plan", "health", "status"])
    p_pl.add_argument("--allocations", type=json.loads, default=None)
    p_pl.set_defaults(func=cmd_planetary)

    p_lon = sub.add_parser("longitudinal", help="Phase 46: epoch-scale metrics")
    p_lon.add_argument("action", choices=["snapshot", "study", "trend", "status"])
    p_lon.add_argument("--metrics", type=json.loads, default=None)
    p_lon.add_argument("--study", default=None)
    p_lon.add_argument("--hypothesis", default=None)
    p_lon.add_argument("--window", default=90)
    p_lon.add_argument("--metric", default="fitness")
    p_lon.set_defaults(func=cmd_longitudinal)

    p_xp = sub.add_parser("experiments", help="Phase 47: A/B self-experiments")
    p_xp.add_argument("action", choices=["start", "assign", "complete", "status"])
    p_xp.add_argument("--name", default=None)
    p_xp.add_argument("--variable", default=None)
    p_xp.add_argument("--control", default=None)
    p_xp.add_argument("--treatment", default=None)
    p_xp.add_argument("--experiment", default=None)
    p_xp.add_argument("--unit", default=None)
    p_xp.add_argument("--outcomes", type=json.loads, default=None)
    p_xp.set_defaults(func=cmd_experiments)

    p_fail = sub.add_parser("failures", help="Phase 48: root-cause corpus")
    p_fail.add_argument("action", choices=["archive", "cluster", "prevent", "nearmiss", "status"])
    p_fail.add_argument("--incident", default=None)
    p_fail.add_argument("--root-cause", default=None)
    p_fail.add_argument("--trigger", default=None)
    p_fail.add_argument("--context", default=None)
    p_fail.add_argument("--fix", default=None)
    p_fail.add_argument("--rationale", default=None)
    p_fail.add_argument("--component", default=None)
    p_fail.add_argument("--detail", default=None)
    p_fail.set_defaults(func=cmd_failures)

    p_mi = sub.add_parser("metainvariant", help="Phase 49: meta-invariant proof")
    p_mi.add_argument("action", choices=["check", "attest", "status"])
    p_mi.add_argument("--transitions", type=json.loads, default=None)
    p_mi.set_defaults(func=cmd_metainvariant)

    p_ep = sub.add_parser("epoch", help="Phase 50: decade program + capstone")
    p_ep.add_argument("action", choices=["decade", "registry", "capstone", "status"])
    p_ep.add_argument("--actor", default=None)
    p_ep.add_argument("--phases", type=json.loads, default=None)
    p_ep.add_argument("--arcs", type=json.loads, default=None)
    p_ep.set_defaults(func=cmd_epoch)
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return 1

    setup_logging()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
