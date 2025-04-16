import pytest
from unittest.mock import patch, mock_open
from gitblend.commands import version


def test_version_run():
    mock_pyproject_content = """[tool.poetry]
name = "gitblend"
version = "0.1.0"
"""
    with patch("builtins.open", mock_open(read_data=mock_pyproject_content)):
        with patch("builtins.print") as mock_print:
            version.run(None)
            mock_print.assert_called_once_with("GitBlend version 0.1.0")
