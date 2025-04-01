#!/usr/bin/env python3

import argparse
import sys
from gitblend.commands import delete_tag

def main():
    parser = argparse.ArgumentParser(prog="gitblend", description="GitBlend - A Git utility tool")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Delete tag command
    delete_tag_parser = subparsers.add_parser("delete-tag", help="Delete a git tag locally and remotely")
    delete_tag_parser.add_argument("tag", type=str, help="The name of the tag to delete")
    delete_tag_parser.set_defaults(func=delete_tag.run)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
