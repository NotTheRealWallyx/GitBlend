import subprocess
import sys
import unittest
from unittest.mock import MagicMock, patch

from gitblend.commands.commits.revert import run


class TestRevertCommand(unittest.TestCase):
    @patch("subprocess.run")
    def test_revert_local_commits(self, mock_subprocess_run):
        args = MagicMock(num_commits=3, push=False)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_subprocess_run.assert_called_once_with(
                ["/usr/bin/git", "revert", "HEAD~3..HEAD"], text=True, check=True
            )
            mock_print.assert_any_call("✅ Reverted the last 3 commits.")

    @patch("subprocess.run")
    def test_revert_with_remote(self, mock_subprocess_run):
        args = MagicMock(num_commits=2, push=True)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_subprocess_run.assert_any_call(
                ["/usr/bin/git", "revert", "HEAD~2..HEAD"], text=True, check=True
            )
            mock_subprocess_run.assert_any_call(
                ["/usr/bin/git", "push"], text=True, check=True
            )
            mock_print.assert_any_call("✅ Reverted the last 2 commits.")
            mock_print.assert_any_call("✅ Changes pushed to the remote repository.")

    @patch(
        "subprocess.run",
        side_effect=subprocess.CalledProcessError(
            returncode=1, cmd="git revert", output="", stderr="error: failed to revert"
        ),
    )
    def test_revert_git_error(self, mock_subprocess_run):
        args = MagicMock(num_commits=1, push=False)

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_print.assert_any_call(
                "❌ Error running git command: Command 'git revert' returned non-zero exit status 1.",
                file=sys.stderr,
            )


if __name__ == "__main__":
    unittest.main()
