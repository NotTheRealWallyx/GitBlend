import sys
import unittest
from unittest.mock import MagicMock, patch

from gitblend.commands.tags.rename import run


class TestRenameTagCommand(unittest.TestCase):

    @patch("gitblend.commands.tags.delete_tag.run")
    @patch("gitblend.commands.tags.create_tag.run")
    def test_rename_tag_success(self, mock_create_tag, mock_delete_tag):
        args = MagicMock(old_tag="v1.0", new_tag="v1.1")

        with patch("builtins.print") as mock_print:
            run(args)

            mock_delete_tag.assert_called_once_with(args)
            mock_create_tag.assert_called_once_with(args)

            mock_print.assert_any_call(
                "✅ Tag 'v1.0' has been renamed to 'v1.1' successfully."
            )

    @patch("gitblend.commands.tags.delete_tag.run")
    @patch("gitblend.commands.tags.create_tag.run")
    def test_rename_tag_delete_failure(self, mock_create_tag, mock_delete_tag):
        mock_delete_tag.side_effect = SystemExit(1)
        args = MagicMock(old_tag="v1.0", new_tag="v1.1")

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_delete_tag.assert_called_once_with(args)
            mock_create_tag.assert_not_called()

            mock_print.assert_any_call(
                "❌ Error while renaming tag 'v1.0' to 'v1.1': 1", file=sys.stderr
            )

    @patch("gitblend.commands.tags.delete_tag.run")
    @patch("gitblend.commands.tags.create_tag.run")
    def test_rename_tag_create_failure(self, mock_create_tag, mock_delete_tag):
        mock_create_tag.side_effect = SystemExit(1)
        args = MagicMock(old_tag="v1.0", new_tag="v1.1")

        with patch("builtins.print") as mock_print:
            with self.assertRaises(SystemExit):
                run(args)

            mock_delete_tag.assert_called_once_with(args)
            mock_create_tag.assert_called_once_with(args)

            mock_print.assert_any_call(
                "❌ Error while renaming tag 'v1.0' to 'v1.1': 1", file=sys.stderr
            )


if __name__ == "__main__":
    unittest.main()
