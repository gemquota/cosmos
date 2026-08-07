#!/usr/bin/env python3
"""Run a pulse with full RRP v2 protocol including all telemetry dimensions.

Records: AmbiguityVector, TokenBudget, QuestionQualityIndex, 
         UserSatisfactionDelta, TemporalVelocity, TopicCoverage,
         TransactionLedger, Checkpoints, Decision log, contradictions.
"""

import json, logging, sys, time, uuid
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rsis.memory import KnowledgeGraph
from rsis.telemetry import TelemetryCollector, TelemetryEvent
from rsis.config import CONFIG
from rsis.signals.stub_detector import StubDetector
from rack.rrp_engine import run_rrp_session, RRPEngine

logging.basicConfig(level=logging.WARNING, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('rrp_pulse')

PULSES_DIR = Path(__file__).parent / "pulses"
PULSES_DIR.mkdir(parents=True, exist_ok=True)


def capture_telemetry() -> dict:
    """Capture full RSIS system state for pre/post pulse snapshot."""
    kg = KnowledgeGraph()
    state: dict = {}
    strategies: dict = {}
    rsis_state = Path(CONFIG.workspace_dir) / ".rsis"
    try:
        state = json.loads((rsis_state / "identity_state.json").read_text())
        strategies = json.loads((rsis_state / "strategies.json").read_text())
    except (OSError, ValueError):
        pass
    history = state.get("history") or []
    last_signal = history[-1].get("signal", "") if history else ""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": "0.0.14",
        "improvements": {
            "total": kg.node_count,
            "successful": kg.node_count,
            "rate": 0.0,
        },
        "kg": {"nodes": kg.node_count, "edges": kg.edge_count,
               "max_nodes": 0},
        "identity": {
            "cycle": state.get("cycle", 0),
            "params": state.get("params", {}),
            "last_signal": last_signal,
            "snapshots": len(history),
        },
        "strategies": {
            "generation": strategies.get("generation", 0),
            "population": len(strategies.get("population", [])),
        },
    }


PULSES_DIR = Path(__file__).parent / "pulses"
PULSES_DIR.mkdir(parents=True, exist_ok=True)


