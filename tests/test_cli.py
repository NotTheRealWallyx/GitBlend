import unittest
from unittest.mock import patch, MagicMock
from gitblend.cli import main


def mock_run(args):
    print(f"Command executed with args: {args}")


class TestCLI(unittest.TestCase):
    @patch("gitblend.commands.create_tag.run", side_effect=mock_run)
    @patch(
        "sys.argv",
        ["gitblend", "create-tag", "v1.0", "--message", "Initial release", "--push"],
    )
    def test_create_tag_command(self, mock_create_tag):
        main()
        mock_create_tag.assert_called_once()

    @patch("gitblend.commands.delete_tag.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "delete-tag", "v1.0"])
    def test_delete_tag_command(self, mock_delete_tag):
        main()
        mock_delete_tag.assert_called_once()

    @patch("gitblend.commands.list_tags.run", side_effect=mock_run)
    @patch("sys.argv", ["gitblend", "list-tags"])
    def test_list_tags_command(self, mock_list_tags):
        main()
        mock_list_tags.assert_called_once()


if __name__ == "__main__":
    unittest.main()
