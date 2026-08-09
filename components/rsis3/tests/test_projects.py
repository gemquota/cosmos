"""Phase 11 — cross-project generalization tests (profiles, goal seeds)."""
import json
import tempfile
import unittest
from pathlib import Path

from rsis.projects import (
    default_profile, goal_sources, init_project, list_projects, load_project,
    project_goal_seeds, slugify,
)
from rsis.launch import plan_batch


class ProjectsTest(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.ws = self.tmp / "ws"
        self.ws.mkdir()
        (self.ws / "rack").mkdir()
        self.mykb = self.tmp / "mykb"
        (self.mykb / "wiki" / "syntheses").mkdir(parents=True)

    def tearDown(self):
        self._tmp.cleanup()

    def _seed(self, name="alpha", title="Cross-project durable rule",
              tags=("project:alpha",)):
        front = (f"---\ntype: \"synthesis\"\ntitle: \"{title}\"\n"
                 f"tags: \"{', '.join(tags)}\"\ntimestamp: \"2026-08-09T00:00:00Z\"\n"
                 "status: \"stable\"\n---\n\nbody\n")
        (self.mykb / "wiki" / "syntheses" /
         f"seed-{name}.md").write_text(front)

    def test_slugify(self):
        self.assertEqual(slugify("My Repo!"), "my-repo")
        self.assertEqual(slugify("a/b"), "a-b")

    def test_init_and_load_profile(self):
        profile = init_project(self.ws, "/tmp/external-repo",
                               goals=["fix the build"], allowed_paths=["src"])
        self.assertEqual(profile["name"], "external-repo")
        self.assertEqual(profile["repo"], "/tmp/external-repo")
        self.assertEqual(profile["goals"], ["fix the build"])
        self.assertEqual(profile["allowed_paths"], ["src"])
        path = self.ws / "rack" / "projects" / "external-repo.json"
        self.assertTrue(path.is_file())
        loaded = load_project(self.ws, "external-repo")
        self.assertEqual(loaded["goals"], ["fix the build"])
        # create-only: init again returns existing, does not overwrite
        again = init_project(self.ws, "/tmp/other", name="external-repo",
                             goals=["overwrite me"])
        self.assertEqual(again["goals"], ["fix the build"])

    def test_list_projects(self):
        init_project(self.ws, "/tmp/repo-a")
        init_project(self.ws, "/tmp/repo-b")
        names = [p["name"] for p in list_projects(self.ws)]
        self.assertEqual(names, ["repo-a", "repo-b"])

    def test_default_profile(self):
        p = default_profile(self.ws)
        self.assertEqual(p["name"], "ws")
        self.assertIn("self-improve the codebase", p["goals"])

    def test_project_goal_seeds_provenance(self):
        self._seed()
        seeds = project_goal_seeds(self.ws, self.mykb, "alpha")
        self.assertEqual(len(seeds), 1)
        self.assertEqual(seeds[0]["provenance"]["project"], "alpha")
        self.assertEqual(seeds[0]["provenance"]["source"], "mykb-synthesis")
        self.assertTrue(seeds[0]["rel"].endswith(".md"))
        # other project's seeds are not visible
        self.assertEqual(project_goal_seeds(self.ws, self.mykb, "beta"), [])

    def test_goal_sources_include_seeds(self):
        self._seed(tags=("project:external-repo",))
        profile = init_project(self.ws, "/tmp/external-repo",
                               goals=["tune the pipeline"])
        goals = goal_sources(profile, self.ws, self.mykb, limit=3)
        self.assertIn("tune the pipeline", goals)
        self.assertTrue(any("seed from external-repo" in g for g in goals))

    def test_plan_batch_project_goal(self):
        plan = plan_batch(2, 1, goal="tune project x")
        run_goals = {g for _, g in plan if g != "self-improve the codebase"}
        self.assertEqual(run_goals, {"tune project x"})
        # default still space-sourced
        plan2 = plan_batch(1, 1)
        self.assertEqual(plan2[0][1], "from-space")


if __name__ == "__main__":
    unittest.main()
