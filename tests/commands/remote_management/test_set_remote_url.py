from unittest.mock import MagicMock, patch

from gitblend.commands.remote_management import set_remote_url


def test_set_remote_url_sets_url(capsys):
    args = MagicMock()
    args.remote = "origin"
    args.url = "https://github.com/user/new-repo.git"
    with patch("subprocess.run") as mock_run:
        set_remote_url.run(args)
        mock_run.assert_called_once_with(
            [set_remote_url.GIT_EXECUTABLE, "remote", "set-url", args.remote, args.url],
            text=True,
            check=True,
        )
        captured = capsys.readouterr()
        assert f"Remote '{args.remote}' URL set to: {args.url}" in captured.out
