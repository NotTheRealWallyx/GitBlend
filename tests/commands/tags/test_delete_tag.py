import subprocess
import sys
import unittest
from unittest.mock import MagicMock, patch

from gitblend.commands.tags.delete import run


class TestDeleteTagCommand(unittest.TestCase):

    @patch("subprocess.run")
    def test_delete_tag_success(self, mock_run):
        mock_run.return_value = MagicMock(returncode=0)

        args = MagicMock(tag="v1.0")

        with patch("builtins.print") as mock_print:
            run(args)

            mock_print.assert_any_call("✅ Tag 'v1.0' deleted locally.")
            mock_print.assert_any_call("✅ Tag 'v1.0' deleted remotely.")

    @patch("subprocess.run")
    def test_delete_tag_local_failure(self, mock_run):
        def side_effect(cmd, *args, **kwargs):
            if "-d" in cmd:
                raise subprocess.CalledProcessError(
                    returncode=1,
                    cmd="git tag -d",
                    output="",
                    stderr="error: tag does not exist",
                )
            return MagicMock(returncode=0)

        mock_run.side_effect = side_effect

        args = MagicMock(tag="v1.0")

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_print.assert_any_call(
                "❌ Tag 'v1.0' does not exist locally.", file=sys.stderr
            )

    @patch("subprocess.run")
    def test_delete_tag_remote_failure(self, mock_run):
        def side_effect(cmd, *args, **kwargs):
            if "push" in cmd:
                raise subprocess.CalledProcessError(
                    returncode=1,
                    cmd="git push",
                    output="",
                    stderr="error: failed to delete remote tag",
                )
            return MagicMock(returncode=0)

        mock_run.side_effect = side_effect

        args = MagicMock(tag="v1.0")

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_print.assert_any_call("✅ Tag 'v1.0' deleted locally.")
            mock_print.assert_any_call(
                "❌ Failed to delete remote tag 'v1.0'.", file=sys.stderr
            )


if __name__ == "__main__":
    unittest.main()
