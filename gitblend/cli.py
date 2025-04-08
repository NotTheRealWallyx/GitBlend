import argparse
import sys
from gitblend.commands import delete_tag, list_tags, create_tag


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


def main():
    parser = argparse.ArgumentParser(
        prog="gitblend", description="GitBlend - A Git utility tool"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_create_tag_command(subparsers)
    add_delete_tag_command(subparsers)
    add_list_tags_command(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)
