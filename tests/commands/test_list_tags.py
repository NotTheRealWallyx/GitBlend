import subprocess
import sys
import unittest
from unittest.mock import MagicMock, patch

from gitblend.commands.list_tags import run


class TestListTagsCommand(unittest.TestCase):

    @patch("subprocess.run")
    def test_list_tags_with_tags(self, mock_run):
        mock_run.return_value = MagicMock(stdout="v1.0\nv1.1\nv2.0\n", returncode=0)

        with patch("builtins.print") as mock_print:
            run([])

            mock_print.assert_any_call("📋 Git Tags:")
            mock_print.assert_any_call("v1.0")
            mock_print.assert_any_call("v1.1")
            mock_print.assert_any_call("v2.0")

    @patch("subprocess.run")
    def test_list_tags_no_tags(self, mock_run):
        mock_run.return_value = MagicMock(stdout="", returncode=0)

        with patch("builtins.print") as mock_print:
            run([])

            mock_print.assert_any_call("No tags found in the repository.")

    @patch("subprocess.run")
    def test_list_tags_git_error(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="git tag", output="", stderr="fatal: not a git repository"
        )

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run([])

            mock_print.assert_any_call(
                "❌ Error running git command: Command 'git tag' returned non-zero exit status 1.",
                file=sys.stderr,
            )


if __name__ == "__main__":
    unittest.main()
