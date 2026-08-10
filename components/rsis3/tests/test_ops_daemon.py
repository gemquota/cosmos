"""Phase 4 — cycle daemon tests (lockfile, backoff, once-mode runs)."""
import tempfile
import unittest
from pathlib import Path

from rsis.ops_daemon import CycleLock, _daemon_artifacts, next_backoff, run_forever


class BackoffTest(unittest.TestCase):
    def test_sequence(self):
        seq = (300, 900, 1800)
        self.assertEqual(next_backoff(0, seq), 0)
        self.assertEqual(next_backoff(1, seq), 300)
        self.assertEqual(next_backoff(2, seq), 900)
        self.assertEqual(next_backoff(3, seq), 1800)
        self.assertEqual(next_backoff(4, seq), 1800)  # clamped


class LockTest(unittest.TestCase):
    def test_lock_excludes_second(self):
        with tempfile.TemporaryDirectory() as d:
            lockfile = Path(d) / "cycle.lock"
            a = CycleLock(lockfile)
            b = CycleLock(lockfile)
            self.assertTrue(a.acquire())
            self.assertFalse(b.acquire())
            a.release()
            self.assertTrue(b.acquire())
            b.release()


class CommitTest(unittest.TestCase):
    def _seed(self, root, pkg, mykb):
        import subprocess as sp
        pkg.mkdir()
        mykb.mkdir()
        sp.run(["git", "init", "-q"], cwd=root, check=True)
        sp.run(["git", "config", "user.email", "t@t"], cwd=root, check=True)
        sp.run(["git", "config", "user.name", "t"], cwd=root, check=True)
        (root / "seed.txt").write_text("x")
        sp.run(["git", "add", "-A"], cwd=root, check=True)
        sp.run(["git", "commit", "-qm", "seed"], cwd=root, check=True)

    def _run_once(self, root, pkg, mykb, fake):
        return run_forever(
            interval_s=1, cycles=1, goal_space_cycle=1, disk_pct=None,
            backoff=(1, 2, 3), lockfile=pkg / "rack" / "cycle.lock",
            workspace=pkg, mykb=mykb, package_root=pkg,
            bridge_url=None, snapshots=False, commit=True, push=False,
            once=True, executor=fake)

    def test_cycle_committed(self):
        import subprocess as sp
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pkg = root / "rsis3"
            mykb = root / "mykb"
            self._seed(root, pkg, mykb)

            def fake(loop, goal, disk):
                (mykb / "log.md").write_text("cycle log\n")
                return 0

            rc = self._run_once(root, pkg, mykb, fake)
            self.assertEqual(rc, 0)
            log = sp.run(["git", "log", "--oneline", "-2"], cwd=root,
                         capture_output=True, text=True, check=True).stdout
            self.assertIn("rsis: cadence cycle", log)
            tracked = sp.run(["git", "ls-files"], cwd=root,
                             capture_output=True, text=True,
                             check=True).stdout
            self.assertIn("mykb/log.md", tracked)

    def test_stray_file_not_swept(self):
        import subprocess as sp
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pkg = root / "rsis3"
            mykb = root / "mykb"
            self._seed(root, pkg, mykb)

            def fake(loop, goal, disk):
                (pkg / "stray.txt").write_text("unrelated edit")
                return 0

            rc = self._run_once(root, pkg, mykb, fake)
            self.assertEqual(rc, 0)
            log = sp.run(["git", "log", "--oneline"], cwd=root,
                         capture_output=True, text=True, check=True).stdout
            self.assertNotIn("rsis: cadence cycle", log)
            tracked = sp.run(["git", "ls-files"], cwd=root,
                             capture_output=True, text=True,
                             check=True).stdout
            self.assertNotIn("stray.txt", tracked)
            self.assertTrue((pkg / "stray.txt").exists())

    def test_noop_cycle_skips_commit(self):
        import subprocess as sp
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            pkg = root / "rsis3"
            mykb = root / "mykb"
            self._seed(root, pkg, mykb)
            rc = self._run_once(root, pkg, mykb,
                                fake=lambda loop, goal, disk: 0)
            self.assertEqual(rc, 0)
            log = sp.run(["git", "log", "--oneline"], cwd=root,
                         capture_output=True, text=True, check=True).stdout
            self.assertEqual(len(log.splitlines()), 1)  # seed only


