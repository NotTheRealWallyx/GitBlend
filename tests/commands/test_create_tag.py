import subprocess
import sys
import unittest
from unittest.mock import MagicMock, patch

from gitblend.commands.create_tag import run


class TestCreateTagCommand(unittest.TestCase):

    @patch("subprocess.run")
    def test_create_tag_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)

        args = MagicMock(tag="v1.0", message="Initial release", push=False)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_print.assert_any_call("✅ Tag 'v1.0' created successfully.")

    @patch("subprocess.run")
    def test_create_tag_and_push_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)

        args = MagicMock(tag="v1.0", message="Initial release", push=True)

        with patch("builtins.print") as mock_print:
            run(args)

            mock_print.assert_any_call("✅ Tag 'v1.0' created successfully.")
            mock_print.assert_any_call("✅ Tag 'v1.0' pushed to remote repository.")

    @patch("subprocess.run")
    def test_create_tag_failure(self, mock_run):
        mock_run.side_effect = subprocess.CalledProcessError(
            returncode=1, cmd="git tag", output="", stderr="error: tag already exists"
        )

        args = MagicMock(tag="v1.0", message="Initial release", push=False)

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_print.assert_any_call(
                "❌ Error running git command: Command 'git tag' returned non-zero exit status 1.",
                file=sys.stderr,
            )

    @patch("subprocess.run")
    def test_push_tag_failure(self, mock_run):
        def side_effect(cmd, *args, **kwargs):
            if "push" in cmd:
                raise subprocess.CalledProcessError(
                    returncode=1,
                    cmd="git push",
                    output="",
                    stderr="error: failed to push",
                )
            return MagicMock(returncode=0)

        mock_run.side_effect = side_effect

        args = MagicMock(tag="v1.0", message="Initial release", push=True)

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_print.assert_any_call("✅ Tag 'v1.0' created successfully.")
            mock_print.assert_any_call(
                "❌ Error running git command: Command 'git push' returned non-zero exit status 1.",
                file=sys.stderr,
            )


if __name__ == "__main__":
    unittest.main()
