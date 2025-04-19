import subprocess
import sys
import unittest
from unittest.mock import MagicMock, patch

from gitblend.commands.commits.create import run
from gitblend.utils import GIT_EXECUTABLE


class TestCreateCommitCommand(unittest.TestCase):

    @patch("subprocess.run")
    def test_create_commit_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)

        args = MagicMock(message="Initial commit", add=False, sign=False)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_run.assert_called_once_with(
                [GIT_EXECUTABLE, "commit", "--allow-empty", "-m", "Initial commit"],
                text=True,
                check=True,
            )
            mock_print.assert_any_call(
                "✅ Commit created successfully with message: 'Initial commit'"
            )

    @patch("subprocess.run")
    def test_create_commit_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="git commit", output="", stderr="error: failed to commit"
        )

        args = MagicMock(message="Initial commit")

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_print.assert_any_call(
                "❌ Error running git command: Command 'git commit' returned non-zero exit status 1.",
                file=sys.stderr,
            )

    @patch("subprocess.run")
    def test_create_commit_with_add(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)

        args = MagicMock(message="Initial commit", add=True, sign=False)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_run.assert_any_call(
                [GIT_EXECUTABLE, "add", "."], text=True, check=True
            )
            mock_run.assert_any_call(
                [GIT_EXECUTABLE, "commit", "--allow-empty", "-m", "Initial commit"],
                text=True,
                check=True,
            )
            mock_print.assert_any_call("✅ All files added to the commit.")
            mock_print.assert_any_call(
                "✅ Commit created successfully with message: 'Initial commit'"
            )

    @patch("subprocess.run")
    def test_create_commit_with_sign(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)

        args = MagicMock(message="Initial commit", sign=True)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_run.assert_any_call(
                [
                    GIT_EXECUTABLE,
                    "commit",
                    "--allow-empty",
                    "-m",
                    "Initial commit",
                    "--gpg-sign",
                ],
                text=True,
                check=True,
            )
            mock_print.assert_any_call("✅ All files added to the commit.")
            mock_print.assert_any_call(
                "✅ Commit created successfully with message: 'Initial commit'"
            )


if __name__ == "__main__":
    unittest.main()
