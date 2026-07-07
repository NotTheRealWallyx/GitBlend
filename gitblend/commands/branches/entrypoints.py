from gitblend.commands.branches import show_branches


def add_show_branches_command(subparsers):
    show_branches_parser = subparsers.add_parser(
        "show-branches", help="Show all local Git branches for the current repository"
    )
    show_branches_parser.set_defaults(func=show_branches.run)


def add_branches_commands(subparsers):
    """Add all branch commands to the CLI."""
    add_show_branches_command(subparsers)
