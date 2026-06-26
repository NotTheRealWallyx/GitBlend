import subprocess
from unittest import TestCase, mock

from gitblend.commands.self_update import get_repo_path, run


class TestGetRepoPath(TestCase):
    @mock.patch("os.path.exists", return_value=False)
    def test_returns_none_when_config_missing(self, _):
        self.assertIsNone(get_repo_path())

    @mock.patch("builtins.open", mock.mock_open(read_data="/home/user/GitBlend\n"))
    @mock.patch("os.path.exists", return_value=True)
    def test_returns_stripped_path(self, _):
        self.assertEqual(get_repo_path(), "/home/user/GitBlend")


class TestSelfUpdateRun(TestCase):
    def _make_args(self):
        return mock.Mock()

    @mock.patch("gitblend.commands.self_update.get_repo_path", return_value=None)
    def test_exits_when_no_config(self, _):
        with self.assertRaises(SystemExit):
            run(self._make_args())

    @mock.patch("os.path.isdir", return_value=False)
    @mock.patch(
        "gitblend.commands.self_update.get_repo_path", return_value="/fake/repo"
    )
    def test_exits_when_repo_missing(self, _get, _isdir):
        with self.assertRaises(SystemExit):
            run(self._make_args())

    @mock.patch("shutil.rmtree")
    @mock.patch("subprocess.run")
    @mock.patch("os.listdir", return_value=["gitblend-0.1.0.tar.gz"])
    @mock.patch("os.path.isdir", return_value=True)
    @mock.patch(
        "gitblend.commands.self_update.get_repo_path", return_value="/fake/repo"
    )
    def test_happy_path(self, _get, _isdir, _listdir, mock_run, mock_rmtree):
        run(self._make_args())

        calls = mock_run.call_args_list
        self.assertEqual(
            calls[0], mock.call(["git", "pull"], cwd="/fake/repo", check=True)
        )
        self.assertEqual(
            calls[1], mock.call(["poetry", "build"], cwd="/fake/repo", check=True)
        )
        self.assertEqual(
            calls[2],
            mock.call(
                ["pipx", "install", "--force", "/fake/repo/dist/gitblend-0.1.0.tar.gz"],
                check=True,
            ),
        )
        mock_rmtree.assert_called_once_with("/fake/repo/dist", ignore_errors=True)

    @mock.patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "git"))
    @mock.patch("os.path.isdir", return_value=True)
    @mock.patch(
        "gitblend.commands.self_update.get_repo_path", return_value="/fake/repo"
    )
    def test_exits_on_git_pull_failure(self, _get, _isdir, _run):
        with self.assertRaises(SystemExit):
            run(self._make_args())
