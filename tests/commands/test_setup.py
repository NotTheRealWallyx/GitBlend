import unittest
from unittest.mock import MagicMock, mock_open, patch

import toml

from gitblend.commands.setup import run
from gitblend.config import CONFIG_PATH


class TestSetupCommand(unittest.TestCase):

    @patch("os.path.exists", return_value=False)
    @patch("builtins.input", side_effect=["y", "n", "yes"])
    def test_setup_writes_answers_to_config(self, mock_input, mock_exists):
        args = MagicMock(force=False)
        opened = mock_open()

        with patch("builtins.open", opened):
            with patch("builtins.print") as mock_print:
                run(args)

        written = "".join(call.args[0] for call in opened().write.call_args_list)
        self.assertEqual(
            toml.loads(written),
            {"commit": {"add": True, "sign": False, "allow_empty": True}},
        )
        mock_print.assert_any_call(f"✅ Configuration written to {CONFIG_PATH}")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.input", return_value="n")
    def test_setup_aborts_when_overwrite_declined(self, mock_input, mock_exists):
        args = MagicMock(force=False)

        with patch("builtins.open") as mock_file:
            with patch("builtins.print") as mock_print:
                run(args)

        mock_file.assert_not_called()
        mock_print.assert_any_call(
            "Setup cancelled. Existing configuration left untouched."
        )

    @patch("os.path.exists", return_value=True)
    @patch("builtins.input", side_effect=["n", "n", "n"])
    def test_setup_force_skips_overwrite_prompt(self, mock_input, mock_exists):
        args = MagicMock(force=True)
        opened = mock_open()

        with patch("builtins.open", opened):
            with patch("builtins.print"):
                run(args)

        written = "".join(call.args[0] for call in opened().write.call_args_list)
        self.assertEqual(
            toml.loads(written),
            {"commit": {"add": False, "sign": False, "allow_empty": False}},
        )


if __name__ == "__main__":
    unittest.main()
