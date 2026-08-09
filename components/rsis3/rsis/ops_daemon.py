"""Cycle daemon — 3-minute cadence with lockfile, backoff, healthcheck.

Schedules ``launch --cycles 1`` on the standing rhythm so cycles run
sustainably in the background. A lockfile guarantees parallel sessions
never double-run; repeated failures back off 5/15/30 minutes; the bridge
port is healthchecked before every cycle. Optional Phase 5 flags add
bridge supervision (auto-restart) and auto-retuning from convergence
proposals.

Usage:
    python -m rsis cycle-daemon [--once] [--interval 180] [--cycles 1]
        [--backoff 300,900,1800] [--bridge-url http://localhost:8787]
        [--supervise-bridge] [--auto-retune] [--commit] [--push]
        [--dry-run]

Env:
    RSIS_CYCLE_INTERVAL_S   cadence in seconds (default 180)
    RSIS_CYCLE_BACKOFF_S    comma-separated backoff sequence (default 300,900,1800)
    RSIS_CYCLE_AUTO_RETUNE  "1" enables auto-retuning
    RSIS_CYCLE_COMMIT       "1" commits each cycle's artifacts (T0)
    RSIS_CYCLE_PUSH         "1" pulls --rebase + pushes after each commit
    RSIS_RETUNE_MIN_INTERVAL_S minimum seconds between auto-retunes (default 21600)
"""

from __future__ import annotations

import json
import logging
import os
import socket
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Optional

logger = logging.getLogger(__name__)

DEFAULT_INTERVAL_S = 180
DEFAULT_BACKOFF = (300, 900, 1800)  # 5 / 15 / 30 min


def _now_ts() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def next_backoff(consecutive_failures: int, sequence=DEFAULT_BACKOFF) -> int:
    """Backoff for the Nth consecutive failure (clamped to the sequence)."""
    if consecutive_failures <= 0:
        return 0
    idx = min(consecutive_failures - 1, len(sequence) - 1)
    return int(sequence[idx])


