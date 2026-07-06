import unittest
from unittest.mock import mock_open, patch

from gitblend.config import load_config


class TestLoadConfig(unittest.TestCase):

    def test_missing_config_returns_empty_dict(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            self.assertEqual(load_config(), {})

    def test_valid_config_is_loaded(self):
        config_content = "[commit]\nsign = true\nadd = true\n"
        with patch("builtins.open", mock_open(read_data=config_content)):
            config = load_config()

        self.assertEqual(config, {"commit": {"sign": True, "add": True}})

    def test_invalid_config_is_ignored(self):
        with patch("builtins.open", mock_open(read_data="not [ valid toml")):
            with patch("builtins.print") as mock_print:
                config = load_config()

        self.assertEqual(config, {})
        mock_print.assert_called_once()


if __name__ == "__main__":
    unittest.main()
