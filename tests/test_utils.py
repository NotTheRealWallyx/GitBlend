from unittest import mock
from io import StringIO
from git import InvalidGitRepositoryError, GitCommandError
from gitblend.utils import handle_git_errors


def test_handle_git_errors_invalid_repo():
    @handle_git_errors
    def mock_function():
        raise InvalidGitRepositoryError()

    with mock.patch("sys.stderr", new_callable=StringIO) as mock_stderr, mock.patch(
        "sys.exit"
    ) as mock_exit:
        mock_function()
        assert (
            mock_stderr.getvalue() == "❌ Error: Not inside a valid Git repository.\n"
        )
        mock_exit.assert_called_once_with(1)


def test_handle_git_errors_git_command_error():
    @handle_git_errors
    def mock_function():
        raise GitCommandError("git status", "Some error occurred")

    with mock.patch("sys.stderr", new_callable=StringIO) as mock_stderr, mock.patch(
        "sys.exit"
    ) as mock_exit:
        mock_function()
        assert (
            mock_stderr.getvalue()
            == "❌ Git command error: Cmd('git') failed due to: 'Some error occurred'\n"
            "  cmdline: git status\n"
        )
        mock_exit.assert_called_once_with(1)


def test_handle_git_errors_no_error():
    @handle_git_errors
    def mock_function():
        return "Success"

    result = mock_function()
    assert result == "Success"
