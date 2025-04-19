import subprocess
import unittest
from unittest.mock import patch

from gitblend.utils import handle_git_errors


class TestHandleGitErrors(unittest.TestCase):

    def test_handle_git_errors_success(self):
        @handle_git_errors
        def mock_git_command():
            return "Success"

        result = mock_git_command()
        self.assertEqual(result, "Success")

    def test_handle_git_errors_failure(self):
        @handle_git_errors
        def mock_git_command():
            raise subprocess.CalledProcessError(1, "git")

        with self.assertRaises(SystemExit) as cm:
            mock_git_command()
        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
