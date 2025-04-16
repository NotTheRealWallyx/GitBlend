from unittest import TestCase, mock

from gitblend.commands.update_all import (
    has_stash,
    is_dirty,
    pop_stash,
    pull_changes,
    run,
    stash_changes,
    switch_branch,
)


class TestUpdateAll(TestCase):
    @mock.patch("subprocess.run")
    def test_is_dirty(self, mock_run):
        mock_run.return_value.stdout = " M file.txt\n"
        self.assertTrue(is_dirty("/fake/repo"))

        mock_run.return_value.stdout = ""
        self.assertFalse(is_dirty("/fake/repo"))

    @mock.patch("subprocess.run")
    def test_stash_changes(self, mock_run):
        stash_changes("/fake/repo")
        mock_run.assert_called_with(
            ["git", "stash", "save", "Auto-stash before updating main"],
            cwd="/fake/repo",
            check=True,
        )

    @mock.patch("subprocess.run")
    def test_switch_branch(self, mock_run):
        switch_branch("/fake/repo", "main")
        mock_run.assert_called_with(
            ["git", "checkout", "main"], cwd="/fake/repo", check=True
        )

    @mock.patch("subprocess.run")
    def test_pull_changes(self, mock_run):
        pull_changes("/fake/repo")
        mock_run.assert_called_with(["git", "pull"], cwd="/fake/repo", check=True)

    @mock.patch("subprocess.run")
    def test_has_stash(self, mock_run):
        mock_run.return_value.stdout = "stash@{0}: WIP on main: abc123 Commit message\n"
        self.assertTrue(has_stash("/fake/repo"))

        mock_run.return_value.stdout = ""
        self.assertFalse(has_stash("/fake/repo"))

    @mock.patch("subprocess.run")
    def test_pop_stash(self, mock_run):
        pop_stash("/fake/repo")
        mock_run.assert_called_with(
            ["git", "stash", "pop"], cwd="/fake/repo", check=True
        )

    @mock.patch("subprocess.run")
    @mock.patch("gitblend.commands.update_all.find_git_repos")
    def test_run(self, mock_find_git_repos, mock_run):
        mock_find_git_repos.return_value = ["/fake/repo1", "/fake/repo2"]

        args = mock.Mock()
        args.path = None
        args.only_clean = False

        run(args)

        # Breakdown of subprocess calls:
        # 1. Get current branch (2 repos)
        # 2. Check if dirty (2 repos)
        # 3. Stash changes (2 repos)
        # 4. Switch to main branch (2 repos)
        # 5. Pull changes (2 repos)
        # 6. Switch back to original branch (2 repos)
        # 7. Pop stash (2 repos)
        # Total = 16 calls
        self.assertEqual(mock_run.call_count, 16)
        mock_find_git_repos.assert_called_once()
