from gitblend.commands.commits import create


def add_create_commit_command(subparsers):
    create_commit_parser = subparsers.add_parser(
        "commit", help="Create a new Git commit with a message"
    )
    create_commit_parser.add_argument(
        "--message", type=str, required=True, help="The commit message"
    )
    create_commit_parser.add_argument(
        "--add",
        action="store_true",
        help="Add all files to the commit (equivalent to 'git add .')",
    )
    create_commit_parser.set_defaults(func=create.run)


def add_commits_commands(subparsers):
    """Add all commits-related commands to the CLI."""
    add_create_commit_command(subparsers)
