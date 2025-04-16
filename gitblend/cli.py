import argparse
import sys

from gitblend.commands import update_all, version
from gitblend.commands.tags import create_tag, delete_tag, list_tags, rename


def add_create_tag_command(subparsers):
    create_tag_parser = subparsers.add_parser("create-tag", help="Create a new Git tag")
    create_tag_parser.add_argument(
        "tag", type=str, help="The name of the tag to create"
    )
    create_tag_parser.add_argument(
        "--message", type=str, required=True, help="The message for the tag"
    )
    create_tag_parser.add_argument(
        "--push",
        action="store_true",
        help="Push the tag to the remote repository",
    )
    create_tag_parser.set_defaults(func=create_tag.run)


def add_delete_tag_command(subparsers):
    delete_tag_parser = subparsers.add_parser(
        "delete-tag", help="Delete a git tag locally and remotely"
    )
    delete_tag_parser.add_argument(
        "tag", type=str, help="The name of the tag to delete"
    )
    delete_tag_parser.set_defaults(func=delete_tag.run)


def add_list_tags_command(subparsers):
    list_tags_parser = subparsers.add_parser(
        "list-tags", help="List all Git tags in the repository"
    )
    list_tags_parser.set_defaults(func=list_tags.run)


def add_rename_tag_command(subparsers):
    rename_tag_parser = subparsers.add_parser(
        "rename-tag", help="Rename an existing Git tag"
    )
    rename_tag_parser.add_argument(
        "old_tag", type=str, help="The name of the tag to rename"
    )
    rename_tag_parser.add_argument("new_tag", type=str, help="The new name for the tag")
    rename_tag_parser.set_defaults(func=rename.run)


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

    add_create_tag_command(subparsers)
    add_delete_tag_command(subparsers)
    add_list_tags_command(subparsers)
    add_rename_tag_command(subparsers)
    add_update_all_command(subparsers)
    add_version_command(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)
