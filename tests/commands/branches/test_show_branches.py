from unittest.mock import MagicMock, patch

from gitblend.commands.branches import show_branches


def test_show_branches_prints_branches(capsys):
    mock_result = MagicMock()
    mock_result.stdout = "* main\n  feature/foo"
    with patch("subprocess.run", return_value=mock_result) as mock_run:
        show_branches.run(args=MagicMock())
        mock_run.assert_called_once_with(
            [show_branches.GIT_EXECUTABLE, "branch"],
            text=True,
            capture_output=True,
            check=True,
        )
        captured = capsys.readouterr()
        assert "Local branches:" in captured.out
        assert "main" in captured.out
