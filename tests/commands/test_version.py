from unittest.mock import patch

from gitblend.commands import version


def test_version_run():
    with patch("gitblend.commands.version.get_version", return_value="0.1.0"):
        with patch("builtins.print") as mock_print:
            version.run(None)
            mock_print.assert_called_once_with("GitBlend version 0.1.0")
