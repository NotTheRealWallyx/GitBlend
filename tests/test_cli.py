import unittest
from unittest.mock import patch

from gitblend.cli import main


def mock_run(args):
    print(f"Command executed with args: {args}")


class TestTagCommands(unittest.TestCase):
    """Test the command routing for tags."""

    @patch("gitblend.commands.tags.create.run", side_effect=mock_run)
    @patch(
        "sys.argv",
        ["gitblend", "create-tag", "v1.0", "--message", "Initial release", "--push"],
    )
    def test_create_tag_command(self, mock_create_tag):
        main()
        mock_create_tag.assert_called_once()

    @patch("gitblend.commands.tags.delete.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "delete-tag", "v1.0"])
    def test_delete_tag_command(self, mock_delete_tag):
        main()
        mock_delete_tag.assert_called_once()

    @patch("gitblend.commands.tags.list.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "list-tags"])
    def test_list_tags_command(self, mock_list_tags):
        main()
        mock_list_tags.assert_called_once()

    @patch("gitblend.commands.tags.rename.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "rename-tag", "v1.0", "v1.1"])
    def test_rename_tag_command(self, mock_rename_tag):
        main()
        mock_rename_tag.assert_called_once()


class TestCommitsCommands(unittest.TestCase):
    """Test the command routing for commits."""

    @patch("gitblend.commands.commits.create.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "commit", "-m", "Innitial commit"])
    def test_commit_command(self, mock_revert):
        main()
        mock_revert.assert_called_once()

    @patch("gitblend.commands.commits.revert.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "revert", "3", "--push"])
    def test_revert_command(self, mock_revert):
        main()
        mock_revert.assert_called_once()


class TestGeneralCommands(unittest.TestCase):
    """Test the command routing for general commands."""

    @patch("gitblend.commands.version.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "version"])
    def test_version_command(self, mock_version):
        """Test the version command routing."""
        main()
        mock_version.assert_called_once()

    def test_update_all_command(self):
        """Test the update-all command routing."""
        args = ["update-all", "--path", "/mock/path"]

        with patch("gitblend.cli.update_all.run") as mock_run:
            with patch("sys.argv", ["gitblend"] + args):
                main()

            mock_run.assert_called_once()
            called_args = mock_run.call_args[0][0]
            assert called_args.path == "/mock/path"
            assert not called_args.only_clean

    def test_update_all_command_with_only_clean(self):
        """Test the update-all command with --only-clean flag."""
        args = ["update-all", "--only-clean"]

        with patch("gitblend.cli.update_all.run") as mock_run:
            with patch("sys.argv", ["gitblend"] + args):
                main()

            mock_run.assert_called_once()
            called_args = mock_run.call_args[0][0]
            assert called_args.only_clean
            assert called_args.path is None


class TestRemoteManagementCommands(unittest.TestCase):
    """Test the command routing for remote management commands."""

    @patch("gitblend.commands.remote_management.show_remotes.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "show-remotes"])
    def test_show_remotes_command(self, mock_show_remotes):
        main()
        mock_show_remotes.assert_called_once()

    @patch(
        "gitblend.commands.remote_management.set_remote_url.run", side_effect=mock_run
    )
    @patch(
        "sys.argv",
        [
            "gitblend",
            "set-remote-url",
            "origin",
            "https://github.com/user/new-repo.git",
        ],
    )
    def test_set_remote_url_command(self, mock_set_remote_url):
        main()
        mock_set_remote_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()