class CycleLock:
    """Advisory fcntl lockfile; fails fast when another daemon holds it."""

    def __init__(self, path: Path):
        self.path = path
        self._fh = None

    def acquire(self) -> bool:
        import fcntl
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fh = open(self.path, "w", encoding="utf-8")
        try:
            fcntl.flock(fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            fh.close()
            return False
        fh.seek(0)
        fh.write(str(os.getpid()))
        fh.truncate()
        fh.flush()
        self._fh = fh
        return True

    def release(self) -> None:
        if self._fh is not None:
            import fcntl
            try:
                fcntl.flock(self._fh, fcntl.LOCK_UN)
            except OSError:
                pass
            self._fh.close()
            self._fh = None


def bridge_healthy(url: str, timeout: float = 5.0) -> bool:
    if not url:
        return True
    try:
        with urllib.request.urlopen(url.rstrip("/") + "/health", timeout=timeout) as r:
            return r.status == 200
    except Exception:
        return False


def port_open(port: int, host: str = "127.0.0.1") -> bool:
    try:
        with socket.create_connection((host, port), timeout=1.0):
            return True
    except OSError:
        return False


def try_start_bridge(port: int, bridge_dir: Path) -> Optional[subprocess.Popen]:
    """Start the Node bridge if its port is free; returns the process or None."""
    if port_open(port):
        return None
    import shutil
    node = shutil.which("node")
    if not node:
        logger.warning("bridge supervise: node not found")
        return None
    try:
        env = dict(os.environ)
        env["RSIS_BRIDGE_PORT"] = str(port)
        proc = subprocess.Popen(
            [node, "rack/bridge/server.mjs"],
            cwd=str(bridge_dir), env=env,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return proc
    except Exception as e:
        logger.warning("bridge supervise failed: %s", e)
        return None


def run_one_cycle(cycles: int, goal_space_cycle: int, disk_pct: Optional[int],
                  package_root: Path,
                  executor: Optional[Callable] = None) -> dict:
    from rsis.launch import run_batch
    return run_batch(cycles, goal_space_cycle, disk_pct=disk_pct,
                     executor=executor, cwd=package_root)


def maybe_auto_retune(workspace: Path, mykb: Path, package_root: Path,
                      min_interval_s: int) -> bool:
    """Apply a convergence proposal at most once per min_interval_s."""
    from rsis.convergence import apply_proposal, detect, last_applied, write_proposal, file_backlog_note
    report = detect(workspace)
    if not report.get("detected"):
        return False
    last = last_applied(workspace)
    if last:
        try:
            last_ts = datetime.fromisoformat(last["ts"].replace("Z", "+00:00"))
            elapsed = (datetime.now(timezone.utc) - last_ts).total_seconds()
            if elapsed < min_interval_s:
                return False
        except ValueError:
            pass
    write_proposal(workspace, report)
    file_backlog_note(mykb, report)
    print(f"  🔁 auto-retune: {report['command']}")
    apply_proposal(workspace, report, package_root)
    return True


def _commit_cycle(repo: Path, commit: bool, push: bool, label: str) -> None:
    """Commit cycle artifacts (T0: every cycle leaves a committed artifact)."""
    if not commit:
        return
    proc = subprocess.run(["git", "add", "-A"], cwd=str(repo),
                          capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        logger.warning("daemon git add failed: %s", proc.stderr.strip())
    proc = subprocess.run(
        ["git", "commit", "-m", f"rsis: {label} — {_now_ts()}"],
        cwd=str(repo), capture_output=True, text=True, timeout=120)
    if proc.returncode not in (0, 1):
        logger.warning("daemon git commit failed: %s", proc.stderr.strip())
    if push:
        for args in (["git", "pull", "--rebase", "origin", "main"],
                     ["git", "push", "origin", "main"]):
            proc = subprocess.run(args, cwd=str(repo), capture_output=True,
                                  text=True, timeout=120)
            if proc.returncode != 0:
                logger.warning("daemon git %s failed: %s", args[1], proc.stderr.strip())


def run_forever(*, interval_s: int, cycles: int, goal_space_cycle: int,
                disk_pct: Optional[int], backoff=DEFAULT_BACKOFF,
                lockfile: Path, workspace: Path, mykb: Path,
                package_root: Path, bridge_url: Optional[str] = None,
                supervise_bridge: bool = False, auto_retune: bool = False,
                snapshots: bool = True, commit: bool = False,
                push: bool = False, once: bool = False,
                executor: Optional[Callable] = None) -> int:
    """Main daemon loop. Returns process exit code."""
    lock = CycleLock(lockfile)
    if not lock.acquire():
        print(f"  ✗ cycle daemon already running (lock held: {lockfile})")
        return 2
    print(f"  🔒 lock acquired: {lockfile} (pid {os.getpid()})")
    consecutive = 0
    try:
        while True:
            started = time.time()
            if bridge_url and not bridge_healthy(bridge_url):
                consecutive += 1
                print(f"  ⚠ bridge healthcheck failed ({bridge_url}) — "
                      f"failure #{consecutive}")
                if supervise_bridge:
                    port = int((os.environ.get("RSIS_BRIDGE_PORT") or "8787"))
                    proc = try_start_bridge(port, package_root)
                    print(f"  🔁 bridge supervise: {'started pid ' + str(proc.pid) if proc else 'already up'}")
            else:
                consecutive = 0

            print(f"  ▶ cycle at {_now_ts()} — launch --cycles {cycles}")
            result = run_one_cycle(cycles, goal_space_cycle, disk_pct,
                                   package_root, executor=executor)
            ok = result.get("exit_code") == 0
            if ok:
                consecutive = 0
                if auto_retune:
                    maybe_auto_retune(workspace, mykb, package_root,
                                      int(os.environ.get("RSIS_RETUNE_MIN_INTERVAL_S", "21600")))
                if snapshots:
                    _stage_all(repo_root(package_root))
                    _regen_snapshots(repo_root(package_root))
                if commit:
                    _commit_cycle(repo_root(package_root), commit=True,
                                  push=push, label="cadence cycle")
                print(f"  ✓ cycle ok (rc=0) in {time.time() - started:.1f}s")
            else:
                consecutive += 1
                wait = next_backoff(consecutive, backoff)
                print(f"  ✗ cycle failed (failure #{consecutive}) — "
                      f"backing off {wait}s")
                if not once:
                    time.sleep(wait)
                    continue

            if once:
                return 0 if ok else 1
            time.sleep(interval_s)
    finally:
        lock.release()
        print("  🔓 lock released")


def repo_root(package_root: Path) -> Path:
    """Repo root = the ancestor of ``package_root`` holding gen-static-data.py."""
    p = Path(package_root).resolve()
    for cand in (p, *p.parents):
        if (cand / "gen-static-data.py").is_file():
            return cand
    return p.parent


def _stage_all(repo: Path) -> None:
    """Stage everything so gen-static-data.py sees new files in git ls-files."""
    proc = subprocess.run(["git", "add", "-A"], cwd=str(repo),
                          capture_output=True, text=True, timeout=120)
    if proc.returncode != 0:
        logger.warning("daemon git add failed: %s", proc.stderr.strip())


def _regen_snapshots(repo: Path) -> None:
    try:
        subprocess.run(
            [sys.executable, str(repo / "gen-static-data.py")],
            cwd=str(repo), timeout=120, check=False)
    except Exception as e:
        logger.warning("snapshot regen failed: %s", e)


def main(args) -> int:
    interval = int(os.environ.get("RSIS_CYCLE_INTERVAL_S") or args.interval)
    backoff = tuple(int(x) for x in
                    (os.environ.get("RSIS_CYCLE_BACKOFF_S") or
                     ",".join(str(b) for b in DEFAULT_BACKOFF)).split(",") if x.strip())
    auto_retune = args.auto_retune or os.environ.get("RSIS_CYCLE_AUTO_RETUNE") == "1"
    commit = args.commit or os.environ.get("RSIS_CYCLE_COMMIT") == "1"
    push = args.push or os.environ.get("RSIS_CYCLE_PUSH") == "1"
    if args.dry_run:
        print("cycle-daemon plan:")
        print(f"  interval: {interval}s · cycles: {args.cycles} · backoff: {backoff}")
        print(f"  bridge-url: {args.bridge_url or 'none'} · supervise: {args.supervise_bridge} · auto-retune: {auto_retune} · commit: {commit} · push: {push}")
        return 0
    return run_forever(
        interval_s=interval, cycles=args.cycles,
        goal_space_cycle=args.goal_space_cycle, disk_pct=args.disk_pct,
        backoff=backoff, lockfile=args.lockfile,
        workspace=args.workspace, mykb=args.mykb,
        package_root=args.package_root, bridge_url=args.bridge_url,
        supervise_bridge=args.supervise_bridge, auto_retune=auto_retune,
        snapshots=not args.no_snapshots, commit=commit, push=push,
        once=args.once)