class DaemonArtifactsTest(unittest.TestCase):
    def test_owned_paths_only(self):
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            pkg = repo / "rsis3"
            mykb = repo / "mykb"
            for p in (pkg / ".rsis", pkg / "rack" / "bridge" / "cycles",
                      mykb / "wiki" / "syntheses"):
                p.mkdir(parents=True)
            (mykb / "log.md").write_text("x")
            paths = _daemon_artifacts(pkg, mykb, repo, snapshots=False)
            self.assertEqual(paths, [
                "rsis3/.rsis", "rsis3/rack/bridge/cycles",
                "mykb/wiki/syntheses", "mykb/log.md"])
            self.assertNotIn("rsis3/rack/pulses/dashboard-data.json", paths)
            # snapshot paths appear only when the files actually exist
            (repo / "rsis3" / "rack" / "pulses").mkdir(parents=True)
            (repo / "rsis3" / "rack" / "pulses"
             / "dashboard-data.json").write_text("{}")
            paths_snap = _daemon_artifacts(pkg, mykb, repo, snapshots=True)
            self.assertIn("rsis3/rack/pulses/dashboard-data.json", paths_snap)

    def test_ignored_paths_dropped(self):
        import subprocess as sp
        with tempfile.TemporaryDirectory() as d:
            repo = Path(d)
            pkg = repo / "rsis3"
            mykb = repo / "mykb"
            (pkg / ".rsis").mkdir(parents=True)
            (mykb / "wiki" / "syntheses").mkdir(parents=True)
            (mykb / "log.md").write_text("x")
            (repo / ".gitignore").write_text("rsis3/.rsis/\n")
            sp.run(["git", "init", "-q"], cwd=repo, check=True)
            paths = _daemon_artifacts(pkg, mykb, repo, snapshots=False)
            self.assertNotIn("rsis3/.rsis", paths)
            self.assertIn("mykb/wiki/syntheses", paths)


class RunForeverTest(unittest.TestCase):
    def _run_once(self, executor, expect_rc):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            ws = tmp / "ws"; ws.mkdir()
            mykb = tmp / "mykb"; mykb.mkdir()
            rc = run_forever(
                interval_s=1, cycles=1, goal_space_cycle=1, disk_pct=None,
                backoff=(1, 2, 3), lockfile=tmp / "cycle.lock",
                workspace=ws, mykb=mykb, package_root=tmp,
                bridge_url=None, supervise_bridge=False, auto_retune=False,
                snapshots=False, once=True, executor=executor)
            self.assertEqual(rc, expect_rc)

    def test_once_success(self):
        self._run_once(lambda loop, goal, disk: 0, expect_rc=0)

    def test_once_failure(self):
        self._run_once(lambda loop, goal, disk: 1, expect_rc=1)

    def test_lock_held_returns_2(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            ws = tmp / "ws"; ws.mkdir()
            mykb = tmp / "mykb"; mykb.mkdir()
            lock = CycleLock(tmp / "cycle.lock")
            self.assertTrue(lock.acquire())
            try:
                rc = run_forever(
                    interval_s=1, cycles=1, goal_space_cycle=1, disk_pct=None,
                    backoff=(1, 2, 3), lockfile=tmp / "cycle.lock",
                    workspace=ws, mykb=mykb, package_root=tmp,
                    bridge_url=None, snapshots=False, once=True,
                    executor=lambda loop, goal, disk: 0)
                self.assertEqual(rc, 2)
            finally:
                lock.release()


if __name__ == "__main__":
    unittest.main()
