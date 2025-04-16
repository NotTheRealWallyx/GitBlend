from gitblend.commands.tags import create, delete, list, rename


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
    create_tag_parser.set_defaults(func=create.run)


def add_delete_tag_command(subparsers):
    delete_tag_parser = subparsers.add_parser(
        "delete-tag", help="Delete a git tag locally and remotely"
    )
    delete_tag_parser.add_argument(
        "tag", type=str, help="The name of the tag to delete"
    )
    delete_tag_parser.set_defaults(func=delete.run)


def add_list_tags_command(subparsers):
    list_tags_parser = subparsers.add_parser(
        "list-tags", help="List all Git tags in the repository"
    )
    list_tags_parser.set_defaults(func=list.run)


def add_rename_tag_command(subparsers):
    rename_tag_parser = subparsers.add_parser(
        "rename-tag", help="Rename an existing Git tag"
    )
    rename_tag_parser.add_argument(
        "old_tag", type=str, help="The name of the tag to rename"
    )
    rename_tag_parser.add_argument("new_tag", type=str, help="The new name for the tag")
    rename_tag_parser.set_defaults(func=rename.run)


def add_tags_commands(subparsers):
    """Add all tag-related commands to the CLI."""
    add_create_tag_command(subparsers)
    add_delete_tag_command(subparsers)
    add_list_tags_command(subparsers)
    add_rename_tag_command(subparsers)
