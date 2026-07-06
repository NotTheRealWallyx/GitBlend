from gitblend.commands.commits import create, revert
from gitblend.config import load_config


def add_create_commit_command(subparsers):
    commit_config = load_config().get("commit", {})

    create_commit_parser = subparsers.add_parser(
        "commit", help="Create a new Git commit with a message"
    )
    create_commit_parser.add_argument(
        "positional_message",
        nargs="?",
        metavar="message",
        help="The commit message",
    )
    create_commit_parser.add_argument(
        "-m", "--message", type=str, help="The commit message"
    )
    create_commit_parser.add_argument(
        "-a",
        "--add",
        action="store_true",
        help="Add all files to the commit (equivalent to 'git add .')",
    )
    create_commit_parser.add_argument(
        "-s",
        "--sign",
        action="store_true",
        help="Sign the commit with the user's GPG key",
    )
    create_commit_parser.set_defaults(
        func=create.run,
        add=bool(commit_config.get("add", False)),
        sign=bool(commit_config.get("sign", False)),
    )


def add_revert_command(subparsers):
    revert_parser = subparsers.add_parser("revert", help="Revert the last N commits")
    revert_parser.add_argument(
        "num_commits", type=int, help="The number of commits to revert"
    )
    revert_parser.add_argument(
        "--push",
        action="store_true",
        help="Push the changes to the remote repository",
    )
    revert_parser.set_defaults(func=revert.run)


def add_commits_commands(subparsers):
    """Add all commits-related commands to the CLI."""
    add_create_commit_command(subparsers)
    add_revert_command(subparsers)
