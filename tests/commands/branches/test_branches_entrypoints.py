from unittest.mock import MagicMock

from gitblend.commands.branches import entrypoints


def test_add_show_branches_command_sets_func():
    subparsers = MagicMock()
    parser = MagicMock()
    subparsers.add_parser.return_value = parser
    entrypoints.add_show_branches_command(subparsers)
    subparsers.add_parser.assert_called_once_with(
        "show-branches",
        help="Show all local Git branches for the current repository",
    )
    parser.set_defaults.assert_called_once()
    assert (
        "func" in parser.set_defaults.call_args[1]
        or "func" in parser.set_defaults.call_args[0][0]
    )