def run_pulse(pulse_num: int, num_goals: int = 4, x: int = 3, y: int = 3, z: int = 3,
              u: int = 4, m: int = 1, depth: int = 2) -> dict:
    """Execute a full RRP v2 pulse with complete telemetry."""
    start_time = datetime.now(timezone.utc)
    telemetry = TelemetryCollector()

    print(f"\n{'='*60}")
    print(f"  PULSE {pulse_num:03d} — RRP v2 Full Protocol")
    print(f"  Config: U={u} M={m} X={x} Y={y} Z={z} Depth={depth}")
    print(f"{'='*60}\n")

    # 1. Pre-state
    print("📊 Capturing pre-state...")
    pre_state = capture_telemetry()

    # 2. Detect signals
    print(f"🔍 Scanning for signals (target={num_goals})...")
    sd = StubDetector(CONFIG.workspace_dir)
    try:
        stubs = sd.scan_by_priority(top_n=num_goals)
    except Exception:
        stubs = sd.scan_by_priority()
    print(f"   Found {len(stubs)} stubs/findings")

    # Generate goal descriptions from stubs
    goals_info = []
    for i, stub in enumerate(stubs):
        if i >= num_goals:
            break
        # Handle both StubFind objects and dicts
        if hasattr(stub, 'to_dict'):
            filepath = stub.file if hasattr(stub, 'file') else 'unknown.py'
            func = stub.name if hasattr(stub, 'name') and stub.name else filepath.split('/')[-1].replace('.py', '')
        else:
            filepath = stub.get('file', 'unknown.py')
            func = stub.get('function', stub.get('name', 'unnamed'))
        desc = f"Improve {func} in {filepath} — address {stub.pattern if hasattr(stub, 'pattern') else 'signal'}"
        goals_info.append((desc, [filepath]))

    if not goals_info:
        # Fallback: create generic improvement goals
        targets = [
            ("Improve type safety across RSIS modules", ["rsis/codegen.py"]),
            ("Add error handling to rsis/checkpoint.py", ["rsis/checkpoint.py"]),
            ("Refactor rsis/loop_l2.py for better maintainability", ["rsis/loop_l2.py"]),
            ("Add logging to rsis/memory.py operations", ["rsis/memory.py"]),
        ]
        goals_info = targets[:num_goals]
        print(f"   (using {len(goals_info)} improvement goals)")

    # 3. Run RRP v2 sessions with full telemetry
    print(f"\n🔬 RRP v2 Protocol ({len(goals_info)} goals)...")
    print(f"   {'─'*52}\n")

    goals_data = []
    improvements_data = []

    for idx, (desc, files) in enumerate(goals_info):
        print(f"   ┌─ Goal [{idx+1}/{len(goals_info)}]")
        print(f"   │ {desc[:80]}")

        # Run full RRP v2 session
        result = run_rrp_session(
            goal_description=desc,
            target_files=files,
            x=x, y=y, z=z,
            u=u, m=m, depth=depth
        )

        # Build goal data in pulse format
        decision = result["decision"]
        confidence = decision["confidence"]
        constraints = result["constraints"]
        locked = [k for k, v in constraints.items() if v == "LOCKED"]

        gt = "implementation" if ("stub" in desc.lower() or "implement" in desc.lower()) else "improvement"

        gd = {
            "goal_index": idx,
            "description": desc,
            "file": files[0] if files else "unknown",
            "function": files[0].split("/")[-1].replace(".py", "") if files else "unnamed",
            "type": gt,
            "rrp_refinement": {
                "constraints": constraints,
                "locked": locked,
                "trace_count": result["telemetry"]["transaction_count"],
                "rounds": result["rounds_completed"],
                "total_questions": result["total_questions"],
            },
            "rrp_evaluation": {
                "decision": decision["decision"],
                "confidence": confidence,
                "score_avg": round(1.0 - result["telemetry"]["ambiguity"]["avg"], 3),
                "trace": {
                    "goal_analysis": {
                        "phase": "goal_analysis",
                        "reasoning": f"Goal: {desc[:200]} | Type: {gt} | Target: {files[0] if files else 'N/A'}",
                        "conclusion": f"Analyzed via RRP v2 ({result['total_questions']} questions, {result['rounds_completed']} rounds)",
                        "goal_type": gt,
                    },
                    "constraint_extraction": {
                        "phase": "constraint_extraction",
                        "reasoning": f"RRP v2 extracted {len(constraints)} constraints across {len([k for k,v in constraints.items() if v == 'LOCKED'])} locked types",
                        "constraints": constraints,
                        "locked": locked,
                    },
                    "ambiguity_assessment": {
                        "phase": "ambiguity_assessment",
                        "reasoning": f"Ambiguity reduced through {result['rounds_completed']} rounds of structured questioning",
                        "ambiguity": result["telemetry"]["ambiguity"],
                        "avg_ambiguity": result["telemetry"]["ambiguity"]["avg"],
                    },
                    "evaluation": {
                        "phase": "evaluation",
                        "reasoning": decision["reasoning"],
                        "decision": decision["decision"],
                        "confidence": confidence,
                        "suggestions": [
                            f"RRP v2: {result['total_questions']} questions across {result['rounds_completed']} rounds",
                            f"Ambiguity converged to {result['telemetry']['ambiguity']['avg']:.2f}",
                            f"Topics covered: {', '.join(result['telemetry']['topic_coverage']['topics']) or 'none'}",
                        ],
                    },
                },
                "rrp_telemetry": {
                    "ambiguity": result["telemetry"]["ambiguity"],
                    "budget": result["telemetry"]["budget"],
                    "quality_index": result["telemetry"]["quality_index"],
                    "satisfaction": result["telemetry"]["satisfaction"],
                    "timing": result["telemetry"]["timing"],
                    "topic_coverage": result["telemetry"]["topic_coverage"],
                    "transaction_count": result["telemetry"]["transaction_count"],
                    "checkpoint_count": result["telemetry"]["checkpoint_count"],
                },
                "session_id": result["session_id"],
                "contradictions": result["contradictions"],
                "conversation": result["conversation_log"],
                "ledger": result["ledger"],
            },
        }
        goals_data.append(gd)

        success = decision["decision"] == "PASS"
        improvements_data.append({
            "goal_index": idx, "success": success, "applied": success, "attempts": 1,
        })

        telemetry.record(TelemetryEvent(
            event_type="rrp_v2_evaluation",
            metadata={
                "goal_index": idx, "goal": desc[:60],
                "decision": decision["decision"],
                "confidence": confidence,
                "ambiguity_avg": result["telemetry"]["ambiguity"]["avg"],
                "topics": result["telemetry"]["topic_coverage"]["bitmask"],
                "questions": result["total_questions"],
            }
        ))

        # Print summary
        tel = result["telemetry"]
        amb = tel["ambiguity"]
        print(f"   ├─ Rounds: {result['rounds_completed']}, Questions: {result['total_questions']}")
        print(f"   ├─ Decision: {decision['decision']} (conf={confidence:.2f})")
        print(f"   ├─ Ambiguity: avg={amb['avg']:.2f} converged={amb['converged']}")
        print(f"   ├─ Constraints: {len(constraints)} total, {len(locked)} locked")
        print(f"   ├─ Topics: {tel['topic_coverage']['topics'] or 'none'}")
        print(f"   ├─ Quality: {tel['quality_index']['average']:.2f} | Satisfaction: {tel['satisfaction']['cumulative']:.2f} {tel['satisfaction']['trend']}")
        print(f"   ├─ Budget: {tel['budget']['saturation_pct']}% | Timing: {tel['timing']['total_duration_s']}s")
        print(f"   └─ Ledger: {tel['transaction_count']} entries, {tel['checkpoint_count']} checkpoints\n")

    # 4. Post-state
    print("📊 Capturing post-state...")
    post_state = capture_telemetry()

    # 5. Compile pulse
    end_time = datetime.now(timezone.utc)
    duration_s = (end_time - start_time).total_seconds()
    approved = sum(1 for g in goals_data if g["rrp_evaluation"]["decision"] == "PASS")
    held = sum(1 for g in goals_data if g["rrp_evaluation"]["decision"] == "HOLD")

    pulse = {
        "pulse": f"{pulse_num:03d}",
        "timestamp_start": start_time.isoformat(),
        "timestamp_end": end_time.isoformat(),
        "type": "rrp_v2_full",
        "protocol": "RRP v2 — Full Telemetry (AmbiguityVector, TokenBudget, QualityIndex, Satisfaction, TemporalVelocity, TopicCoverage, TransactionLedger)",
        "rrp_config": {"u": u, "m": m, "x": x, "y": y, "z": z, "depth": depth},
        "pre_state": pre_state,
        "post_state": post_state,
        "signals": {"total_stubs": len(stubs), "goals_evaluated": len(goals_info)},
        "goals": goals_data,
        "improvements": improvements_data,
        "summary": {
            "goals_generated": len(goals_info),
            "goals_approved": approved,
            "goals_held": held,
            "goals_rejected": len(goals_info) - approved - held,
            "duration_seconds": round(duration_s, 1),
            "eval_mode": "rrp_v2_full",
            "total_questions": sum(g["rrp_refinement"]["total_questions"] for g in goals_data),
            "total_rounds": sum(g["rrp_refinement"]["rounds"] for g in goals_data),
            "avg_ambiguity": round(sum(g["rrp_evaluation"]["trace"]["ambiguity_assessment"]["avg_ambiguity"] for g in goals_data) / max(len(goals_data), 1), 3),
        },
        "rrp_telemetry_aggregate": {
            "total_questions": sum(g["rrp_refinement"]["total_questions"] for g in goals_data),
            "total_rounds": sum(g["rrp_refinement"]["rounds"] for g in goals_data),
            "total_ledger_entries": sum(g["rrp_evaluation"]["rrp_telemetry"]["transaction_count"] for g in goals_data),
            "total_checkpoints": sum(g["rrp_evaluation"]["rrp_telemetry"]["checkpoint_count"] for g in goals_data),
            "avg_quality_index": round(sum(g["rrp_evaluation"]["rrp_telemetry"]["quality_index"]["average"] for g in goals_data) / max(len(goals_data), 1), 3),
            "avg_satisfaction": round(sum(g["rrp_evaluation"]["rrp_telemetry"]["satisfaction"]["cumulative"] for g in goals_data) / max(len(goals_data), 1), 3),
            "avg_budget_saturation": round(sum(g["rrp_evaluation"]["rrp_telemetry"]["budget"]["saturation_pct"] for g in goals_data) / max(len(goals_data), 1), 1),
            "all_topics": list(set(t for g in goals_data for t in g["rrp_evaluation"]["rrp_telemetry"]["topic_coverage"]["topics"])),
        },
    }

    # Save pulse
    pulse_path = PULSES_DIR / f"pulse-{pulse_num:03d}.json"
    with open(pulse_path, "w") as f:
        json.dump(pulse, f, indent=2, default=str)

    latest_path = PULSES_DIR / "latest.json"
    with open(latest_path, "w") as f:
        json.dump(pulse, f, indent=2, default=str)

    # Print summary
    agg = pulse["rrp_telemetry_aggregate"]
    print(f"{'='*60}")
    print(f"  PULSE {pulse_num:03d} COMPLETE")
    print(f"{'='*60}")
    print(f"  Duration: {duration_s:.1f}s")
    print(f"  Goals: {len(goals_info)} evaluated, {approved} PASS, {held} HOLD")
    print(f"  Questions: {agg['total_questions']} across {agg['total_rounds']} rounds")
    print(f"  Avg Ambiguity: {pulse['summary']['avg_ambiguity']:.2f}")
    print(f"  Avg Quality: {agg['avg_quality_index']:.2f} | Avg Satisfaction: {agg['avg_satisfaction']:.2f}")
    print(f"  Budget Saturation: {agg['avg_budget_saturation']}%")
    print(f"  Ledger Entries: {agg['total_ledger_entries']} | Checkpoints: {agg['total_checkpoints']}")
    print(f"  Topics: {agg['all_topics']}")
    print(f"  File: {pulse_path}\n")

    return pulse


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run RRP v2 full protocol pulse")
    parser.add_argument("--pulse", type=int, default=12, help="Pulse number (default: 12)")
    parser.add_argument("--goals", type=int, default=4, help="Number of goals to evaluate")
    parser.add_argument("--x", type=int, default=3, help="Open-ended questions per round")
    parser.add_argument("--y", type=int, default=2, help="Multi-choice follow-ups per answer")
    parser.add_argument("--z", type=int, default=2, help="Number of questioning rounds")
    parser.add_argument("--u", type=int, default=4, help="Use case (1-6)")
    parser.add_argument("--m", type=int, default=1, help="Execution mode (1-3)")
    parser.add_argument("--depth", type=int, default=2, help="Analysis depth (1-3)")
    args = parser.parse_args()
    run_pulse(args.pulse, args.goals, x=args.x, y=args.y, z=args.z,
              u=args.u, m=args.m, depth=args.depth)
