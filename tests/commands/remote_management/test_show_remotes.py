from unittest.mock import MagicMock, patch

from gitblend.commands.remote_management import show_remotes


def test_show_remotes_prints_remotes(capsys):
    mock_result = MagicMock()
    mock_result.stdout = "origin\thttps://github.com/user/repo.git (fetch)\norigin\thttps://github.com/user/repo.git (push)"
    with patch("subprocess.run", return_value=mock_result) as mock_run:
        show_remotes.run(args=MagicMock())
        mock_run.assert_called_once_with(
            [show_remotes.GIT_EXECUTABLE, "remote", "-v"],
            text=True,
            capture_output=True,
            check=True,
        )
        captured = capsys.readouterr()
        assert "Git remotes:" in captured.out
        assert "origin" in captured.out
