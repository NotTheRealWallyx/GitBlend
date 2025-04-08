import unittest
from unittest.mock import patch, MagicMock
from gitblend.commands import rename_tag


class TestRenameTag(unittest.TestCase):

    @patch("gitblend.commands.delete_tag.run")
    @patch("gitblend.commands.create_tag.run")
    def test_rename_tag_success(self, mock_create_tag, mock_delete_tag):
        args = MagicMock()
        args.old_tag = "v1.0"
        args.new_tag = "v1.1"

        rename_tag.run(args)

        mock_delete_tag.assert_called_once_with(args)
        mock_create_tag.assert_called_once_with(args)

    @patch("gitblend.commands.delete_tag.run")
    @patch("gitblend.commands.create_tag.run")
    def test_rename_tag_nonexistent_old_tag(self, mock_create_tag, mock_delete_tag):
        mock_delete_tag.side_effect = SystemExit(1)

        args = MagicMock()
        args.old_tag = "nonexistent"
        args.new_tag = "v1.1"

        with self.assertRaises(SystemExit):
            rename_tag.run(args)

        mock_delete_tag.assert_called_once_with(args)
        mock_create_tag.assert_not_called()

    @patch("gitblend.commands.delete_tag.run")
    @patch("gitblend.commands.create_tag.run")
    def test_rename_tag_create_error(self, mock_create_tag, mock_delete_tag):
        mock_create_tag.side_effect = Exception("Create tag error")

        args = MagicMock()
        args.old_tag = "v1.0"
        args.new_tag = "v1.1"

        with self.assertRaises(Exception):
            rename_tag.run(args)

        mock_delete_tag.assert_called_once_with(args)
        mock_create_tag.assert_called_once_with(args)


if __name__ == "__main__":
    unittest.main()
