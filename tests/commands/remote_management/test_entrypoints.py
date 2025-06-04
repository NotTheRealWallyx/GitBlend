from unittest.mock import MagicMock

from gitblend.commands.remote_management import entrypoints


def test_add_show_remotes_command_sets_func():
    subparsers = MagicMock()
    parser = MagicMock()
    subparsers.add_parser.return_value = parser
    entrypoints.add_show_remotes_command(subparsers)
    subparsers.add_parser.assert_called_once_with(
        "show-remotes", help="Show all Git remotes for the current repository"
    )
    parser.set_defaults.assert_called_once()
    assert (
        "func" in parser.set_defaults.call_args[1]
        or "func" in parser.set_defaults.call_args[0][0]
    )


def test_add_set_remote_url_command_sets_func():
    subparsers = MagicMock()
    parser = MagicMock()
    subparsers.add_parser.return_value = parser
    entrypoints.add_set_remote_url_command(subparsers)
    subparsers.add_parser.assert_called_once_with(
        "set-remote-url", help="Change the URL of a Git remote"
    )
    parser.add_argument.assert_any_call(
        "remote", type=str, help="The name of the remote (e.g., origin)"
    )
    parser.add_argument.assert_any_call(
        "url", type=str, help="The new URL for the remote"
    )
    parser.set_defaults.assert_called_once()
    assert (
        "func" in parser.set_defaults.call_args[1]
        or "func" in parser.set_defaults.call_args[0][0]
    )
