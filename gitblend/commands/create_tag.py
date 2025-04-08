from git import Repo, GitCommandError
from gitblend.utils import handle_git_errors
import sys


@handle_git_errors
def run(args):
    """Create a new Git tag."""
    tag_name = args.tag
    message = args.message
    push = args.push

    repo = Repo(search_parent_directories=True)

    try:
        repo.create_tag(tag_name, message=message)
        print(f"✅ Tag '{tag_name}' created successfully.")
    except GitCommandError as e:
        print(f"❌ Failed to create tag '{tag_name}': {e}", file=sys.stderr)
        sys.exit(1)

    # Push the tag if requested
    if push:
        try:
            repo.git.push("origin", tag_name)
            print(f"✅ Tag '{tag_name}' pushed to remote repository.")
        except GitCommandError as e:
            print(f"❌ Failed to push tag '{tag_name}': {e}", file=sys.stderr)
            sys.exit(1)
