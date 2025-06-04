import argparse
import sys

from gitblend.commands import update_all, version
from gitblend.commands.commits.entrypoints import add_commits_commands
from gitblend.commands.remote_management.entrypoints import (
    add_remote_management_commands,
)
from gitblend.commands.tags.entrypoints import add_tags_commands


def add_update_all_command(subparsers):
    update_all_parser = subparsers.add_parser(
        "update-all", help="Update all Git repositories on the computer"
    )
    update_all_parser.add_argument(
        "--path",
        type=str,
        help="The starting path to search for repositories (default: home directory)",
    )
    update_all_parser.add_argument(
        "--only-clean",
        action="store_true",
        help="Only update repositories that are on main and have no uncommitted changes",
    )
    update_all_parser.set_defaults(func=update_all.run)


def add_version_command(subparsers):
    version_parser = subparsers.add_parser(
        "version", help="Display the current version of GitBlend"
    )
    version_parser.set_defaults(func=version.run)


def main():
    parser = argparse.ArgumentParser(
        prog="gitblend", description="GitBlend - A Git utility tool"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_tags_commands(subparsers)
    add_commits_commands(subparsers)
    add_remote_management_commands(subparsers)

    add_update_all_command(subparsers)
    add_version_command(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)
