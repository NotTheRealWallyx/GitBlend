from gitblend.commands.remote_management import set_remote_url, show_remotes
from gitblend.utils import GIT_EXECUTABLE


def add_show_remotes_command(subparsers):
    show_remotes_parser = subparsers.add_parser(
        "show-remotes", help="Show all Git remotes for the current repository"
    )
    show_remotes_parser.set_defaults(func=show_remotes.run)


def add_set_remote_url_command(subparsers):
    set_remote_url_parser = subparsers.add_parser(
        "set-remote-url", help="Change the URL of a Git remote"
    )
    set_remote_url_parser.add_argument(
        "remote", type=str, help="The name of the remote (e.g., origin)"
    )
    set_remote_url_parser.add_argument(
        "url", type=str, help="The new URL for the remote"
    )
    set_remote_url_parser.set_defaults(func=set_remote_url.run)


def add_remote_management_commands(subparsers):
    """Add all remote management commands to the CLI."""
    add_show_remotes_command(subparsers)
    add_set_remote_url_command(subparsers)
