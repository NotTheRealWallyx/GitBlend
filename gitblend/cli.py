#!/usr/bin/env python3

import argparse
import sys
from gitblend.commands import delete_tag, list_tags


def main():
    parser = argparse.ArgumentParser(
        prog="gitblend", description="GitBlend - A Git utility tool"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Delete tag command
    delete_tag_parser = subparsers.add_parser(
        "delete-tag", help="Delete a git tag locally and remotely"
    )
    delete_tag_parser.add_argument(
        "tag", type=str, help="The name of the tag to delete"
    )
    delete_tag_parser.set_defaults(func=delete_tag.run)

    # List tags command
    list_tags_parser = subparsers.add_parser(
        "list-tags", help="List all Git tags in the repository"
    )
    list_tags_parser.set_defaults(func=list_tags.run)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)
